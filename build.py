"""Build the praemonit.com holding page from the logo repo.

Run: python3 -I build.py            (expects ../praemonit-logo/final)
Writes index.html, favicon.svg, favicon-32.png, apple-touch-icon.png, og.png.
"""
import re
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOGO = HERE.parent / "praemonit-logo" / "final"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

animated = (LOGO / "animated" / "pest-radar-stacked-dark.svg").read_text(encoding="utf-8")
static = (LOGO / "pest-radar-stacked-dark.svg").read_text(encoding="utf-8")
# the two inline SVGs must not share ids
static = re.sub(r'id="([^"]+)"', r'id="s-\1"', static)
static = re.sub(r'url\(#([^)]+)\)', r'url(#s-\1)', static)
label = 'role="img" aria-label="Pest Radar by Praemonit"'
animated = animated.replace("<svg ", f'<svg class="logo moving" {label} ', 1)
static = static.replace("<svg ", f'<svg class="logo still" {label} ', 1)

CSS = """
:root{color-scheme:dark}
*{box-sizing:border-box}
html,body{height:100%;margin:0}
body{background:#010101;color:#FEFEFE;font:17px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans",Helvetica,Arial,sans-serif;
  display:flex;flex-direction:column;-webkit-font-smoothing:antialiased}
main{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:48px 24px;text-align:center}
.logo{width:min(100%,560px);height:auto;display:block}
.still{display:none}
@media (prefers-reduced-motion:reduce){.moving{display:none}.still{display:block}}
h1{font-size:clamp(22px,3.4vw,30px);font-weight:600;letter-spacing:.01em;margin:44px 0 10px}
p{margin:0 auto;max-width:38em;color:#B9BABA}
p + p{margin-top:16px}
"""

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Praemonit — Pest Radar</title>
<meta name="description" content="Pest Radar by Praemonit is designed to identify changes in pest populations before they become apparent.">
<meta name="theme-color" content="#010101">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:title" content="Praemonit — Pest Radar">
<meta property="og:description" content="Identifying changes in pest populations before they become apparent.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://praemonit.com/">
<meta property="og:image" content="https://praemonit.com/og.png">
<style>{CSS}</style>
</head>
<body>
<main>
{animated}
{static}
<h1>Forewarned is forearmed.</h1>
<p>Pest Radar is designed to identify changes in pest populations before they become apparent, providing early warning and proactive management.</p>
<p lang="nl">Pest Radar is ontworpen om veranderingen in plaagpopulaties te herkennen voordat ze zichtbaar worden, waardoor je vroegtijdig gewaarschuwd wordt en proactief kunt ingrijpen.</p>
</main>
</body>
</html>
"""
(HERE / "index.html").write_text(HTML, encoding="utf-8")

shutil.copy(LOGO / "app-icon-dark.svg", HERE / "favicon.svg")
shutil.copy(LOGO / "png" / "app-icon-dark-32.png", HERE / "favicon-32.png")
shutil.copy(LOGO / "png" / "app-icon-dark-180.png", HERE / "apple-touch-icon.png")

# the share image, 1200 x 630: the static lockup on field black
og = HERE / "_og.html"
og.write_text(f"<!doctype html><style>html,body{{margin:0;height:100%;background:#010101}}"
              f"body{{display:flex;align-items:center;justify-content:center}}svg{{width:860px;height:auto}}</style>{static}", encoding="utf-8")
subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                "--window-size=1200,630", f"--screenshot={HERE / 'og.png'}", f"file://{og}"], capture_output=True, timeout=60)
og.unlink()
print("built", sorted(p.name for p in HERE.iterdir() if p.is_file()))
