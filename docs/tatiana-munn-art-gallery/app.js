
const drawer = document.getElementById('purchaseDrawer');
const purchaseArtwork = document.getElementById('purchaseArtwork');
const artworksData = JSON.parse(document.getElementById('artworksData')?.textContent || '[]');
const artworksById = new Map(artworksData.map((art) => [art.id, art]));
const artworksByTitle = new Map(artworksData.map((art) => [art.title, art]));
const assetBase = window.MOONN_ART_GALLERY_BASE_URL || '';

function assetUrl(path) {
  if (!path || /^https?:\/\//i.test(path) || path.startsWith('data:')) return path;
  if (!assetBase) return path;
  return `${assetBase.replace(/\/?$/, '/')}${String(path).replace(/^\.?\//, '')}`;
}

function resolveArtwork(value) {
  if (!value) return artworksData[0] || null;
  return artworksById.get(value) || artworksByTitle.get(value) || artworksData.find((art) => art.title === value) || artworksData[0] || null;
}

function openPurchase(artworkOrTitle) {
  const art = typeof artworkOrTitle === 'object' ? artworkOrTitle : resolveArtwork(artworkOrTitle);
  if (art && purchaseArtwork) purchaseArtwork.value = art.title;
  drawer?.setAttribute('aria-hidden', 'false');
}
function closePurchase() { drawer?.setAttribute('aria-hidden', 'true'); }

function initTildaCart() {
  const cartRecord = document.querySelector('[data-record-type="706"][id]');
  if (!cartRecord || typeof window.t_onFuncLoad !== 'function') return;
  window.t_onFuncLoad('tcart__init', () => {
    try {
      window.tcart__init(cartRecord.id.replace(/^rec/, ''), { cssClassName: '' });
    } catch (error) {
      console.warn('Moonn art cart init skipped', error);
    }
  });
}

function repairTildaOrderFormHandlers() {
  const cartRecord = document.querySelector('[data-record-type="706"][id]');
  const form = document.querySelector('.t706__cartwin form.js-form-proccess');
  if (!cartRecord || !form) return;
  try {
    if (window.initForms && cartRecord.id) delete window.initForms[cartRecord.id];
    if (typeof window.t_forms__initFormFields === 'function') window.t_forms__initFormFields(cartRecord);
    if (typeof window.t_forms__addInputItsGood === 'function') window.t_forms__addInputItsGood(cartRecord);
    if (typeof window.t_forms__addAttrAction === 'function') window.t_forms__addAttrAction(cartRecord);
    if (typeof window.t_forms__onSubmit === 'function') window.t_forms__onSubmit(cartRecord);
    if (typeof window.t_forms__onClick === 'function') window.t_forms__onClick(cartRecord);
    if (typeof window.t_forms__onRender === 'function') window.t_forms__onRender(cartRecord);
    if (typeof window.t_forms__addFocusOnTab === 'function') window.t_forms__addFocusOnTab(cartRecord);
  } catch (error) {
    console.warn('Moonn art order form repair skipped', error);
  }
}

function enhanceTildaPaymentUi() {
  const cart = document.querySelector('.t706__cartwin, .t706');
  if (!cart) return;
  repairTildaOrderFormHandlers();
  cart.querySelectorAll('.t-submit, button[type="submit"], .t-btnflex_type_submit').forEach((submit) => {
    const submitText = submit.querySelector('.t-btnflex__text, span') || submit;
    if ((submitText.textContent || '').trim() !== 'Перейти к оплате') submitText.textContent = 'Перейти к оплате';
    submit.setAttribute('aria-label', 'Перейти к оплате через T-Bank');
  });
}

function openArtworkPayment(art) {
  if (!art) return false;
  initTildaCart();
  if (typeof window.tcart__addProduct !== 'function' || typeof window.tcart__openCart !== 'function') return false;
  const image = art.checkoutImage || assetUrl(art.image);
  const product = {
    name: art.checkoutName || `${art.title} — картина Татьяны Мунн`,
    price: Number(art.priceValue || 0),
    amount: Number(art.priceValue || 0),
    quantity: 1,
    img: image,
    sku: art.sku || art.id,
  };
  try {
    if (window.tcart && Array.isArray(window.tcart.products)) window.tcart.products = [];
    window.tcart__addProduct(product);
    if (typeof window.tcart__reDrawCartIcon === 'function') window.tcart__reDrawCartIcon();
    window.tcart__openCart();
    setTimeout(enhanceTildaPaymentUi, 200);
    setTimeout(enhanceTildaPaymentUi, 900);
    return true;
  } catch (error) {
    console.warn('Moonn art payment open skipped', error);
    return false;
  }
}

initTildaCart();
setTimeout(initTildaCart, 300);
setTimeout(initTildaCart, 1200);
setInterval(enhanceTildaPaymentUi, 1500);

document.querySelectorAll('[data-open-purchase]').forEach((button) => {
  button.addEventListener('click', (event) => {
    event.preventDefault();
    const art = resolveArtwork(button.dataset.artId || button.dataset.artTitle || purchaseArtwork?.value);
    if (!openArtworkPayment(art)) openPurchase(art);
  });
});
document.querySelectorAll('[data-close-purchase]').forEach((button) => button.addEventListener('click', closePurchase));

document.querySelector('[data-copy-request]')?.addEventListener('click', () => {
  const form = drawer?.querySelector('form');
  const data = new FormData(form);
  const text = [
    'Здравствуйте. Хочу обсудить покупку картины Татьяны Мунн.',
    `Картина: ${data.get('artwork') || ''}`,
    `Стоимость: ${(resolveArtwork(data.get('artwork')) || {}).price || ''}`,
    `Имя: ${data.get('name') || ''}`,
    `Контакт: ${data.get('contact') || ''}`,
    `Комментарий: ${data.get('message') || ''}`,
  ].join('\n');
  navigator.clipboard?.writeText(text);
  const toast = document.createElement('div');
  toast.className = 'copy-toast';
  toast.textContent = 'Текст заявки скопирован';
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 1800);
});

function calculatePersonalCode(seed) {
  let hash = 2166136261;
  for (let i = 0; i < seed.length; i += 1) {
    hash ^= seed.charCodeAt(i);
    hash = Math.imul(hash, 16777619);
  }
  const n = Math.abs(hash >>> 0);
  const a = String(100 + (n % 900));
  const b = String(100 + (Math.floor(n / 997) % 900));
  const c = String(100 + (Math.floor(n / 7919) % 900));
  return `${a} ${b} ${c}`;
}

const codeForm = document.getElementById('codeForm');
function updateCode() {
  if (!codeForm) return;
  const fio = document.getElementById('fio')?.value || '';
  const birth = document.getElementById('birth')?.value || '';
  const time = document.getElementById('birthTime')?.value || '';
  const request = document.getElementById('request')?.value || '';
  const code = calculatePersonalCode(`${fio}|${birth}|${time}|${request}|TatianaMoonn`);
  document.querySelectorAll('.js-code').forEach((node) => { node.textContent = code; });
}
codeForm?.addEventListener('submit', (event) => { event.preventDefault(); updateCode(); });
codeForm?.addEventListener('input', updateCode);
updateCode();
window.MoonnArtGalleryPayment = { artworks: artworksData, openArtworkPayment, openPurchase };

window.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    closePurchase();
    document.getElementById('artModal')?.setAttribute('aria-hidden', 'true');
  }
});
