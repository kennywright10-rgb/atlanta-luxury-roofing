#!/usr/bin/env python3
"""
Generate contact-atlanta-luxury-roofing.html
"""

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Contact Atlanta Luxury Roofing for a free roofing estimate. Call (404) 632-6599 or fill out our quote form. 1-business-day response guarantee.">
    <meta name="canonical" href="https://atlantaluxuryroofing.com/contact-atlanta-luxury-roofing">
    <title>Contact Us | Atlanta Luxury Roofing | Free Estimate</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root {
            --gold: #c9a96e;
            --ink: #141210;
            --mid: #1e1a16;
            --cream: #e8e2d9;
            --light: #faf8f5;
            --muted: #8a8278;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            color: var(--ink);
            background: var(--light);
            line-height: 1.6;
        }

        a {
            color: var(--gold);
            text-decoration: none;
            transition: color 0.3s ease;
        }

        a:hover {
            color: var(--mid);
        }

        /* Navigation & Footer placeholders */
        #nav-placeholder, #footer-placeholder {
            width: 100%;
        }

        /* Hero Section */
        .hero {
            padding: 6rem 2rem;
            background: var(--light);
            text-align: center;
        }

        .hero h1 {
            font-family: 'Cormorant Garamond', serif;
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color: var(--ink);
            letter-spacing: -1px;
        }

        .hero p {
            font-size: 1.2rem;
            color: var(--muted);
            max-width: 600px;
            margin: 0 auto;
        }

        /* Container */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        /* Two-Column Layout */
        .contact-main {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            padding: 4rem 2rem;
            background: white;
        }

        .contact-info {
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }

        .contact-info h2 {
            font-family: 'Cormorant Garamond', serif;
            font-size: 2rem;
            color: var(--ink);
            margin-bottom: 1rem;
        }

        .contact-block {
            border-left: 3px solid var(--gold);
            padding-left: 1.5rem;
        }

        .contact-block h3 {
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--muted);
            margin-bottom: 0.5rem;
        }

        .contact-block-content {
            font-size: 1.1rem;
            color: var(--ink);
        }

        .phone-prominent {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--gold);
            margin: 0.5rem 0;
        }

        .contact-block p {
            margin: 0.5rem 0;
            color: var(--ink);
        }

        .contact-block a {
            font-weight: 500;
        }

        .response-promise {
            background: rgba(201, 169, 110, 0.08);
            padding: 1.5rem;
            border-radius: 6px;
            margin-top: 1rem;
        }

        .response-promise p {
            margin: 0;
            color: var(--ink);
            font-size: 0.95rem;
        }

        .response-promise strong {
            color: var(--gold);
        }

        /* Quote Form */
        .quote-form-container {
            display: flex;
            flex-direction: column;
        }

        .quote-form-container h2 {
            font-family: 'Cormorant Garamond', serif;
            font-size: 2rem;
            color: var(--ink);
            margin-bottom: 2rem;
        }

        .quote-form {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        .form-group {
            display: flex;
            flex-direction: column;
        }

        .form-group label {
            font-weight: 500;
            color: var(--ink);
            margin-bottom: 0.5rem;
            font-size: 0.95rem;
        }

        .form-group input,
        .form-group textarea,
        .form-group select {
            padding: 0.75rem;
            border: 1px solid var(--cream);
            border-radius: 4px;
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            color: var(--ink);
        }

        .form-group textarea {
            resize: vertical;
            min-height: 120px;
        }

        .form-group input:focus,
        .form-group textarea:focus,
        .form-group select:focus {
            outline: none;
            border-color: var(--gold);
            box-shadow: 0 0 0 2px rgba(201, 169, 110, 0.1);
        }

        .form-submit {
            background: var(--gold);
            color: white;
            padding: 1rem 2rem;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.3s ease;
            align-self: flex-start;
        }

        .form-submit:hover {
            background: var(--mid);
        }

        /* What to Expect */
        .what-to-expect {
            padding: 4rem 2rem;
            background: var(--light);
        }

        .what-to-expect h2 {
            font-family: 'Cormorant Garamond', serif;
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 3rem;
            color: var(--ink);
        }

        .steps-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 2rem;
        }

        .step {
            text-align: center;
        }

        .step-number {
            font-family: 'Cormorant Garamond', serif;
            font-size: 3rem;
            color: var(--gold);
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .step h3 {
            font-size: 1.2rem;
            margin-bottom: 0.75rem;
            color: var(--ink);
        }

        .step p {
            font-size: 0.95rem;
            color: var(--muted);
            line-height: 1.6;
        }

        /* Service Area */
        .service-area {
            padding: 4rem 2rem;
            background: white;
        }

        .service-area h2 {
            font-family: 'Cormorant Garamond', serif;
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 2rem;
            color: var(--ink);
        }

        .neighborhoods {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: center;
            margin-bottom: 3rem;
        }

        .neighborhood-tag {
            background: var(--mid);
            color: white;
            padding: 0.6rem 1.2rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
        }

        /* Map Placeholder */
        .map-placeholder {
            background: var(--light);
            padding: 3rem 2rem;
            border-radius: 8px;
            text-align: center;
            border: 2px dashed var(--cream);
        }

        .map-placeholder h3 {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.5rem;
            color: var(--ink);
            margin-bottom: 1rem;
        }

        .map-placeholder p {
            color: var(--muted);
            margin-bottom: 1.5rem;
        }

        .map-neighborhoods {
            display: flex;
            flex-wrap: wrap;
            gap: 0.8rem;
            justify-content: center;
        }

        .map-tag {
            background: var(--mid);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 16px;
            font-size: 0.85rem;
        }

        /* FAQ */
        .faq-section {
            padding: 4rem 2rem;
            background: var(--light);
        }

        .faq-section h2 {
            font-family: 'Cormorant Garamond', serif;
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 3rem;
            color: var(--ink);
        }

        .faq-container {
            max-width: 700px;
            margin: 0 auto;
        }

        .faq-item {
            background: white;
            margin-bottom: 1.5rem;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }

        .faq-question {
            padding: 1.5rem;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: white;
            transition: background 0.3s ease;
        }

        .faq-question:hover {
            background: var(--light);
        }

        .faq-question h3 {
            font-size: 1rem;
            color: var(--ink);
            font-weight: 600;
            margin: 0;
        }

        .faq-toggle {
            color: var(--gold);
            font-size: 1.5rem;
            font-weight: 700;
        }

        .faq-answer {
            display: none;
            padding: 1.5rem;
            background: var(--light);
            border-top: 1px solid var(--cream);
            color: var(--ink);
            font-size: 0.95rem;
            line-height: 1.7;
        }

        .faq-answer.active {
            display: block;
        }

        @media (max-width: 768px) {
            .contact-main {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .hero h1 {
                font-size: 2.5rem;
            }

            .steps-grid {
                grid-template-columns: 1fr;
            }

            .neighborhoods {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <div id="nav-placeholder"></div>

    <!-- Hero -->
    <section class="hero">
        <h1>Let's Talk About Your Roof</h1>
        <p>Get a free, no-obligation estimate from Atlanta's roofing experts</p>
    </section>

    <!-- Contact Main -->
    <section class="contact-main">
        <!-- Left: Contact Info -->
        <div class="contact-info">
            <h2>Get in Touch</h2>

            <div class="contact-block">
                <h3>Call Us Now</h3>
                <div class="phone-prominent">(404) 632-6599</div>
                <p>Let's discuss your roofing needs directly</p>
            </div>

            <div class="contact-block">
                <h3>Email</h3>
                <div class="contact-block-content">
                    <a href="mailto:hello@atlantaluxuryroofing.com">hello@atlantaluxuryroofing.com</a>
                </div>
            </div>

            <div class="contact-block">
                <h3>Response Guarantee</h3>
                <div class="response-promise">
                    <p>We respond to all inquiries within <strong>1 business day</strong>. If you prefer to speak with someone immediately, call us at (404) 632-6599.</p>
                </div>
            </div>

            <div class="contact-block">
                <h3>Service Hours</h3>
                <p>Monday – Friday: 8:00 AM – 5:00 PM</p>
                <p>Saturday: 9:00 AM – 2:00 PM</p>
                <p>Sunday: Closed</p>
            </div>
        </div>

        <!-- Right: Quote Form -->
        <div class="quote-form-container">
            <h2>Free Estimate</h2>
            <form class="quote-form" action="https://formsubmit.co/hello@atlantaluxuryroofing.com" method="POST">
                <div class="form-group">
                    <label for="name">Your Name *</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email Address *</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="phone">Phone Number *</label>
                    <input type="tel" id="phone" name="phone" required>
                </div>
                <div class="form-group">
                    <label for="address">Property Address *</label>
                    <input type="text" id="address" name="address" required>
                </div>
                <div class="form-group">
                    <label for="project-type">Project Type *</label>
                    <select id="project-type" name="project_type" required>
                        <option value="">Select a project type</option>
                        <option value="new-roof">New Roof Installation</option>
                        <option value="replacement">Roof Replacement</option>
                        <option value="repair">Roof Repair</option>
                        <option value="inspection">Roof Inspection</option>
                        <option value="gutters">Gutters & Accessories</option>
                        <option value="insurance-claim">Insurance Claim / Damage Assessment</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="details">Project Details</label>
                    <textarea id="details" name="details" placeholder="Tell us about your roofing needs, any urgency, or what brought you to us..."></textarea>
                </div>
                <button type="submit" class="form-submit">Request Your Free Estimate</button>
            </form>
        </div>
    </section>

    <!-- What to Expect -->
    <section class="what-to-expect">
        <div class="container">
            <h2>Our Process</h2>
            <div class="steps-grid">
                <div class="step">
                    <div class="step-number">1</div>
                    <h3>Submit Form or Call</h3>
                    <p>Fill out our quick form or call us directly. Tell us what you need, and we'll listen.</p>
                </div>
                <div class="step">
                    <div class="step-number">2</div>
                    <h3>Schedule Inspection</h3>
                    <p>We'll call you within 1 business day to schedule a time that works for you.</p>
                </div>
                <div class="step">
                    <div class="step-number">3</div>
                    <h3>Free On-Site Assessment</h3>
                    <p>Our experts arrive on time, evaluate your roof, and answer all your questions.</p>
                </div>
                <div class="step">
                    <div class="step-number">4</div>
                    <h3>Detailed Proposal</h3>
                    <p>We send a comprehensive, itemized proposal within 48 hours. No surprises.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Service Area -->
    <section class="service-area">
        <div class="container">
            <h2>Service Area</h2>
            <p style="text-align: center; color: var(--muted); margin-bottom: 2rem;">We proudly serve all of Atlanta Metro and the surrounding neighborhoods</p>
            <div class="neighborhoods">
                <div class="neighborhood-tag">Buckhead</div>
                <div class="neighborhood-tag">Druid Hills</div>
                <div class="neighborhood-tag">Milton</div>
                <div class="neighborhood-tag">Alpharetta</div>
                <div class="neighborhood-tag">Peachtree Hills</div>
                <div class="neighborhood-tag">Vinings</div>
                <div class="neighborhood-tag">Sandy Springs</div>
                <div class="neighborhood-tag">Inman Park</div>
                <div class="neighborhood-tag">East Cobb</div>
                <div class="neighborhood-tag">Dunwoody</div>
                <div class="neighborhood-tag">Marietta</div>
                <div class="neighborhood-tag">Kennesaw</div>
                <div class="neighborhood-tag">Roswell</div>
                <div class="neighborhood-tag">Gwinnett County</div>
            </div>

            <!-- Map Placeholder -->
            <div class="map-placeholder">
                <h3>Serving the Atlanta Metro Area</h3>
                <p>We're based in Atlanta and service the entire metro area from North Fulton to Gwinnett County.</p>
                <div class="map-neighborhoods">
                    <span class="map-tag">North Atlanta</span>
                    <span class="map-tag">Central Atlanta</span>
                    <span class="map-tag">East Atlanta</span>
                    <span class="map-tag">West Atlanta</span>
                    <span class="map-tag">North Suburbs</span>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQ -->
    <section class="faq-section">
        <div class="container">
            <h2>Frequently Asked Questions</h2>
            <div class="faq-container">
                <div class="faq-item">
                    <div class="faq-question" onclick="toggleFaq(this)">
                        <h3>How long does a roofing inspection take?</h3>
                        <span class="faq-toggle">+</span>
                    </div>
                    <div class="faq-answer">
                        Most roof inspections take between 30 to 60 minutes, depending on the size and complexity of your roof. We'll examine the structure from above and below, check for any issues, and discuss our findings with you in detail before we leave.
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question" onclick="toggleFaq(this)">
                        <h3>Do you offer financing options?</h3>
                        <h3>Do you offer financing options?</h3>
                        <span class="faq-toggle">+</span>
                    </div>
                    <div class="faq-answer">
                        Yes, we work with several financing partners to make premium roofing affordable. We can discuss flexible payment options during your estimate consultation. Many homeowners also use their insurance settlement to cover costs.
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question" onclick="toggleFaq(this)">
                        <h3>Are you insured and bonded?</h3>
                        <span class="faq-toggle">+</span>
                    </div>
                    <div class="faq-answer">
                        Absolutely. Atlanta Luxury Roofing is fully licensed, insured, and bonded. We carry comprehensive liability insurance and workers' compensation to protect you, your home, and our team while we work.
                    </div>
                </div>

                <div class="faq-item">
                    <div class="faq-question" onclick="toggleFaq(this)">
                        <h3>What's included in your warranty?</h3>
                        <span class="faq-toggle">+</span>
                    </div>
                    <div class="faq-answer">
                        We offer a 10-year workmanship warranty on all our installations and repairs. We also help coordinate manufacturer warranties on materials. Our warranty covers defects in workmanship and materials for a full decade.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <div id="footer-placeholder"></div>

    <!-- JSON-LD Schema -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "ContactPage"],
        "name": "Atlanta Luxury Roofing",
        "url": "https://atlantaluxuryroofing.com",
        "contactUrl": "https://atlantaluxuryroofing.com/contact-atlanta-luxury-roofing",
        "telephone": "(404) 632-6599",
        "email": "hello@atlantaluxuryroofing.com",
        "address": {
            "@type": "PostalAddress",
            "addressCountry": "US",
            "addressRegion": "GA",
            "addressLocality": "Atlanta",
            "postalCode": "30301"
        },
        "areaServed": [
            {
                "@type": "City",
                "name": "Atlanta, GA"
            },
            {
                "@type": "City",
                "name": "Buckhead, GA"
            },
            {
                "@type": "City",
                "name": "Milton, GA"
            },
            {
                "@type": "City",
                "name": "Alpharetta, GA"
            },
            {
                "@type": "City",
                "name": "Sandy Springs, GA"
            },
            {
                "@type": "City",
                "name": "Roswell, GA"
            }
        ],
        "openingHours": [
            "Mo-Fr 08:00-17:00",
            "Sa 09:00-14:00"
        ]
    }
    </script>

    <script>
        function toggleFaq(element) {
            const answer = element.nextElementSibling;
            const toggle = element.querySelector('.faq-toggle');

            answer.classList.toggle('active');
            toggle.textContent = answer.classList.contains('active') ? '−' : '+';
        }
    </script>

    <script src="components.js"></script>
</body>
</html>'''

# Write to file
with open('/sessions/zealous-charming-edison/mnt/Desktop/AtlantaLuxuryRoofing/contact-atlanta-luxury-roofing.html', 'w') as f:
    f.write(html_content)

print("File generated: contact-atlanta-luxury-roofing.html")
