# Review Report: Mapping Leaf Area Index (LAI) in Urban Forest

**Manuscript:** Mapping Leaf Area Index (LAI) in Urban Forest
**Authors:** Hermann T., van Selm M., Venverloo T., Duarte F., Ratti C.
**Target:** Springer Nature journal (sn-jnl template, sn-mathphys-num bibliography style)
**Pages:** 16 main text + 7 supplementary + 4 references = 27 total
**Figures:** 8 (6 main + 2 supplementary) | **Tables:** 4 (2 main + 2 supplementary)
**References:** 38
**Review date:** 2026-03-18

---

## 1. Overall Assessment

The paper presents an automated framework for estimating per-tree Leaf Area Index (LAI) in urban forests by integrating LiDAR point clouds, high-resolution aerial imagery (RGB+NIR), deep learning crown segmentation, and voxelization-based LAI calculation. A machine learning pipeline then predicts LAI from morphological and spectral features for trees without dense LiDAR. Applied to Amsterdam (12,350 trees), the best model (XGBoost) achieves R^2 = 0.784, a 39% improvement over allometric baselines.

The work addresses a genuine and timely need (scalable urban canopy assessment for heat mitigation). The methodology is sound, the experimental design is rigorous (stratified splits, ablation study, multiple models), and the writing is generally clear. However, several factual errors in the Discussion, a questionable reference, and gaps in validation strength need attention before submission.

**Submission Readiness Score: 6.5 / 10**
(Solid foundation; needs targeted revisions before submission)

---

## 2. Structure Assessment

| Section | Pages | Assessment |
|---------|-------|------------|
| Abstract | ~0.5 | Good length (~160 words), covers motivation/method/results/impact |
| Introduction | 1.5 | Well-structured problem-gap-contribution flow |
| Methods | 4.0 | Comprehensive; four subsections with good detail |
| Results | 5.0 | Thorough; dataset description + model comparison + feature analysis |
| Discussion | 3.0 | Four clear subsections; BUT contains factual errors (see below) |
| Conclusion | 1.0 | Concise summary |
| Declarations | 0.5 | Present but incomplete (see checklist) |
| Supplementary | 7.0 | Good: hyperparameter details, ablation study, species-specific results |

**Verdict:** Structure follows standard IMRD format. Well-proportioned. The Discussion is the longest section after Results, which is appropriate.

---

## 3. Section-by-Section Feedback

### 3.1 Title

**Issue:** "Mapping Leaf Area Index (LAI) in Urban Forest" is generic and grammatically incomplete (missing article or plural).

**Suggestions:**
- "Mapping Leaf Area Index in Urban Forests Using LiDAR and Machine Learning"
- "Automated Leaf Area Index Estimation for Urban Trees from Multi-Modal Remote Sensing"
- At minimum: "Urban Forest" -> "Urban Forests"

### 3.2 Abstract

**Strengths:** Concise, quantitative (R^2, 39% improvement, 3x more trees), and practical.
**Minor:** Keywords list has 4 terms. Most Springer journals recommend 4-6; consider adding "LiDAR", "Remote Sensing", or "Machine Learning".

### 3.3 Introduction (Section 1)

**Strengths:**
- Strong opening anchored to 2024 temperature record and Paris Agreement
- Clear progression: climate urgency -> UHI -> trees as countermeasure -> LAI as key metric -> current measurement gaps -> proposed solution
- Good citation density (20 of 38 total refs appear here)

**Issues:**
- **CRITICAL -- Reference [3] is wrong.** It cites "2023 UN Secretary-General Report on Cooperatives in Social Development" for the claim that "over half the world's population resides" in urban areas. This should cite a UN urbanization report (e.g., UN DESA World Urbanization Prospects 2018). A wrong citation for a basic factual claim is a red flag for reviewers.
- Paragraph 3 ("This paper presents...") repeats information from the abstract almost verbatim. Consider rephrasing for variety.

### 3.4 Methods (Section 2)

**Strengths:**
- Data provenance is clear (Amsterdam, July 2023, 0.25m imagery, 25 pts/m^2 LiDAR)
- NDVI contrast enhancement pipeline is well-described and visualized (Fig. 2)
- Feature construction is thorough (58 features across 6 categories)
- Data splits are sound (70/15/15, stratified by LAI quintiles with secondary height stratification)
- Eight models compared including an ecological baseline
- Reproducibility details present (seed=42, software versions, hardware specs)

