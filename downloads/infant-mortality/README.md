# SignalPair Episode 04 — infant mortality by world region

This directory is the public-facing reproducibility package for the local
methodology-page candidate.

## Scope

- indicator: World Bank WDI `SP.DYN.IMRT.IN`;
- upstream producer: UN Inter-agency Group for Child Mortality Estimation;
- unit: deaths before age 1 per 1,000 live births;
- period: 1990–2024;
- geographic unit: seven official World Bank regional aggregates;
- observations: 245 region-years;
- frozen source snapshot last updated: 2026-07-13.

The regional values are official WDI aggregate observations. They are not
arithmetic country averages calculated by SignalPair.

## Files

- `data-region-year.csv`: exact annual regional data used by the animation;
- `source-contract.md`: source, unit, coverage and aggregation rules;
- `scientific-audit.json`: machine-readable endpoint results and QA facts;
- `qa-report.md`: human-readable scientific and visual QA summary;
- `prepare-regions.py`: reproducible extraction of the regional series;
- `audit-data.py`: reproducible source and claim audit;
- `SHA256SUMS.txt`: checksums for the files above.

## Interpretation boundary

The episode asks which region had the largest **absolute** decline from 1990
to 2024. It does not identify causes, evaluate policies or imply that every
country followed its regional aggregate.

Publication authority: none. This package remains a local review candidate.
