# Variation 3 v2: Detailed Analysis Design

**Date:** 2026-03-24
**Branch:** `alternative-framing/real-world-impact`
**Target Journal:** Nature Cities

This document details the two core analyses needed to make the pruned reframing work: (1) "Planners' View vs. Reality" and (2) the Heat Vulnerability × Shade Deficiency overlay. It also inventories the Amsterdam open geodata sources available to support them.

---

## Part A: Amsterdam Open Geodata Sources

The Netherlands has one of the best open geodata infrastructures in Europe. Everything below is free and publicly accessible.

### A.1 Heat Stress Data

**Klimaateffectatlas (Climate Impact Atlas)**
- URL: https://www.klimaateffectatlas.nl/en/
- Format: Interactive map; underlying rasters via PDOK WMS/WCS (GeoTIFF)
- Resolution: 5–100 m grid depending on indicator
- Variables: Perceived temperature (PET), heat stress days, tropical nights, UHI intensity
- Access: Free, no registration. Raster data via PDOK services.
- Use: Primary heat exposure layer for the vulnerability overlay.

**Amsterdam Hitte Kaart (Amsterdam Heat Map)**
- URL: https://maps.amsterdam.nl/ (search "hitte" or "warmte")
- Format: WMS/WFS, some layers downloadable as GeoJSON/Shapefile
- Resolution: 5–10 m raster for thermal maps
- Variables: Surface temperature (Landsat-derived), shade coverage, green infrastructure, cool spots
- Access: Free via Amsterdam Maps portal.
- Use: Amsterdam-specific high-resolution heat exposure. Can be directly overlaid with tree data.

**Satellite Land Surface Temperature**
- Sources: Landsat 8/9 (30 m optical / 100 m thermal), ECOSTRESS (70 m), Sentinel-3
- Format: GeoTIFF
- Access: Free via USGS EarthExplorer, Copernicus. Some pre-processed Dutch datasets via NHI.
- Use: Create custom LST maps for specific dates if the Klimaateffectatlas resolution is insufficient.

---

### A.2 Neighborhood Boundaries & Demographics

**CBS Wijken en Buurten (Neighborhoods and Districts)**
- URL: https://www.cbs.nl/nl-nl/dossier/nederland-regionaal/geografische-data/wijk-en-buurtkaart-2023
- Format: Shapefile, GeoPackage, GeoJSON — pre-joined with demographic attributes
- Levels: Gemeente (municipality) → Wijk (district, ~22 in Amsterdam) → Buurt (neighborhood, ~481 in Amsterdam)
- **Key variables included in the geographic file:**
  - Population, density, age groups (0–14, 15–24, 25–44, 45–64, 65+)
  - Household composition (single, couple, family)
  - Housing stock (total dwellings, ownership vs. rental, construction year)
  - Average WOZ value (property tax valuation)
  - Income (average per recipient)
  - Surface area (land, water)
- Access: Free direct download. Updated annually (2023 most recent).
- **Use: This is the foundational layer. Join all other datasets to these geometries. The pre-joined demographics are immediately usable for vulnerability index construction.**

**PDOK Administrative Boundaries**
- URL: https://www.pdok.nl/ → bestuurlijke grenzen
- Format: WFS, GML, GeoJSON
- WFS endpoint: `https://service.pdok.nl/cbs/wijkenbuurten/2023/wfs/v1_0`
- Use: Alternative source via API. Pure geometry (no attributes) — use CBS version instead for pre-joined data.

**CBS Kerncijfers Wijken en Buurten (Key Figures by Neighborhood)**
- URL: https://www.cbs.nl/nl-nl/reeksen/kerncijfers-wijken-en-buurten / StatLine API: https://opendata.cbs.nl/
- Format: CSV, OData API
- Resolution: Buurt level (finest public administrative level)
- **~100+ indicators including:**
  - Demographics: total population, age groups, % elderly (65+), % non-Western migration background, household size
  - Income: average personal income, % low-income households, % below social minimum
  - Housing: WOZ value, % owner-occupied, % social housing, construction period
  - Liveability: Leefbaarometer composite score
- Access: Free. CSV tables and API.
- **Use: Core vulnerability data. % elderly, % low income, housing density, % social housing are standard heat vulnerability index inputs.**

---

### A.3 Land Use Data

