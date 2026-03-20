# Submission Checklist: Springer Nature Journal

**Manuscript:** Mapping Leaf Area Index (LAI) in Urban Forests
**Template:** sn-jnl (Springer Nature journal article)
**Date:** 2026-03-18

Use this checklist to track every item needed before submission. Items marked [BLOCKING] must be resolved; items marked [RECOMMENDED] should be addressed if possible.

---

## A. Manuscript Text

- [x] **[BLOCKING] Fix Discussion error: Linear Regression R^2 value**
  ~~Section 4.1 states "Linear Regression (R^2 = 0.563)" -- actual value is 0.774 (Table 1).~~ Fixed in d35b6c5: now reads R^2 = 0.774.

- [x] **[BLOCKING] Fix Discussion error: deltaR^2 = 0.21 comparison**
  ~~Section 4.1 says "gap between machine learning approaches and linear models."~~ Fixed in d35b6c5: now correctly references "allometric baseline."

- [x] **[BLOCKING] Replace Reference [3]**
  ~~Cites "2023 UN Secretary-General Report on Cooperatives."~~ Fixed in d35b6c5: BibTeX entry now points to UN DESA World Urbanization Prospects 2018.

- [x] **[BLOCKING] Replace "[repository URL]" placeholder**
  ~~Methods section contained "[repository URL]".~~ Fixed in d35b6c5: placeholder removed.

- [x] **[BLOCKING] Fix title grammar**
  ~~"Urban Forest" -> "Urban Forests".~~ Fixed in d35b6c5: title now reads "Urban Forests."

- [ ] **[RECOMMENDED] Standardize "Leaf Area Index" capitalization**
  Inconsistent use of "Leaf Area Index" vs "leaf area index" throughout. Pick one convention and apply consistently.

- [ ] **[RECOMMENDED] Fix "in context where" (p.4)**
  Should be "in contexts where" (plural).

- [ ] **[RECOMMENDED] Reduce Abstract-Introduction overlap**
  Introduction paragraph 3 closely mirrors the abstract. Rephrase for variety.

---

## B. Figures

- [ ] **[RECOMMENDED] Add pipeline/workflow diagram**
  An end-to-end methodology figure (Data sources -> Preprocessing -> Segmentation -> Voxel LAI -> ML Pipeline -> City-wide map) is standard for methods papers and conspicuously absent.

- [ ] **[RECOMMENDED] Add predicted vs. actual scatter plot**
  Standard for regression papers. Currently residual analysis is text-only (Section 3.2.2).

- [ ] **[RECOMMENDED] Check figure resolution**
  Springer Nature requires minimum 300 DPI for all figures. Verify especially Fig. 3 and Supp. Fig. 8 (which contain small axis labels).

- [ ] **[RECOMMENDED] Fix Supplementary Figure 2 float placement**
  Heading appears on p.17 but figure renders on p.18.

- [ ] **[RECOMMENDED] Ensure all figures have consistent font sizes**
  Axis labels in Fig. 3 (dataset overview) may be too small for print.

---

## C. References and Citations

- [x] **[BLOCKING] Replace Reference [3]** (see Section A above — fixed in d35b6c5)

- [ ] **[BLOCKING] Add XGBoost citation**
  Chen, T. & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. KDD. This is the primary method and must be cited.

- [ ] **[BLOCKING] Add scikit-learn citation**
  Pedregosa, F. et al. (2011). Scikit-learn: Machine Learning in Python. JMLR. Used for 6 of 8 models.

- [ ] **[RECOMMENDED] Fix BibTeX warning for Ref [1]**
  Empty `institution` field for WMO report. Add "World Meteorological Organization".

- [ ] **[RECOMMENDED] Consider adding SHAP 2020 paper**
  Currently cites only Lundberg & Lee 2017 (NeurIPS). The comprehensive Lundberg et al. 2020 (Nature Machine Intelligence) is now standard.

- [ ] **[RECOMMENDED] Verify DeepForest citation**
  Currently cites Weinstein et al. 2020 (cross-site learning). Consider also citing the DeepForest software paper if different from ref [21].

---

## D. Supplementary Materials

- [ ] **[BLOCKING] Separate supplementary materials from main PDF**
  Springer Nature requires supplementary information as separate file(s). Currently embedded in the same PDF (pp. 17-23).

- [ ] **[RECOMMENDED] Create separate supplementary file(s)**
  Options: (a) single combined Supplementary Information PDF, or (b) separate files for Supplementary Methods and Supplementary Results.

- [ ] **[RECOMMENDED] Add Supplementary Methods S1 reference for SVR final config**
  SVR section says "Final configuration selected based on minimum validation RMSE" but doesn't list the actual selected hyperparameters (unlike RF and XGBoost).

---

## E. Author and Metadata Requirements

- [ ] **[BLOCKING] Confirm co-author contributions**
  `contribution_statement.md` shows all co-author roles tagged "[VERIFY WITH AUTHOR]". Each co-author must confirm their CRediT roles before submission.

- [ ] **[BLOCKING] Obtain co-author approval of final manuscript**
  All authors must review and approve the manuscript before submission. Email templates exist in `coauthor_emails/`.

- [ ] **[RECOMMENDED] Add ORCID identifiers for all authors**
  Springer Nature strongly encourages ORCID iDs. At minimum, the corresponding author should have one.

