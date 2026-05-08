(function(){
  var id='moonn-teen-camp-home-banner';
  var targetUrl='/podrostkovyy-lager-psihologiya';
  var imageUrl='https://cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages@b28b5f48939f8f640a218be50ac278ca24969ace/assets/teen-psychology-camp-2026/tatiana-moonn-teen-psychology-camp-hero-2026.jpg';
  function addStyle(){
    if(document.getElementById(id+'-style')) return;
    var style=document.createElement('style');
    style.id=id+'-style';
    style.textContent='.moonn-teen-camp-home-banner{font-family:Inter,Arial,sans-serif;position:relative;z-index:3;max-width:1120px;margin:28px auto;padding:28px;border-radius:28px;background:linear-gradient(135deg,rgba(249,246,255,.96),rgba(236,245,255,.96));box-shadow:0 18px 48px rgba(58,47,120,.12);border:1px solid rgba(119,87,214,.18);display:grid;grid-template-columns:minmax(0,1.25fr) minmax(260px,.75fr);gap:24px;align-items:center;overflow:hidden}.moonn-teen-camp-home-banner:before{content:"";position:absolute;width:260px;height:260px;border-radius:999px;right:-90px;top:-90px;background:radial-gradient(circle at 35% 35%,rgba(255,80,185,.42),rgba(84,170,255,.28) 55%,rgba(255,255,255,0) 72%);filter:blur(2px);pointer-events:none}.moonn-teen-camp-home-kicker{display:inline-flex;width:max-content;max-width:100%;padding:8px 12px;border-radius:999px;background:rgba(255,255,255,.75);color:#6b3bd2;font-size:13px;font-weight:700;line-height:1.2;margin-bottom:12px;box-shadow:inset 0 0 0 1px rgba(107,59,210,.16)}.moonn-teen-camp-home-title{font-size:clamp(28px,3.8vw,48px);line-height:1.05;margin:0 0 12px;color:#18205c;font-weight:900;letter-spacing:0}.moonn-teen-camp-home-text{font-size:18px;line-height:1.48;color:#4f5688;margin:0 0 20px;max-width:690px}.moonn-teen-camp-home-actions{display:flex;flex-wrap:wrap;gap:12px;align-items:center}.moonn-teen-camp-home-button{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 22px;border-radius:999px;background:linear-gradient(135deg,#7b4dff,#21b7ff);color:#fff!important;text-decoration:none!important;font-weight:800;box-shadow:0 14px 26px rgba(72,99,255,.24);transition:transform .2s ease,box-shadow .2s ease}.moonn-teen-camp-home-button:hover{transform:translateY(-2px);box-shadow:0 18px 34px rgba(72,99,255,.32)}.moonn-teen-camp-home-note{font-size:14px;color:#6b719b}.moonn-teen-camp-home-media{position:relative;border-radius:22px;overflow:hidden;box-shadow:0 18px 42px rgba(18,31,84,.18);background:#fff}.moonn-teen-camp-home-media img{display:block;width:100%;height:auto;aspect-ratio:4/3;object-fit:cover}.moonn-teen-camp-home-badge{position:absolute;left:14px;bottom:14px;padding:9px 12px;border-radius:14px;background:rgba(255,255,255,.9);color:#18205c;font-size:13px;font-weight:800;box-shadow:0 8px 24px rgba(18,31,84,.12)}@media(max-width:860px){.moonn-teen-camp-home-banner{grid-template-columns:1fr;margin:22px 16px;padding:22px;border-radius:22px}.moonn-teen-camp-home-text{font-size:16px}.moonn-teen-camp-home-media{order:-1}.moonn-teen-camp-home-button{width:100%}}';
    document.head.appendChild(style);
  }
  function mount(){
    if(document.getElementById(id)) return;
    var root=document.querySelector('#allrecords')||document.body;
    if(!root) return;
    addStyle();
    var records=Array.prototype.slice.call(root.querySelectorAll('.r'));
    var anchor=records.find(function(el){return el.offsetHeight>180;}) || records[0] || root.firstElementChild;
    var banner=document.createElement('section');
    banner.id=id;
    banner.className='moonn-teen-camp-home-banner';
    banner.setAttribute('aria-label','Подростковый лагерь по психологии');
    banner.innerHTML='<div><div class="moonn-teen-camp-home-kicker">6-10 июля · Москва · подростки 3-5 человек</div><h2 class="moonn-teen-camp-home-title">Подростковый лагерь по психологии</h2><p class="moonn-teen-camp-home-text">Пять дней практики с Татьяной Мунн: эмоции, уверенность, общение, безопасная камерная группа и городские задания в центре Москвы.</p><div class="moonn-teen-camp-home-actions"><a class="moonn-teen-camp-home-button" href="'+targetUrl+'">Узнать программу</a><span class="moonn-teen-camp-home-note">Цветной бульвар · 10:00-18:00</span></div></div><a class="moonn-teen-camp-home-media" href="'+targetUrl+'" aria-label="Открыть страницу подросткового лагеря"><img src="'+imageUrl+'" alt="Подростковый психологический лагерь Татьяны Мунн в Москве"><span class="moonn-teen-camp-home-badge">Летняя программа 2026</span></a>';
    if(anchor && anchor.parentNode){anchor.parentNode.insertBefore(banner, anchor.nextSibling);} else {root.insertBefore(banner, root.firstChild);}
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', mount); else mount();
})();
