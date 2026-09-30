# Alexander Hounsou — Studio portfolio

Static HTML/CSS/JavaScript portfolio. No package install or build is required.

## Pages

- `/`: homepage
- `/nomi/`: Nomi case study
- `/aie-insured-portal/`: AIE case study
- `/coverage-collective/`: Coverage Collective case study
- `/resume/`: résumé and downloadable PDF

Run locally from the repository root with `python3 -m http.server 8000`, then open `http://localhost:8000`.

`vercel.json` maps the homepage and case routes to their static files. Git-triggered deployment is disabled for the `studio-redesign` review branch only. No production branch setting is changed.

The previous single-page site (`portfolio.html`, `images/`, SVG sources) was replaced by this version; it remains in git history. The website uses optimized assets under `assets/`.

## Fonts

Work Sans is self-hosted in four weights, subset for the portfolio. Copyright 2019 The Work Sans Project Authors. Licensed under SIL Open Font License 1.1; see `assets/fonts/OFL.txt`. Source: https://github.com/google/fonts/tree/main/ofl/worksans

## Validation

`python3 scripts/validate_portfolio.py` checks the five pages, local links, anchors, image/font references, responsive styles and static routing. `node --check app.js` checks JavaScript syntax. The PDF contains selectable text and was visually checked. Browser layout/interaction checks were not completed in the authoring environment.
