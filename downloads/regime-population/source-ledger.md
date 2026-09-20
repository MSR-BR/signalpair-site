# Source ledger — V-002

Status: frozen for V-003 collection, with freshness guards. Inspection date:
2026-09-16.

| ID | Role | Authority / material | Frozen locator | License / boundary |
| --- | --- | --- | --- | --- |
| `SRC-VDEM16-DATA` | Controlling regime source and aligned 1973–2024 population | V-Dem Country-Year Full+Others v16: `v2x_regime_amb`, `v2x_regime`, `e_wb_pop` | DOI `10.23696/vdemds26`; GitHub tag `V16`, commit `f4dd26922e658442524dfd954bf14f7ebe622d5d` | CC BY-SA 4.0; attribution and share-alike apply to distributed derivatives |
| `SRC-VDEM16-CODEBOOK` | Definition authority | V-Dem Codebook v16 | https://www.v-dem.net/documents/70/codebook_v16.pdf | Cite V-Dem v16 and the RoW paper |
| `SRC-ROW-2018` | Conceptual method | Lührmann, Tannenberg & Lindberg (2018), Regimes of the World | https://doi.org/10.17645/pag.v6i1.1214 | Method reference; does not replace the v16 data snapshot |
| `SRC-WB-WDI2-POP` | 2025 endpoint population and world coverage reference | WDI source 2, `SP.POP.TOTL` | https://api.worldbank.org/v2 | CC BY 4.0; mutable source guarded by `lastupdated` |
| `SRC-OWID-ROW-CHECK` | Secondary replication and processing audit only | OWID Grapher `political-regime-amb-row` | https://ourworldindata.org/grapher/political-regime-amb-row | Not canonical; includes OWID historical imputation |

## Controlling hierarchy

1. V-Dem v16 data and codebook control regime classification and V-Dem unit
   identity.
2. `e_wb_pop` in the same V-Dem release controls 1973–2024 population weights.
3. Current WDI source 2 controls only the documented 2025 extension and `WLD`
   coverage reference.
4. OWID is a cross-check and discovery layer, never the canonical political-unit
   universe.

## Required citations

- Coppedge et al. (2026), *V-Dem Country-Year Dataset v16*, DOI
  `10.23696/vdemds26`.
- Lührmann, Tannenberg & Lindberg (2018), *Regimes of the World (RoW)*.
- World Bank, World Development Indicators, indicator `SP.POP.TOTL`, frozen
  snapshot date and source release.

## License consequence

V-Dem is CC BY-SA 4.0 and WDI is CC BY 4.0. Any public downloadable derivative
containing V-Dem data must preserve attribution and be distributed under
compatible share-alike terms. Video frames may display derived summaries with
attribution; methodology downloads must carry an explicit license notice.

## Freshness guards

- V-Dem tag: `V16`.
- V-Dem commit: `f4dd26922e658442524dfd954bf14f7ebe622d5d`.
- V-Dem data blob: `5a472621427337cebf032a9c4e397e0bedd57aea`.
- WDI source 2 `lastupdated`: `2026-07-13`.

Any mismatch before V-003 collection reopens V-002.

## V-003 collection receipt

- Snapshot: `20260916T194441Z`.
- V-Dem raw data: 33,878,255 bytes; SHA-256
  `39b412d39a061c18f20c98e4ad4d6355b05a0441df31be4ee9aec420dc3d95ea`;
  Git blob identity reproduced.
- Codebook: 3,617,986 bytes; frozen SHA-256 reproduced.
- WDI source 2 remained `lastupdated = 2026-07-13`.
- Seven small API/metadata responses are preserved in
  `raw/v003-20260916T194441Z/`.
- V-Dem data and codebook are in Dropbox-synced
  `bulk/videos/004-regime-population/source-downloads/v003-20260916T194441Z/`.
- Full request and artifact hashes: `../manifests/v003-data-lineage.json`.

V-003 found 172 safe one-to-one 2025 matches. PSE/PSG, TZA/ZZB and SOM/SML
require authoritative splits; Taiwan is unmatched. None was filled.
