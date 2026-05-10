const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const INPUT = path.join(ROOT, "output", "yandex-services-reviews-scan-2026-05-09.json");
const OUTPUT = path.join(ROOT, "assets", "moonn-yandex-all-reviews-layer.js");

const PROFILE_URL = "https://uslugi.yandex.ru/profile/TatyanaKumskovamunn-948629";
const ROOT_ID = "moonn-yandex-all-reviews-layer";
const EXCERPT_LIMIT = 360;

function normalizeText(value) {
  return String(value || "").replace(/\r\n/g, "\n").replace(/[ \t]+\n/g, "\n").trim();
}

function cleanReviewText(value) {
  return normalizeText(value)
    .replace(/\nВ начало(?:\n\d+)*\s*$/u, "")
    .replace(/\nЧитать все отзывы[\s\S]*$/u, "")
    .replace(/\nВы\s+сотрудничали\s+с[\s\S]*$/u, "")
    .replace(/\s*\.{3}\s*Читать далее\s*$/u, "")
    .replace(/\s*…\s*Читать далее\s*$/u, "")
    .trim();
}

function compactKey(value) {
  return normalizeText(value).replace(/\s+/g, " ");
}

function excerptFromText(text) {
  const normalized = normalizeText(text);
  if (normalized.length <= EXCERPT_LIMIT) {
    return { excerpt: normalized, isTruncated: false };
  }

  const softCut = normalized.slice(0, EXCERPT_LIMIT + 1);
  const lastSpace = softCut.lastIndexOf(" ");
  const cutAt = lastSpace > Math.floor(EXCERPT_LIMIT * 0.72) ? lastSpace : EXCERPT_LIMIT;
  return { excerpt: normalized.slice(0, cutAt).trim(), isTruncated: true };
}

function getYear(date) {
  const match = String(date || "").match(/\d{4}$/);
  return match ? match[0] : "без даты";
}

function readReviews() {
  const payload = JSON.parse(fs.readFileSync(INPUT, "utf8"));
  const records = payload.reviews
    .map((item) => {
      const text = cleanReviewText(item.text);
      return {
        author: String(item.author || "").trim() || "Автор отзыва",
        date: String(item.date || "").trim(),
        text,
        isTeaser: /\bЧитать далее\b/u.test(String(item.text || "")),
      };
    })
    .filter((item) => item.text);

  const hasFullText = new Set(
    records
      .filter((item) => !item.isTeaser)
      .map((item) => [item.author, item.date].join("\u0001"))
  );
  const seen = new Set();
  return records
    .filter((item) => !item.isTeaser || !hasFullText.has([item.author, item.date].join("\u0001")))
    .filter((item) => {
      const key = [item.author, item.date, compactKey(item.text)].join("\u0001");
      if (seen.has(key)) return false;
      seen.add(key);
      return true;
    })
    .map((item) => ({ ...item, ...excerptFromText(item.text) }));
}

