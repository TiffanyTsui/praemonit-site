# praemonit-site

The holding page for **praemonit.com**: the animated *Pest Radar by Præmonit* lockup on field black, one line in English and Dutch, and the company line.

```bash
python3 -I build.py
```

`build.py` reads the logo from `../praemonit-logo/final` and writes `index.html` (self-contained, no script; the still logo replaces the animation for visitors who ask for reduced motion), the favicons and `og.png`.

Not published yet. The route that matches `solara.farm`: a public repo with GitHub Pages, a `CNAME` file holding `praemonit.com`, and at Namecheap four A records to GitHub Pages plus `www` as a CNAME to `tiffanytsui.github.io`.
