# Video 005 — V-005 analysis and sensitivity report

Status: **analytically complete; independently reproduced; not public copy**  
Scope: frozen V-003 panel + frozen V-004 method  
Publication authority: **none**

## Question and hypotheses

Question: from 2001 to 2023, as adult obesity rose robustly, did
undernourishment more often rise with it or fall?

- **H1:** among countries and areas with a robust obesity rise, the share with
  a robust PoU fall is greater than the share with a robust PoU rise, while both
  groups are non-zero.
- **H2:** the same ordering, `p_F > p_R > 0`, survives every sensitivity
  scenario frozen in V-004 and an independent reproduction.

This is a descriptive ecological comparison. It is not a causal test and does
not compare the same people within a country.

## Frozen inputs

- Panel: `clean/v003-country-midpoint-panel.csv`
- Panel SHA-256:
  `01f808160e9cfd251000ee807847a642051d4dec6568bf95ec522eb24693c1f8`
- Method: `method/v004-statistical-contract.json`
- Method SHA-256:
  `fc0d4b571203eeaa11c04db7b3942df8e742b57bd630ef4b733c90cb52ff03d1`
- Registry: 217 World Bank non-aggregate countries and areas × 23 PoU
  midpoint years, 2001–2023.

The obesity estimate is robustly rising only when the full endpoint change
interval is above zero. PoU values reported as below 2.5% are treated as the
interval `[0, 2.5]` in the primary analysis.

## Primary result

For the 2001→2023 comparison:

| Quantity | Result |
|---|---:|
| Pair-comparable countries and areas | 161 |
| Conditional denominator: robust obesity rise | 133 |
| R — PoU robust rise | 28 |
| F — PoU robust fall | 81 |
| U — PoU direction indeterminate | 24 |
| O — obesity not robustly rising | 28 |
| `p_R` among R+F+U | 21.1% |
| `p_F` among R+F+U | 60.9% |
| `p_U` among R+F+U | 18.0% |
| `p_F − p_R` | +39.8 percentage points |

The frozen H1 rule returns **SUPPORTED**.

## Registered sensitivities

All 13 frozen scenarios return `p_F > p_R > 0`.

| Scenario | Comparable | Conditional | R | F | U | F−R, pp | Status |
|---|---:|---:|---:|---:|---:|---:|---|
| Primary 2001→2023 | 161 | 133 | 28 | 81 | 24 | 39.8 | Supported |
| Endpoint 2021 | 162 | 133 | 31 | 79 | 23 | 36.1 | Supported |
| Endpoint 2022 | 162 | 133 | 32 | 77 | 24 | 33.8 | Supported |
| Baseline 2002 | 161 | 131 | 26 | 85 | 20 | 45.0 | Supported |
| Baseline 2003 | 161 | 127 | 24 | 85 | 18 | 48.0 | Supported |
| Exclude every censored-PoU endpoint pair | 99 | 92 | 28 | 63 | 1 | 38.0 | Supported |
| Leave out East Asia & Pacific | 141 | 117 | 27 | 70 | 20 | 36.8 | Supported |
| Leave out Europe & Central Asia | 113 | 103 | 27 | 68 | 8 | 39.8 | Supported |
| Leave out Latin America & Caribbean | 135 | 108 | 23 | 61 | 24 | 35.2 | Supported |
| Leave out MENA, Afghanistan & Pakistan | 142 | 119 | 21 | 74 | 24 | 44.5 | Supported |
| Leave out North America | 159 | 131 | 28 | 81 | 22 | 40.5 | Supported |
| Leave out South Asia | 157 | 129 | 28 | 77 | 24 | 38.0 | Supported |
| Leave out Sub-Saharan Africa | 119 | 91 | 14 | 55 | 22 | 45.1 | Supported |

The independent validator reproduced all pair states and scenarios without
importing the primary analysis implementation. Its 28 checks all pass.
Therefore, the frozen H2 rule returns **SUPPORTED**.

## Heterogeneity and descriptive context

The global result is not uniform by region. In the primary endpoint
classification:

| Region | Conditional n | R | F | U | F−R, pp |
|---|---:|---:|---:|---:|---:|
| East Asia & Pacific | 16 | 1 | 11 | 4 | 62.5 |
| Europe & Central Asia | 30 | 1 | 13 | 16 | 40.0 |
| Latin America & Caribbean | 25 | 5 | 20 | 0 | 60.0 |
| MENA, Afghanistan & Pakistan | 14 | 7 | 7 | 0 | 0.0 |
| North America | 2 | 0 | 0 | 2 | 0.0 |
| South Asia | 4 | 0 | 4 | 0 | 100.0 |
| Sub-Saharan Africa | 42 | 14 | 26 | 2 | 28.6 |

This regional table is a diagnostic, not a ranking and not a regional
hypothesis test. Small denominators and censoring matter.

Population-weighted context is descriptive only. The 161 endpoint-comparable
countries and areas cover 7.708 billion recorded people: 71.4% live in the F
group, 11.8% in R and 16.8% in the public ambiguous group A. These shares do not
enter H1 or H2.

## Visual and temporal diagnostics

- In 2023, the public map counts are R=28, F=81 and A=52.
- 149 of 161 comparable endpoint entities have an exact match in the pinned
  low-resolution geometry; 12 remain in counts but require an off-map device.
- The largest adjacent public-state turnover is 2007→2008, with 22 changes
  among entities comparable in both frames.
- That turnover is **not** an independent annual shock: each adjacent PoU
  midpoint shares two source years with the next midpoint.

![V-005 internal analytical overview](../derived/v005-analysis/v005-results-and-sensitivity-overview.png)

## Required limitations

1. The hypotheses were formulated after prior exploratory inspection. The
   source, data-quality, classification and sensitivity rules were then frozen
   prospectively; this is not a pristine preregistration.
2. WHO obesity estimates and FAO PoU estimates describe different populations
   and have different uncertainty structures.
3. National co-movement does not identify causes or individual-level
   transitions.
4. PoU uses centered three-year moving averages, so adjacent visual frames are
   overlapping summaries.
5. PoU censoring below 2.5% creates an indeterminate category and materially
   reduces the no-censor sensitivity sample.
6. Results are conditional on comparable countries and areas, not all 217
   registry entities.
7. Geometry is presentation only; analytical counts include off-map entities.

## Reproduction and handoff

- Primary implementation: `analytics/run_v005_analysis.py`
- Independent implementation: `analytics/validate_v005_analysis.py`
- Validation: `manifests/v005-validation.json`
- Notebook: `notebooks/v005-analysis-and-sensitivity.ipynb`
- Rendered notebook: `notebooks/v005-analysis-and-sensitivity.html`

V-005 establishes the numerical result. **V-006 must decide the concise answer,
the limitations hierarchy and what may be communicated publicly.** This report
does not authorize a storyboard, render, site update, upload or publication.

