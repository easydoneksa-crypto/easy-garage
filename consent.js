/* Easy Garage — cookie & ads consent (Saudi PDPL: opt-in before advertising cookies).
   Ads stay paused until the visitor accepts. Choice is stored on this device only. */
(function(){
  var KEY="eg-consent",c=null;
  try{c=localStorage.getItem(KEY)}catch(e){}
  window.adsbygoogle=window.adsbygoogle||[];
  window.adsbygoogle.pauseAdRequests=(c==="yes")?0:1;
  window.EG_CONSENT=c;
  var T={
    ar:["نستخدم ملفات تعريف الارتباط لعرض الإعلانات فقط، ولا نجمع اسمك أو أي بيانات شخصية. توافق على الإعلانات؟","موافق","رفض","سياسة الخصوصية"],
    en:["We use cookies only to show ads. We don’t collect your name or any personal details. Allow ads?","Allow","Decline","Privacy policy"],
    it:["Usiamo i cookie solo per mostrare pubblicità. Non raccogliamo il tuo nome né dati personali. Consenti la pubblicità?","Consenti","Rifiuta","Privacy"],
    es:["Usamos cookies solo para mostrar anuncios. No recopilamos tu nombre ni datos personales. ¿Permitir anuncios?","Permitir","Rechazar","Privacidad"],
    zh:["我们仅使用 Cookie 来显示广告，不收集你的姓名或任何个人信息。允许显示广告吗？","允许","拒绝","隐私政策"],
    ru:["Мы используем cookie только для показа рекламы и не собираем ваше имя или личные данные. Разрешить рекламу?","Разрешить","Отклонить","Конфиденциальность"],
    ja:["広告表示のためだけに Cookie を使用します。名前や個人情報は収集しません。広告を許可しますか？","許可","拒否","プライバシー"],
    tr:["Çerezleri yalnızca reklam göstermek için kullanıyoruz. Adınızı veya kişisel bilgilerinizi toplamıyoruz. Reklamlara izin veriyor musunuz?","İzin ver","Reddet","Gizlilik"]
  };
  function lang(){var l=(document.documentElement.lang||"en").slice(0,2).toLowerCase();return T[l]?l:"en"}
  function base(){return /\/(ar|en|it|es|zh|ru|ja|tr)\/?(index\.html)?$/.test(location.pathname)?"../":""}
  function set(v){try{localStorage.setItem(KEY,v)}catch(e){}window.EG_CONSENT=v;
    if(v==="yes"){window.adsbygoogle.pauseAdRequests=0}else{window.adsbygoogle.pauseAdRequests=1}
    var b=document.getElementById("egc");if(b)b.remove()}
  window.EG_resetConsent=function(){try{localStorage.removeItem(KEY)}catch(e){}window.adsbygoogle.pauseAdRequests=1;show()};
  function show(){
    if(document.getElementById("egc"))return;
    var t=T[lang()],rtl=lang()==="ar",d=document.createElement("div");d.id="egc";d.setAttribute("role","dialog");d.setAttribute("aria-live","polite");d.dir=rtl?"rtl":"ltr";
    d.style.cssText="position:fixed;left:8px;right:8px;bottom:calc(8px + env(safe-area-inset-bottom,0px));z-index:2147483000;max-width:640px;margin:0 auto;background:#1f2327;color:#eef1f4;border:2px solid #ffc61a;border-radius:14px;padding:12px 14px;font:14px/1.5 system-ui,-apple-system,Segoe UI,Tahoma,sans-serif;box-shadow:0 10px 30px rgba(0,0,0,.6);display:flex;flex-wrap:wrap;gap:10px;align-items:center";
    var p=document.createElement("p");p.style.cssText="margin:0;flex:1 1 260px";p.textContent=t[0]+" ";
    var a=document.createElement("a");a.href=base()+"privacy.html";a.target="_blank";a.rel="noopener";a.textContent=t[3];a.style.color="#ffc61a";p.appendChild(a);
    function btn(txt,prim,v){var b=document.createElement("button");b.type="button";b.textContent=txt;b.style.cssText="border:0;border-radius:10px;padding:9px 16px;font:700 14px system-ui,sans-serif;cursor:pointer;"+(prim?"background:#ffc61a;color:#111":"background:#3a3f45;color:#fff");b.onclick=function(){set(v)};return b}
    d.appendChild(p);d.appendChild(btn(t[1],true,"yes"));d.appendChild(btn(t[2],false,"no"));
    (document.body||document.documentElement).appendChild(d);
  }
  var OWN=/(^|\.)easygaragesimulator\.com$/.test(location.hostname);
  /* Visit counter (GoatCounter): no cookies, no personal data, IP not stored. Own domain only, never on itch.io or in the app. */
  if(OWN){var g=document.createElement("script");g.async=true;g.src="https://gc.zgo.at/count.js";g.setAttribute("data-goatcounter","https://easygarage.goatcounter.com/count");(document.head||document.documentElement).appendChild(g)}
  if(OWN&&c!=="yes"&&c!=="no"){if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",show);else show()}
})();
