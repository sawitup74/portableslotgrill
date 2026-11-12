"""portableslotgrill.com build. Run: python3 build.py
To switch on visit counting, replace portableslotgrill in GOATCOUNTER below with the real GoatCounter code, then rebuild."""
GOATCOUNTER = "https://portableslotgrill.goatcounter.com/count"
DOMAIN = "https://portableslotgrill.com"
UTM_SOURCE = "portableslotgrill"
SITE_NAME = "Portable Slot Grill"
LASTMOD = "2026-10-31"
THEME_COLOR = "#0f5e63"
HOME_IMG = "c07"
HOME_TITLE = "Portable Slot Grill: Grilling Guides for Tailgates, Camping, RV, Beach and Patio"
HOME_DESC = "Practical portable grilling guides: tailgates, campsites, RV trips, beaches, parks and small patios, plus how to pack, carry and store a flat-pack charcoal grill."
BRAND_HTML = '<span class="pill">portable</span><span class="wm">slot<b>grill</b><small>guides</small></span>'
FOOTER_BLURB = "<b>Portable Slot Grill</b> is a set of practical guides for grilling away from home: tailgates, campsites, RV parks, beaches, picnic areas and small patios, and how to pack and carry the grill. It's published by Slot Grill."
NOTE = "Specs and prices come from SlotGrill.com. Always cook outdoors on a stable, non-combustible surface and follow the rules of the park, venue, campground or building where you are."
CATS = {
 "places": ("where-to-grill", "Where to Grill", "Tailgates, campsites, RV parks, beaches, picnic areas, backyards and small patios: how to set up and cook in each.", "Where"),
 "transport": ("transport-and-storage", "Transport &amp; Storage", "Packing a flat-pack grill in a car, RV, boat or backpack, keeping soot contained, and storing it at home.", "Pack &amp; store"),
 "howto": ("portable-grilling-how-tos", "On-the-Go How-Tos", "Lighting, heat control, coolers and food safety, wind, surfaces and ash when you're away from a kitchen.", "How-tos"),
 "recipes": ("portable-recipes", "Portable Recipes", "Easy-to-pack recipes for grates and griddle plates: prep at home, cook anywhere.", "Recipes"),
 "about": ("about-portable-slot-grill", "The Grill &amp; About", "Compact vs Full Size, about the site, the FAQ and a glossary.", "About"),
}
NAV_CATS = ["places", "transport", "howto", "recipes", "about"]
FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="#0f5e63"/><circle cx="44" cy="20" r="7" fill="#ffc83d"/><rect x="14" y="30" width="36" height="6" rx="3" fill="#fff"/><rect x="14" y="40" width="36" height="6" rx="3" fill="#ffc83d"/></svg>'
CSS = """
:root{--teal:#0f5e63;--teal2:#16808a;--sun:#ffc83d;--coral:#ef6a4c;--bg:#fffdf7;--card:#fff;--ink:#14302f;--mute:#546b6a;--line:#e3ece9;--mint:#e6f4f1}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;font:17px/1.7 'Gill Sans','Gill Sans MT','Trebuchet MS',Calibri,sans-serif;color:var(--ink);background:var(--bg)}
h1,h2,h3{font-family:'Trebuchet MS','Gill Sans',Verdana,sans-serif;line-height:1.18;font-weight:800}
a{color:var(--teal2)}img{max-width:100%;height:auto;display:block}
.top{background:#fff;border-bottom:3px solid var(--sun);position:sticky;top:0;z-index:9}
.nav{max-width:1100px;margin:auto;display:flex;align-items:center;gap:1.2rem;padding:.6rem 1rem}
.brand{display:flex;align-items:center;gap:.45rem;text-decoration:none;color:var(--teal)}
.pill{background:var(--teal);color:#fff;border-radius:999px;padding:.12rem .6rem;font-size:.78rem;font-weight:700;letter-spacing:.04em}
.wm{font-weight:800;font-size:1.2rem;letter-spacing:-.01em}.wm b{color:var(--coral)}.wm small{font-weight:600;font-size:.72rem;color:var(--mute);margin-left:.3rem;text-transform:uppercase;letter-spacing:.1em}
.nav nav{flex:1;display:flex;gap:1rem;justify-content:flex-end}.nav nav a{color:var(--ink);text-decoration:none;font-size:.95rem;padding:.25rem .6rem;border-radius:999px}.nav nav a:hover{background:var(--mint)}
.btn{display:inline-block;background:var(--coral);color:#fff!important;text-decoration:none;font-weight:800;padding:.75rem 1.3rem;border-radius:999px}
.btn:hover{background:#d9573b}.btn.small{padding:.45rem .9rem;font-size:.88rem;background:var(--teal)}.btn.ghost{background:#fff;color:var(--teal)!important}
main{max-width:780px;margin:auto;padding:1.2rem 1rem 2rem}main.wide{max-width:1100px}
.crumbs{font-size:.85rem;color:var(--mute)}.crumbs a{color:var(--mute)}
h1{font-size:clamp(1.9rem,4.5vw,2.8rem);margin:.4rem 0 .6rem;color:var(--teal)}h2{margin-top:2.3rem;font-size:1.5rem}h2::after{content:"";display:block;width:48px;height:4px;border-radius:2px;background:var(--sun);margin-top:.4rem}
.lede{font-size:1.15rem;color:var(--mute)}
.hero-img{border-radius:22px;margin:1rem 0 1.4rem;aspect-ratio:16/9;object-fit:cover;width:100%}
.facts{display:flex;flex-wrap:wrap;gap:.5rem;margin:1rem 0}.facts span{background:var(--mint);border-radius:999px;padding:.3rem .9rem}
.tbl{overflow-x:auto;margin:1rem 0}table{border-collapse:separate;border-spacing:0;width:100%;background:#fff;font-size:.95rem;border:1px solid var(--line);border-radius:14px;overflow:hidden}th,td{border-bottom:1px solid var(--line);padding:.6rem .75rem;text-align:left;vertical-align:top}th{background:var(--mint);color:var(--teal)}
.note{background:#fff7dd;border-radius:14px;padding:.85rem 1.1rem}
details{background:#fff;border:1px solid var(--line);border-radius:14px;margin:.5rem 0;padding:.65rem 1rem}summary{cursor:pointer;font-weight:700;color:var(--teal)}
.product{display:grid;grid-template-columns:190px 1fr;gap:1.2rem;align-items:center;background:var(--mint);border-radius:22px;padding:1.2rem;margin:2rem 0}
.product img{border-radius:16px;aspect-ratio:1;object-fit:cover}.product h3{margin:.1rem 0 .3rem;font-size:1.3rem;color:var(--teal)}.kicker{text-transform:uppercase;letter-spacing:.12em;font-size:.72rem;color:var(--coral);font-weight:800;margin:0}
.price{font-weight:800;font-size:1.25rem}.price s{color:var(--mute);font-weight:400;font-size:.95rem;margin-left:.5rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1.1rem}
.card{background:#fff;border-radius:18px;text-decoration:none;color:var(--ink);overflow:hidden;box-shadow:0 2px 10px rgba(15,94,99,.08);transition:box-shadow .15s}.card:hover{box-shadow:0 6px 20px rgba(15,94,99,.18)}
.card img{aspect-ratio:16/10;object-fit:cover;width:100%}.card div{padding:.85rem 1rem}.card h3{margin:0 0 .3rem;font-size:1.06rem;color:var(--teal)}.card p{margin:0;font-size:.9rem;color:var(--mute)}
.hero{background:var(--teal);color:#fff;border-radius:28px;display:grid;grid-template-columns:1.1fr 1fr;gap:2rem;align-items:center;padding:2.4rem;margin:.6rem 0 1.2rem;position:relative;overflow:hidden}
.hero::before{content:"";position:absolute;right:-60px;top:-60px;width:220px;height:220px;border-radius:50%;background:var(--sun);opacity:.9}
.hero>*{position:relative}.hero h1{color:#fff;font-size:clamp(2rem,4.8vw,3.1rem)}.hero p{color:#d8efec}.hero img{border-radius:20px}.hero .kicker{color:var(--sun)}
.places{display:flex;flex-wrap:wrap;gap:.5rem;margin:1rem 0}.places a{background:#fff;color:var(--teal);text-decoration:none;border-radius:999px;padding:.4rem 1rem;font-weight:700;box-shadow:0 1px 4px rgba(0,0,0,.08)}
.hsec h2 a{color:inherit;text-decoration:none}.related ul{columns:2;gap:2rem}
footer{background:var(--teal);color:#cde6e3;padding:2.4rem 1rem;margin-top:3rem;font-size:.92rem}footer .in{max-width:1100px;margin:auto}footer a{color:#fff}.fbrand .wm{color:#fff}.fbrand .wm small{color:#cde6e3}.fbrand .pill{background:var(--sun);color:var(--teal)}.fbrand{display:flex;gap:.45rem;align-items:center;margin-bottom:.6rem}
.small-note{font-size:.85rem;color:var(--mute)}
@media(max-width:780px){.nav nav{display:none}.nav{justify-content:space-between}.hero{grid-template-columns:1fr;padding:1.5rem}.product{grid-template-columns:1fr}.related ul{columns:1}body{font-size:16.5px}}
"""
# ---------------- engine (shared by all guide sites; config is at the top of this file) ----------------
import json, html, os, sys, re, glob