- [ ] **[RECOMMENDED] Verify all author email addresses are correct**
  Currently: thermann@mit.edu, mvanselm@mit.edu, tvenver@mit.edu, fduarte@mit.edu, ratti@mit.edu.

- [ ] **[RECOMMENDED] Verify affiliations are current and correctly formatted**
  Three affiliations listed. Confirm all authors' affiliation numbers are correct.

---

## F. Declarations (Required by Springer Nature)

- [ ] **[BLOCKING] Funding statement**
  Currently "Not applicable." If the research was conducted at MIT Senseable City Lab, verify there is truly no funding source (grants, fellowships). Editors will likely question this.

- [ ] **[BLOCKING] Competing Interests**
  Currently "The authors declare no competing interests." -- OK if accurate.

- [ ] **[BLOCKING] Data Availability**
  Currently "available from the corresponding author upon reasonable request." Springer Nature prefers data in public repositories. The Hugging Face dataset (mentioned in README) should be referenced here if it contains the study data.

- [ ] **[BLOCKING] Code Availability**
  References github.com/senseable-city-lab. The repository must exist and contain the code (or at minimum a landing page with timeline) before submission.

- [ ] **[RECOMMENDED] Ethics approval**
  Add explicit statement: "Not applicable -- this study used publicly available remote sensing data and did not involve human subjects or animal experiments."

- [ ] **[RECOMMENDED] Consent to participate / Consent to publish**
  Add "Not applicable" for both (standard for non-human-subjects research).

---

## G. Journal-Specific Requirements

- [ ] **[BLOCKING] Select target journal**
  The manuscript uses the generic sn-jnl template. Identify the specific Springer Nature journal (e.g., *Scientific Reports*, *Urban Ecosystems*, *Landscape and Urban Planning* [Elsevier -- different publisher], *Environmental Monitoring and Assessment*). The journal choice affects formatting, word limits, and scope fit.

- [ ] **[BLOCKING] Check word/page count limits**
  Main text is ~5,500 words (excluding references and supplementary). Verify against target journal limits. *Scientific Reports* has no strict limit; other journals may.

- [ ] **[BLOCKING] Check reference limit**
  38 references. Most Springer journals allow 40-60 for research articles. Should be fine, but verify against target journal.

- [ ] **[RECOMMENDED] Check figure count limit**
  8 figures (6 main + 2 supplementary). Some journals limit main-text figures to 6-8.

- [ ] **[RECOMMENDED] Prepare structured abstract if required**
  Current abstract is unstructured. Some Springer journals require structured abstracts (Background, Methods, Results, Conclusions).

---

## H. Cover Letter

- [ ] **[BLOCKING] Verify cover letter is current**
  `cover_letter.pdf` exists. Ensure it references the correct journal, is addressed to the correct editor, and highlights the paper's significance and fit.

- [ ] **[RECOMMENDED] Mention novelty explicitly in cover letter**
  Key selling points: (1) 3x more trees detected than municipal database, (2) 39% improvement over allometric baselines, (3) framework works with variable LiDAR density.

---

## I. LaTeX / Compilation

- [ ] **[RECOMMENDED] Resolve hyperref bookmark warnings**
  Two warnings about bookmark level differences in Acknowledgements/Declarations section. Likely caused by using `\subparagraph` for Acknowledgements/Declarations headings -- restructure to avoid.

- [ ] **[RECOMMENDED] Address underfull vbox/hbox warnings**
  Multiple underfull warnings (cosmetic). Consider adding `\raggedbottom` or adjusting page breaks.

- [ ] **[RECOMMENDED] Upgrade TeX Live**
  Currently using TeX Live 2019. The sn-jnl template may have updates for newer distributions.

- [x] **[RECOMMENDED] Ensure .tex source files are included in submission**
  ~~Source files appeared excluded from git.~~ Fixed in d35b6c5: .tex, .bib, and section files now tracked in draft/sections/.

---

## J. Pre-Submission Final Checks

- [ ] Run spell-check on final manuscript
- [ ] Verify all cross-references resolve correctly (\ref, \cite)
- [ ] Verify all figures are referenced in the text
- [ ] Verify all tables are referenced in the text
- [ ] Confirm all supplementary items are referenced from main text
- [ ] Do a final PDF proof-read of the compiled document
- [ ] Verify DOI links in references are functional
- [ ] Check that the Hugging Face dataset URL in README is accessible
- [ ] Get written approval from all co-authors

---

## Summary: Critical Path to Submission

**Phase 1 -- Must fix (days 1-3):**
1. ~~Correct the two Discussion factual errors (R^2 values)~~ DONE
2. ~~Replace wrong Reference [3]~~ DONE
3. Add missing software citations (XGBoost, scikit-learn) — STILL TODO
4. ~~Replace "[repository URL]" placeholder~~ DONE
5. ~~Fix title grammar~~ DONE

**Phase 2 -- Co-author coordination (days 1-7, parallel):**
6. Send co-author emails (templates ready in coauthor_emails/)
7. Confirm CRediT contributions
8. Obtain manuscript approval from all authors

**Phase 3 -- Polish (days 4-7):**
9. Add pipeline diagram and predicted vs. actual plot
10. Separate supplementary materials
11. Verify/deposit code repository
12. Select target journal and verify compliance

**Phase 4 -- Submit (days 7-10):**
13. Final proof-read
14. Upload to journal submission system
15. Submit cover letter + manuscript + supplementary + figures
