# Submission Checklist — Nature Cities

**Manuscript:** Mapping Leaf Area Index (LAI) in Urban Forests
**Target journal:** Nature Cities (backup: npj Urban Sustainability)
**Last updated:** 2026-03-24

---

## YOUR MANUAL TODO LIST

### BLOCKING

1. [ ] **Cull references to ≤50** — Currently 81 references. Nature Cities caps at ~50. Remove low-priority citations.

2. [ ] **Separate supplementary materials into standalone PDF** — Springer requires SI as a separate file. Currently embedded in main PDF (pp. 17–23). Recommended approach: single combined Supplementary Information PDF.

3. [ ] **Fix funding statement** — Currently "Not applicable." Confirm with Fabio/Carlo whether Senseable City Lab grants or fellowships apply. Editors will question this.

4. [ ] **Verify cover letter before submission** — Rewritten this session. Review the PDF and confirm tone/content.

### RECOMMENDED

5. [ ] **Add pipeline/workflow diagram** — End-to-end methodology figure. Standard for methods papers, conspicuously absent.

6. [ ] **Add predicted-vs-actual scatter plot** — Standard for regression papers. `results/training/pred_vs_actual.png` exists but is not in the manuscript; regenerate from source at 300 DPI if including.

7. [ ] **Re-export 4 aerial/sensor images from source at higher native resolution** — The current figures were Lanczos-upscaled to meet DPI requirements but ideally should be re-exported from the GIS/processing pipeline at ≥1280px. Originals saved in `_originals/` subdirectories. Affected files:
   - `methods/RGB_zone0.png` (was 640px JPEG, now 1280px PNG)
   - `methods/CIR_zone0.png` (was 640px JPEG, now 1280px PNG)
   - `methods/tree_viz.png` (was 628px, now 1256px)
   - `methods/06_final_combined.png` (was 640px, now 1280px)

8. [ ] **Add ORCID identifiers** — At minimum, add yours as corresponding author.

9. [ ] **Add ethics/consent statements** — "Not applicable" for ethics approval, consent to participate, consent to publish.

10. [ ] **Fix BibTeX empty `institution` field for Ref [1]** — Add "World Meteorological Organization".

11. [ ] **Consider adding Lundberg et al. 2020 SHAP paper** — Nature Machine Intelligence reference alongside the 2017 NeurIPS paper.

12. [ ] **Final spell-check and proof-read** of compiled PDF.

---

## COMPLETED

### This session
- [x] **Target journal selected** — Nature Cities (backup: npj Urban Sustainability)
- [x] **Cover letter rewritten** — Emphasises methodological novelty over raw metrics; title fixed; open data/code mentioned; 1-page PDF
- [x] **Data availability updated** — Now references Hugging Face dataset URL + Amsterdam open data portal
- [x] **Code availability updated** — Now references `github.com/thrmnn/LAI`
- [x] **CRediT author contributions rewritten** — Confirmed roles, removed all `[VERIFY WITH AUTHOR]` tags
- [x] **All figures upscaled to 300 DPI** — Matplotlib plots resampled to 2×; aerial images Lanczos-upscaled; supplementary DPI metadata corrected. Originals in `_originals/` dirs
- [x] **JPEG→PNG conversion** — `RGB_zone0` and `CIR_zone0` converted to PNG; LaTeX refs updated
- [x] **Intro–abstract overlap reduced** — Paragraphs 3–5 rewritten with complementary framing
- [x] **Hyperref bookmark warnings fixed** — `\phantomsection` + `\pdfbookmark[1]` for backmatter
- [x] **Repo cleaned** — 11 stale files removed (old analyses, backups, zips, scratch notes)
- [x] **PDF recompiled** — 28 pages, 0 errors, 0 warnings, 0 undefined refs (22 MB with high-res figures)
- [x] **Co-author approval obtained** — All confirmed

### Prior sessions
- [x] Fix Discussion R² values
- [x] Replace wrong Reference [3]
- [x] Fix title grammar ("Urban Forests")
- [x] Replace "[repository URL]" placeholder
- [x] Add XGBoost and scikit-learn citations
- [x] Ensure .tex source files tracked in git
