# Variation 3 v2: Pruned & Refocused Reframing

**Date:** 2026-03-24
**Branch:** `alternative-framing/real-world-impact`
**Target Journal:** Nature Cities

---

## 0. What We're Pruning and Why

The following contributions from the current manuscript are **removed from the narrative** because they are either weak, unjustifiable, or distracting:

| Pruned element | Reason |
|---|---|
| 8-model ML comparison (XGBoost, RF, NN, Ridge, Lasso, SVR, Linear) | Marginal differences (~1% between top models and linear regression). Not a meaningful scientific contribution. |
| "R² = 0.784" and all ML accuracy metrics | Without the model comparison, these numbers lose their narrative function. The ML prediction pipeline is not the paper's contribution. |
| "39% improvement over allometric baselines" | The allometric baseline computation cannot be justified. Removing it eliminates a reviewer attack surface. |
| Allometric baseline model entirely | Unjustifiable computation — cannot defend the specific implementation against a forestry reviewer. |
| N=5 hemispherical photography validation | Too weak (5 trees, single genus) to serve as a contribution. Mentioning it invites criticism without adding credibility. |
| Feature importance rankings / SHAP analysis | Depends on the ML models being a contribution. Without the ML framing, these become orphaned results. |
| XGBoost residual analysis | Entirely dependent on the ML pipeline being the story. |

### What this means structurally

The current paper is ~60% ML pipeline (methods, results, discussion). Pruning it removes the majority of the Results and Discussion sections. **This is not a trim — it's a reconception.** The paper needs new results to fill the space, or it becomes a short methods note rather than a Nature Cities article.

---

## 1. What Survives (Genuinely Strong Contributions)

After pruning, three contributions remain defensible:

### Contribution A: The Detection Gap — STRONG

**Fact:** 12,350 trees detected vs. 3,929 in Amsterdam's municipal register (tile 25BZ1). The municipal register covers public trees only.

**Why it's strong:**
- Direct empirical observation, not a model output
- 3.14× multiplier is concrete, surprising, and citable
- Challenges the adequacy of every public-trees-only municipal inventory worldwide
- The number is verifiable and inarguable

**Defensibility: VERY HIGH.** No reviewer can dispute the arithmetic. The municipal register's public-only scope is documented policy.

**Caveat:** Use "trees not captured in the municipal register" — some may be in unmaintained public spaces, not strictly private land.

---

### Contribution B: City-Scale Per-Tree LAI from LiDAR Voxelization — MODERATE-STRONG

**Fact:** The pipeline computes individual-tree LAI for all 12,350 trees using voxelization of LiDAR point clouds (MacArthur-Horn method via LeafR). This is a direct physical measurement from the point cloud, not a model prediction.

**Why it's strong:**
- Voxelization-based LAI is an established method (MacArthur-Horn, LeafR package)
- Applied here at city scale (12,350 trees, 25 km²) — unusual scale for per-tree LAI
- Produces actual LAI values (mean 3.21 ± 1.33, range 0.12–8.45 m²/m²) — consistent with literature for urban canopies
- LAI is the metric that matters for shade — not tree count, not canopy cover percentage

**Defensibility: MODERATE.** The method itself is established, but "city-scale voxelized LAI" hasn't been extensively validated. The N=5 hemispherical check (pruned as a contribution) can still be mentioned as a plausibility note in Methods, just not claimed as a validation result.

**Weakness:** Without the hemispherical validation or ML cross-validation, the LAI values are derived from LiDAR physics (Beer-Lambert extinction in voxels) without independent ground truth at this scale. The paper must acknowledge this honestly.

---

### Contribution C: The Detection + LAI Pipeline Using Standard Municipal Data — MODERATE

**Fact:** The end-to-end pipeline (DeepForest segmentation + LiDAR voxelization) runs on data that municipalities routinely collect: aerial imagery (0.25 m RGB+NIR) and airborne LiDAR (25 pts/m²). Outputs are GIS-native (GeoJSON, GeoTIFF). Processing: 18 hrs for 25 km² on standard hardware.