# --- Search Console schema helpers ---
# Guide sites do not sell products and have no reviews. Do not emit Product
# JSON-LD (Search Console flags missing aggregateRating/review). Use Brand.
def product_schema_compact(valid_from="2026-11-04"):
    return {"@type":"Brand","name":"Slot Grill","url":"https://slotgrill.com/"}
def product_schema_aggregate(valid_from="2026-11-04"):
    return {"@type":"Brand","name":"Slot Grill","url":"https://slotgrill.com/"}
# --- end schema helpers ---
SG = "https://slotgrill.com"
UTM = "utm_source=%s&amp;utm_medium=referral&amp;utm_campaign=guide-site" % UTM_SOURCE
def sg(path=""):
    return SG + path + ("&amp;" if "?" in path else "?") + UTM
COMPACT = sg("/products/slot-grill-compact-carbon-steel-free-shipping")
FULL = sg("/products/slot-grill-carbon-steel-collapsible-bbq-grill")
GRID = sg("/products/slot-grill-griddle-plancha")
BALM = sg("/products/seasoning-balm-for-slot-grill")
THERMO = sg("/products/slot-grill-instant-read-digital-meat-thermometer")
BUNDLE = sg("/products/seasoning-balm-meat-thermometer-bundle")
SHOP = sg("/collections/all")
SPECS = sg("/pages/slot-grill-specs-setup-care")
ABOUTSG = sg("/pages/about-slot-grill")
MADE = sg("/pages/made-in-usa")
SGFAQ = sg("/pages/faq-frequently-asked-questions")
CONTACT = sg("/pages/contact")
HOME = sg("/")
CDN = "https://cdn.shopify.com/s/files/1/0721/8833/0172/files/"
IMG = {k: CDN + v for k, v in dict(
    c07="compact-07.jpg?v=1792382833", c28="compact-28.jpg?v=1792382861", c08="compact-08.jpg?v=1792382834",
    c13="compact-13.jpg?v=1792382834", both16="both-16.jpg?v=1792382825", both02="both-02.jpg?v=1792382824",
    full01="full-size-01.jpg?v=1792382862", full08="full-size-08.jpg?v=1792382863", full10="full-size-10.jpg?v=1792382864",
    full13="full-size-13.jpg?v=1792382866", grid1="griddle-add-on.jpg?v=1793024225", grid2="griddle-add-on-two.jpg?v=1793024983",
    balm="seasoning-balm-main.jpg?v=1791978819", thermo="thermometer-red-clean.jpg?v=1791939312",
    bundle="balm-thermometer-bundle-v3.jpg?v=1791943793").items()}
