# Submission Checklist: Springer Nature Journal

**Manuscript:** Mapping Leaf Area Index (LAI) in Urban Forests
**Template:** sn-jnl (Springer Nature journal article)
**Last updated:** 2026-03-24

---

## YOUR MANUAL TODO LIST (prioritised)

### BLOCKING — submission will be rejected without these

1. [ ] **Select target journal** — Everything (word limits, ref count, formatting, cover letter addressee) depends on this. Nature Cities and npj Urban Sustainability are the two candidates in CLAUDE.md.

2. [ ] **Cull references to ≤50** — Currently 81 references. Nature Cities caps at ~50. Identify and remove low-priority citations after journal selection.

3. [ ] **Separate supplementary materials into standalone PDF** — Springer requires supplementary information as separate file(s). Currently embedded in main PDF (pp. 17–23). Options: (a) single combined SI PDF, or (b) separate Supplementary Methods + Supplementary Results files.

4. [ ] **Create/populate GitHub repository** — `github.com/senseable-city-lab` is referenced in the manuscript. Must exist (at minimum a landing page with code-upon-acceptance note) before submission.

5. [ ] **Fix funding statement** — Currently "Not applicable." Confirm with Fabio/Carlo whether MIT Senseable City Lab grants, fellowships, or other funding sources apply. Editors will question this.

6. [ ] **Fix data availability statement** — Currently "available upon reasonable request." If the Hugging Face dataset contains study data, reference it explicitly. Springer prefers public repositories.

7. [ ] **Send co-author emails and obtain approval** — Templates ready in `coauthor_emails/`. Each co-author must: (a) confirm CRediT roles (currently tagged `[VERIFY WITH AUTHOR]` in `contribution_statement.md`), (b) approve the final manuscript in writing.

8. [ ] **Verify cover letter** — Ensure it references the correct journal, correct editor, and highlights key selling points (3× tree detection, 39% improvement, adaptive LiDAR).

### BLOCKING — figures

9. [ ] **Regenerate 4 method figures at higher resolution** — These are too small for print at 300 DPI:
   - `methods/RGB_zone0.jpeg` (640px, used twice) — re-export from GIS source
   - `methods/CIR_zone0.jpeg` (640px) — re-export from GIS source
   - `methods/tree_viz.png` (628px) — re-export from visualisation code
   - `methods/06_final_combined.png` (640px) — re-export from preprocessing pipeline

10. [ ] **Re-export 5 matplotlib plots at `dpi=300`** — Currently 150 DPI. Add `plt.savefig(..., dpi=300)`:
    - `results/training/overview_multi_panel.png`
    - `results/training/model_comparison.png`
    - `results/training/feature_importance_plot.png`
    - `results/training/lai_vs_height_analysis.png`
    - `results/training/ndvi_vs_lai_analysis.png`

### RECOMMENDED — improves chances but not a hard blocker

11. [ ] **Add pipeline/workflow diagram** — End-to-end methodology figure (Data → Preprocessing → Segmentation → Voxel LAI → ML → City map). Standard for methods papers.

12. [ ] **Add predicted-vs-actual scatter plot** — Standard for regression papers. `results/training/pred_vs_actual.png` exists (432×432, 72 DPI) but is not referenced in the manuscript and needs regeneration at 300 DPI.

13. [ ] **Add ORCID identifiers** — Springer strongly encourages them. At minimum, add yours as corresponding author.

14. [ ] **Add ethics/consent statements** — Add "Not applicable" for ethics approval, consent to participate, and consent to publish (standard for remote sensing studies with no human subjects).

15. [ ] **Fix BibTeX warning for Ref [1]** — Empty `institution` field for WMO report. Add "World Meteorological Organization".

16. [ ] **Consider adding SHAP 2020 paper** — Lundberg et al. 2020 (Nature Machine Intelligence) is now the standard reference alongside the 2017 NeurIPS paper.

17. [ ] **Final spell-check and proof-read** of compiled PDF.

---

## COMPLETED (automated, this session)

- [x] Fix hyperref bookmark warnings — added `\phantomsection` + `\pdfbookmark[1]` for Acknowledgements/Declarations
- [x] Reduce Abstract–Introduction overlap — rewrote intro paragraphs 3–5 with complementary framing
- [x] Audit figure DPI — all 25 images checked, findings in items 9–10 above
- [x] Verify LAI capitalization — already consistent throughout ("Leaf Area Index")
- [x] Verify "in contexts where" grammar — already correct
- [x] PDF compiles cleanly — 28 pages, 0 errors, 0 warnings, 0 undefined references

## COMPLETED (prior sessions)

- [x] Fix Discussion R² values (Linear Regression: 0.774, allometric baseline comparison)
- [x] Replace wrong Reference [3] (UN DESA World Urbanization Prospects 2018)
- [x] Fix title grammar ("Urban Forest" → "Urban Forests")
- [x] Replace "[repository URL]" placeholder
- [x] Add XGBoost and scikit-learn citations
- [x] Ensure .tex source files tracked in git
