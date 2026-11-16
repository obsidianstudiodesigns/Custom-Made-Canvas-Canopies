"""Generate privacy.html, terms.html, 404.html, robots.txt, sitemap.xml and site.webmanifest.

Run from the project root:  python -I tools/build_pages.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://obsidianstudiodesigns.github.io/Custom-Made-Canvas-Canopies/"
NAME = "Custom Made Canvas Canopies"
UPDATED = "16 November 2026"
UPDATED_ISO = "2026-11-16"
EMAIL = "marketing.neelscanopy@gmail.com"
PHONE = "082 950 8390"
ADDRESS = "5 Jan Booysen Street, Annlin, Pretoria, 0182"


def head(title, desc, path, robots="index,follow"):
    url = BASE + path
    return f"""<!doctype html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#0e100c">
<meta name="color-scheme" content="dark">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:locale" content="en_ZA">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}assets/img/og-share.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preload" href="assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav nav--page" data-state="scrolled">
  <div class="nav__inner wrap">
    <a class="brand" href="./" aria-label="{NAME}, home">
      <img src="assets/img/mark-120.png" alt="" width="40" height="40">
      <span class="brand__text"><span>Custom Made</span><strong>Canvas Canopies</strong></span>
    </a>
    <div class="nav__cta" style="margin-left:auto">
      <a class="btn btn--ghost btn--sm" href="./">Back to home</a>
    </div>
  </div>
</header>
"""


FOOT = f"""<footer class="foot">
  <div class="wrap foot__base" style="margin-top:0;border-top:0;padding-top:0">
    <p>&copy; 2026 {NAME}. All rights reserved.</p>
    <nav class="foot__legal" aria-label="Legal">
      <a href="privacy.html">Privacy policy</a>
      <a href="terms.html">Terms of use</a>
    </nav>
    <p class="credit">Website designed by <a href="https://obsidianstudiodesigns.co.za/" target="_blank" rel="noopener">Obsidian Studio Designs</a></p>
  </div>
</footer>
</body>
</html>
"""


def legal(title, h1, desc, path, body):
    html = head(f"{title} | {NAME}", desc, path) + f"""<main id="main">
  <section class="legal-hero">
    <div class="wrap" style="max-width:820px">
      <h1>{h1}</h1>
      <p>Last updated: {UPDATED}</p>
    </div>
  </section>
  <section class="legal">
    <div class="wrap">
{body}
    </div>
  </section>
</main>
""" + FOOT
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as fh:
        fh.write(html)


PRIVACY = f"""      <h2>Who we are</h2>
      <p>{NAME} builds canvas canopies, cattle rails, hunting rails, roof racks, canvas covers, awnings and shadenets from {ADDRESS}. In this policy, "we", "us" and "our" mean {NAME}. We respect your privacy and handle your personal information in line with the Protection of Personal Information Act, 4 of 2013 (POPIA).</p>

      <h2>What information we collect</h2>
      <p>We only collect information you choose to give us when you contact us, ask for a quote or have work done. This can include:</p>
      <ul>
        <li>your name, phone number and email address;</li>
        <li>details and photos of your vehicle, trailer, boat, caravan or property;</li>
        <li>what you would like built or repaired, and any messages you send us;</li>
        <li>invoicing and payment details needed to complete a job.</li>
      </ul>

      <h2>The quote form on this website</h2>
      <p>The quote form does not store or send anything to a server. When you press "Send on WhatsApp", your browser opens WhatsApp with your message filled in, and nothing is sent until you press send in WhatsApp yourself. Messages sent through WhatsApp are also covered by WhatsApp's own privacy policy.</p>

      <h2>How we use your information</h2>
      <ul>
        <li>to answer your enquiry and prepare a quote;</li>
        <li>to plan, build, fit and deliver your order;</li>
        <li>to invoice you and keep the records the law requires;</li>
        <li>to follow up on your job or a warranty question.</li>
      </ul>
      <p>We do not sell, rent or trade your personal information. We do not add you to marketing lists without your permission.</p>

      <h2>Photos of our work</h2>
      <p>We sometimes share photos of finished builds on this website and our Facebook page. We take care not to show number plates, faces or addresses where they can identify you. If you would rather your vehicle or property is not shown, tell us and we will remove it.</p>

      <h2>Cookies and third parties</h2>
      <p>This website does not use tracking or advertising cookies. It is hosted on GitHub Pages, which may keep basic technical logs (such as IP addresses) to keep the service secure. The map in the contact section is loaded from Google Maps, and links to WhatsApp and Facebook take you to those services, which have their own privacy policies.</p>

      <h2>How long we keep information</h2>
      <p>We keep your information only as long as we need it for the purpose you gave it to us, or as long as tax and business law requires. After that we delete or destroy it safely.</p>

      <h2>Keeping it safe</h2>
      <p>We take reasonable steps to protect your information against loss, misuse and unauthorised access, and only people who need it to do your job can see it.</p>

      <h2>Your rights</h2>
      <p>Under POPIA you may ask what information we hold about you, ask us to correct or delete it, or object to how we use it. To do this, contact us using the details below. If you are unhappy with how we handled your information, you may lodge a complaint with the Information Regulator of South Africa at <a href="https://inforegulator.org.za/" target="_blank" rel="noopener">inforegulator.org.za</a>.</p>

      <h2>Contact us</h2>
      <p>{NAME}, attention Neels du Plessis<br>{ADDRESS}<br>Phone: <a href="tel:+27829508390">{PHONE}</a><br>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>

      <h2>Changes to this policy</h2>
      <p>We may update this policy from time to time. The latest version will always be on this page, with the date it was last updated.</p>"""

TERMS = f"""      <h2>About these terms</h2>
      <p>These terms apply to your use of this website, run by {NAME} from {ADDRESS}. By using the website you agree to them. If you do not agree, please do not use the website.</p>

      <h2>Information on this website</h2>
      <p>We work hard to keep the information on this website accurate, but it is for general information only. Products, finishes, capacities and options shown here are examples of our work and can change. Every build is custom, so the final specification is the one agreed with you in your written quote.</p>

      <h2>Quotes and orders</h2>
      <ul>
        <li>A quote is valid for the period stated on it. If no period is stated, it is valid for 14 days.</li>
        <li>Work starts once you have accepted the quote and paid any deposit we ask for.</li>
        <li>Lead times are estimates and depend on materials and our workload. We will keep you informed of any delay.</li>
        <li>Changes you ask for after a build has started may affect the price and the completion date.</li>
        <li>Payment terms, warranty and any other conditions of sale will be set out in your quote or invoice.</li>
      </ul>

      <h2>Photos of our work</h2>
      <p>The photos on this website show real builds by {NAME}, along with a few illustrative images used to set the scene. Colours and finishes may look different on your screen.</p>

      <h2>Intellectual property</h2>
      <p>The text, photos, logo and design of this website belong to {NAME} or are used with permission. You may not copy or reuse them for commercial purposes without our written consent.</p>

      <h2>Links to other websites</h2>
      <p>This website links to services such as WhatsApp, Facebook and Google Maps. We are not responsible for their content or how they handle your information.</p>

      <h2>Limitation of liability</h2>
      <p>To the extent the law allows, {NAME} is not liable for any loss or damage that comes from using this website or relying on its content. Nothing in these terms limits your rights under the Consumer Protection Act, 68 of 2008.</p>

      <h2>Governing law</h2>
      <p>These terms are governed by the laws of the Republic of South Africa.</p>

      <h2>Contact us</h2>
      <p>Questions about these terms? Call <a href="tel:+27829508390">{PHONE}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""


