#!/usr/bin/env python3
"""
Generate luxury-roofing-service-area-atlanta.html
Core30 SEO page for AtlantaLuxuryRoofing.com covering all 14 Atlanta neighborhoods
"""

import json
from datetime import datetime

# Design tokens
DESIGN_TOKENS = {
    "gold": "#c9a96e",
    "ink": "#141210",
    "mid": "#1e1a16",
    "card": "#242018",
    "cream": "#e8e2d9",
    "light": "#faf8f5",
    "muted": "#8a8278",
}

# 14 Target neighborhoods
NEIGHBORHOODS = [
    {
        "name": "Buckhead",
        "link": "/luxury-roofing-buckhead",
        "description": "Atlanta's premier residential community. Estate homes with complex rooflines and exacting material standards.",
        "material": "Standing seam metal",
        "county": "City of Atlanta"
    },
    {
        "name": "Milton",
        "link": "/luxury-roofing-milton-ga",
        "description": "Cherokee County horse country. Modern farmhouse and French country estates with standing seam and slate.",
        "material": "Standing seam metal, slate",
        "county": "Cherokee County"
    },
    {
        "name": "Alpharetta",
        "link": "/luxury-roofing-alpharetta",
        "description": "Windward and Manor Golf communities. Premium materials for Fulton County's fastest-growing luxury market.",
        "material": "Standing seam metal, slate",
        "county": "Fulton County"
    },
    {
        "name": "Sandy Springs",
        "link": "/luxury-roofing-sandy-springs",
        "description": "Independent city with Chattahoochee River corridor estates. Strong copper gutter demand.",
        "material": "Copper, standing seam",
        "county": "Fulton County"
    },
    {
        "name": "Roswell",
        "link": "/luxury-roofing-roswell-ga",
        "description": "Historic Canton Street area and newer luxury builds. Historic Preservation Commission experience.",
        "material": "Slate, standing seam",
        "county": "Fulton County"
    },
    {
        "name": "Johns Creek",
        "link": "/luxury-roofing-johns-creek",
        "description": "St. Ives and Country Club of the South. Fulton County luxury with strong synthetic slate demand.",
        "material": "Synthetic slate, standing seam",
        "county": "Fulton County"
    },
    {
        "name": "East Cobb",
        "link": "/luxury-roofing-east-cobb",
        "description": "Indian Hills corridor. The original Atlanta suburb for cedar shake and standing seam.",
        "material": "Cedar shake, standing seam",
        "county": "Cobb County"
    },
    {
        "name": "Vinings",
        "link": "/luxury-roofing-vinings",
        "description": "Buckhead-adjacent Cobb County estates. Copper accents and standing seam for the Chattahoochee corridor.",
        "material": "Copper, standing seam",
        "county": "Cobb County"
    },
    {
        "name": "Brookhaven",
        "link": "/luxury-roofing-brookhaven",
        "description": "City of Brookhaven. Ashford Park and Drew Valley luxury infill with modern material preferences.",
        "material": "Standing seam metal, synthetic slate",
        "county": "DeKalb County"
    },
    {
        "name": "Dunwoody",
        "link": "/luxury-roofing-dunwoody",
        "description": "City of Dunwoody. Dunwoody Club Forest and Georgetown Road corridor luxury homes.",
        "material": "Standing seam metal, slate",
        "county": "DeKalb County"
    },
    {
        "name": "Druid Hills",
        "link": "/luxury-roofing-druid-hills",
        "description": "Olmsted-designed historic district. Period-accurate Welsh and Vermont slate for National Register homes.",
        "material": "Welsh slate, Vermont slate",
        "county": "DeKalb County"
    },
    {
        "name": "Virginia-Highland",
        "link": "/luxury-roofing-virginia-highland",
        "description": "1920s Tudors and craftsman bungalows. Complex rooflines and period-appropriate materials.",
        "material": "Slate, cedar shake",
        "county": "City of Atlanta"
    },
    {
        "name": "Morningside",
        "link": "/luxury-roofing-morningside-atlanta",
        "description": "Morningside-Lenox Park. Historic and luxury infill with City of Atlanta permits.",
        "material": "Slate, copper",
        "county": "City of Atlanta"
    },
    {
        "name": "Inman Park",
        "link": "/luxury-roofing-inman-park",
        "description": "Atlanta's oldest planned suburb. Victorian estates and Queen Anne cottages with slate and copper.",
        "material": "Slate, copper",
        "county": "City of Atlanta"
    }
]

