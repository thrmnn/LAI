# Contribution Rationale

## Research Question

How can cities obtain accurate, comprehensive maps of individual-tree canopy density (Leaf Area Index) across entire urban forests—including private-property trees—using automated remote sensing and machine learning, without relying on costly manual surveys?

## Gap Analysis

**What is currently known.** Urban trees are among the most effective countermeasures to the Urban Heat Island effect, reducing ambient temperatures by 0.5–2.0 °C and mean radiant temperatures by up to 20 °C. Leaf Area Index (LAI)—the ratio of one-sided leaf area to ground area—directly determines a tree's shading capacity and its contribution to carbon sequestration, air quality improvement, and stormwater management. Accurate, spatially explicit LAI data is therefore essential for evidence-based urban heat mitigation planning.

**Why existing approaches fall short.** Current practice depends on manual arborist surveys requiring 20–30 minutes per tree and yielding infrequent, incomplete inventories. Crucially, municipal databases document only publicly managed trees, omitting an estimated 70% of the urban forest on private land. This systematic under-counting can underestimate ecosystem services by 15–35%. Remote sensing alternatives exist but face their own barriers: LiDAR-based canopy density estimation requires high-density point clouds (>20 pts/m²) unavailable in many cities, and traditional allometric models that infer LAI from height alone ignore crown architecture, spectral condition, and species-specific variation—limiting predictive accuracy.

**Who benefits from closing this gap.** Municipal planners lack the quantitative, wall-to-wall canopy density maps needed to prioritize tree planting in heat-vulnerable neighborhoods. Without individual-tree LAI data covering entire jurisdictions, heat mitigation strategies remain reactive and spatially biased toward public land.

## Our Contribution

**A fully automated, multi-modal framework.** We integrate LiDAR point clouds, high-resolution RGB+NIR imagery, and deep-learning crown segmentation (DeepForest) with voxelization-based LAI estimation and a machine learning prediction pipeline. Applied to Amsterdam (12,350 trees across 25 km²), XGBoost achieves R² = 0.784 and RMSE = 0.620 m²/m²—a 39% improvement over allometric baselines—while detecting three times more trees than the municipal database.

**Adaptive to data availability.** The framework accommodates variable LiDAR densities (5–20 pts/m²) through adaptive voxel sizing, and feature ablation shows that morphological and spectral features alone capture 98.9% of achievable performance. Cities lacking LiDAR can leverage the trained prediction model with coarser height estimates (projected R² ≈ 0.65–0.70), lowering the barrier to adoption.

**Actionable for planning.** Outputs are delivered in standard GIS formats (GeoJSON, GeoTIFF) and include per-tree LAI estimates, crown polygons with genus attribution, and city-wide LAI maps at 0.5 m² resolution. Processing scales to full-city deployment in under 48 hours via cloud parallelization at marginal cost (<$200), enabling municipalities to integrate quantitative shade assessment into heat mitigation and environmental justice planning.