def notfound():
    html = head(f"Page not found | {NAME}", "This page could not be found.", "404.html", robots="noindex") + """<main id="main" class="notfound">
  <div>
    <h1>Off the map.</h1>
    <p>This page took a wrong turn somewhere. Head back to the homepage to see our builds.</p>
    <a class="btn btn--accent btn--lg" href="/Custom-Made-Canvas-Canopies/">Back to home</a>
  </div>
</main>
""" + FOOT
    # 404 is served from any path, so make relative asset links absolute
    html = html.replace('href="assets/', 'href="/Custom-Made-Canvas-Canopies/assets/') \
               .replace('src="assets/', 'src="/Custom-Made-Canvas-Canopies/assets/') \
               .replace('href="favicon', 'href="/Custom-Made-Canvas-Canopies/favicon') \
               .replace('href="apple-touch', 'href="/Custom-Made-Canvas-Canopies/apple-touch') \
               .replace('href="site.webmanifest', 'href="/Custom-Made-Canvas-Canopies/site.webmanifest') \
               .replace('href="privacy.html', 'href="/Custom-Made-Canvas-Canopies/privacy.html') \
               .replace('href="terms.html', 'href="/Custom-Made-Canvas-Canopies/terms.html') \
               .replace('href="./"', 'href="/Custom-Made-Canvas-Canopies/"')
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as fh:
        fh.write(html)


def small_files():
    files = {
        "robots.txt": f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {BASE}sitemap.xml\n",
        "sitemap.xml": f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url>
    <loc>{BASE}</loc>
    <lastmod>{UPDATED_ISO}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
    <image:image><image:loc>{BASE}assets/img/og-share.jpg</image:loc></image:image>
    <image:image><image:loc>{BASE}assets/img/canvas-hilux-1200.webp</image:loc></image:image>
    <image:image><image:loc>{BASE}assets/img/rails-cruiser-1200.webp</image:loc></image:image>
    <image:image><image:loc>{BASE}assets/img/hunt-navara-1000.webp</image:loc></image:image>
    <image:image><image:loc>{BASE}assets/img/tank-pour-1200.webp</image:loc></image:image>
  </url>
  <url>
    <loc>{BASE}privacy.html</loc>
    <lastmod>{UPDATED_ISO}</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>{BASE}terms.html</loc>
    <lastmod>{UPDATED_ISO}</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
</urlset>
""",
        "site.webmanifest": """{
  "name": "Custom Made Canvas Canopies",
  "short_name": "Canvas Canopies",
  "description": "Canvas canopies, cattle rails, hunting frames and roof racks, made to measure in Pretoria.",
  "lang": "en-ZA",
  "start_url": "/Custom-Made-Canvas-Canopies/",
  "scope": "/Custom-Made-Canvas-Canopies/",
  "display": "standalone",
  "background_color": "#0e100c",
  "theme_color": "#0e100c",
  "icons": [
    { "src": "icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "icon-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ]
}
""",
        ".nojekyll": "",
        ".gitignore": "_source/\n__pycache__/\n*.log\n.DS_Store\n.claude/\nassets/img/_sizes.txt\n",
    }
    for fn, txt in files.items():
        with open(os.path.join(ROOT, fn), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(txt)


if __name__ == "__main__":
    legal("Privacy policy", "Privacy policy",
          f"How {NAME} collects, uses and protects your personal information, in line with POPIA.",
          "privacy.html", PRIVACY)
    legal("Terms of use", "Terms of use",
          f"The terms that apply when you use the {NAME} website.", "terms.html", TERMS)
    notfound()
    small_files()
    print("pages written")