# Product facts below are copied from slotgrill.com product and specs pages (checked 2026-10-31).
PRODUCTS = {
 "compact": dict(name="Slot Grill Compact", url=COMPACT, img="c07", alt="Slot Grill Compact carbon steel charcoal grill",
    facts='12-gauge carbon steel · about 14 lb · 16.25" × 9" cooking area · packs about 1" thick · made in the USA (Texas)',
    price="$89.97", was="$99.97", btn="See the Compact at SlotGrill.com"),
 "full": dict(name="Slot Grill Full Size", url=FULL, img="full01", alt="Slot Grill Full Size carbon steel charcoal grill",
    facts='10-gauge carbon steel · about 27.6 lb · 20.5" × 11.25" cooking area · packs about 1.25" thick · made in the USA (Texas)',
    price="$149.97", was="$159.97", btn="See the Full Size at SlotGrill.com"),
 "griddle": dict(name="Slot Grill Griddle Add-On", url=GRID, img="grid1", alt="Slot Grill griddle plancha add-on plates",
    facts="Carbon steel flat-top plates made for the Slot Grill two-piece top. One or two plates, for the Compact or the Full Size. Stacks flat with the grill. Grill not included.",
    price="from $20.00", was="", btn="See the griddle at SlotGrill.com"),
}
PAGES = []
def page(slug, title, desc, img, body, cat, faq=None):
    global PAGES
    PAGES = [p for p in PAGES if p[0] != slug]
    PAGES.append((slug, title, desc, img, body, cat, faq or []))
