/**
 * CMS Data Loader
 * Loads company, heroes, and about data from JSON files and populates page elements.
 * Elements keep their hardcoded fallback text for SEO and fast first paint.
 */
(function() {
  var isEN = document.documentElement.lang === 'en';
  var base = isEN ? '../' : '';
  var page = (location.pathname.split('/').pop() || 'index.html').replace('.html', '') || 'index';

  function pick(obj, key) {
    return isEN && obj[key + '_en'] != null ? obj[key + '_en'] : obj[key];
  }

  function setText(id, val) {
    var el = document.getElementById(id);
    if (el && val != null) el.innerHTML = val;
  }

  /* ── Copyright year (no fetch needed) ── */
  var cy = document.getElementById('copyrightYear');
  if (cy) cy.textContent = new Date().getFullYear();

  /* ── Company data ── */
  fetch(base + 'data/company.json')
    .then(function(r) { return r.json(); })
    .then(function(d) {
      /* Footer social links */
      var ig = document.getElementById('footerInstagram');
      if (ig) ig.href = d.instagram;
      var li = document.getElementById('footerLinkedin');
      if (li) li.href = d.linkedin;

      /* Footer copyright company name */
      setText('copyrightName', d.name);

      /* Contact page – company details */
      var cd = document.getElementById('companyDetails');
      if (cd) {
        var addrLabel = isEN ? 'Address:' : 'Adresa:';
        var idLabel = isEN ? 'Company ID / VAT ID:' : 'I\u010C/DI\u010C:';
        var phoneLabel = isEN ? 'Phone:' : 'Telefon:';
        cd.innerHTML =
          '<p><span class="label">' + d.name + '</span></p>' +
          '<p><span class="label">' + addrLabel + '</span> ' + d.address + '</p>' +
          '<p><span class="label">' + idLabel + '</span> ' + d.ico + '/' + d.dic + '</p>' +
          '<p><span class="label">E-mail:</span> ' + d.email + '</p>' +
          '<p><span class="label">' + phoneLabel + '</span> ' + d.phone + '</p>';
      }
    })
    .catch(function() {});

  /* ── Heroes ── */
  fetch(base + 'data/heroes.json')
    .then(function(r) { return r.json(); })
    .then(function(d) {
      var h = d[page];
      if (!h) return;
      setText('heroTitle', pick(h, 'title'));
      setText('heroSubtitle', pick(h, 'subtitle'));
    })
    .catch(function() {});

  /* ── About / content sections ── */
  fetch(base + 'data/about.json')
    .then(function(r) { return r.json(); })
    .then(function(d) {
      /* "Čím se zabýváme" – onas page */
      if (d.whatWeDo) {
        setText('aboutHeading', pick(d.whatWeDo, 'heading'));
        var at = document.getElementById('aboutText');
        if (at) {
          var paras = pick(d.whatWeDo, 'paragraphs');
          if (paras) at.innerHTML = paras.map(function(p) { return '<p>' + p + '</p>'; }).join('');
        }
      }

      /* "Co umíme" – index */
      if (d.indexSection) {
        setText('coUmimeHeading', pick(d.indexSection, 'heading'));
        setText('coUmimeText', pick(d.indexSection, 'text'));
      }

      /* "Proč s námi" – index */
      if (d.whyWorkWithUs) {
        setText('whyHeading', pick(d.whyWorkWithUs, 'heading'));
        setText('whyText', pick(d.whyWorkWithUs, 'text'));
      }

      /* Team section – onas */
      if (d.teamSection) {
        setText('teamHeading', pick(d.teamSection, 'heading'));
        setText('teamSubtitle', pick(d.teamSection, 'subtitle'));
      }

      /* Contact info – kontakt page */
      if (d.contactInfo) {
        setText('kontaktInfoHeading', pick(d.contactInfo, 'heading'));
        setText('kontaktInfoText', pick(d.contactInfo, 'text'));
        setText('infoCardText', pick(d.contactInfo, 'infoCardText'));
        setText('companyHeading', pick(d.contactInfo, 'companyHeading'));
      }

      /* Contact form heading + description (shared across pages) */
      if (d.contactForm) {
        setText('formHeading', pick(d.contactForm, 'heading'));
        setText('formText', pick(d.contactForm, 'text'));
      }

      /* Services section heading – sluzby page */
      if (d.servicesSection) {
        setText('servicesHeading', pick(d.servicesSection, 'heading'));
        setText('servicesText', pick(d.servicesSection, 'text'));
      }

      /* Selected project heading – index */
      if (d.selectedProject) {
        setText('selectedProjectHeading', pick(d.selectedProject, 'heading'));
      }
    })
    .catch(function() {});
})();
