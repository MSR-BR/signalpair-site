# Source and data contract — V-002

Status: **FROZEN FOR V-003 COLLECTION AND QUALITY AUDIT**

## Decision first

V-002 adopts the exact WHO GHO and WDI snapshots collected on 2026-09-19 as
the production inputs for V-003. A live equality check on 2026-09-20 found the
controlling API responses unchanged.

The contract passes with one material temporal asymmetry: obesity is an annual
modelled estimate for calendar year `t`, while national prevalence of
undernourishment is a three-year moving average centred on WDI label `t`.
Therefore 2001 means obesity in 2001 paired with PoU for 2000–2002, and 2023
means obesity in 2023 paired with PoU for 2022–2024. Adjacent animation frames
overlap two of three PoU years and are not independent annual observations.

This asymmetry does not invalidate the descriptive country-period question,
but it must remain visible in the method and later public-language contracts.

## Controlling sources and releases

| Role | Controlling source | Frozen release | Exact snapshot |
| --- | --- | --- | --- |
| adult obesity values and intervals | WHO Global Health Observatory `NCD_BMI_30A` | row release timestamp `2026-05-27T16:07:31.457+02:00` | `who-gho-NCD_BMI_30A-both-sexes-age18plus.json`, SHA-256 `0e0a02b…dd99` |
| obesity definition/method | WHO indicator metadata; NCD-RisC Nature paper | 2026 obesity release | GHO metadata snapshot plus cited institutional pages |
| obesity methods/code companion | NCD-RisC Zenodo DOI `10.5281/zenodo.20161247` | version 2.0, updated 2026-05-13 | `zenodo-20161247-record.json`, SHA-256 `01394a7…ad4` |
| national PoU values | FAO, retrieved through WDI source 2 `SN.ITK.DEFC.ZS` | WDI `lastupdated=2026-07-13` | `worldbank-SN.ITK.DEFC.ZS-2001-2023.json`, SHA-256 `17dc400…985` |
| population context | WDI source 2 `SP.POP.TOTL` | WDI `lastupdated=2026-07-13` | `worldbank-SP.POP.TOTL-2001-2023.json`, SHA-256 `277062d…dab` |
| entity registry | World Bank country endpoint | snapshot 2026-09-19 | `worldbank-countries.json`, SHA-256 `94881d8…37a` |
| map geometry | Natural Earth Admin 0 Countries 1:110m | upstream commit `ca96624a56bd078437bca8184e78163e5039ad19` | template asset SHA-256 `6866c87…77f` |

The GHO country output is controlling for values. Zenodo is a methods and code
companion and must not be substituted for the complete GHO output table.
Nature publication or correction prose is not a data table.

## Frozen variables

### Adult obesity

- indicator: `NCD_BMI_30A`;
- definition: percentage of adults aged 18+ with BMI at least 30 kg/m²;
- statistic: age-standardized estimated prevalence, percent;
- sex: `SEX_BTSX`;
- age: `AGEGROUP_YEARS18-PLUS`;
- geography field: `SpatialDim`;
- time field: `TimeDim`, calendar year;
- estimate: `NumericValue`;
- posterior uncertainty limits: `Low`, `High`;
- required release field: `Date`.

WHO states that estimates come from a Bayesian hierarchical meta-regression
using population-based measured-height/weight studies. The uncertainty limits
reflect posterior uncertainty from sampling error, study characteristics and
data availability. SignalPair's non-overlap rule is a conservative
classification choice, not a significance test.

### Prevalence of undernourishment

- indicator: `SN.ITK.DEFC.ZS`;
- upstream producer: FAO;
- retrieval layer: World Bank WDI source 2;
- definition: estimated percentage of the population whose habitual food
  consumption is insufficient for the dietary energy needed for a normal,
  active and healthy life;
- geography field: `countryiso3code`;
- API midpoint label: `date`;
- value: `value`, percent;
- national temporal support: centred three-year moving average.

FAO says PoU is useful for persistent food-deprivation trends, but not for
identifying undernourished individuals or evaluating short-term events and
policies. The full historical series may be revised with each edition; the
frozen snapshot must therefore never be mixed with values from another release.

## Temporal contract

For midpoint label `t`:

- obesity support: calendar year `t`;
- PoU support: `t-1` through `t+1`;
- visual label: midpoint year `t` may be used only with a persistent disclosure
  that PoU is a centred three-year estimate;
- methodology label: always preserve the exact period, such as `2022–2024`;
- no frame may be called an independent yearly measurement;
- no adjacent-frame change may be framed as a one-year shock;
- 2001–2023 is retained because both frozen sources cover all midpoint labels.