def esc(s): return html.escape(s, quote=True)
def L(slug, text): return '<a href="/%s.html">%s</a>' % (slug, text)
def X(url, text): return '<a href="%s">%s</a>' % (url, text)
def ul(items): return "<ul>" + "".join("<li>%s</li>" % i for i in items) + "</ul>"
def ol(items): return "<ol>" + "".join("<li>%s</li>" % i for i in items) + "</ol>"
def table(head, rows):
    return '<div class="tbl"><table><tr>' + "".join("<th>%s</th>" % h for h in head) + "</tr>" + "".join(
        "<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in rows) + "</table></div>"
def tip(t): return '<p class="note">%s</p>' % t
TEMPS_ROWS = [("Beef, pork, lamb and veal steaks, chops and roasts", "145°F, then rest 3 minutes"),
    ("Ground beef, pork, lamb and veal (burgers, fresh sausage)", "160°F"),
    ("Chicken and turkey, whole, pieces or ground", "165°F"),
    ("Fish and shellfish", "145°F, or flesh opaque and flakes with a fork"),
    ("Egg dishes", "160°F; cook eggs until yolks and whites are firm"),
    ("Precooked sausage, hot dogs and leftovers", "Reheat to 165°F")]
def temps():
    return ("<h2>Safe internal temperatures</h2><p>Check the thickest part with an instant-read thermometer, away from bone. These are USDA minimum safe temperatures; tougher cuts like brisket and ribs are cooked well past them for tenderness.</p>"
            + table(["Food", "Minimum internal temperature"], TEMPS_ROWS))
def recipe(intro, serves, time, ingr, steps, tips=None, extra="", size="compact"):
    p = PRODUCTS[size]
    h = intro + '<div class="facts"><span><b>Serves</b> %s</span><span><b>Time</b> %s</span><span><b>Grill</b> <a href="%s">%s</a></span></div>' % (serves, time, p["url"], p["name"])
    h += "<h2>Ingredients</h2>" + ul(ingr) + "<h2>Method</h2>" + ol(steps) + extra
    if tips: h += "<h2>Tips</h2>" + ul(tips)
    return h + temps()
def faqld(faq):
    if not faq: return ""
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": html.unescape(re.sub("<[^>]+>", "", q)), "acceptedAnswer": {"@type": "Answer", "text": html.unescape(re.sub("<[^>]+>", "", a))}} for q, a in faq]}) + "</script>"
def faqhtml(faq, h="Questions people ask"):
    return ("<h2>%s</h2>" % h + "".join('<details><summary>%s</summary><p>%s</p></details>' % (q, a) for q, a in faq)) if faq else ""
def productbox(kind="compact"):
    p = PRODUCTS[kind]
    was = "<s>%s</s>" % p["was"] if p["was"] else ""
    return ('<aside class="product"><img src="%s" alt="%s" loading="lazy"><div><p class="kicker">From the maker in Buna, Texas</p><h3>%s</h3><p>%s</p><p class="price">%s%s</p><a class="btn" href="%s">%s</a></div></aside>'
            % (IMG[p["img"]], esc(p["alt"]), p["name"], p["facts"], p["price"], was, p["url"], p["btn"]))
def crumbs(items):
    return '<p class="crumbs">' + " › ".join(('<a href="%s">%s</a>' % (u, t)) if u else t for t, u in items) + "</p>"
def shell(title, desc, slug, inner, img=None, faq=None, kind="Article", trail=None, wide=False):
    canon = DOMAIN + ("/" if slug == "index" else "/%s.html" % slug)
    img = img or IMG["c07"]
    ld = [{"@context": "https://schema.org", "@type": "WebSite" if slug == "index" else kind, "name": html.unescape(title),
           "url": canon, "description": html.unescape(desc), "image": img,
           "publisher": {"@type": "Organization", "name": SITE_NAME, "url": DOMAIN + "/"},
           "about": product_schema_aggregate()}]
    if kind == "Article" and slug != "index": ld[0]["headline"] = html.unescape(title)
    if trail:
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": html.unescape(re.sub("<[^>]+>", "", t)), "item": DOMAIN + (u if u else "/%s.html" % slug)} for i, (t, u) in enumerate(trail)]})
    lds = "".join('<script type="application/ld+json">%s</script>' % json.dumps(x) for x in ld)
    nav = "".join('<a href="/%s.html">%s</a>' % (CATS[k][0], CATS[k][3]) for k in NAV_CATS) + '<a href="/faq.html">FAQ</a>'
    foot = " · ".join('<a href="/%s.html">%s</a>' % (c[0], c[1]) for c in CATS.values()) + ' · <a href="/faq.html">FAQ</a> · <a href="/glossary.html">Glossary</a> · <a href="/about.html">About</a> · <a href="/compact-vs-full-size-slot-grill.html">Compact vs Full Size</a>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(html.unescape(title))}</title><meta name="description" content="{esc(html.unescape(desc))}"><link rel="canonical" href="{canon}">
<meta property="og:type" content="{'website' if slug=='index' else 'article'}"><meta property="og:site_name" content="{SITE_NAME}"><meta property="og:title" content="{esc(html.unescape(title))}"><meta property="og:description" content="{esc(html.unescape(desc))}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{img}">
<meta name="theme-color" content="{THEME_COLOR}"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css">{lds}{faqld(faq)}</head><body>
<header class="top"><div class="nav"><a class="brand" href="/" aria-label="{SITE_NAME} home">{BRAND_HTML}</a><nav>{nav}</nav><a class="btn small" href="{HOME}">SlotGrill.com</a></div></header>
<main class="{'wide' if wide else ''}">{inner}</main>
<footer><div class="in"><div class="fbrand">{BRAND_HTML}</div><p>{FOOTER_BLURB}</p><p>Slot Grill is a collapsible carbon steel charcoal grill made in the USA by Keith in Buna, Texas. Slot Grill® is a registered trademark. Genuine Slot Grills are sold at <a href="{HOME}">SlotGrill.com</a>, the @SlotGrill TikTok Shop and @SlotGrill on the Shop app. Questions about an order or the grill? Use the <a href="{CONTACT}">Slot Grill contact form</a>.</p><p class="flinks"><a href="/">Home</a> · {foot}</p></div></footer>
<script data-goatcounter="{GOATCOUNTER}" async src="//gc.zgo.at/count.js"></script><script>document.addEventListener("click",function(e){{var a=e.target.closest&&e.target.closest('a[href*="//slotgrill.com"]');if(a&&window.goatcounter&&window.goatcounter.count){{window.goatcounter.count({{path:"click-to-slotgrill/"+location.pathname,title:"Click to slotgrill.com",event:true}})}}}});</script></body></html>
'''
def related(slug, cat):
    rel = [p for p in PAGES if p[5] == cat and p[0] != slug][:8]
    if not rel: return ""
    c = CATS[cat]
    return '<nav class="related"><h2>More in %s</h2><ul>' % c[1] + "".join('<li><a href="/%s.html">%s</a></li>' % (p[0], p[1]) for p in rel) + '</ul><p><a href="/%s.html">All %s →</a></p></nav>' % (c[0], c[1])
def article(slug, title, desc, img, body, cat, faq):
    c = CATS[cat]
    wc = lambda b: len(re.sub("<[^>]+>", " ", b).split())
    for blk in globals().get("EXTRA", {}).get(cat, []):
        if wc(body) >= 520: break
        if blk[:60] not in body: body += blk
    trail = [("Home", "/"), (c[1], "/%s.html" % c[0]), (title, None)]
    kind = "big" if "full" in img else "compact"
    box = productbox("full" if kind == "big" else "compact")
    if "griddle" in body.lower() and cat != "about": box += productbox("griddle")
    inner = (crumbs(trail) + '<article><h1>%s</h1><p class="lede">%s</p><img class="hero-img" src="%s" alt="%s">' % (title, desc, IMG[img], esc(html.unescape(title)) + " – Slot Grill")
             + body + (faqhtml(faq) if slug != "faq" else "") + "</article>" + box + related(slug, cat) + '<p class="small-note">%s</p>' % NOTE)
    return shell(title, desc, slug, inner, img=IMG[img], faq=faq, trail=trail)
def cardgrid(ps):
    return '<div class="grid">' + "".join('<a class="card" href="/%s.html"><img src="%s" alt="" loading="lazy"><div><h3>%s</h3><p>%s</p></div></a>' % (s, IMG[i], t, d) for s, t, d, i, *_ in ps) + "</div>"
def build():
    open("style.css", "w").write(CSS)
    open("favicon.svg", "w").write(FAVICON)
    open("CNAME", "w").write(DOMAIN.split("//")[1] + "\n")
    for f in sorted(glob.glob("content_*.py")): exec(open(f).read(), globals())
    # FAQ page aggregates every page's questions
    allq = [(q, a, p) for p in PAGES for q, a in p[6] if p[0] != "faq"]
    base = [p for p in PAGES if p[0] == "faq"]
    if base:
        b = base[0]
        body = b[4] + "".join('<h2>%s</h2>' % CATS[k][1] + "".join('<details><summary>%s</summary><p>%s <a href="/%s.html">Read: %s</a></p></details>' % (q, a, p[0], p[1]) for q, a, p in allq if p[5] == k) for k in CATS)
        page("faq", b[1], b[2], b[3], body, b[5], b[6])
    for f in glob.glob("*.html"): os.remove(f)
    for p in PAGES: open(p[0] + ".html", "w").write(article(*p))
    for k, c in CATS.items():
        ps = [p for p in PAGES if p[5] == k]
        trail = [("Home", "/"), (c[1], None)]
        open(c[0] + ".html", "w").write(shell(c[1] + " | " + SITE_NAME, c[2], c[0], crumbs(trail) + "<h1>%s</h1><p class=\"lede\">%s</p>" % (c[1], c[2]) + cardgrid(ps) + productbox(), kind="CollectionPage", trail=trail, wide=True))
    open("index.html", "w").write(shell(HOME_TITLE, HOME_DESC, "index", home_html(), img=IMG[HOME_IMG], wide=True))
    open("404.html", "w").write(shell("Page not found | " + SITE_NAME, "That page isn't here. Browse the guides instead.", "404",
        "<h1>That page isn't here</h1><p>The link may be old or mistyped. Try one of these:</p>" + ul(['<a href="/">Home</a>'] + ['<a href="/%s.html">%s</a>' % (c[0], c[1]) for c in CATS.values()] + ['<a href="/faq.html">FAQ</a>']), kind="WebPage"))
    urls = [DOMAIN + "/"] + ["%s/%s.html" % (DOMAIN, c[0]) for c in CATS.values()] + ["%s/%s.html" % (DOMAIN, p[0]) for p in PAGES]
    open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join("  <url><loc>%s</loc><lastmod>%s</lastmod></url>\n" % (u, LASTMOD) for u in urls) + "</urlset>\n")
    open("robots.txt", "w").write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % DOMAIN)
    print(len(PAGES), "articles +", len(CATS), "hubs + home")
def home_html():
    secs = "".join('<section class="hsec"><h2><a href="/%s.html">%s</a></h2><p>%s</p>%s</section>' % (c[0], c[1], c[2], cardgrid([p for p in PAGES if p[5] == k][:6])) for k, c in CATS.items())
    return HOME_HERO + secs + '<section class="hsec"><h2>The two Slot Grills, side by side</h2><p>Both are tab-and-slot, carbon steel, made in Texas. ' + L("compact-vs-full-size-slot-grill", "Full comparison →") + "</p>" + productbox("compact") + productbox("full") + "</section>"
if __name__ == "__main__":
    build()

# Indexing post-process (2026-11-09): 404 noindex, redirect stubs without noindex, real sitemap lastmod
import subprocess as _sp, sys as _sys
_sp.run([_sys.executable, "postfix_indexing.py"])