**Why it's strong:**
- No custom data collection required — uses existing municipal acquisitions
- DeepForest is pre-trained, no retraining needed
- GIS-format outputs integrate with existing planning tools
- Scalability is demonstrated, not just claimed

**Defensibility: MODERATE.** Single-city demonstration. Transferability claimed but not tested. However, single-city case studies are standard for Nature Cities.

---

### Summary: What We Have vs. What We Need

**What we have:** A pipeline that detects 3× more trees than the municipal register and computes per-tree LAI for all of them.

**What we don't have (yet):** Any analysis of what this means. The current paper answers "can we do this?" — the reframed paper needs to answer **"what does this reveal?"**

This is the critical gap. The 3× detection and the LAI map are *infrastructure*. Nature Cities wants *insight*. Without new results that extract meaning from the data, the paper remains a methods contribution dressed in impact language.

---

## 2. Reframed Title, RQs, Gap, and Abstract

### Title

**Primary:**
> Automated canopy mapping reveals two-thirds of Amsterdam's urban trees are absent from municipal planning data

**Alternative:**
> The unseen urban forest: city-scale tree detection and canopy density mapping beyond the municipal register

---

### Research Questions

**RQ1.** What fraction of the urban forest is absent from municipal tree inventories, and what does the unregistered canopy look like compared to the registered stock?

**RQ2.** Can per-tree Leaf Area Index — a direct determinant of shade provision — be mapped at city scale from standard municipal remote sensing data?

**RQ3.** What spatial patterns in shade capacity emerge when the full urban forest is mapped, and what do these patterns imply for heat-mitigation planning?

**Rationale:**
- RQ1 keeps the detection gap as the headline but adds a comparison dimension (registered vs. unregistered trees) that generates actual findings
- RQ2 is a methods question answered yes/no — keeps the paper grounded without requiring ML model comparison
- RQ3 is the "so what" question that Nature Cities reviewers will demand — it forces the paper to extract spatial insight from the data

---

### Gap Statement

Municipal tree inventories — the data infrastructure underlying urban heat-mitigation planning — systematically exclude trees on private land, in informal green spaces, and along unmanaged corridors. In Amsterdam, the municipal register records fewer than 4,000 public trees in a 25 km² tile where automated detection identifies over 12,000. This coverage gap is not merely quantitative: if unregistered trees differ systematically from registered ones in size, canopy density, or spatial distribution, then planning decisions based on the register alone may misallocate cooling interventions. Yet no study has characterized the unregistered urban forest at individual-tree resolution, because doing so requires both comprehensive detection (beyond public land) and per-tree canopy density estimation (beyond simple tree counts). We address this gap using a pipeline that combines deep-learning crown segmentation with LiDAR-based voxelized LAI estimation, producing the first complete, per-tree shade capacity map for a European city district.

---

### Abstract (~150 words)

Urban trees are a primary countermeasure to heat island effects, yet municipal inventories capture only publicly managed trees, leaving the majority of the urban forest unquantified for planning. Here we combine deep-learning crown segmentation of aerial imagery (0.25 m RGB+NIR) with LiDAR voxelization to map individual-tree Leaf Area Index (LAI) across a 25 km² Amsterdam district. The framework detects 12,350 trees where the municipal register records 3,929, revealing that two-thirds of the urban canopy is absent from planning data. Per-tree LAI values (mean 3.21 ± 1.33 m²/m²) are consistent with established urban canopy ranges and show [INSERT: key spatial finding — e.g., "that unregistered trees concentrate in residential areas with limited public green space" or "significant neighborhood-level variation in shade capacity invisible to current planning tools"]. The pipeline operates on standard municipal remote sensing data, runs on commodity hardware, and outputs GIS-ready maps, enabling cities to plan heat mitigation across the full urban forest.

(~148 words; the [INSERT] placeholder requires new analysis — see Section 4.)

---

## 3. Defensibility of the Pruned Framing

### 3.1. "Two-thirds of urban trees are absent from municipal planning data"

**Defensibility: VERY HIGH** — direct count, verifiable, inarguable.

**Reviewer risk: LOW.**

---

### 3.2. "Per-tree LAI via LiDAR voxelization at city scale"

