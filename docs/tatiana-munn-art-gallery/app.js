
const drawer = document.getElementById('purchaseDrawer');
const purchaseArtwork = document.getElementById('purchaseArtwork');

function openPurchase(title) {
  if (title && purchaseArtwork) purchaseArtwork.value = title;
  drawer?.setAttribute('aria-hidden', 'false');
}
function closePurchase() { drawer?.setAttribute('aria-hidden', 'true'); }

document.querySelectorAll('[data-open-purchase]').forEach((button) => {
  button.addEventListener('click', () => openPurchase(button.dataset.artTitle || purchaseArtwork?.value));
});
document.querySelectorAll('[data-close-purchase]').forEach((button) => button.addEventListener('click', closePurchase));

document.querySelector('[data-copy-request]')?.addEventListener('click', () => {
  const form = drawer?.querySelector('form');
  const data = new FormData(form);
  const text = [
    'Здравствуйте. Хочу обсудить покупку картины Татьяны Мунн.',
    `Картина: ${data.get('artwork') || ''}`,
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

window.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    closePurchase();
    document.getElementById('artModal')?.setAttribute('aria-hidden', 'true');
  }
});
