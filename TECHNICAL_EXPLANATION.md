# Technical Explanation Document

## Tier 1: Intuitive Explanation

### What problem does this solve, and why should I care?

Cities need trees to stay cool—but they do not actually know how much shade their trees provide, or even where most of their trees are. Municipal tree databases typically record only public trees along streets and in parks, missing roughly two-thirds of all urban trees that grow on private land, in backyards, and along waterways. It is as if a city tried to plan its road network while only knowing about highways and ignoring every neighborhood street.

Shade is not just about having a tree—it depends on how thick and leafy the canopy is. A mature elm with dense foliage cools the ground beneath it far more than a young, sparse sapling of the same height. Scientists measure this canopy thickness using Leaf Area Index (LAI): essentially, how many layers of leaves you would stack up if you flattened them over the ground beneath the tree. A high-LAI tree is like a thick umbrella; a low-LAI tree is like a parasol with holes.

Our work solves both problems at once. Using aerial photographs and laser scanning data that many cities already collect, we built an automated system that (1) finds every tree—public and private—across an entire city district, and (2) measures each tree's canopy density individually. Applied to Amsterdam, we found three times more trees than the city's official records and estimated each tree's shade capacity with roughly 78% accuracy—far better than traditional rules of thumb based on tree height alone. The result is a detailed "shade map" that planners can use to decide exactly where new trees would do the most good for cooling heat-stressed neighborhoods.

---

## Tier 2: Technical Overview

### How does it work at a high level?

The framework operates as a four-stage pipeline processing two primary data sources: airborne LiDAR point clouds (25 pts/m²) providing three-dimensional canopy structure, and high-resolution aerial imagery (0.25 m RGB + near-infrared) capturing spectral reflectance.

**Stage 1 — Tree detection and crown delineation.** Individual tree crowns are detected from RGB imagery using DeepForest, a pre-trained deep learning model based on a RetinaNet object-detection architecture. Before detection, an NDVI-based contrast enhancement step suppresses non-vegetated pixels (buildings, roads) to reduce false positives. The model outputs bounding-box polygons for each detected tree, which are then matched against municipal records to assign genus labels where available.

**Stage 2 — LiDAR-based LAI estimation (ground truth).** For each detected crown, the corresponding LiDAR points are extracted and converted into a voxel grid (0.5 m³ resolution). Leaf Area Density (LAD) is computed per voxel layer using the MacArthur–Horn method, which estimates foliage density from the probability that a laser pulse is intercepted at each canopy height. LAI is obtained by vertically integrating the LAD profile—summing leaf density from ground to canopy top. This physically grounded estimate serves as the training target for the prediction model.

**Stage 3 — Feature engineering and ML prediction.** Fifty-eight features are constructed across six categories: base morphology (height, crown diameter), spectral indices (NDVI statistics), allometric transformations (log-height, power-law terms), spectral–structural interactions (NDVI × height), height-class indicators, and species/geospatial context. Eight regression models are trained and compared; XGBoost achieves the best performance (R² = 0.784, RMSE = 0.620 m²/m²), improving 39% over an allometric baseline that uses only height and crown diameter.

**Stage 4 — City-wide deployment.** The trained model predicts per-tree LAI across the full study area, including trees lacking LiDAR coverage. Outputs are exported as GeoJSON (tree polygons with attributes) and GeoTIFF (0.5 m² LAI raster), directly compatible with municipal GIS platforms.

The key design principle is *adaptivity*: the voxelization stage adjusts to variable LiDAR densities (5–20 pts/m²), and the ML model can operate with degraded inputs—feature ablation shows base morphological and spectral features alone capture 98.9% of full-model performance.

---

## Tier 3: Technical Depth

### What are the technical details and trade-offs?

**Voxelization and LAI derivation.** The LAI calculation follows the MacArthur–Horn formulation as implemented in the LeafR package. Each tree's point cloud is discretized into a 3D voxel grid at 0.5 m³ resolution. For each horizontal voxel column, the Leaf Area Density at height layer *k* is:

$$\text{LAD}(k) = \ln\!\left(\frac{S(k)}{S(k+1)}\right) \cdot \frac{1}{\Delta z}$$

where *S(k)* is the number of LiDAR pulses entering layer *k* and *S(k+1)* is the number exiting (penetrating to the next layer), following Beer–Lambert light extinction. LAI is the vertical integral: $\text{LAI} = \sum_k \text{LAD}(k) \cdot \Delta z$. The 0.5 m³ voxel size balances spatial resolution against point-density sensitivity; coarser voxels tolerate sparser LiDAR but lose within-crown structural detail.

**Model architecture and regularization.** XGBoost was configured via Bayesian hyperparameter optimization (Optuna, 100 trials) over learning rate, max depth, subsample ratio, and L1/L2 regularization strength. The model's sequential boosting corrects residuals from prior trees, which proves effective for the heteroskedastic error structure observed at high LAI values (>6.0 m²/m²), where canopy self-occlusion introduces measurement noise. Random Forest achieved identical R² (0.784) but with 2.3× longer training time; the near-convergence of bagging and boosting suggests the underlying signal is well-captured by ensemble methods generally, with diminishing returns from architectural complexity.

**Validation strategy and known limitations.** Model evaluation uses a stratified train/validation/test split (70/15/15%, N = 7,085 trees), stratified on LAI quintiles cross-cut with height tertiles to ensure balanced representation. Residual diagnostics show near-zero bias (mean residual = 0.003), approximately normal error distribution (skewness = 0.14, kurtosis = 3.21), and no significant spatial autocorrelation (Moran's I = 0.023, p = 0.18). Physical validation against hemispherical photography (N = 5 Ulmus trees) yields RMSE = 0.86 m²/m² (~27% relative error), comparable to inter-method uncertainty in ground-truth LAI measurement (typically 15–30%).

**Key trade-offs and limitations.** (1) The hemispherical validation sample (N = 5, single genus) is too small to establish cross-species accuracy bounds; expanded field validation is a priority for future work. (2) LiDAR occlusion in deep canopies degrades LAD estimates for tall trees (>25 m: MAE = 0.58 vs. 0.41 for 8–15 m trees), an inherent limitation of airborne scanning geometry. (3) The model was trained on Amsterdam's managed urban forest; transferability to cities with different species compositions, climate zones, or management regimes requires empirical testing—though the dominance of morphological over species-specific features (98.9% performance retention without species data) suggests reasonable generalizability. (4) Single-epoch data collection captures one phenological snapshot; seasonal LAI variation is not modeled but could be addressed through repeat acquisitions.