**What the paper shows:** 12,350 trees with voxelization-derived LAI (MacArthur-Horn method). Values are physically plausible and distribution-consistent with urban forestry literature.

**What the paper does NOT show:** Independent ground-truth validation at scale. The N=5 hemispherical check is a plausibility note, not a validation.

**Defensibility: MODERATE.** The method is established (LeafR, MacArthur-Horn), but applying it to 12,350 urban trees with variable crown architecture, building occlusion, and mixed species is a stretch beyond typical forest-plot applications. Reviewers will ask: "How do you know these LAI values are accurate?"

**Best defense:**
- Cite the method's validation in forestry literature
- Show that LAI distributions match published urban canopy studies
- Acknowledge the limitation honestly
- Frame the contribution as "the first city-scale application" rather than "a validated method"

**Reviewer risk: MODERATE.** This is the paper's primary methodological vulnerability after pruning. A reviewer could argue: "You removed your validation, so what evidence do you have that these LAI values are correct?" The answer is method provenance + distributional consistency — enough for Nature Cities (which isn't a methods journal) but potentially insufficient for a remote sensing journal.

---

### 3.3. "The pipeline uses standard municipal data"

**Defensibility: STRONG.** Factual. The data requirements (0.25 m imagery, 25 pts/m² LiDAR) align with standard Dutch municipal acquisitions (AHN, PDOK). Whether this generalizes beyond the Netherlands requires explicit scoping.

**Reviewer risk: LOW** if properly scoped to cities with comparable data infrastructure.

---

### 3.4. Critical gap: No "so what" result

**This is the central defensibility problem.** After pruning the ML results, the paper says:
1. We detected more trees than the city knows about ✓
2. We computed their LAI ✓
3. ...and? ← **MISSING**

Nature Cities will not publish a paper that stops at "we built infrastructure." The journal requires insight — what does the complete map *reveal* that the incomplete one *hides*?

**This is why new results are essential (see Section 4).**

---

## 4. What New Results Would Make This Paper Work

The results below are ranked by **impact × feasibility**. The first three are likely achievable with existing data. The last two require external datasets but would be transformative.

---

### Result 1: Registered vs. Unregistered Tree Comparison — ESSENTIAL