# Materials with service pages
MATERIALS = [
    {
        "name": "Standing Seam Metal",
        "link": "/luxury-roofing-standing-seam-metal",
        "icon": "🏛️",
        "description": "Modern elegance with 50-year durability"
    },
    {
        "name": "Natural Slate",
        "link": "/luxury-roofing-natural-slate",
        "icon": "🪨",
        "description": "Welsh and Vermont heritage materials"
    },
    {
        "name": "Copper",
        "link": "/luxury-roofing-copper",
        "icon": "🔶",
        "description": "Architect-grade accents and gutters"
    },
    {
        "name": "Cedar Shake",
        "link": "/luxury-roofing-cedar-shake",
        "icon": "🌲",
        "description": "Historic authenticity, modern performance"
    },
    {
        "name": "Synthetic Slate",
        "link": "/luxury-roofing-synthetic-slate",
        "icon": "✨",
        "description": "Period accuracy with engineered durability"
    }
]

def generate_html():
    """Generate the complete HTML file"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Premium luxury roofing across Atlanta's finest neighborhoods. Standing seam metal, natural slate, copper, and cedar shake installation in Buckhead, Milton, Alpharetta, Sandy Springs, and 10 more communities.">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="Atlanta Luxury Roofing Service Area | All Metro Neighborhoods">
    <meta property="og:description" content="Serving 14 luxury residential neighborhoods across Atlanta metro with specialist expertise in standing seam metal, slate, copper, and cedar shake roofing.">
    <meta property="og:image" content="https://atlantaluxuryroofing.com/og-service-area.jpg">
    <meta name="geo.position" content="33.7490;-84.3880">
    <meta name="geo.placename" content="Atlanta, Georgia">
    <meta name="geo.region" content="US-GA">
    <link rel="canonical" href="https://atlantaluxuryroofing.com/luxury-roofing-service-area-atlanta">

    <title>Atlanta Luxury Roofing Service Area | All Metro Neighborhoods</title>

    <style>
        :root {{
            --gold: {DESIGN_TOKENS["gold"]};
            --ink: {DESIGN_TOKENS["ink"]};
            --mid: {DESIGN_TOKENS["mid"]};
            --card: {DESIGN_TOKENS["card"]};
            --cream: {DESIGN_TOKENS["cream"]};
            --light: {DESIGN_TOKENS["light"]};
            --muted: {DESIGN_TOKENS["muted"]};
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: var(--light);
            color: var(--ink);
            line-height: 1.6;
        }}

        .page-wrapper {{
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }}

        main {{
            flex: 1;
        }}

        /* Navigation & Footer placeholders */
        #nav-placeholder {{
            background: var(--ink);
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 100;
        }}

        #footer-placeholder {{
            background: var(--mid);
            padding: 3rem 2rem;
            margin-top: 4rem;
        }}

        /* Hero Section */
        .hero {{
            background: linear-gradient(135deg, var(--mid) 0%, var(--card) 100%);
            color: var(--light);
            padding: 6rem 2rem;
            text-align: center;
        }}

        .hero h1 {{
            font-family: 'Cormorant Garamond', serif;
            font-size: 3.5rem;
            margin-bottom: 2rem;
            font-weight: 400;
            letter-spacing: 0.05em;
        }}

        .trust-bar {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            max-width: 1000px;
            margin: 0 auto;
            padding-top: 2rem;
            border-top: 1px solid rgba(201, 169, 110, 0.3);
        }}

        .trust-stat {{
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        .trust-stat-value {{
            font-family: 'Cormorant Garamond', serif;
            font-size: 2.5rem;
            color: var(--gold);
            margin-bottom: 0.5rem;
        }}

        .trust-stat-label {{
            font-size: 0.9rem;
            color: var(--cream);
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }}

        /* Intro Section */
        .intro {{
            background: var(--light);
            padding: 4rem 2rem;
            max-width: 900px;
            margin: 0 auto;
        }}

        .intro p {{
            font-size: 1.1rem;
            line-height: 1.8;
            color: var(--mid);
            margin-bottom: 1.5rem;
        }}

        /* Neighborhoods Grid */
        .neighborhoods-section {{
            padding: 4rem 2rem;
            background: var(--light);
        }}

        .section-title {{
            font-family: 'Cormorant Garamond', serif;
            font-size: 2.5rem;
            color: var(--ink);
            text-align: center;
            margin-bottom: 3rem;
            font-weight: 400;
        }}

        .neighborhoods-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }}

        .neighborhood-card {{
            background: white;
            border: 1px solid #e5e0d4;
            padding: 2rem;
            border-radius: 4px;
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
        }}

        .neighborhood-card:hover {{
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
            border-color: var(--gold);
            transform: translateY(-2px);
        }}

        .neighborhood-card h3 {{
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.8rem;
            color: var(--ink);
            margin-bottom: 0.5rem;
            font-weight: 400;
        }}

        .neighborhood-card p {{
            color: var(--muted);
            margin-bottom: 1rem;
            flex-grow: 1;
            font-size: 0.95rem;
            line-height: 1.6;
        }}

        .material-badge {{
            display: inline-block;
            background: var(--light);
            color: var(--ink);
            padding: 0.5rem 1rem;
            border-radius: 3px;
            font-size: 0.85rem;
            margin-bottom: 1rem;
            font-weight: 500;
        }}

        .neighborhood-link {{
            display: inline-block;
            color: var(--gold);
            text-decoration: none;
            font-weight: 500;
            border-bottom: 1px solid var(--gold);
            transition: all 0.2s;
            align-self: flex-start;
        }}

        .neighborhood-link:hover {{
            color: var(--ink);
            border-bottom-color: var(--ink);
        }}

        /* Local Expertise Section */
        .expertise {{
            background: var(--mid);
            color: var(--light);
            padding: 4rem 2rem;
        }}

        .expertise-content {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        .expertise h2 {{
            font-family: 'Cormorant Garamond', serif;
            font-size: 2.5rem;
            margin-bottom: 2rem;
            font-weight: 400;
        }}

        .jurisdiction-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }}

        .jurisdiction-card {{
            background: var(--card);
            padding: 2rem;
            border-left: 3px solid var(--gold);
        }}

        .jurisdiction-card h3 {{
            color: var(--gold);
            margin-bottom: 1rem;
            font-family: 'Cormorant Garamond', serif;
        }}

        .jurisdiction-card ul {{
            list-style: none;
            padding: 0;
        }}

        .jurisdiction-card li {{
            padding: 0.3rem 0;
            font-size: 0.95rem;
        }}

        /* Materials Section */
        .materials-section {{
            padding: 4rem 2rem;
            background: var(--light);
        }}

        .materials-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }}

        .material-card {{
            background: white;
            border: 1px solid #e5e0d4;
            padding: 2rem;
            text-align: center;
            border-radius: 4px;
            transition: all 0.3s ease;
        }}

        .material-card:hover {{
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
            border-color: var(--gold);
        }}

        .material-icon {{
            font-size: 3rem;
            margin-bottom: 1rem;
        }}

        .material-card h3 {{
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.6rem;
            color: var(--ink);
            margin-bottom: 0.5rem;
            font-weight: 400;
        }}

        .material-card p {{
            color: var(--muted);
            font-size: 0.95rem;
            margin-bottom: 1.5rem;
        }}

        .material-link {{
            display: inline-block;
            color: var(--gold);
            text-decoration: none;
            font-weight: 500;
            border-bottom: 1px solid var(--gold);
            transition: all 0.2s;
        }}

        .material-link:hover {{
            color: var(--ink);
            border-bottom-color: var(--ink);
        }}

        /* Quote Form Section */
        .quote-section {{
            background: var(--light);
            padding: 4rem 2rem;
        }}

        .quote-container {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            max-width: 1000px;
            margin: 0 auto;
            border-radius: 4px;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        }}

        .quote-left {{
            background: var(--mid);
            color: var(--light);
            padding: 3rem 2rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }}

        .quote-left h2 {{
            font-family: 'Cormorant Garamond', serif;
            font-size: 2.2rem;
            margin-bottom: 1.5rem;
            font-weight: 400;
        }}

        .quote-left p {{
            font-size: 1rem;
            margin-bottom: 1.5rem;
            line-height: 1.7;
            color: var(--cream);
        }}

        .quote-contact {{
            font-size: 1.3rem;
            color: var(--gold);
            font-weight: 500;
        }}

        .quote-right {{
            background: white;
            padding: 3rem 2rem;
        }}

        .form-group {{
            margin-bottom: 1.5rem;
        }}

        .form-group label {{
            display: block;
            margin-bottom: 0.5rem;
            color: var(--ink);
            font-weight: 500;
            font-size: 0.9rem;
        }}

        .form-group input,
        .form-group textarea {{
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 3px;
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            color: var(--ink);
        }}

        .form-group textarea {{
            resize: vertical;
            min-height: 100px;
        }}

        .form-group input:focus,
        .form-group textarea:focus {{
            outline: none;
            border-color: var(--gold);
            box-shadow: 0 0 0 2px rgba(201, 169, 110, 0.1);
        }}

        .submit-btn {{
            background: var(--gold);
            color: var(--ink);
            padding: 1rem 2rem;
            border: none;
            border-radius: 3px;
            font-weight: 600;
            font-size: 0.95rem;
            cursor: pointer;
            transition: all 0.2s;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            width: 100%;
        }}

        .submit-btn:hover {{
            background: var(--ink);
            color: var(--gold);
        }}

        @media (max-width: 768px) {{
            .hero h1 {{
                font-size: 2rem;
            }}

            .section-title {{
                font-size: 1.8rem;
            }}

            .quote-container {{
                grid-template-columns: 1fr;
            }}

            .neighborhoods-grid {{
                grid-template-columns: 1fr;
            }}

            .trust-bar {{
                gap: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="page-wrapper">
        <!-- Navigation -->
        <div id="nav-placeholder">
            <!-- components.js will inject navigation here -->
        </div>

        <main>
            <!-- Hero Section -->
            <section class="hero">
                <h1>Serving Atlanta's Finest Neighborhoods</h1>
                <div class="trust-bar">
                    <div class="trust-stat">
                        <div class="trust-stat-value">18+</div>
                        <div class="trust-stat-label">Years Experience</div>
                    </div>
                    <div class="trust-stat">
                        <div class="trust-stat-value">14</div>
                        <div class="trust-stat-label">Communities</div>
                    </div>
                    <div class="trust-stat">
                        <div class="trust-stat-value">500+</div>
                        <div class="trust-stat-label">Homes Served</div>
                    </div>
                    <div class="trust-stat">
                        <div class="trust-stat-value">10 Yr</div>
                        <div class="trust-stat-label">Warranty</div>
                    </div>
                </div>
            </section>

            <!-- Intro Section -->
            <section class="intro">
                <p>We exclusively serve Atlanta's luxury residential market. Our service area covers the neighborhoods where homeowners invest in standing seam metal, natural slate, copper, and cedar shake — materials that require specialist skill and local permit knowledge.</p>
                <p>Whether you're managing an estate in Buckhead, maintaining a historic Victorian in Inman Park, or upgrading a modern farmhouse in Milton, we bring local expertise to every project.</p>
            </section>

            <!-- Neighborhoods Section -->
            <section class="neighborhoods-section">
                <h2 class="section-title">Our Service Area</h2>
                <div class="neighborhoods-grid">
"""

    # Add neighborhood cards
    for neighborhood in NEIGHBORHOODS:
        html += f"""                    <div class="neighborhood-card">
                        <h3>{neighborhood["name"]}</h3>
                        <p>{neighborhood["description"]}</p>
                        <div class="material-badge">{neighborhood["material"]}</div>
                        <a href="{neighborhood["link"]}" class="neighborhood-link">View service details →</a>
                    </div>
"""

    html += """                </div>
            </section>

            <!-- Local Expertise Section -->
            <section class="expertise">
                <div class="expertise-content">
                    <h2>Why Local Expertise Matters</h2>
                    <p style="margin-bottom: 2rem; font-size: 1.05rem;">Each Atlanta jurisdiction has different permit requirements, inspection protocols, and historic preservation standards. We know all 14.</p>
                    <div class="jurisdiction-grid">
                        <div class="jurisdiction-card">
                            <h3>City of Atlanta</h3>
                            <ul>
                                <li>• Buckhead</li>
                                <li>• Virginia-Highland</li>
                                <li>• Inman Park</li>
                                <li>• Morningside</li>
                            </ul>
                        </div>
                        <div class="jurisdiction-card">
                            <h3>Fulton County</h3>
                            <ul>
                                <li>• Alpharetta</li>
                                <li>• Sandy Springs</li>
                                <li>• Johns Creek</li>
                                <li>• Roswell</li>
                            </ul>
                        </div>
                        <div class="jurisdiction-card">
                            <h3>Cobb County</h3>
                            <ul>
                                <li>• East Cobb</li>
                                <li>• Vinings</li>
                            </ul>
                        </div>
                        <div class="jurisdiction-card">
                            <h3>DeKalb County</h3>
                            <ul>
                                <li>• Druid Hills</li>
                                <li>• Brookhaven</li>
                                <li>• Dunwoody</li>
                            </ul>
                        </div>
                        <div class="jurisdiction-card">
                            <h3>Cherokee County</h3>
                            <ul>
                                <li>• Milton</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Materials Section -->
            <section class="materials-section">
                <h2 class="section-title">Premium Materials We Install</h2>
                <div class="materials-grid">
"""

    # Add material cards
    for material in MATERIALS:
        html += f"""                    <div class="material-card">
                        <div class="material-icon">{material["icon"]}</div>
                        <h3>{material["name"]}</h3>
                        <p>{material["description"]}</p>
                        <a href="{material["link"]}" class="material-link">Learn more →</a>
                    </div>
"""

    html += """                </div>
            </section>

            <!-- Quote Form Section -->
            <section class="quote-section">
                <div class="quote-container">
                    <div class="quote-left">
                        <h2>Get Your Free Quote</h2>
                        <p>Specialized luxury roofing assessment for your Atlanta home. Let's discuss your project goals, materials, and timeline.</p>
                        <div class="quote-contact">(404) 632-6599</div>
                    </div>
                    <div class="quote-right">
                        <form action="https://formsubmit.co/hello@atlantaluxuryroofing.com" method="POST">
                            <div class="form-group">
                                <label for="name">Your Name</label>
                                <input type="text" id="name" name="name" required>
                            </div>
                            <div class="form-group">
                                <label for="email">Email Address</label>
                                <input type="email" id="email" name="email" required>
                            </div>
                            <div class="form-group">
                                <label for="phone">Phone Number</label>
                                <input type="tel" id="phone" name="phone">
                            </div>
                            <div class="form-group">
                                <label for="neighborhood">Your Neighborhood</label>
                                <input type="text" id="neighborhood" name="neighborhood" placeholder="e.g., Buckhead, Milton, Alpharetta">
                            </div>
                            <div class="form-group">
                                <label for="message">Project Details</label>
                                <textarea id="message" name="message" placeholder="Tell us about your roofing needs, current condition, or materials of interest..."></textarea>
                            </div>
                            <button type="submit" class="submit-btn">Request Free Quote</button>
                        </form>
                    </div>
                </div>
            </section>
        </main>

        <!-- Footer -->
        <div id="footer-placeholder">
            <!-- components.js will inject footer here -->
        </div>
    </div>

    <!-- JSON-LD Structured Data -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "Atlanta Luxury Roofing",
        "url": "https://atlantaluxuryroofing.com",
        "telephone": "(404) 632-6599",
        "email": "hello@atlantaluxuryroofing.com",
        "address": {{
            "@type": "PostalAddress",
            "addressLocality": "Atlanta",
            "addressRegion": "Georgia",
            "addressCountry": "US"
        }},
        "areaServed": [
            {{"@type": "City", "name": "Buckhead", "addressCountry": "US"}},
            {{"@type": "City", "name": "Milton", "addressCountry": "US"}},
            {{"@type": "City", "name": "Alpharetta", "addressCountry": "US"}},
            {{"@type": "City", "name": "Sandy Springs", "addressCountry": "US"}},
            {{"@type": "City", "name": "Roswell", "addressCountry": "US"}},
            {{"@type": "City", "name": "Johns Creek", "addressCountry": "US"}},
            {{"@type": "City", "name": "East Cobb", "addressCountry": "US"}},
            {{"@type": "City", "name": "Vinings", "addressCountry": "US"}},
            {{"@type": "City", "name": "Brookhaven", "addressCountry": "US"}},
            {{"@type": "City", "name": "Dunwoody", "addressCountry": "US"}},
            {{"@type": "City", "name": "Druid Hills", "addressCountry": "US"}},
            {{"@type": "City", "name": "Virginia-Highland", "addressCountry": "US"}},
            {{"@type": "City", "name": "Morningside", "addressCountry": "US"}},
            {{"@type": "City", "name": "Inman Park", "addressCountry": "US"}}
        ],
        "description": "Premium luxury roofing across Atlanta's finest neighborhoods. Standing seam metal, natural slate, copper, and cedar shake installation.",
        "image": "https://atlantaluxuryroofing.com/og-service-area.jpg"
    }}
    </script>

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {{
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://atlantaluxuryroofing.com"
            }},
            {{
                "@type": "ListItem",
                "position": 2,
                "name": "Service Area",
                "item": "https://atlantaluxuryroofing.com/luxury-roofing-service-area-atlanta"
            }}
        ]
    }}
    </script>

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "Atlanta Luxury Roofing Service Area | All Metro Neighborhoods",
        "description": "Premium luxury roofing across Atlanta's finest neighborhoods. Standing seam metal, natural slate, copper, and cedar shake installation in Buckhead, Milton, Alpharetta, Sandy Springs, and 10 more communities.",
        "image": "https://atlantaluxuryroofing.com/og-service-area.jpg",
        "author": {{
            "@type": "Organization",
            "name": "Atlanta Luxury Roofing"
        }},
        "publisher": {{
            "@type": "Organization",
            "name": "Atlanta Luxury Roofing",
            "url": "https://atlantaluxuryroofing.com"
        }},
        "datePublished": "{datetime.now().isoformat()}"
    }}
    </script>

    <!-- Components.js for nav/footer injection -->
    <script src="/components.js"></script>
</body>
</html>
"""

    return html


def main():
    """Generate and write the HTML file"""
    output_path = "/sessions/zealous-charming-edison/mnt/Desktop/AtlantaLuxuryRoofing/luxury-roofing-service-area-atlanta.html"

    # Generate HTML
    html_content = generate_html()

    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # Get file size
    import os
    file_size = os.path.getsize(output_path)
    file_size_kb = file_size / 1024

    print(f"✓ Generated: {output_path}")
    print(f"✓ File size: {file_size:,} bytes ({file_size_kb:.2f} KB)")
    print(f"✓ Neighborhoods: 14")
    print(f"✓ Materials: 5")
    print(f"✓ Jurisdictions: 5")
    print(f"✓ Structured data: LocalBusiness + BreadcrumbList + Article")


if __name__ == "__main__":
    main()