**BBG (Bestand Bodemgebruik / Land Use Database)**
- URL: https://www.cbs.nl/nl-nl/dossier/nederland-regionaal/geografische-data/bestand-bodemgebruik
- Format: Shapefile, GeoPackage
- Resolution: 1:10,000; minimum mapping unit ~0.1 ha
- Categories: ~37 classes including residential, commercial, industrial, recreational, forest, water, transport
- Access: Free. Most recent: BBG 2017.
- Use: Land use composition per neighborhood. Calculate imperviousness. Stratify tree analysis by land use type.

**BGT (Basisregistratie Grootschalige Topografie)**
- URL: https://www.pdok.nl/ → BGT
- Format: GML, GeoPackage, WFS
- Resolution: Object-level (~20 cm accuracy)
- Key layers: `BegroeidTerreindeel` (vegetated), `Wegdeel` (roads + surface material), `Pand` (building footprints), **`Boom` (individual trees with crown projections)**
- Access: Free. Bulk download via PDOK ATOM feed.
- **Use: The `Boom` layer provides an independent tree point dataset for cross-validation. Surface material types from `Wegdeel` can estimate imperviousness and heat retention.**

---

### A.4 Socioeconomic & Vulnerability Data

**Leefbaarometer (Liveability Monitor)**
- URL: https://www.leefbaarometer.nl/
- Format: Interactive map, CSV, API
- Resolution: 100 m grid and buurt level
- Variables: Composite liveability score (1–10), sub-dimensions (housing quality, public space, amenities, safety, population composition)
- Access: Free.
- Use: "Public space" and "physical environment" sub-scores as green space quality proxies.

**GGD Amsterdam / RIVM Gezondheidsmonitor**
- URL: https://www.volksgezondheidenzorg.info/
- Format: Tables, CSV
- Resolution: GGD-regio level (coarser than buurt); some at gemeente level
- Variables: Self-reported health, chronic disease, overweight, heat-related complaints, social isolation
- Access: Free (aggregated). Microdata requires CBS Remote Access.
- Use: Health indicators for vulnerability. Note: spatial resolution is coarser — may need municipality-level data.

---

### A.5 Tree and Green Infrastructure Data

**Amsterdam Bomenkaart (Amsterdam Tree Map)**
- URL: https://data.amsterdam.nl/ (search "bomen")
- API endpoint: `https://api.data.amsterdam.nl/v1/bomen/stamgegevens/`
- Format: GeoJSON, CSV, WFS, REST API
- Resolution: Individual tree points
- Variables: Location, species (Dutch + Latin), planting year, crown diameter, trunk circumference, health status, management category, **owner (municipality, private, housing corporation)**
- Access: Free. Bulk GeoJSON downloadable.
- **Use: This is Amsterdam's official tree register — the 3,929 trees in your study. The owner field and management category can help characterize what types of trees are "missing." One of the most complete municipal tree inventories in Europe.**

**Atlas Natuurlijk Kapitaal**
- URL: https://www.atlasnatuurlijkkapitaal.nl/
- Format: WMS, downloadable rasters/vectors
- Resolution: 25–100 m
- Variables: Urban green space classification, ecosystem service maps (cooling, air quality, carbon sequestration), heat mitigation potential
- Access: Free.
- Use: Pre-computed cooling/ecosystem service layers — saves modeling effort. Direct comparison with your per-tree approach.

---

### A.6 Coordinate System Note

All Dutch government data uses **Rijksdriehoekstelsel (RD New / EPSG:28992)**. Ensure your analysis pipeline handles this CRS. PDOK services also support WGS84 (EPSG:4326).

**Key Dutch search terms:** Boom/bomen = tree/trees, Buurt = neighborhood, Wijk = district, Hitte = heat, Groen = green, Bodemgebruik = land use, Inkomen = income, Bevolking = population, Gezondheid = health.

---

### A.7 Recommended Core Dataset Stack

| Layer | Source | Format | Resolution | Priority |
|-------|--------|--------|------------|----------|
| Heat stress | Klimaateffectatlas / Amsterdam hitte kaart | GeoTIFF/WMS | 5–100 m | High |
| Neighborhoods + demographics | CBS Wijk-en-Buurtkaart 2023 | Shapefile/GPKG | Buurt (~481 in AMS) | High |
| Socioeconomic detail | CBS Kerncijfers | CSV / OData API | Buurt | High |
| Official tree register | Amsterdam Bomenkaart | GeoJSON/API | Individual tree | High |
| Land use | BBG + BGT | Shapefile/GML | Object to 0.1 ha | Medium-High |
| Liveability | Leefbaarometer | CSV/grid | 100 m / buurt | Medium |
| Health | GGD/RIVM | CSV/tables | Gemeente/GGD-regio | Medium |
| Ecosystem services | Atlas Natuurlijk Kapitaal | WMS/raster | 25–100 m | Supplementary |

