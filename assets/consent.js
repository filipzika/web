/* Cookie consent + Google tag (Consent Mode v2, basic mode).
   Google tag loads only after the visitor accepts marketing cookies. */
(function () {
  var TAG_ID = 'AW-18438073048';
  var KEY = 'fb_consent';
  var MAX_AGE = 365 * 24 * 60 * 60 * 1000; // ask again after 12 months

  var en = (document.documentElement.lang || '').toLowerCase().indexOf('en') === 0;
  var T = en ? {
    text: 'We use cookies to measure the results of our Google Ads campaigns. They are only set if you allow them.',
    more: 'Details',
    moreHref: '/en/cookies.html',
    accept: 'Allow',
    reject: 'Decline',
    label: 'Cookie consent'
  } : {
    text: 'Cookies používáme k měření výsledků našich kampaní v Google Ads. Uložíme je jen s vaším svolením.',
    more: 'Podrobnosti',
    moreHref: '/cookies.html',
    accept: 'Povolit',
    reject: 'Odmítnout',
    label: 'Souhlas s cookies'
  };

  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;

  gtag('consent', 'default', {
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    analytics_storage: 'denied',
    functionality_storage: 'granted',
    security_storage: 'granted'
  });

  function read() {
    try {
      var v = JSON.parse(localStorage.getItem(KEY));
      if (v && (v.s === 'granted' || v.s === 'denied') && Date.now() - v.t < MAX_AGE) return v.s;
    } catch (e) {}
    return null;
  }

  function save(state) {
    try { localStorage.setItem(KEY, JSON.stringify({ s: state, t: Date.now() })); } catch (e) {}
  }

  var tagLoaded = false;
  function loadTag() {
    if (tagLoaded) return;
    tagLoaded = true;
    if (document.querySelector('script[src*="googletagmanager.com/gtag/js"]')) return;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + TAG_ID;
    document.head.appendChild(s);
    gtag('js', new Date());
    gtag('config', TAG_ID);
  }

  function grant() {
    gtag('consent', 'update', {
      ad_storage: 'granted',
      ad_user_data: 'granted',
      ad_personalization: 'granted'
    });
    loadTag();
  }

  function clearAdCookies() {
    var host = location.hostname.replace(/^www\./, '');
    document.cookie.split(';').forEach(function (c) {
      var name = c.split('=')[0].trim();
      if (/^_gcl_|^_gac_/.test(name)) {
        ['', '; domain=' + host, '; domain=.' + host].forEach(function (d) {
          document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + d;
        });
      }
    });
  }

  function deny() {
    gtag('consent', 'update', {
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied'
    });
    clearAdCookies();
  }

  var CSS =
    '.fbc{position:fixed;left:0;right:0;margin:0 auto;bottom:16px;z-index:9999;width:calc(100% - 32px);max-width:420px;' +
    'box-sizing:border-box;padding:16px 16px 14px;border-radius:16px;' +
    'background:rgba(28,27,36,.94);-webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px);' +
    'border:1px solid rgba(106,97,217,.28);box-shadow:0 12px 32px rgba(0,0,0,.45);' +
    'font-family:"Satoshi",system-ui,sans-serif;color:#fefdf9;' +
    'opacity:0;transform:translateY(8px);transition:opacity .25s ease,transform .25s ease}' +
    '.fbc.fbc-in{opacity:1;transform:none}' +
    '.fbc p{margin:0 0 12px;font-size:14px;line-height:1.5;letter-spacing:.14px;color:#d6d5de}' +
    '.fbc p a{color:#a9a3f0;text-decoration:underline;text-underline-offset:2px}' +
    '.fbc-row{display:flex;gap:8px}' +
    '.fbc button{flex:1;font:inherit;font-size:14px;font-weight:500;letter-spacing:.28px;' +
    'padding:9px 12px;border-radius:10px;cursor:pointer;color:#fefdf9;' +
    'background:rgba(254,253,249,.07);border:1px solid rgba(254,253,249,.18);transition:background .2s,border-color .2s}' +
    '.fbc button:hover{background:rgba(106,97,217,.28);border-color:rgba(106,97,217,.6)}' +
    '.fbc button:focus-visible,.fbc a:focus-visible{outline:2px solid #6a61d9;outline-offset:2px}' +
    '@media (max-width:480px){.fbc{bottom:12px;width:calc(100% - 24px)}}' +
    '@media (prefers-reduced-motion:reduce){.fbc{transition:none}}';

  var bar = null;
  function hide() {
    if (!bar) return;
    bar.remove();
    bar = null;
  }

  function show() {
    if (bar) return;
    if (!document.getElementById('fbc-style')) {
      var st = document.createElement('style');
      st.id = 'fbc-style';
      st.textContent = CSS;
      document.head.appendChild(st);
    }
    bar = document.createElement('div');
    bar.className = 'fbc';
    bar.setAttribute('role', 'region');
    bar.setAttribute('aria-label', T.label);
    bar.innerHTML =
      '<p>' + T.text + ' <a href="' + T.moreHref + '">' + T.more + '</a></p>' +
      '<div class="fbc-row">' +
      '<button type="button" data-fbc="denied">' + T.reject + '</button>' +
      '<button type="button" data-fbc="granted">' + T.accept + '</button>' +
      '</div>';
    bar.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-fbc]');
      if (!b) return;
      var state = b.getAttribute('data-fbc');
      save(state);
      state === 'granted' ? grant() : deny();
      hide();
    });
    document.body.appendChild(bar);
    requestAnimationFrame(function () { requestAnimationFrame(function () { bar && bar.classList.add('fbc-in'); }); });
  }

  // Reopen from any element with data-cookie-settings (e.g. button on the cookies page)
  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-cookie-settings]');
    if (!el) return;
    e.preventDefault();
    show();
  });

  var stored = read();
  if (stored === 'granted') {
    grant();
  } else if (stored === null) {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', show);
    else show();
  }
})();
