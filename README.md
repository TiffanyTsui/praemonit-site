# praemonit-site

The holding page for **praemonit.com**: the animated *Pest Radar by Præmonit* lockup on field black, and one generic sentence in English and Dutch. No company line.

```bash
python3 -I build.py
```

`build.py` reads the logo from `../praemonit-logo/final` and writes `index.html` (self-contained, no script; the still logo replaces the animation for visitors who ask for reduced motion), the favicons and `og.png`.

Published with GitHub Pages from `main`; `CNAME` holds `praemonit.com`. DNS for the domain is set at the registrar: four A records to GitHub Pages and `www` as a CNAME to `tiffanytsui.github.io`.
