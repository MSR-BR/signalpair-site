# C-009/L05 regional source contract

## Production source

- provider: World Bank World Development Indicators API;
- indicator: `SP.DYN.IMRT.IN`;
- unit: infant deaths per 1,000 live births;
- upstream producer: UN Inter-agency Group for Child Mortality Estimation;
- frozen snapshot last updated: 2026-07-13;
- license: CC BY 4.0.

## Aggregation rule

The pilot uses the official World Bank aggregate observations already present
in the frozen V006 API snapshot. It does not calculate an arithmetic mean of
country rates. The seven displayed aggregate codes are:

- `SSF`: Sub-Saharan Africa;
- `SAS`: South Asia;
- `MEA`: Middle East, North Africa, Afghanistan & Pakistan;
- `EAS`: East Asia & Pacific;
- `LCN`: Latin America & Caribbean;
- `ECS`: Europe & Central Asia;
- `NAC`: North America.

## Coverage rule

Every displayed region has one non-null observation for every year from 1990
through 2024. The regional pilot does not claim coverage before 1990.

Publication authority: none.
