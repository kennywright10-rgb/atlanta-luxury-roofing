/**
 * Atlanta Luxury Roofing — Shared Components
 * Injects nav and footer into pages.
 * Supports both #nav-placeholder / #footer-placeholder AND legacy #site-nav / #site-footer
 */

(function () {

  const sharedCSS = `
    <style id="alr-shared-styles">
      /* ── NAV ─────────────────────────────────────── */
      #alr-navbar {
        position: fixed; top: 0; left: 0; right: 0; z-index: 9000;
        padding: 16px 48px;
        display: flex; align-items: center; justify-content: space-between;
        background: #ffffff;
        border-bottom: 1px solid rgba(28,25,21,0.1);
        transition: padding 0.3s, box-shadow 0.3s;
        font-family: 'Inter', sans-serif;
      }
      #alr-navbar.scrolled { padding: 11px 48px; box-shadow: 0 2px 20px rgba(28,25,21,0.08); }
      .nav-logo {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.2rem; font-weight: 500; letter-spacing: 0.06em;
        color: #1c1915; text-decoration: none; flex-shrink: 0;
      }
      .nav-logo .gold { color: #c9a96e; }
      .nav-links { display: flex; gap: 28px; list-style: none; }
      .nav-links a {
        font-size: 0.7rem; font-weight: 500; letter-spacing: 0.12em;
        text-transform: uppercase; color: #7a7268; text-decoration: none; transition: color 0.2s;
      }
      .nav-links a:hover { color: #1c1915; }
      .nav-right { display: flex; align-items: center; gap: 20px; }
      .nav-phone {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.05rem; color: #a8854a; text-decoration: none; letter-spacing: 0.04em;
      }
      .nav-cta {
        display: inline-block; background: #c9a96e; color: #141210;
        font-size: 0.68rem; font-weight: 700; letter-spacing: 0.14em;
        text-transform: uppercase; padding: 11px 20px; text-decoration: none;
        border-radius: 2px; transition: background 0.2s; white-space: nowrap;
      }
      .nav-cta:hover { background: #d4b87e; }
      /* Spacer so hero doesn't hide behind fixed nav */
      .alr-nav-spacer { height: 60px; }

      /* ── FOOTER ──────────────────────────────────── */
      #alr-footer {
        background: #1a1814; border-top: 1px solid rgba(201,169,110,0.2);
        padding: 72px 56px 40px; color: #e8e2d9; font-family: 'Inter', sans-serif;
      }
      #alr-footer .footer-top {
        display: grid; grid-template-columns: 1.5fr 1fr 1fr 1fr;
        gap: 48px; padding-bottom: 56px;
        border-bottom: 1px solid rgba(201,169,110,0.15); margin-bottom: 40px;
      }
      #alr-footer .footer-logo {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.2rem; font-weight: 500; letter-spacing: 0.06em;
        color: #e8e2d9; text-decoration: none; display: block; margin-bottom: 16px;
      }
      #alr-footer .footer-logo .gold { color: #c9a96e; }
      #alr-footer .footer-brand p {
        font-size: 0.84rem; font-weight: 300; color: #8c8478; line-height: 1.75;
      }
      #alr-footer .footer-col h5 {
        font-size: 0.62rem; font-weight: 600; letter-spacing: 0.18em;
        text-transform: uppercase; color: #c9a96e; margin-bottom: 20px;
      }
      #alr-footer .footer-col ul { list-style: none; }
      #alr-footer .footer-col li { margin-bottom: 10px; }
      #alr-footer .footer-col a {
        font-size: 0.84rem; font-weight: 300; color: #8c8478;
        text-decoration: none; transition: color 0.2s;
      }
      #alr-footer .footer-col a:hover { color: #e8e2d9; }
      #alr-footer .footer-bottom {
        display: flex; align-items: center; justify-content: space-between;
      }
      #alr-footer .footer-bottom p { font-size: 0.73rem; font-weight: 300; color: #8c8478; }
      #alr-footer .footer-license {
        font-size: 0.7rem; font-weight: 300;
        color: rgba(140,132,120,0.55); text-align: right;
      }

      /* ── RESPONSIVE ──────────────────────────────── */
      @media (max-width: 1100px) {
        #alr-navbar, #alr-navbar.scrolled { padding-left: 24px; padding-right: 24px; }
        .nav-links { display: none; }
        #alr-footer { padding: 56px 24px 32px; }
        #alr-footer .footer-top { grid-template-columns: 1fr 1fr; gap: 32px; }
        #alr-footer .footer-bottom { flex-direction: column; gap: 12px; text-align: center; }
        #alr-footer .footer-license { text-align: center; }
      }
      @media (max-width: 640px) {
        #alr-footer .footer-top { grid-template-columns: 1fr; }
        .nav-cta { display: none; }
      }h
    </style>
  `;

  const navHTML = `
    <div class="alr-nav-spacer"></div>
    <nav id="alr-navbar">
      <a href="/" class="nav-logo">Atlanta <span class="gold">Luxury</span> Roofing</a>
      <ul class="nav-links">
        <li><a href="/roofing-resources-atlanta">Resources</a></li>
        <li><a href="/luxury-roofing-service-area-atlanta">Service Area</a></li>
        <li><a href="/roofing-cost-calculator-atlanta">Cost Calculator</a></li>
        <li><a href="/reviews-atlanta-luxury-roofing">Reviews</a></li>
        <li><a href="/about-atlanta-luxury-roofing">About</a></li>
      </ul>
      <div class="nav-right">
        <a href="tel:+16782429769" class="nav-phone">(678) 242-9769</a>
        <a href="/contact-atlanta-luxury-roofing" class="nav-cta">Free Consultation</a>
      </div>
    </nav>
  `;

  const footerHTML = `
    <div id="alr-footer">
      <div class="footer-top">
        <div class="footer-brand">
          <a href="/" class="footer-logo">Atlanta <span class="gold">Luxury</span> Roofing</a>
          <p>Specialty roofing for Atlanta's finest homes. Standing seam metal, natural slate, copper, cedar shake, and synthetic slate — installed by craftsmen who have spent careers mastering these materials.</p>
          <p style="margin-top:14px;font-size:0.8rem;color:#8c8478;">(678) 242-9769 &nbsp;&bull;&nbsp; hello@atlantaluxuryroofing.com</p>
        </div>
        <div class="footer-col">
          <h5>Materials</h5>
          <ul>
            <li><a href="/standing-seam-metal-roof-cost-atlanta">Standing Seam Metal</a></li>
            <li><a href="/natural-slate-roof-cost-atlanta">Natural Slate</a></li>
            <li><a href="/copper-roofing-atlanta">Copper Roofing</a></li>
            <li><a href="/cedar-shake-roofing-atlanta">Cedar Shake</a></li>
            <li><a href="/synthetic-slate-roofing-atlanta">Synthetic Slate</a></li>
            <li><a href="/roofing-cost-calculator-atlanta">Cost Calculator</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Service Areas</h5>
          <ul>
            <li><a href="/luxury-roofing-buckhead">Buckhead</a></li>
            <li><a href="/luxury-roofing-milton-ga">Milton</a></li>
            <li><a href="/luxury-roofing-alpharetta">Alpharetta</a></li>
            <li><a href="/luxury-roofing-sandy-springs">Sandy Springs</a></li>
            <li><a href="/luxury-roofing-roswell-ga">Roswell</a></li>
            <li><a href="/luxury-roofing-service-area-atlanta">All 14 Areas &rarr;</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Company</h5>
          <ul>
            <li><a href="/about-atlanta-luxury-roofing">About Us</a></li>
            <li><a href="/reviews-atlanta-luxury-roofing">Client Reviews</a></li>
            <li><a href="/roofing-resources-atlanta">Roofing Guides</a></li>
            <li><a href="/roof-repair-vs-replacement-atlanta">Repair vs. Replace</a></li>
            <li><a href="/contact-atlanta-luxury-roofing">Contact</a></li>
            <li><a href="tel:+16782429769">(678) 242-9769</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Atlanta Luxury Roofing &nbsp;&bull;&nbsp; Atlanta, Georgia &nbsp;&bull;&nbsp; All rights reserved.</p>
        <p class="footer-license">Licensed Georgia Roofing Contractor &nbsp;&bull;&nbsp; Fully Insured &nbsp;&bull;&nbsp; Bonded</p>
      </div>
    </div>
  `;

  document.addEventListener('DOMContentLoaded', function () {
    // Inject shared styles once
    if (!document.getElementById('alr-shared-styles')) {
      document.head.insertAdjacentHTML('beforeend', sharedCSS);
    }

    // Support both ID conventions
    const navSlots = ['nav-placeholder', 'site-nav'];
    navSlots.forEach(function(id) {
      const el = document.getElementById(id);
      if (el) el.innerHTML = navHTML;
    });

    const footerSlots = ['footer-placeholder', 'site-footer'];
    footerSlots.forEach(function(id) {
      const el = document.getElementById(id);
      if (el) el.innerHTML = footerHTML;
    });

    // Scroll behavior
    const navbar = document.getElementById('alr-navbar');
    if (navbar) {
      window.addEventListener('scroll', function () {
        navbar.classList.toggle('scrolled', window.scrollY > 40);
      });
    }
  });
})();