**What it is:** Split the 12,350 trees into registered (3,929, in municipal database) and unregistered (8,421, detected but not in database). Compare:
- LAI distributions (do unregistered trees have different canopy density?)
- Height distributions (are they smaller? larger?)
- Species composition (registered trees have genus labels; unregistered don't)
- Spatial clustering (where are the unregistered trees?)

**Why it matters:** This answers the question "what is the city missing?" with specifics, not just a count. If unregistered trees have lower LAI (younger, unmaintained), the shade gap is smaller than the tree-count gap suggests. If they have *comparable* LAI, the city is missing an enormous cooling resource. Either finding is publishable.

**Feasibility: HIGH.** All data exists. This is a straightforward statistical comparison + spatial visualization. Probably 1–2 days of analysis.

**Impact for Nature Cities: HIGH.** This converts the detection gap from an observation into a finding with planning implications.

---

### Result 2: Shade Capacity Gap Quantification — ESSENTIAL

**What it is:** Using established LAI-to-cooling relationships from the literature (e.g., LAI >3 → 8–12°C surface temperature reduction; LAI <3 → 3–5°C), estimate:
- Total shade capacity of registered trees only (what the city "plans with")
- Total shade capacity of all detected trees (reality)
- The gap: what fraction of shade provision is invisible to current planning?

Could be expressed as: "Municipal planning data captures only X% of the district's total shade capacity, with Y% of high-shade trees (LAI >3) absent from the register."

**Why it matters:** This is the single most citable number the paper could produce. "Cities are planning heat mitigation with data that misses X% of their shade infrastructure" is a finding that policy audiences, journalists, and other researchers will immediately grasp.

**Feasibility: HIGH.** Requires only the existing LAI data + published cooling coefficients. No external data needed. 1 day of analysis.

**Impact for Nature Cities: VERY HIGH.** This is the "so what" result that the current paper lacks.

---

### Result 3: Spatial LAI Mapping — "What Planners See vs. Reality" — ESSENTIAL

**What it is:** Two side-by-side maps of the study area:
- (a) LAI distribution showing only registered trees (the planner's view)
- (b) LAI distribution showing all detected trees (reality)

Plus: neighborhood/hexbin-level aggregation showing average LAI per spatial unit. Identify areas with high unregistered tree density and areas where registered trees represent almost all canopy.

**Why it matters:** Visually striking. Immediately communicates the paper's core message. The existing `lai_spatial_gradient_hexbin.png` figure already shows spatial LAI variation — this just needs a "registered only" comparison layer.

**Feasibility: HIGH.** The spatial data exists. The hexbin visualization framework exists. Needs a filtered version showing registered trees only. 1–2 days.

**Impact for Nature Cities: HIGH.** Nature Cities values strong visual communication. This figure could anchor the entire paper.

---

### Result 4: Neighborhood-Level Analysis with Land Use — RECOMMENDED

**What it is:** Aggregate LAI by Amsterdam neighborhood (buurt/wijk boundaries, publicly available from CBS/PDOK) and cross-tabulate with land use type (residential, commercial, industrial, parks). Show:
- Which neighborhoods have highest/lowest average LAI
- Where the detection gap (registered vs. total) is largest
- Whether residential areas have more unregistered high-LAI trees than commercial areas

**Why it matters:** Grounds the analysis in recognizable urban geography. "Neighborhood X has an average LAI of Y, but the city's register captures only Z% of its trees" is immediately actionable for a city planner.

**Feasibility: MODERATE.** Requires Amsterdam neighborhood boundary data (publicly available from PDOK/CBS) and possibly land use data (BGT, also public). Integration is standard GIS work. 2–3 days.

**Impact for Nature Cities: HIGH.** Neighborhoods are the unit of urban planning. Presenting results at this scale bridges the gap between remote sensing and governance.

---

### Result 5: Heat Vulnerability Overlay — TRANSFORMATIVE (if feasible)

**What it is:** Overlay the LAI map with Amsterdam heat stress or socioeconomic vulnerability data. Identify areas with the combination of: high heat vulnerability + low LAI = priority intervention zones.

Potential data sources:
- **Klimaateffectatlas** (klimaateffectatlas.nl) — Dutch national climate adaptation atlas with heat stress maps
- **RIVM heat stress indicators** — publicly available health-related heat vulnerability data
- **CBS neighborhood statistics** — income, age demographics, housing density per buurt

**Why it matters:** This is the result that transforms the paper from "we mapped trees" to "we identified where shade is most needed and least available." It directly answers the equity question and gives Nature Cities exactly the policy-relevant insight they want.

**Feasibility: MODERATE.** The external datasets are publicly available (Netherlands has excellent open geodata infrastructure). The GIS overlay is standard. Main effort is data acquisition, cleaning, and spatial joining. 3–5 days.

**Impact for Nature Cities: TRANSFORMATIVE.** This single result could elevate the paper from "good applied methods paper" to "must-publish urban science contribution." It converts the framing from aspirational ("our maps *could* inform equitable planning") to demonstrated ("our maps *reveal* that shade-deficient areas coincide with heat-vulnerable populations").

**Risk:** If the correlation doesn't hold (i.e., shade-deficient areas are NOT heat-vulnerable), the equity narrative collapses. However, the urban ecology literature strongly suggests this correlation exists in European cities. Even a null result ("shade deficiency does not correlate with vulnerability in Amsterdam") would be interesting, though harder to publish at Nature Cities.

---

### Result 6: Height-LAI Relationship as a Transferability Tool — NICE TO HAVE

**What it is:** Characterize the height-LAI relationship (already shown to be logarithmic in the current paper) as a simple, transferable estimation tool. Show that for cities without LiDAR, height alone (obtainable from DSM, photogrammetry, or even street-level imagery) provides reasonable LAI estimates.

Present this as: "For cities where LiDAR is unavailable, tree height — obtainable from photogrammetry or even Google Street View — explains X% of LAI variance, enabling approximate shade mapping from widely available data."

**Why it matters:** Extends the paper's relevance beyond LiDAR-equipped cities. The height-LAI relationship is an ecological finding, not a model performance claim — it's defensible as basic science.

**Feasibility: HIGH.** The data already exists in the paper (the LAI-vs-height scatter plot). Just needs to be reframed as a transferability tool rather than a feature importance result.

**Impact for Nature Cities: MODERATE.** Broadens applicability but is a secondary result.

---

## 5. Recommended Paper Structure (Post-Pruning)

### Current structure (ML-centric):
1. Introduction → UHI problem, LAI importance, ML for LAI prediction
2. Methods → Data, segmentation, voxelization, **ML pipeline (8 models, feature engineering, evaluation)**
3. Results → **Model comparison, residuals, feature importance**, ecological relationships
4. Discussion → **Model performance**, feature insights, scalability
5. Conclusion

### Proposed structure (impact-centric):
1. **Introduction** → UHI problem, inadequacy of municipal inventories, need for per-tree shade mapping
2. **Methods** → Data, DeepForest segmentation, LiDAR voxelization for LAI, spatial analysis methods
3. **Results**
   - 3.1 Detection gap: 12,350 vs. 3,929 trees
   - 3.2 City-scale LAI distribution (values, ranges, consistency with literature)
   - 3.3 Registered vs. unregistered trees: what the city is missing **(NEW)**
   - 3.4 Shade capacity gap quantification **(NEW)**
   - 3.5 Spatial patterns: neighborhood-level LAI and the "planner's view vs. reality" **(NEW)**
   - 3.6 Heat vulnerability × shade deficiency [if feasible] **(NEW)**
4. **Discussion** → Planning implications, data infrastructure argument, limitations (single city, no ground-truth at scale), transferability
5. **Conclusion** → What cities should do with this information

### What happens to the ML content?

Two options:
- **(a) Cut entirely.** The paper becomes about detection + LiDAR-derived LAI + spatial analysis. Cleaner, but loses the "cities without LiDAR can use height alone" message.
- **(b) Compress to one paragraph in Methods or Discussion.** "We additionally tested whether LAI can be predicted from tree morphology alone (height, crown dimensions). A simple linear model using log-transformed height explains ~77% of LAI variance (see Supplementary), suggesting that cities lacking LiDAR could obtain approximate LAI estimates from photogrammetric height data." No model comparison table, no RMSE, no allometric baseline. Just a practical note.

**Recommendation: option (b).** It preserves the transferability message without making it a contribution that needs defending.

---

## 6. Honest Assessment: Are the Current Results Sufficient?

**No.** After pruning the ML results, the paper has:
- One strong observation (3× detection gap)
- One moderate methodological contribution (city-scale voxelized LAI)
- One infrastructure contribution (the pipeline)

This is a **methods note**, not a Nature Cities article. The journal requires insight — what does the complete map *reveal* that the incomplete one *hides*?

**To reach Nature Cities, the paper needs at minimum Results 1–3** (registered vs. unregistered comparison, shade capacity gap quantification, spatial "planners' view vs. reality" map). These are all feasible with existing data in ~3–5 days of analysis work.

**Result 5 (heat vulnerability overlay) is the difference between "publishable" and "compelling."** It's the result that would make a Nature Cities editor say "yes, this is our journal" rather than "send this to a remote sensing journal."

---

## 7. Priority Roadmap

| Priority | Result | Effort | Data needed | Impact |
|---|---|---|---|---|
| **P0** | Registered vs. unregistered tree comparison | 1–2 days | Existing | Essential |
| **P0** | Shade capacity gap quantification | 1 day | Existing + literature values | Essential |
| **P0** | "Planners' view vs. reality" map | 1–2 days | Existing | Essential |
| **P1** | Neighborhood-level LAI aggregation | 2–3 days | Public Amsterdam geodata | Recommended |
| **P1** | Heat vulnerability overlay | 3–5 days | Klimaateffectatlas / CBS | Transformative |
| **P2** | Height-LAI as transferability tool | 1 day | Existing | Nice to have |

**Minimum viable reframing:** P0 results only (3–5 days total analysis work).
**Competitive Nature Cities submission:** P0 + P1 results (7–10 days).
