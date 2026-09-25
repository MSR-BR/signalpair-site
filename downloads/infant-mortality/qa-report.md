# QA — V006 scientific and visual audit

Status: **PASS**

## Scientific result

- All 245 region-year values match the frozen World Bank WDI snapshot.
- Seven official regional aggregates have complete annual coverage from 1990
  through 2024, with no nulls or duplicate region-years.
- The L07 phrase “fall fastest” was ambiguous: South Asia leads the absolute
  decline, while East Asia & Pacific leads the percentage decline.
- The repaired hook asks for the “biggest drop” and explicitly shows the unit,
  operationalized as 1990 minus 2024 deaths before age 1 per 1,000 live births.
- The supported absolute result is South Asia: 85.5 to 23.2, a drop of 62.3.
- No causal claim or forced conclusion is shown.

## Visual and technical result

- 1080 × 1920, 30 fps, 34.5 s, H.264 High, yuv420p, no audio.
- 1,035 frames; first and last frame hashes match exactly.
- Nine checkpoints have no content in the reserved right or lower Shorts zones.
- Bars begin at zero and share a fixed 0–110 scale; the observed maximum is
  102.9.
- Direct region labels supplement color; the chart does not rely on color alone.
- Smooth between-year motion is visual interpolation between annual
  observations and must be disclosed as such on the methodology page.
- Master SHA-256: `5a46cad0b8b2c38c88211c6f4ecc118eafcf7bcee03618166c7d97fdd7d3776d`.

The master is local-only. No upload, scheduling or publication is authorized.