---

## Part B: "Planners' View vs. Reality" Analysis Design

### B.1 Figures to Produce

#### Figure A (Main Text, HERO FIGURE): Three-Panel "Visibility Gap" Map

Three-panel horizontal layout (a-b-c), single row. Full page width (170 mm for Nature/Springer two-column).

**Panel (a) — "Planner's View"**
- Only the 3,929 registered municipal trees as point markers on a light grey basemap
- Single color (dark teal, `#2c7fb8`) — no LAI encoding. The point is to show sparsity.
- Title: "Municipal register (N = 3,929)"

**Panel (b) — "Full Canopy"**
- All 12,350 detected trees as point markers
- Color-coded by LAI using sequential green colormap (`YlGn` or custom `#f7fcb1` → `#004529`)
- Same spatial extent, same basemap as panel (a)
- Title: "Detected trees (N = 12,350)"

**Panel (c) — "The Invisible Forest"**
- Only the 8,421 unregistered trees (detected minus registered)
- Color-coded by LAI using same green colormap as panel (b)
- Title: "Unregistered trees (N = 8,421)"

Shared colorbar for LAI (0–8.5 m²/m²) below panels (b) and (c). North arrow and scale bar on panel (a) only. Basemap: very light grey building footprints — must not compete with tree points.

**Why this works:** The visual emptiness of panel (a) versus the density of panel (b) creates an immediate, visceral contrast. Panel (c) isolates exactly what planners are missing. This is the figure editors remember.

---

#### Figure B (Main Text): Hexbin Detection Ratio Map

Single panel. Hexagonal grid (edge ~150 m, ~5.85 ha hexbins — consistent with existing `lai_spatial_gradient_hexbin.png`).

For each hexbin compute: `detection_ratio = N_total / N_registered`. Where `N_registered = 0`, assign special category ("no registered trees").

Color hexbins by ratio using sequential warm ramp (`YlOrRd`) with log scaling. Most values will be 1.5–10+.

Annotate 2–3 hexbins with actual counts (e.g., "Registered: 12 / Detected: 87, ratio 7.25×"). Include histogram inset showing ratio distribution across all hexbins.

**What it shows:** Spatial variation in the information gap. Some areas: planners see half. Others: planners see one in ten.

---

#### Figure C (Main Text): LAI Distribution Comparison

Overlaid kernel density plot:
- Registered trees (N=3,929) in teal/blue
- Unregistered trees (N=8,421) in orange/coral
- All trees (N=12,350) as dashed black line
- Vertical lines at means. KS test p-value on figure.
- Background bands showing shade categories (see B.3)

Single column (85 mm). Y-axis: density (normalized). X-axis: LAI 0–9 m²/m².

---

#### Figure D (Supplementary): Cumulative Shade Capacity Gap

Stacked bar or waterfall diagram: total cumulative LAI for (i) registered only, (ii) unregistered only, (iii) all. Express as: "The municipal register captures X% of total shade-producing canopy." Optionally break down by shade category.

---

#### Figure E (Supplementary): Unregistered Tree Clustering

Getis-Ord Gi* hotspot map of unregistered tree density. Overlay neighborhood or land-use boundaries.

---

#### Display Item Budget

Nature Cities allows ~8 display items. The three-panel map (A) is highest priority. Hexbin ratio map (B) and LAI comparison (C) are strong main-text candidates. Current paper has ~6 main figures — consolidate or move existing ecological scatter plots to supplementary to make room.

---

### B.2 Statistical Analyses

#### Population Comparison: Registered vs. Unregistered Trees

| Test | Purpose | Report |
|------|---------|--------|
| Two-sample Kolmogorov-Smirnov | LAI distribution difference | D-statistic, p-value |
| Welch's t-test | Mean LAI difference | Means, difference, 95% CI, t, p |
| Mann-Whitney U | Median LAI difference (non-parametric) | U, p |
| Cohen's d | Effect size | d = (mean1 − mean2) / pooled SD |

Repeat for **height** and **NDVI** to characterize whether unregistered trees differ morphologically.

#### Summary Statistics Table (Main Text)