The mandatory adjacent-year checks in H2 test sensitivity to neighbouring
overlapping windows. They are not independent replications.

## Censoring and uncertainty

WDI metadata says a displayed value of `2.5` may signify PoU below 2.5%.
Because the API does not distinguish exact 2.5 from censored below-2.5 values:

- every exact API value `2.5` is interval-censored as `[0, 2.5]`;
- it must display as `<2.5`, not `2.5%`;
- 1.25 is allowed only as a declared midpoint sensitivity;
- uncensored PoU values are frozen as source point estimates, not falsely
  described as having zero model uncertainty;
- a complete-case sensitivity excluding any endpoint-censored country remains
  mandatory.

WHO posterior intervals and PoU censoring intervals represent different kinds
of uncertainty and must never be described as directly equivalent.

## Entity universe and joins

The registry is the frozen World Bank country endpoint snapshot. Rows whose
`region.value` is `Aggregates` are excluded. This leaves 217 candidate
non-aggregate entities before joining the indicators.

Allowed joins:

- WHO `SpatialDim` to frozen World Bank `id`, exact code only;
- WDI `countryiso3code` to frozen World Bank `id`, exact code only;
- population on exact entity code plus midpoint year;
- geometry through a reviewed explicit crosswalk in V-003.

Name-only, fuzzy and many-to-one joins are prohibited. Any code exception must
be listed with source evidence, not silently rewritten. Aggregates, unmatched
entities and off-map entities remain separate and reportable. No interpolation,
carry-forward, extrapolation or geographical imputation is allowed.

Until V-003 audits the taxonomy, internal documents should use
`non-aggregate entities`; public use of `countries` is conditional on the
reviewed entity table.

## Grain and expected keys

- raw WHO grain: one indicator × geography × year × sex × age row;
- raw PoU grain: one WDI entity × midpoint year row;
- raw population grain: one WDI entity × year row;
- clean obesity key: `(entity_code, year)` after frozen dimensions;
- clean PoU key: `(entity_code, midpoint_year)`;
- clean joined key: `(entity_code, midpoint_year)`;
- duplicate keys, conflicting duplicates or null keys are stop conditions.

The joined row must retain `pou_period_start` and `pou_period_end`; reducing the
three-year period to a bare year field is prohibited.

## Missingness and exclusions

- no imputation;
- null values remain null, never zero;
- a country-period enters `E(t)` only when both focal measures exist for the
  baseline and comparison required by the estimand;
- missing obesity, missing PoU, censored PoU, registry mismatch and geometry
  mismatch are distinct reason codes;
- population missingness affects only population-weighted context, not the
  equal-country primary estimand;
- annual and endpoint denominators must be emitted before any percentages.

## Licensing and attribution

- WHO datasets/APIs: CC BY 4.0 unless otherwise indicated, with WHO's binding
  additions; cite WHO, item, URL and access date; do not imply endorsement and
  do not use WHO's name/emblem as branding.
- WDI: CC BY 4.0 unless indicator metadata says otherwise, with attribution to
  the World Bank and data provider; third-party terms remain controlling.
- PoU attribution: `Food and Agriculture Organization of the United Nations
  (FAO), retrieved via World Development Indicators`; FAO catalog reuse also
  remains subject to the FAO Statistical Database Terms of Use.
- Zenodo methods package: CC BY 4.0; cite DOI and version.
- Natural Earth geometry: public domain; boundary disclaimer remains required.

A future download package must include these attributions, source URLs, access
date, release identifiers and exact hashes. Logos are not licensed by the data
licenses and are not authorized.

## Revision policy and stop conditions

The frozen local snapshots, not mutable APIs, control V-003; never silently refresh an input.
A newer release may be considered only through an explicit
contract revision; mixing releases is prohibited.

Stop and reopen V-002 if:

- any adopted snapshot hash differs;
- release, indicator, dimensions, units or definitions cannot be reproduced;
- PoU midpoint labels cannot be tied to centred three-year windows;
- censoring cannot be preserved;
- duplicate or conflicting entity-year keys exist;
- entity matching requires undocumented assumptions;
- licensing or attribution is incompatible with the intended public package;
- V-003 finds material schema drift, hidden aggregates or break-in-series;
- the temporal asymmetry cannot be communicated honestly in a Short.

## Authority boundary

This contract authorizes V-003 to collect, normalize and audit only. It does
not authorize a formal answer, causal interpretation, storyboard, render,
methodology-page deployment, YouTube upload, scheduling or publication.