**Issues:**
- **Section 2.1:** "Raw LiDAR point clouds were manually classified based on HSV color values" -- this is a manual step in an ostensibly "automated framework." Acknowledge this or explain how it could be automated.
- **Section 2.2:** DeepForest is described as producing "bounding boxes" but the pipeline clearly needs polygons for per-tree LiDAR clipping. The conversion from bounding boxes to crown polygons is not described.
- **Section 2.3:** The voxel size (0.5m^3) is stated but sensitivity to this choice is never tested. Given the claim of adaptability to 5-20 pts/m^2 densities, a voxel-size sensitivity analysis would strengthen the paper.
- **Code placeholder on p.7:** Text reads "[repository URL]" -- must be replaced before submission.
- **Missing pipeline diagram:** A single workflow figure showing the end-to-end pipeline (imagery + LiDAR -> preprocessing -> segmentation -> voxel LAI -> ML prediction) would greatly improve readability. This is standard for methods papers and its absence is notable.

### 3.5 Results (Section 3)

**Strengths:**
- Clear dataset characterization (Fig. 3): LAI, height, NDVI, spatial distributions
- Model comparison is comprehensive (Table 1, Fig. 4) with statistical significance testing
- Residual analysis covers bias, normality, spatial autocorrelation (Moran's I), and height-class performance
- Feature importance uses three complementary methods (XGBoost gain, RF Gini, SHAP)
- Ablation study (Supplementary Table 3) is well-designed

**Issues:**
- **Table 1:** XGBoost and Random Forest both show R^2 = 0.784. The text says the difference is "marginal though statistically significant (p = 0.003)." Reporting identical R^2 to 3 decimal places while claiming statistical significance is confusing. Report to 4 decimal places or clarify that the difference is in RMSE/MAE.
- **Section 3.1:** "267,974 trees across diverse urban contexts" is mentioned for the municipal database but only 3,929 matched trees in the study tile. This ratio (1.5%) is never explained -- presumably the 267k covers all Amsterdam while the tile covers a small area, but this should be explicit.
- **No residual plot figure:** The residual analysis (Section 3.2.2) is entirely text-based. A predicted vs. actual scatter plot would be expected by reviewers.

### 3.6 Discussion (Section 4)

**CRITICAL ERRORS:**

1. **Section 4.1, paragraph 1:** "XGBoost achieved superior predictive performance (R^2 = 0.784) compared to Random Forest (R^2 = 0.784) and **Linear Regression (R^2 = 0.563)**"

   Table 1 shows Linear Regression R^2 = 0.774, not 0.563. The value 0.564 belongs to the Allometric Baseline. This appears to conflate "Linear Regression" with "Allometric Baseline." **Must be corrected.**

2. **Section 4.1, paragraph 3:** "The substantial gap between machine learning approaches and **linear models (deltaR^2 = 0.21)**"

   The actual gap between XGBoost (0.784) and Linear Regression (0.774) is 0.01, not 0.21. The 0.22 gap is between XGBoost and the Allometric Baseline. The text incorrectly labels the allometric baseline as "linear models." **Must be corrected.**

**Other issues:**
- Section 4.3 (Validation): The hemispherical photography validation with N=5 trees (all Ulmus) is acknowledged as limited but still forms a weak pillar for the paper's validation claims. Consider framing this as "preliminary" rather than "confirmation."
- Section 4.4 (Limitations): Thorough and honest. Good coverage of occlusion, temporal alignment, species ID, computational cost. No action needed.

### 3.7 Conclusion (Section 5)

Concise and appropriate. Recapitulates key findings without overstatement. The sentence about "70% of urban forests" being excluded by manual methods could use a citation.

### 3.8 Declarations

- **Acknowledgements:** "Not applicable" -- Consider whether Amsterdam Institute or any data providers warrant acknowledgement.
- **Funding:** "Not applicable" -- If the research was conducted at MIT SCL, was there truly no funding source? Reviewers/editors may flag this.
- **Code Availability:** References github.com/senseable-city-lab but code is not yet available. Must be deposited (or at minimum a specific repo created) before submission.
- **Author Contributions:** Present in the manuscript. However, the separate `contribution_statement.md` shows all co-author roles are tagged "[VERIFY WITH AUTHOR]" -- these need confirmation.

### 3.9 Supplementary Materials

**Strengths:**
- Hyperparameter details (Supp. Methods S1) are comprehensive and reproducible
- Ablation study (Supp. Results S2) adds methodological rigor
- Species-specific analysis (Supp. Results S3) is informative

**Issues:**
- Supplementary materials are embedded in the same PDF. Springer Nature typically requires these as separate files.
- Supplementary Figure 2 heading appears on p.17 but the figure renders on p.18 (float placement issue).

---

## 4. Reference Quality

**Total references:** 38 (reasonable for a methods paper)
**Date range:** 1969-2025
**Recency:** 13 refs from 2020-2025 (34%), 25 refs from 2016-2025 (66%). Good balance.

**Issues:**
1. **Ref [3] is WRONG** (see Section 3.3 above). The UN cooperatives report has nothing to do with urban population statistics.
2. **BibTeX warning:** Empty `institution` field for ref [1] (WMO report). Should be populated.
3. **No self-citations.** This is fine but unusual; if the authors have prior related work it could be cited to establish track record.
4. **DeepForest tool (ref [21]):** Only the 2020 cross-site learning paper is cited. The original DeepForest package paper (Weinstein et al. 2020, Methods in Ecology and Evolution) may be more appropriate.
5. **No citations for XGBoost (Chen & Guestrin 2016) or scikit-learn (Pedregosa et al. 2011).** These are standard and expected when these tools are central to the methodology.
6. **No SHAP paper by Lundberg et al. 2020 (Nature MI):** Only the 2017 NeurIPS paper is cited. The more comprehensive 2020 paper is now standard.

---

## 5. Figures and Tables

| Element | Quality | Notes |
|---------|---------|-------|
| Fig. 1 (Data sources) | Good | Three panels clearly show RGB, CIR, point cloud |
| Fig. 2 (NDVI enhancement) | Good | Before/after comparison is effective |
| Fig. 3 (Dataset overview) | Adequate | Four panels; axis labels may be too small for print |
| Fig. 4 (Model comparison) | Adequate | Horizontal bar charts are clear but x-axis origin at 0 exaggerates differences |
| Fig. 5 (Feature importance) | Good | Dual-algorithm comparison is informative |
| Fig. 6 (Ecological relationships) | Good | Color coding by confidence/height adds value |
| Table 1 (Model comparison) | Good | Clear metrics, relative improvement column helpful |
| Table 2 (Hemispherical LAI) | Adequate | Only 5 trees; small but honest |
| Supp. Fig. 7 (Hemispherical) | Adequate | Binarized image could use better contrast |
| Supp. Fig. 8 (Species distrib.) | Adequate | Boxplots are readable |
| Supp. Table 3 (Ablation) | Good | Well-designed with delta-R^2 column |
| Supp. Table 4 (Species perf.) | Good | LAI SD column adds context |

**Missing figure:** A predicted vs. actual scatter plot is standard for regression papers and is conspicuously absent.
**Missing figure:** An end-to-end pipeline/workflow diagram.

---

## 6. Writing Quality

- **Clarity:** Generally good. Methods section is precise and replicable.
- **Grammar:** Minor issues (e.g., "in context where" p.4 should be "in contexts where"; "Urban Forest" in title needs article/plural).
- **Jargon balance:** Appropriate for the target audience (remote sensing / urban ecology).
- **Redundancy:** Introduction paragraph 3 and Abstract overlap significantly.
- **Capitalization inconsistency:** "Leaf Area Index" vs "leaf area index" -- standardize throughout.

---

## 7. Priority Action Items (Ranked)

### Must Fix Before Submission
1. **Correct the Discussion errors** (Section 4.1): Linear Regression R^2 is 0.774, not 0.563. The deltaR^2 = 0.21 gap is vs. allometric, not vs. linear models.
2. **Replace Reference [3]** with a correct urbanization citation (e.g., UN DESA World Urbanization Prospects).
3. **Replace "[repository URL]" placeholder** in Methods with actual repository link.
4. **Confirm co-author contributions** -- all currently tagged "[VERIFY WITH AUTHOR]".
5. **Add missing software citations** (XGBoost: Chen & Guestrin 2016; scikit-learn: Pedregosa et al. 2011).

### Strongly Recommended
6. Add a predicted vs. actual scatter plot (standard for regression papers).
7. Add a pipeline/workflow diagram figure.
8. Separate supplementary materials into standalone files per Springer Nature requirements.
9. Fix title grammar: "Urban Forest" -> "Urban Forests" (at minimum).
10. Address the bookmark-level LaTeX warnings in the Acknowledgements/Declarations section.

### Nice to Have
11. Add 1-2 more keywords (e.g., "LiDAR", "Machine Learning").
12. Discuss the manual HSV classification step and its implications for automation claims.
13. Add a voxel-size sensitivity analysis or acknowledge it as a limitation.
14. Report XGBoost vs. RF R^2 to 4 decimal places given the claimed statistical significance.
15. Add ORCID identifiers for all authors.

---

## 8. Submission Readiness Score Breakdown

| Criterion | Score (1-10) | Notes |
|-----------|-------------|-------|
| Scientific rigor | 7.5 | Sound methodology, but weak validation (N=5) |
| Novelty | 7.0 | Incremental; combines existing tools in useful way |
| Writing quality | 7.0 | Clear but has factual errors in Discussion |
| Completeness | 6.0 | Missing pipeline fig, pred vs. actual plot, code repo |
| References | 5.5 | Wrong ref [3], missing standard software citations |
| Figures/Tables | 6.5 | Adequate but missing key standard figures |
| Formatting compliance | 6.0 | Placeholder text, embedded supplements, LaTeX warnings |
| **Overall** | **6.5** | **Needs targeted revisions (1-2 weeks of focused work)** |