| Metric | Registered (N=3,929) | Unregistered (N=8,421) | All (N=12,350) | p-value |
|--------|---------------------|----------------------|----------------|---------|
| LAI mean (SD) | ? | ? | 3.21 (1.33) | ? |
| LAI median [IQR] | ? | ? | ? | ? |
| Height mean (SD) | ? | ? | 12.4 (5.8) | ? |
| NDVI mean (SD) | ? | ? | 0.68 (0.12) | ? |
| Crown diameter mean (SD) | ? | ? | ? | ? |
| Trees with LAI > 4 (%) | ? | ? | ? | ? |
| Trees with LAI > 6 (%) | ? | ? | ? | ? |

#### Information Gap Index (IGI)

At hexbin level:
```
IGI_h = 1 - (N_registered_h / N_total_h)
```
IGI = 0 → register is complete. IGI = 1 → no registered trees.

Report:
- Mean IGI across all hexbins (with 95% CI)
- % hexbins with IGI > 0.5 (planners see less than half)
- % hexbins with IGI > 0.75 (planners see less than one-quarter)

Also compute **LAI-weighted IGI**:
```
IGI_LAI = 1 - (Σ LAI_registered / Σ LAI_total)
```
This captures whether missing trees are disproportionately high-LAI or low-LAI.

#### Spatial Clustering

| Test | Purpose | Report |
|------|---------|--------|
| Global Moran's I | Are unregistered trees spatially clustered? | I, z-score, p |
| Getis-Ord Gi* (local) | Where are hotspots of unregistered trees? | Significant hotspots (p < 0.05, Bonferroni) |
| Ripley's K (optional, supplementary) | Clustering at multiple scales | K(r) vs. CSR envelope |

---

### B.3 Shade Capacity Gap Quantification

#### LAI-to-Shade via Beer-Lambert

```
τ = exp(-k × LAI)        # transmittance (fraction of radiation passing through)
SF = 1 - exp(-k × LAI)   # shade fraction (fraction blocked)
```

**Extinction coefficient k:**
- **k = 0.5**: Standard for broadleaf deciduous urban trees. Shashua-Bar & Hoffman (2000, *Energy and Buildings* 31:221–235); Konarska et al. (2014, *Urban Forestry & Urban Greening* 13:533–542). Most defensible default for Amsterdam's mixed canopy.
- **k = 0.47**: Reported specifically for Ulmus (dominant genus) by Breuer et al. (2003, *Ecological Modelling* 169:313–332).
- **Sensitivity range: k = 0.3 to 0.7.**

For LAI = 3.21 (study mean) and k = 0.5: SF = 1 − exp(−1.605) = **0.80 (80% solar radiation blocked)**.

#### Shade Categories

| Category | LAI range | Shade fraction (k=0.5) | Interpretation |
|----------|-----------|----------------------|----------------|
| Low shade | LAI < 2.0 | SF < 0.63 | Young/small trees, poor canopy health |
| Moderate shade | 2.0 ≤ LAI < 4.0 | 0.63 ≤ SF < 0.86 | Typical urban trees, adequate shade |
| High shade | LAI ≥ 4.0 | SF ≥ 0.86 | Mature, dense canopy; maximum cooling |

Thresholds consistent with Shashua-Bar et al. (2010, *IJOC* 31:1498–1511): LAI > 3 → functionally effective shade. Rahman et al. (2020): LAI > 4 → significant surface temperature reduction (8–12°C vs. 3–5°C).

#### Aggregate Metrics

**Shade capacity ratio:**
```
R_shade = Σ SF_registered / Σ SF_all
```
→ "The municipal register captures only **X%** of total shade capacity."

**Shade capacity multiplier:**
```
M_shade = Σ SF_all / Σ SF_registered
```
→ "Actual shade capacity is **X×** what municipal records suggest."

**High-shade gap:** Count of trees with LAI ≥ 4 that are unregistered / total high-LAI trees.
→ "**Y%** of the district's most effective shade providers are absent from the register."

#### Cooling Translation

Use established empirical relationships (already cited in the paper):
- Canopy shade reduces mean radiant temperature by 5–20°C: Du et al. (2020), Middel et al. (2016)
- Ambient air temperature reduction of 0.5–2.0°C per unit increase in canopy cover: Rahman et al. (2020), Li et al. (2024)
- LAI 2→5 reduces pedestrian air temp by ~1.5–3.0°C in street canyons: Shashua-Bar et al. (2010)

Express gap as: "Unregistered trees contribute an estimated additional **X°C** cooling potential absent from municipal shade inventories." Use carefully — these are geometry-dependent.

---

### B.4 Headline Numbers (Abstract-Worthy)

Ranked by narrative impact:

1. **Detection multiplier:** "3.1× more trees detected than registered (12,350 vs. 3,929)" — already strong, keep.
2. **Shade gap %:** "The municipal register captures only [X]% of total shade capacity" — compute via R_shade. If below 40%, this is extraordinary.
3. **Invisible high-shade count:** "[Y] trees with LAI ≥ 4 are absent from municipal records, representing [Z]% of the area's most effective shade providers."
4. **Information gap index:** "In [P]% of analysis units, planners see less than half the existing tree canopy."

---

### B.5 Narrative Framing

**Language to use:**
- "shade capacity" not "LAI aggregate"
- "cooling infrastructure" not "ecosystem services"
- "detection gap" or "information gap" not "data incompleteness"
- "three times more trees than previously mapped" not "a 3.14× detection ratio"
- "heat-vulnerable neighborhoods" not "areas with high UHI intensity"

**Language to avoid:**
- Don't call the municipal register "ground truth" — it's a partial inventory, not truth
- Don't overclaim cooling benefits — LAI-to-temperature is geometry-dependent. Use "estimated cooling potential" or "shade provision capacity"
- Don't frame municipal databases as failures. Frame as designed for a different purpose (managing public assets) that naturally excludes private-property trees. Automated methods *complement*, not replace, traditional inventories.
- Don't say "revolutionary" or "unprecedented" — the 3× multiplier speaks for itself

**Narrative arc for the Results subsection:**

1. **The count gap.** 12,350 vs. 3,929. The 3.1× multiplier. One sentence referencing Nowak et al. for context (US estimates: municipal inventories capture 15–35% of trees nationally — your 31.8% is independent European confirmation).
2. **Spatial pattern.** Where is the gap worst? Hexbin analysis. Moran's I. Are gaps worse in residential areas (private gardens) vs. commercial/industrial?
3. **LAI differences.** Distribution comparison. KS test. Mean difference. Are unregistered trees systematically lower-LAI (small garden trees) or comparable/higher (large unmanaged mature trees)?
4. **Shade capacity gap.** Shade capacity ratio and multiplier. High-shade unregistered trees. Cooling translation. This paragraph connects data to planning action.

**Key rhetorical move:** Frame every finding as an answer to a planner's question:
- "Where should we plant?" → "First, know where trees already exist. Planners are working from maps showing one-third of actual trees."
- "How much shade do we have?" → "Municipal records underestimate total shade capacity by [X]%."
- "Which neighborhoods need trees?" → "Some areas classified as tree-deficient based on the register may already have substantial unregistered canopy." (This counterintuitive inversion is the kind of finding Nature Cities editors look for.)

---

### B.6 Implementation Checklist

1. **Spatial join:** Match registered trees (municipal database) to detected trees. Proximity threshold: within crown radius or fixed buffer (~3 m). Unmatched detected trees = "unregistered."
2. **Flag each of 12,350 trees** as registered/unregistered.
3. **Hexbin aggregation:** Create hex grid, count per hexbin, compute IGI.
4. **LAI distribution extraction:** Split by registered/unregistered.
5. **Statistical tests:** KS, Welch's t, Mann-Whitney U, Cohen's d, Moran's I, Gi*.
6. **Shade capacity computation:** Beer-Lambert with k=0.5, sensitivity at k=0.3 and 0.7.
7. **Produce figures** A–E.

All achievable with existing data. Estimated effort: **3–5 days.**

---

## Part C: Heat Vulnerability × Shade Deficiency Overlay

### C.1 Conceptual Framework

#### Defining "Shade Deficiency"

Three metrics; compute all three, report sensitivity:

**Option A (primary) — Mean LAI-weighted canopy per area:**
```
shade_intensity = Σ(LAI_i × crown_area_i) / total_area_of_spatial_unit
```
Most directly interpretable as "shade density."

**Option B — Fraction of high-LAI trees:**
Count of trees with LAI > 3.0 / total trees (or / area). Captures whether an area has functionally effective shade. More actionable for policy.

**Option C — Total shade fraction per area:**
Sum of Beer-Lambert SF values / area. Most physically meaningful.

Define "shade deficiency" = inverse or bottom quartile of the shade metric distribution.

**Critical step:** Converting point-level tree detections to areal metrics requires either (a) crown delineations from the detection pipeline, or (b) a kernel density approach (LAI-weighted KDE over the study area, aggregated to spatial units).

#### Defining "Heat Vulnerability"

Standard three-dimension framework (Cutter et al. 2003; Reid et al. 2009):

