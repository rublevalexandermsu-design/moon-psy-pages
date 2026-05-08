(function () {
  'use strict';

  var POLICY_URL = '/politic';
  var POLICY_TITLE = 'Политика обработки персональных данных';
  var CONSENT_TEXT = 'Я согласен(на) на обработку персональных данных в соответствии с политикой обработки персональных данных, а также ознакомлен(а) с использованием cookies и Яндекс.Метрики.';
  var COOKIE_KEY = 'moonn_cookie_notice_accepted_v1';

  function ready(fn) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fn);
    } else {
      fn();
    }
  }

  function el(tag, attrs, text) {
    var node = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (key) {
      if (key === 'className') node.className = attrs[key];
      else node.setAttribute(key, attrs[key]);
    });
    if (text) node.textContent = text;
    return node;
  }

  function injectStyles() {
    if (document.getElementById('moonn-privacy-compliance-style')) return;
    var style = el('style', { id: 'moonn-privacy-compliance-style' });
    style.textContent = [
      '.moonn-consent-box{margin:14px 0 10px;font:14px/1.45 Arial,sans-serif;color:#272235}',
      '.moonn-consent-box label{display:flex;align-items:flex-start;gap:10px;cursor:pointer}',
      '.moonn-consent-box input{width:18px;height:18px;margin-top:2px;flex:0 0 auto}',
      '.moonn-consent-box a{color:#6b35d7;text-decoration:underline}',
      '.moonn-consent-error{display:none;margin-top:8px;color:#b00020;font-size:13px}',
      '.moonn-cookie-notice{position:fixed;left:18px;right:18px;bottom:18px;z-index:2147483000;display:flex;gap:16px;align-items:center;justify-content:space-between;padding:16px 18px;border:1px solid rgba(107,53,215,.22);border-radius:16px;background:rgba(255,255,255,.96);box-shadow:0 16px 45px rgba(43,31,84,.18);font:14px/1.45 Arial,sans-serif;color:#272235;backdrop-filter:blur(10px)}',
      '.moonn-cookie-notice a{color:#6b35d7;text-decoration:underline}',
      '.moonn-cookie-notice button{border:0;border-radius:999px;background:linear-gradient(90deg,#6b35d7,#27b6e8);color:#fff;padding:10px 18px;font-weight:700;cursor:pointer;white-space:nowrap}',
      '@media(max-width:640px){.moonn-cookie-notice{display:block}.moonn-cookie-notice button{margin-top:12px;width:100%}}',
      '.moonn-policy-rewrite{max-width:960px;margin:40px auto;padding:0 20px 70px;font:17px/1.65 Arial,sans-serif;color:#231f2f}',
      '.moonn-policy-rewrite h1{font-size:36px;line-height:1.15;margin:0 0 24px;color:#4a2297}',
      '.moonn-policy-rewrite h2{font-size:24px;line-height:1.25;margin:34px 0 12px;color:#33214f}',
      '.moonn-policy-rewrite ul{padding-left:24px}',
      '.moonn-policy-rewrite a{color:#6b35d7;text-decoration:underline}'
    ].join('\n');
    document.head.appendChild(style);
  }

  function ensureConsentForForm(form) {
    if (!form || form.getAttribute('data-moonn-consent-ready') === '1') return;
    form.setAttribute('data-moonn-consent-ready', '1');

    var box = el('div', { className: 'moonn-consent-box', 'data-moonn-consent': 'true' });
    var label = el('label');
    var checkbox = el('input', {
      type: 'checkbox',
      required: 'required',
      name: 'moonn_personal_data_consent',
      value: 'accepted'
    });
    var span = el('span');
    span.appendChild(document.createTextNode('Я согласен(на) на обработку персональных данных в соответствии с '));
    span.appendChild(el('a', { href: POLICY_URL, target: '_blank', rel: 'noopener' }, 'политикой обработки персональных данных'));
    span.appendChild(document.createTextNode(', а также ознакомлен(а) с использованием cookies и Яндекс.Метрики.'));
    label.appendChild(checkbox);
    label.appendChild(span);
    box.appendChild(label);
    var error = el('div', { className: 'moonn-consent-error' }, 'Чтобы отправить форму, отметьте согласие на обработку персональных данных.');
    box.appendChild(error);

    var submit = form.querySelector('[type="submit"], .t-submit, button');
    if (submit && submit.parentNode) {
      submit.parentNode.insertBefore(box, submit);
    } else {
      form.appendChild(box);
    }

    form.addEventListener('submit', function (event) {
      if (!checkbox.checked) {
        event.preventDefault();
        event.stopPropagation();
        error.style.display = 'block';
        checkbox.focus();
      }
    }, true);
  }

  function enhanceForms() {
    var forms = Array.prototype.slice.call(document.querySelectorAll('form'));
    forms.forEach(ensureConsentForForm);
  }

  function showCookieNotice() {
    try {
      if (localStorage.getItem(COOKIE_KEY) === '1') return;
    } catch (error) {
      return;
    }
    if (document.getElementById('moonn-cookie-notice')) return;
    var notice = el('div', { id: 'moonn-cookie-notice', className: 'moonn-cookie-notice', role: 'dialog', 'aria-label': 'Уведомление cookies' });
    var text = el('div');
    text.appendChild(document.createTextNode('Сайт использует cookies и Яндекс.Метрику, включая аналитику посещений, карту кликов и Webvisor, чтобы улучшать работу страниц. Подробнее — в '));
    text.appendChild(el('a', { href: POLICY_URL }, 'политике обработки персональных данных'));
    text.appendChild(document.createTextNode('.'));
    var button = el('button', { type: 'button' }, 'Понятно');
    button.addEventListener('click', function () {
      try { localStorage.setItem(COOKIE_KEY, '1'); } catch (error) {}
      notice.remove();
    });
    notice.appendChild(text);
    notice.appendChild(button);
    document.body.appendChild(notice);
  }

  function policyHtml() {
    return [
      '<main class="moonn-policy-rewrite" data-moonn-policy-rewrite="true">',
      '<h1>Политика обработки персональных данных</h1>',
      '<p>Настоящая Политика определяет порядок обработки персональных данных пользователей сайта <a href="https://moonn.ru/">https://moonn.ru/</a>.</p>',
      '<p><strong>Оператор:</strong> индивидуальный предприниматель Кумскова Татьяна Михайловна, ИНН 770906685276, ОГРНИП 316774600553212. Электронная почта для обращений по персональным данным: <a href="mailto:moonn.official@yandex.ru">moonn.official@yandex.ru</a>.</p>',
      '<h2>Цели обработки</h2>',
      '<ul><li>обработка заявок на консультации, лекции, курсы, мероприятия и иные услуги;</li><li>связь с пользователем по оставленной заявке;</li><li>запись на мероприятия и информационные рассылки при отдельном согласии;</li><li>обработка платежей и предоставление доступа к оплаченным продуктам, если такие продукты подключены;</li><li>аналитика работы сайта, улучшение структуры страниц и удобства использования;</li><li>исполнение требований законодательства и рассмотрение обращений субъектов персональных данных.</li></ul>',
      '<h2>Категории данных</h2>',
      '<p>В зависимости от формы пользователь может передать имя, телефон, адрес электронной почты, текст сообщения, сведения о выбранной услуге или мероприятии. Также сайт может обрабатывать технические данные: IP-адрес, cookie, сведения о браузере, устройстве, источнике перехода и действиях на сайте.</p>',
      '<h2>Правовые основания</h2>',
      '<p>Обработка осуществляется на основании согласия субъекта персональных данных, необходимости исполнения договора или подготовки к его заключению по запросу пользователя, обязанностей оператора по законодательству РФ, а также законного интереса оператора в обеспечении работоспособности и безопасности сайта.</p>',
      '<h2>Порядок обработки</h2>',
      '<p>Оператор может совершать сбор, запись, систематизацию, накопление, хранение, уточнение, использование, передачу в необходимых случаях, обезличивание, блокирование, удаление и уничтожение персональных данных. Срок обработки определяется достижением целей обработки, отзывом согласия, прекращением обязательств или требованиями законодательства.</p>',
      '<h2>Cookies, Яндекс.Метрика и Webvisor</h2>',
      '<p>Сайт использует cookies и Яндекс.Метрику для аналитики посещаемости, карты кликов, Webvisor, отслеживания переходов по ссылкам и улучшения работы страниц. Пользователь может ограничить cookies в настройках браузера; при отключении cookies часть функций сайта может работать некорректно.</p>',
      '<h2>Сервисы</h2>',
      '<p>Для работы сайта могут использоваться Tilda Publishing, Яндекс.Метрика, Timepad, платёжные сервисы, почтовые и коммуникационные сервисы. Состав сервисов может обновляться при изменении сайта и способов записи на услуги.</p>',
      '<h2>Права пользователя</h2>',
      '<p>Пользователь вправе получить сведения об обработке персональных данных, потребовать уточнения, блокирования или удаления данных, а также отозвать согласие. Обращения направляются на <a href="mailto:moonn.official@yandex.ru">moonn.official@yandex.ru</a>.</p>',
      '<h2>Согласие на обработку персональных данных</h2>',
      '<p>Проставляя отдельную галочку в форме на сайте, пользователь свободно, своей волей и в своём интересе даёт согласие оператору на обработку персональных данных для целей, указанных в настоящей Политике. Согласие действует до достижения целей обработки или до его отзыва.</p>',
      '<h2>Актуализация</h2>',
      '<p>Оператор вправе обновлять Политику при изменении сайта, сервисов, целей обработки или требований законодательства. Актуальная версия размещается на этой странице.</p>',
      '</main>'
    ].join('');
  }

  function rewritePolicyPage() {
    var path = window.location.pathname.replace(/\/+$/, '');
    if (path !== '/politic') return;
    var records = document.getElementById('allrecords');
    if (!records || records.getAttribute('data-moonn-policy-rewritten') === '1') return;
    records.setAttribute('data-moonn-policy-rewritten', '1');
    records.innerHTML = policyHtml();
    document.title = POLICY_TITLE + ' — Татьяна Мунн';
    var description = document.querySelector('meta[name="description"]');
    if (!description) {
      description = el('meta', { name: 'description' });
      document.head.appendChild(description);
    }
    description.setAttribute('content', 'Политика обработки персональных данных сайта moonn.ru: оператор ИП Кумскова Татьяна Михайловна, формы, cookies, Яндекс.Метрика и порядок обращений.');
  }

  ready(function () {
    injectStyles();
    rewritePolicyPage();
    enhanceForms();
    showCookieNotice();
    setTimeout(enhanceForms, 1200);
    setTimeout(enhanceForms, 3000);
  });
})();
