(function () {
  var PROFILE_URL = "https://uslugi.yandex.ru/profile/TatyanaKumskovamunn-948629";
  var REVIEW_URL = PROFILE_URL + "?action=addReview";
  var PATCH_MARKER = "moonn-yandex-reviews-quality-layer";
  var TOP_HERO_ID = "rec1353100721";
  var PROFILE_BLOCK_ID = "rec1352757161";
  var REVIEWS_INTRO_ID = "rec1353045131";
  var FIRST_REVIEW_ID = "rec1353018421";

  function isReviewsPage() {
    return (window.location.pathname || "").replace(/\/$/, "") === "/otzivi";
  }

  function addSourcePanel() {
    if (document.getElementById(PATCH_MARKER)) return;
    var intro = document.getElementById(REVIEWS_INTRO_ID);
    var profile = document.getElementById(PROFILE_BLOCK_ID);
    var anchor = intro || profile || document.querySelector(".r, [id^='rec']");
    if (!anchor || !anchor.parentNode) return;
    var panel = document.createElement("section");
    panel.id = PATCH_MARKER;
    panel.setAttribute("aria-label", "Источник отзывов");
    panel.style.cssText =
      "position:relative;z-index:30;overflow:hidden;max-width:1060px;margin:28px auto;padding:26px;border:1px solid rgba(33,23,38,.12);border-radius:18px;background:#fff;color:#1f1726;font-family:Arial,sans-serif;line-height:1.5;box-shadow:0 16px 44px rgba(44,28,62,.08);";
    panel.innerHTML =
      '<div style="display:flex;gap:18px;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;margin:0 0 16px;">' +
      '<div style="display:inline-flex;align-items:center;gap:10px;padding:10px 14px;border-radius:14px;background:#fff4d6;font-weight:800;color:#21172b;">' +
      '<span style="display:inline-grid;place-items:center;width:28px;height:28px;border-radius:9px;background:#fc0;color:#111;font-weight:900;">Я</span>' +
      '<span>Яндекс Услуги</span>' +
      '</div>' +
      '<div style="display:flex;gap:8px;flex-wrap:wrap;color:#4b3f56;font-size:14px;">' +
      '<span style="padding:8px 10px;border-radius:999px;background:#f6f1fb;">190 оценок</span>' +
      '<span style="padding:8px 10px;border-radius:999px;background:#f6f1fb;">актуальные отзывы 2026</span>' +
      '</div>' +
      '</div>' +
      '<h2 style="margin:0 0 10px;font-size:26px;line-height:1.2;">Проверяемые отзывы с Яндекс Услуг</h2>' +
      '<p style="margin:0 0 14px;">На этой странице собраны отзывы клиентов и участников мероприятий Татьяны Мунн с привязкой к исходному профилю на Яндекс Услугах. Самые новые найденные отзывы относятся к 2026 году.</p>' +
      '<p style="margin:0;display:flex;gap:12px;flex-wrap:wrap;">' +
      '<a style="color:#490094;font-weight:700;" href="' + PROFILE_URL + '" target="_blank" rel="noopener noreferrer">Профиль на Яндекс Услугах</a>' +
      '<a style="color:#490094;font-weight:700;" href="' + REVIEW_URL + '" target="_blank" rel="noopener noreferrer">Оставить отзыв</a>' +
      '</p>';
    anchor.parentNode.insertBefore(panel, anchor.nextSibling);
  }

  function removeLeakedHeadCodeText() {
    Array.prototype.slice.call(document.body.childNodes).forEach(function (node) {
      if (node.nodeType !== Node.TEXT_NODE) return;
      var text = (node.nodeValue || "").trim();
      if (!text) return;
      var looksLikeLeakedHead =
        text.indexOf("<!-- moonn-radiant-sanctuary-theme:start -->") !== -1 ||
        text.indexOf("moonn-yandex-reviews-quality-layer") !== -1 ||
        text.indexOf("cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages") !== -1;
      if (looksLikeLeakedHead) {
        node.parentNode.removeChild(node);
      }
    });
  }

  function reorderIntroBlocks() {
    var records = document.getElementById("allrecords");
    var hero = document.getElementById(TOP_HERO_ID);
    var profile = document.getElementById(PROFILE_BLOCK_ID);
    var intro = document.getElementById(REVIEWS_INTRO_ID);
    var firstReview = document.getElementById(FIRST_REVIEW_ID);
    if (!records || !hero || !profile || !intro || !firstReview) return;

    records.insertBefore(intro, hero);
    records.insertBefore(profile, firstReview);

    var reviewTail = firstReview;
    while (reviewTail && reviewTail.nextElementSibling) {
      var text = (reviewTail.nextElementSibling.innerText || "").replace(/\s+/g, " ").trim();
      if (text.indexOf("Психолог Татьяна Мунн Отзыв клиента") === -1) break;
      reviewTail = reviewTail.nextElementSibling;
    }
    if (reviewTail && reviewTail.nextElementSibling !== hero) {
      records.insertBefore(hero, reviewTail.nextElementSibling);
    }
    hero.setAttribute("data-moonn-moved-down", "true");
  }

  function addLayoutStyles() {
    if (document.getElementById("moonn-yandex-reviews-layout-style")) return;
    var style = document.createElement("style");
    style.id = "moonn-yandex-reviews-layout-style";
    style.textContent =
      "#rec1353045131{background:#fff!important;}" +
      "#rec1353045131 .t-title,#rec1353045131 .t-heading,#rec1353045131 .tn-atom{color:#21172b!important;}" +
      "#rec1353368171{display:none!important;}" +
      "#rec1353100721[data-moonn-moved-down='true']{display:none!important;}" +
      "#moonn-yandex-reviews-quality-layer{box-sizing:border-box;}" +
      "@media (max-width:640px){#moonn-yandex-reviews-quality-layer{margin-left:16px!important;margin-right:16px!important;padding:18px!important;}}";
    document.head.appendChild(style);
  }

  function run() {
    if (!isReviewsPage()) return;
    removeLeakedHeadCodeText();
    reorderIntroBlocks();
    addLayoutStyles();
    addSourcePanel();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