**Exposure (physical heat load):**
- Land surface temperature from Landsat / Klimaateffectatlas
- Impervious surface fraction (from BGT/BBG)
- **DO NOT include canopy cover here — creates circularity with shade metric**

**Sensitivity (population characteristics):**
- % population >65 years old (CBS)
- % population <5 years old (CBS)
- % single-person households (CBS) — strong predictor of heat mortality (social isolation)
- Chronic disease prevalence (GGD, if available at buurt level)

**Adaptive capacity (ability to cope):**
- Median income / % low-income households (CBS)
- WOZ property values (CBS)
- Housing construction era (pre-war = poorly insulated) (CBS)
- AC prevalence (rare in NL — this strengthens the story: shade is the primary cooling mechanism)

**Recommendation:** Keep dimensions separate in the main analysis. Compute composite only for the bivariate map. Reviewers want to see which dimension drives the correlation. A composite index invites arbitrary weighting critiques.

---

### C.2 Spatial Unit Selection

| Unit | Count in 25 km² | Avg area | Pros | Cons |
|------|-----------------|----------|------|------|
| Buurt | ~30–60 | 0.4–0.8 km² | Data-rich, policy-relevant | Low N, MAUP concerns |
| Wijk | ~10–15 | 1.5–2.5 km² | — | Too few for statistics |
| CBS 500 m grid | ~100 | 0.25 km² | Consistent geometry, better N | Less socioeconomic data |
| H3 hexbins (res 8) | ~500–600 | ~0.04 km² | Consistent area, high N | No direct socioeconomic alignment |

**Recommendation:** Use **buurt as primary unit** (policy-relevant, data-rich) with **CBS 500 m grid as sensitivity check**. Report both to address MAUP.

**Critical constraint:** Your 25 km² tile ≠ all of Amsterdam (~219 km²). You must:
- Identify which buurten are fully vs. partially covered
- Exclude buurten with <80% coverage (edge effects)
- Or normalize by covered area only
- Report which approach was used

**Statistical power at buurt level:** With N~40, you can detect Spearman ρ ≥ 0.31 at p < 0.05 (two-tailed). If N < 30, the 500 m grid must become primary (N~100).

---

### C.3 Step-by-Step Methodology

```
STEP 1: Shade Metric Construction
├── 1a. Define spatial units (buurten within tile, coverage ≥ 80%)
├── 1b. Assign each tree (N=12,350) to its spatial unit
├── 1c. Compute per-unit shade metrics (Options A, B, C)
├── 1d. Compute "shade deficiency" = inverted + standardized shade metric
└── 1e. Validate: do shade metrics correlate with Amsterdam's own canopy data?

STEP 2: Vulnerability Metric Construction
├── 2a. Obtain CBS data at buurt level (Kerncijfers + Buurtkaart)
├── 2b. Select indicators:
│   ├── Exposure: LST (Klimaateffectatlas), impervious fraction (BGT/BBG)
│   ├── Sensitivity: % elderly, % young children, % single-person HH
│   └── Adaptive capacity: median income, WOZ, housing age
├── 2c. Standardize each indicator (z-scores within study area)
└── 2d. Validate: compare with existing Amsterdam heat assessments (GGD)

STEP 3: Spatial Overlay
├── 3a. Join shade deficiency and vulnerability by spatial unit
├── 3b. Compute bivariate classification (3×3 quantile matrix)
├── 3c. Map results (bivariate choropleth)
└── 3d. Identify "priority zones" (high vulnerability + high shade deficiency)

STEP 4: Statistical Analysis
├── 4a. Spearman correlations (shade deficiency × each vulnerability indicator)
├── 4b. Bootstrapped 95% CIs for correlations (given small N)
├── 4c. OLS regression → test residuals for spatial autocorrelation (Moran's I)
├── 4d. If significant autocorrelation: spatial lag or spatial error model (PySAL)
├── 4e. 3×3 quantile matrix → chi-squared test for independence
└── 4f. Report population in each cell of the matrix

STEP 5: Sensitivity Analysis
├── Spatial unit: buurt, 500 m grid, 250 m grid
├── Shade metric: Options A, B, C
├── LAI threshold for "high": 2.5, 3.0, 3.5
├── Vulnerability dimensions: all, exposure only, sensitivity only, adaptive only
├── Correlation method: Spearman, Pearson, spatial lag
└── Coverage threshold: 60%, 80%, 100%
Report: "X of Y configurations showed significant positive correlation at p < 0.05"

STEP 6: Interpretation
├── 6a. Quantify population in "priority zones"
├── 6b. Compare with Amsterdam's stated urban greening priorities
└── 6c. Estimate shade deficit (additional high-LAI trees needed for equity)
```

