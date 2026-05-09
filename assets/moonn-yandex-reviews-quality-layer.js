(function () {
  var PROFILE_URL = "https://uslugi.yandex.ru/profile/TatyanaKumskovamunn-948629";
  var REVIEW_URL = PROFILE_URL + "?action=addReview";
  var PATCH_MARKER = "moonn-yandex-reviews-quality-layer";

  function isReviewsPage() {
    return (window.location.pathname || "").replace(/\/$/, "") === "/otzivi";
  }

  function normalize(text) {
    return (text || "").replace(/\s+/g, " ").trim();
  }

  function replaceWeakSeoText() {
    var nodes = Array.prototype.slice.call(document.querySelectorAll("p, div, span"));
    var targets = nodes.filter(function (node) {
      var text = normalize(node.textContent);
      return text.indexOf("дублирую информацию") !== -1 || text.indexOf("поиска информации в интернете") !== -1;
    });
    targets.forEach(function (node) {
      if (node.dataset && node.dataset.moonnReviewQualityPatched) return;
      node.innerHTML =
        'На этой странице собраны отзывы клиентов и участников мероприятий Татьяны Мунн. ' +
        'Каждый отзыв связан с исходным профилем на Яндекс Услугах, чтобы можно было перейти к первоисточнику и проверить контекст публикации. ' +
        '<a href="' + PROFILE_URL + '" target="_blank" rel="noopener noreferrer">Открыть профиль на Яндекс Услугах</a>.';
      if (node.dataset) node.dataset.moonnReviewQualityPatched = "true";
    });
  }

  function addSourcePanel() {
    if (document.getElementById(PATCH_MARKER)) return;
    var heading = Array.prototype.slice.call(document.querySelectorAll("h1, h2")).find(function (item) {
      return /отзывы/i.test(item.textContent || "");
    });
    if (!heading) return;
    var panel = document.createElement("section");
    panel.id = PATCH_MARKER;
    panel.setAttribute("aria-label", "Источник отзывов");
    panel.style.cssText =
      "max-width:960px;margin:28px auto;padding:22px;border:1px solid rgba(73,0,148,.16);border-radius:18px;background:#fff;color:#1f1726;font-family:Arial,sans-serif;line-height:1.5;";
    panel.innerHTML =
      '<h2 style="margin:0 0 10px;font-size:24px;line-height:1.2;">Проверяемые отзывы с Яндекс Услуг</h2>' +
      '<p style="margin:0 0 14px;">Отзывы на странице приведены с указанием источника. Перейдите в профиль Яндекс Услуг, чтобы посмотреть карточку специалиста и оставить новый отзыв после консультации, лекции или мероприятия.</p>' +
      '<p style="margin:0;display:flex;gap:12px;flex-wrap:wrap;">' +
      '<a style="color:#490094;font-weight:700;" href="' + PROFILE_URL + '" target="_blank" rel="noopener noreferrer">Профиль на Яндекс Услугах</a>' +
      '<a style="color:#490094;font-weight:700;" href="' + REVIEW_URL + '" target="_blank" rel="noopener noreferrer">Оставить отзыв</a>' +
      '</p>';
    heading.parentNode.insertBefore(panel, heading.nextSibling);
  }

  function run() {
    if (!isReviewsPage()) return;
    replaceWeakSeoText();
    addSourcePanel();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
