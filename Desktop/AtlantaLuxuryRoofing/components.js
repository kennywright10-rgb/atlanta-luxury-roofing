/**
 * Atlanta Luxury Roofing — Shared Components
 * Edit nav and footer here once; all pages update automatically.
 * Usage: Add <script src="../components.js"></script> (adjust path per page depth)
 *        and place <div id="site-nav"></div> and <div id="site-footer"></div>
 *        where you want them in each page.
 */

(function () {
  /* ─────────────────────────────────────────────
     SHARED STYLES (nav + footer)
     These are injected once into the <head>.
  ───────────────────────────────────────────── */
  const sharedCSS = `
    <style id="alr-shared-styles">
      /* ── SHARED NAV ─────────────────────────────── */
      #site-nav nav {
        position: fixed;
        top: 0; left: 0; right: 0;
        z-index: 100;
        padding: 16px 56px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: #ffffff;
        border-bottom: 1px solid rgba(28,25,21,0.1);
        transition: padding 0.3s, box-shadow 0.3s;
      }
      #site-nav nav.scrolled {
        padding: 12px 56px;
        box-shadow: 0 2px 20px rgba(28,25,21,0.08);
      }
      #site-nav .nav-logo {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.2rem;
        font-weight: 500;
        letter-spacing: 0.06em;
        color: #1c1915;
        text-decoration: none;
      }
      #site-nav .nav-logo .gold { color: #c9a96e; }
      #site-nav .nav-links {
        display: flex; gap: 36px; list-style: none;
      }
      #site-nav .nav-links a {
        font-size: 0.72rem;
        font-weight: 400;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #7a7268;
        text-decoration: none;
        transition: color 0.2s;
      }
      #site-nav .nav-links a:hover { color: #1c1915; }
      #site-nav .nav-right {
        display: flex; align-items: center; gap: 24px;
      }
      #site-nav .nav-phone {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.05rem;
        color: #a8854a;
        text-decoration: none;
        letter-spacing: 0.04em;
      }
      #site-nav .nav-cta {
        display: inline-block;
        background: #c9a96e;
        color: #141210;
        font-family: 'Inter', sans-serif;
        font-size: 0.68rem;
        font-weight: 600;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        padding: 11px 22px;
        text-decoration: none;
        transition: background 0.25s;
        white-space: nowrap;
      }
      #site-nav .nav-cta:hover { background: #dbbf8a; }

      /* ── SHARED FOOTER ──────────────────────────── */
      #site-footer footer {
        background: #1a1814;
        border-top: 1px solid rgba(201,169,110,0.2);
        padding: 72px 56px 40px;
        color: #e8e2d9;
        font-family: 'Inter', sans-serif;
      }
      #site-footer .footer-top {
        display: grid;
        grid-template-columns: 1.5fr 1fr 1fr 1fr;
        gap: 48px;
        padding-bottom: 56px;
        border-bottom: 1px solid rgba(201,169,110,0.15);
        margin-bottom: 40px;
      }
      #site-footer .footer-logo {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.2rem;
        font-weight: 500;
        letter-spacing: 0.06em;
        color: #e8e2d9;
        text-decoration: none;
        display: block;
        margin-bottom: 16px;
      }
      #site-footer .footer-logo .gold { color: #c9a96e; }
      #site-footer .footer-brand p {
        font-size: 0.84rem;
        font-weight: 300;
        color: #8c8478;
        line-height: 1.75;
      }
      #site-footer .footer-col h5 {
        font-size: 0.62rem;
        font-weight: 600;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #c9a96e;
        margin-bottom: 20px;
      }
      #site-footer .footer-col ul { list-style: none; }
      #site-footer .footer-col li { margin-bottom: 10px; }
      #site-footer .footer-col a {
        font-size: 0.84rem;
        font-weight: 300;
        color: #8c8478;
        text-decoration: none;
        transition: color 0.2s;
      }
      #site-footer .footer-col a:hover { color: #e8e2d9; }
      #site-footer .footer-bottom {
        display: flex;
        align-items: center;
        justify-content: space-between;
      }
      #site-footer .footer-bottom p {
        font-size: 0.73rem;
        font-weight: 300;
        color: #8c8478;
      }
      #site-footer .footer-license {
        font-size: 0.7rem;
        font-weight: 300;
        color: rgba(140,132,120,0.55);
        text-align: right;
      }

      /* ── RESPONSIVE ─────────────────────────────── */
      @media (max-width: 1100px) {
        #site-nav nav, #site-nav nav.scrolled { padding-left: 32px; padding-right: 32px; }
        #site-nav .nav-links { display: none; }
        #site-nav .nav-cta { display: none; }
        #site-footer footer { padding: 56px 32px 32px; }
        #site-footer .footer-top { grid-template-columns: 1fr 1fr; gap: 32px; }
        #site-footer .footer-bottom { flex-direction: column; gap: 12px; text-align: center; }
        #site-footer .footer-license { text-align: center; }
      }
      @media (max-width: 640px) {
        #site-footer .footer-top { grid-template-columns: 1fr; }
      }
    </style>
  `;

  /* ─────────────────────────────────────────────
     NAV HTML
     To update nav links or phone number, edit here.
  ───────────────────────────────────────────── */
  const navHTML = `
    <nav id="alr-navbar">
      <a href="/" class="nav-logo">Atlanta <span class="gold">Luxury</span> Roofing</a>
      <ul class="nav-links">
        <li><a href="/#reviews">Reviews</a></li>
        <li><a href="/#how-it-works">How It Works</a></li>
        <li><a href="/#materials">Specialties</a></li>
        <li><a href="/#gallery">Gallery</a></li>
        <li><a href="/#faq">FAQ</a></li>
      </ul>
      <div class="nav-right">
        <a href="tel:+14045550100" class="nav-phone">(404) 555-0100</a>
        <a href="/#quote" class="nav-cta">Free Consultation</a>
      </div>
    </nav>
  `;

  /* ─────────────────────────────────────────────
     FOOTER HTML
     To update footer content, edit here.
  ───────────────────────────────────────────── */
  const footerHTML = `
    <footer>
      <div class="footer-top">
        <div class="footer-brand">
          <a href="/" class="footer-logo">Atlanta <span class="gold">Luxury</span> Roofing</a>
          <p>Specialty roofing for Atlanta's finest homes. Standing seam metal, natural slate, copper, and cedar shake — installed by craftsmen who have spent careers mastering these materials.</p>
        </div>
        <div class="footer-col">
          <h5>Specialties</h5>
          <ul>
            <li><a href="/#materials">Standing Seam Metal</a></li>
            <li><a href="/#materials">Natural Slate</a></li>
            <li><a href="/#materials">Copper Roofing</a></li>
            <li><a href="/#materials">Cedar Shake</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Service Areas</h5>
          <ul>
            <li><a href="/luxury-roofing-buckhead">Buckhead</a></li>
            <li><a href="/luxury-roofing-milton-ga">Milton</a></li>
            <li><a href="/luxury-roofing-alpharetta-ga">Alpharetta</a></li>
            <li><a href="/luxury-roofing-johns-creek-ga">Johns Creek</a></li>
            <li><a href="/luxury-roofing-lake-lanier">Lake Lanier</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Get In Touch</h5>
          <ul>
            <li><a href="tel:+14045550100">(404) 555-0100</a></li>
            <li><a href="/#quote">Free Consultation</a></li>
            <li><a href="mailto:hello@atlantaluxuryroofing.com">Email Us</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2025 Atlanta Luxury Roofing. All rights reserved.</p>
        <p class="footer-license">Georgia State Contractor License #GCQA000000 · Fully Insured · Bonded</p>
      </div>
    </footer>
  `;

  /* ─────────────────────────────────────────────
     INJECT EVERYTHING
  ───────────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', function () {
    // Inject shared styles into <head>
    if (!document.getElementById('alr-shared-styles')) {
      document.head.insertAdjacentHTML('beforeend', sharedCSS);
    }

    // Inject nav
    const navSlot = document.getElementById('site-nav');
    if (navSlot) navSlot.innerHTML = navHTML;

    // Inject footer
    const footerSlot = document.getElementById('site-footer');
    if (footerSlot) footerSlot.innerHTML = footerHTML;

    // Nav scroll behavior (works for any page)
    const navbar = document.getElementById('alr-navbar');
    if (navbar) {
      window.addEventListener('scroll', function () {
        navbar.classList.toggle('scrolled', window.scrollY > 40);
      });
    }
  });
})();