---

### C.4 Scenario Analysis

#### Scenario A: Shade Deficiency Correlates with Vulnerability (equity story)

**Framing:**
- "Per-tree LAI mapping reveals that urban shade provision is inequitably distributed, with heat-vulnerable neighborhoods receiving systematically lower canopy density."
- "Approximately N residents (X% of study area population) live in zones of co-occurring high vulnerability and high shade deficiency."
- "Current tree planting patterns do not compensate for — and may reinforce — existing inequities in heat exposure."

**Nature Cities appeal: VERY HIGH.** Environmental justice result with individual-tree resolution. Frame as: "remote sensing at individual-tree resolution enables equity audits of urban cooling infrastructure that were previously impossible."

#### Scenario B: No Correlation or Inverse Correlation

**This is plausible for Amsterdam.** Dutch cities have strong spatial planning. Amsterdam's Vondelpark, canal-zone trees → wealthy neighborhoods. Bijlmer social housing → designed with significant green space.

**Framing:**
- "Contrary to findings in North American cities, Amsterdam's canopy does not show the expected equity deficit. This may reflect Dutch spatial planning traditions and public housing green space requirements."
- "However, this area-level finding does not account for microscale shade access or pedestrian exposure pathways."

**Paper is still viable** but narrative shifts from "equity deficit" to "comparative urban planning lesson." Less impactful at Nature Cities.

#### Scenario C: Mixed Results (MOST LIKELY)

Correlation with some dimensions but not others. E.g.: correlates with income but not age, or with LST but not health indicators.

**Framing:**
- "The relationship between shade deficiency and heat vulnerability is dimension-dependent. Significant associations with [income/housing] but not [age/health] suggest that canopy distribution reflects [property value gradients] rather than a generalized equity deficit."
- "This dimension-specific pattern implies that shade enhancement should target areas with [specific co-occurring conditions] rather than relying on composite vulnerability indices."

**This is actually the strongest scientific contribution** — adds nuance to the binary "trees correlate with wealth" narrative. Nature Cities values this.

---

### C.5 Figures

#### Main Text: Bivariate Choropleth (HERO FIGURE)

