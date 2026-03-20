# Submission Status: LAI Paper

**Date:** 2026-03-18
**Manuscript:** Mapping Leaf Area Index (LAI) in Urban Forests
**Commit:** d35b6c5 (pushed to origin/main)
**Compiled PDF:** `draft/sn-article.pdf` — 21 pages, 5.2 MB

---

## What's Done

**Phase 1 blocking fixes (all resolved in d35b6c5):**
- Discussion R^2 error corrected: Linear Regression now shows 0.774 (was incorrectly 0.563)
- Delta R^2 comparison now correctly references "allometric baseline" (was "linear models")
- Reference [3] replaced: BibTeX entry updated to UN DESA World Urbanization Prospects 2018
- "[repository URL]" placeholder removed from Methods
- Title grammar fixed: "Urban Forests" (plural)
- All .tex/.bib source files committed and tracked in git

**Compilation:** Manuscript compiles cleanly (pdflatex + bibtex, 3 passes). Only cosmetic warnings remain (underfull boxes, 1 empty BibTeX institution field for WMO report).

---

## What Theo Still Needs To Do Before Submitting

### Blocking (must do)

1. **Add XGBoost citation** — Chen & Guestrin (2016), KDD. Primary method; reviewers will flag its absence.
2. **Add scikit-learn citation** — Pedregosa et al. (2011), JMLR. Used for 6 of 8 models.
3. **Separate supplementary materials** from main PDF into standalone file(s) per Springer Nature requirements.
4. **Confirm co-author contributions** — all CRediT roles in `contribution_statement.md` are tagged "[VERIFY WITH AUTHOR]". Send emails (templates in `coauthor_emails/`).
5. **Obtain co-author approval** of final manuscript from all authors.
6. **Select target journal** — manuscript uses generic sn-jnl template. Confirm specific Springer Nature journal and check word/figure/reference limits.
7. **Verify/create code repository** — Declarations section references github.com/senseable-city-lab but repo must exist before submission.
8. **Verify cover letter** — `cover_letter.pdf` exists; confirm it references the correct journal and editor.
9. **Verify funding statement** — currently "Not applicable." If MIT SCL funded this work, disclose it.
10. **Review data availability** — consider referencing the Hugging Face dataset mentioned in README.

### Recommended (should do)

- Add pipeline/workflow diagram (standard for methods papers)
- Add predicted vs. actual scatter plot (standard for regression papers)
- Standardize "Leaf Area Index" capitalization throughout
- Fix short title placeholder: `\title[Article Title]{...}` still says "Article Title"
- Add ORCID identifiers (at least for corresponding author)
- Add ethics/consent "Not applicable" statements
- Resolve 6 TODO comments in .tex source (Paris Agreement, DeepForest, RetinaNet, LeafR, MacArthur-Horn, SHAP citations)
- Fix BibTeX warning: add `institution = {World Meteorological Organization}` to WMO report entry

### Suggested order

1. Add the 2 missing software citations (XGBoost, scikit-learn) — 10 min
2. Fix the short title placeholder — 1 min
3. Send co-author emails — same day
4. Select target journal — needs team discussion
5. Separate supplementary materials — after journal is selected (format may vary)
6. Create/verify code repository — before submission
7. Final proof-read and submit