function buildJs(reviews) {
  const publicReviews = reviews.map(({ author, date, excerpt, isTruncated }) => ({
    author,
    date,
    excerpt,
    isTruncated,
  }));

  return `(function () {
  var REVIEWS = ${JSON.stringify(publicReviews)};
  var PROFILE_URL = ${JSON.stringify(PROFILE_URL)};
  var ROOT_ID = ${JSON.stringify(ROOT_ID)};

  function isReviewsPage() {
    return (window.location.pathname || "").replace(/\\/$/, "") === "/otzivi";
  }

  function escapeHtml(value) {
    return String(value || "").replace(/[&<>"]/g, function (char) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[char];
    });
  }

  function countByYear() {
    return REVIEWS.reduce(function (acc, item) {
      var match = String(item.date || "").match(/\\d{4}$/);
      var year = match ? match[0] : "без даты";
      acc[year] = (acc[year] || 0) + 1;
      return acc;
    }, {});
  }

  function renderYearStats() {
    var counts = countByYear();
    return Object.keys(counts).sort().reverse().map(function (year) {
      return '<span class="moonn-all-reviews-stat">' + escapeHtml(year) + ': ' + counts[year] + '</span>';
    }).join('');
  }

  function renderReview(item) {
    var suffix = item.isTruncated ? '<span class="moonn-all-review-ellipsis">...</span>' : '';
    return '<article class="moonn-all-review-card">' +
      '<div class="moonn-all-review-meta"><strong>' + escapeHtml(item.author) + '</strong><span>' + escapeHtml(item.date) + '</span></div>' +
      '<p>' + escapeHtml(item.excerpt) + suffix + '</p>' +
      '<a href="' + escapeHtml(PROFILE_URL) + '" target="_blank" rel="noopener noreferrer">Открыть профиль Татьяны Мунн на Яндекс Услугах</a>' +
    '</article>';
  }

  function injectStyles() {
    if (document.getElementById(ROOT_ID + "-style")) return;
    var style = document.createElement("style");
    style.id = ROOT_ID + "-style";
    style.textContent =
      "#" + ROOT_ID + "{background:linear-gradient(135deg,#ffe1f1 0%,#f2ddff 46%,#e8f8ff 100%);padding:64px 24px 72px;color:#21172b;font-family:Arial,sans-serif;}" +
      "#" + ROOT_ID + " .moonn-all-reviews-inner{max-width:1180px;margin:0 auto;}" +
      "#" + ROOT_ID + " .moonn-all-reviews-kicker{display:inline-flex;align-items:center;gap:8px;padding:8px 12px;border-radius:999px;background:#fff4d6;color:#21172b;font-size:14px;font-weight:800;margin-bottom:16px;}" +
      "#" + ROOT_ID + " .moonn-all-reviews-kicker-mark{display:inline-grid;place-items:center;width:24px;height:24px;border-radius:8px;background:#fc0;color:#111;font-weight:900;}" +
      "#" + ROOT_ID + " h2{font-size:34px;line-height:1.15;margin:0 0 12px;letter-spacing:0;color:#21172b;}" +
      "#" + ROOT_ID + " .moonn-all-reviews-lead{max-width:860px;margin:0 0 22px;font-size:17px;line-height:1.55;color:#4b3f56;}" +
      "#" + ROOT_ID + " .moonn-all-reviews-stats{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 28px;}" +
      "#" + ROOT_ID + " .moonn-all-reviews-stat{padding:8px 10px;border-radius:999px;background:#f6f1fb;color:#4b3f56;font-size:14px;}" +
      "#" + ROOT_ID + " .moonn-all-reviews-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;}" +
      "#" + ROOT_ID + " .moonn-all-review-card{border:1px solid rgba(73,0,148,.14);border-radius:12px;padding:18px;background:rgba(255,255,255,.92);box-shadow:0 10px 28px rgba(44,28,62,.08);backdrop-filter:blur(8px);}" +
      "#" + ROOT_ID + " .moonn-all-review-meta{display:flex;justify-content:space-between;gap:12px;margin-bottom:10px;color:#21172b;}" +
      "#" + ROOT_ID + " .moonn-all-review-meta span{white-space:nowrap;color:#6c6075;}" +
      "#" + ROOT_ID + " p{white-space:pre-line;font-size:15px;line-height:1.5;margin:0 0 12px;color:#352a3e;}" +
      "#" + ROOT_ID + " .moonn-all-review-ellipsis{color:#6c6075;}" +
      "#" + ROOT_ID + " a{color:#490094;font-weight:700;text-decoration:underline;}" +
      "@media (max-width:760px){#" + ROOT_ID + "{padding:42px 16px 52px;}#" + ROOT_ID + " h2{font-size:26px;}#" + ROOT_ID + " .moonn-all-reviews-grid{grid-template-columns:1fr;}#" + ROOT_ID + " .moonn-all-review-meta{display:block;}}";
    document.head.appendChild(style);
  }

  function render() {
    if (!isReviewsPage() || document.getElementById(ROOT_ID)) return;
    var profile = document.getElementById("rec1352757161");
    var firstReview = document.getElementById("rec1353018421");
    var anchor = firstReview || profile;
    if (!anchor || !anchor.parentNode) return;
    injectStyles();
    var section = document.createElement("section");
    section.id = ROOT_ID;
    section.innerHTML = '<div class="moonn-all-reviews-inner">' +
      '<div class="moonn-all-reviews-kicker"><span class="moonn-all-reviews-kicker-mark">Я</span>Яндекс Услуги · ' + REVIEWS.length + ' фрагментов отзывов</div>' +
      '<h2>Отзывы клиентов Татьяны Мунн с 2026 по 2021 год</h2>' +
      '<p class="moonn-all-reviews-lead">Здесь показаны точные фрагменты исходных отзывов из профиля Татьяны Мунн на Яндекс Услугах. Карточки идут от новых к старым; полный список первоисточников доступен в профиле.</p>' +
      '<div class="moonn-all-reviews-stats">' + renderYearStats() + '</div>' +
      '<div class="moonn-all-reviews-grid">' + REVIEWS.map(renderReview).join('') + '</div>' +
    '</div>';
    anchor.parentNode.insertBefore(section, anchor);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", render);
  } else {
    render();
  }
})();`;
}

const reviews = readReviews();
fs.writeFileSync(OUTPUT, buildJs(reviews) + "\n", "utf8");
console.log(JSON.stringify({ output: OUTPUT, reviews: reviews.length, years: reviews.reduce((acc, item) => {
  const year = getYear(item.date);
  acc[year] = (acc[year] || 0) + 1;
  return acc;
}, {}) }, null, 2));