3×3 bivariate color scheme (Stevens's bivariate palette: purple-orange-blue).
- X-axis: shade deficiency (low-mid-high)
- Y-axis: vulnerability (low-mid-high)
- 25 km² tile with buurt boundaries
- Highlight "priority zones" (high-high quadrant) with hatching
- Inset: tile location within Amsterdam

**This is the single most important figure.** Must be beautiful and immediately legible.

#### Main Text: Correlation Scatter Matrix

Shade deficiency (x) vs. each vulnerability indicator (y). One panel per indicator (small multiples). Regression line with confidence band. Spearman ρ and p-value per panel. Points = spatial units, sized by population.

#### Main Text: Priority Zone Population

Bar chart or treemap: population distribution across the 3×3 categories.

#### Supplementary Figures

- Shade metric distributions (all three variants)
- Vulnerability indicator maps (one per indicator)
- Sensitivity analysis heatmap (correlations across all parameter combinations)
- MAUP check (repeat bivariate map at 500 m grid)
- Moran's I diagnostics
- LAI box plots by buurt, ordered by vulnerability

---

### C.6 Defensibility

#### Anticipated Reviewer Critiques

**"Only 25 km² — how generalizable?"**
→ "Our tile covers ~11% of Amsterdam's municipal area. Buurten in the study area span [range] of Amsterdam's income distribution, covering [X]% of socioeconomic variance. Full-city analysis, which our methodology enables, would provide definitive evidence."

**"LAI ≠ shade provision."**
→ "LAI is an established proxy for canopy light interception. However, functional shade depends additionally on crown geometry, height, solar angle, and surrounding buildings. Our metric captures canopy density rather than realized pedestrian shade." State in Discussion.

**"Ecological fallacy."**
→ "We analyze spatial associations at the neighborhood level — the appropriate scale for urban planning. We do not claim individual-level shade exposure. Individual assessment would require pedestrian-level shadow modeling, which is beyond scope but enabled by our per-tree data."

**"Why not use canopy cover instead of LAI?"**
→ "Binary canopy cover does not capture functional shade quality. A sparse tree with LAI 1.5 and a dense tree with LAI 5.0 provide vastly different shade. Per-tree LAI captures this functional gradient."

**"Vulnerability indicators are standard census data — what's new?"**
→ Novelty is on the shade side (per-tree LAI at individual-tree resolution). Previous studies used NDVI or % canopy cover. We provide individual-tree functional characterization.

**"Temporality — summer data?"**
→ State acquisition date (July 2023 — peak foliage). Strong for shade analysis. LAI values represent maximum leaf-on conditions.

#### Scoping Claims

Every sentence must use association language:
- **YES:** "is associated with," "correlates with," "co-occurs with"
- **NO:** "causes," "leads to," "exposes residents to"
- **CAREFUL:** "demonstrates inequity" (implies normative judgment → prefer "reveals unequal distribution")

---

### C.7 Key Literature

**Urban heat equity / environmental justice:**
- Hoffman, Shandas & Pendleton (2020). "Effects of Historical Housing Policies on Resident Exposure to Intra-Urban Heat." *Climate* 8(1):12. [Foundational: redlining → heat; establishes US pattern]
- Hsu, Sheriff, Chakraborty & Manya (2021). "Disproportionate exposure to urban heat island intensity." *Nature Communications* 12:2721. [Large-scale US evidence; your paper = European counterpart]
- Chakraborty et al. (2019). "Disproportionately higher exposure to urban heat in lower-income neighborhoods." *ERL* 14:105003.

**Shade/canopy and socioeconomic indicators:**
- Schwarz et al. (2015). "Trees Grow on Money: Urban Tree Canopy Cover and Environmental Justice." *PLoS ONE* 10(4):e0122051. [Definitive US canopy-income study]
- Venter, Krog & Barton (2020). "Linking green infrastructure to urban heat and human health risk mitigation in Oslo." *STOTEN* 709:136193. [European context, directly relevant]
- Riley & Gardiner (2020). "Distributional equity of urban tree canopy cover." *PLoS ONE* 15(7):e0228499.

**Methodology:**
- Anselin (1995). "Local Indicators of Spatial Association — LISA." *Geographical Analysis* 27(2):93–115. [Spatial autocorrelation]
- Fotheringham & Wong (1991). "The modifiable areal unit problem." *E&PA* 23(7):1025–1044. [MAUP]
- Clifford, Richardson & Hemon (1989). "Correlation between two spatial processes." *Biometrics* 45(1):123–134. [Modified significance tests]

**Dutch urban context:**
- Kleerekoper, van Esch & Salcedo (2012). "How to make a city climate-proof." *Resources, Conservation and Recycling* 64:30–38.
- Cite Amsterdam's most recent municipal heat action plan for policy relevance.

---

## Part D: Summary — What to Do and in What Order

### Phase 1: Planners' View vs. Reality (P0, ~3–5 days, existing data)

| Step | Output | Days |
|------|--------|------|
| Spatial join: flag 12,350 trees as registered/unregistered | Binary classification | 0.5 |
| LAI/height/NDVI distribution comparison + statistical tests | Table + Figure C | 1 |
| Hexbin aggregation + IGI computation | Figure B + metrics | 1 |
| Three-panel "Visibility Gap" map | Figure A (hero) | 1 |
| Shade capacity gap (Beer-Lambert) | Headline numbers | 0.5 |
| Spatial clustering (Moran's I, Gi*) | Figure E (supplementary) | 0.5 |

### Phase 2: Heat Vulnerability Overlay (P1, ~5–7 days, requires external data)

| Step | Output | Days |
|------|--------|------|
| Download CBS buurt data + Klimaateffectatlas rasters | Data stack | 1 |
| Compute shade deficiency per buurt | Shade metrics | 1 |
| Compute vulnerability indicators per buurt | Vulnerability metrics | 1 |
| Bivariate overlay + statistical analysis | Correlations, chi-squared | 1 |
| Bivariate choropleth map | Hero figure | 1 |
| Sensitivity analysis (spatial units, metrics, thresholds) | Robustness table | 1–2 |

### Total effort: ~8–12 days of analysis

**Minimum viable submission (P0 only):** 3–5 days → "Planners' view" paper with strong detection gap + shade capacity gap quantification. Publishable at Nature Cities but not compelling.

**Competitive submission (P0 + P1):** 8–12 days → Detection gap + shade capacity + vulnerability overlay. Strong Nature Cities candidate.

### The core pitch to Nature Cities

"Individual-tree LAI mapping from remote sensing enables a new class of equity analysis — not just 'is there canopy?' but 'is the canopy *functionally providing shade* where it is most needed?' That resolution advantage is what separates this from the existing literature."
