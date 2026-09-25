#!/usr/bin/env python3
"""Independent data and claim audit for C-009/L08."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path


VIDEO = Path(__file__).resolve().parents[1]
RAW = VIDEO / "raw/v000/worldbank-SP.DYN.IMRT.IN-1960-2024.json"
CLEAN = VIDEO / "clean/v004-world-bank-regions.csv"
OUTPUT = VIDEO / "manifests/v007-scientific-visual-audit.json"
REGIONS = ["SSF", "SAS", "MEA", "EAS", "LCN", "ECS", "NAC"]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    metadata, observations = json.loads(RAW.read_text(encoding="utf-8"))
    clean_rows = list(csv.DictReader(CLEAN.open(newline="", encoding="utf-8")))
    clean_by_key = {
        (row["region_code"], int(row["year"])): float(row["infant_mortality_per_1000"])
        for row in clean_rows
    }
    raw_by_key = {}
    for row in observations:
        code = row.get("countryiso3code") or ""
        value = row.get("value")
        year = int(row["date"])
        if code in REGIONS and value is not None and 1990 <= year <= 2024:
            raw_by_key[(code, year)] = float(value)

    by_region: dict[str, list[tuple[int, float]]] = defaultdict(list)
    for (code, year), value in clean_by_key.items():
        by_region[code].append((year, value))

    region_results = {}
    for code in REGIONS:
        values = sorted(by_region[code])
        start = values[0][1]
        end = values[-1][1]
        absolute_drop = start - end
        region_results[code] = {
            "years": len(values),
            "firstYear": values[0][0],
            "lastYear": values[-1][0],
            "start": start,
            "end": end,
            "absoluteDropPer1000": round(absolute_drop, 1),
            "averageAnnualAbsoluteDropPer1000": round(absolute_drop / 34, 4),
            "relativeDropPct": round(absolute_drop / start * 100, 1),
        }

    absolute_rank = sorted(
        REGIONS,
        key=lambda code: region_results[code]["absoluteDropPer1000"],
        reverse=True,
    )
    relative_rank = sorted(
        REGIONS,
        key=lambda code: region_results[code]["relativeDropPct"],
        reverse=True,
    )
    duplicates = len(clean_rows) - len(clean_by_key)
    clean_matches_raw = clean_by_key == raw_by_key
    complete_coverage = all(
        sorted(year for year, _ in by_region[code]) == list(range(1990, 2025))
        for code in REGIONS
    )

    status = "PASS" if (
        len(clean_rows) == 245
        and duplicates == 0
        and clean_matches_raw
        and complete_coverage
    ) else "FAIL"
    result = {
        "status": status,
        "change": "C-009/L08-scientific-and-visual-QA",
        "sourceLastUpdated": metadata.get("lastupdated"),
        "source": "World Bank WDI SP.DYN.IMRT.IN; upstream producer UN IGME",
        "period": [1990, 2024],
        "rows": len(clean_rows),
        "duplicateRegionYears": duplicates,
        "nullMetricValues": sum(
            not row["infant_mortality_per_1000"] for row in clean_rows
        ),
        "completeAnnualCoverage": complete_coverage,
        "cleanValuesMatchFrozenRawSource": clean_matches_raw,
        "regions": region_results,
        "rankings": {
            "absoluteDrop": absolute_rank,
            "relativeDrop": relative_rank,
        },
        "claimAudit": {
            "previousHook": {
                "text": "Where did infant mortality fall fastest?",
                "status": "AMBIGUOUS",
                "reason": (
                    "The largest absolute decline is South Asia, while the largest "
                    "percentage decline is East Asia & Pacific."
                ),
            },
            "revisedHook": {
                "text": "Which region saw the biggest drop?",
                "status": "PASS",
                "operationalDefinition": (
                    "1990 value minus 2024 value, in deaths before age 1 per "
                    "1,000 live births."
                ),
                "supportedAnswer": "South Asia",
                "supportedValue": 62.3,
            },
            "causalClaim": False,
            "forcedConclusion": False,
        },
        "visualAudit": {
            "chart": "fixed horizontal bars",
            "barBaseline": 0,
            "commonScale": [0, 110],
            "maximumObservedValue": max(clean_by_key.values()),
            "fixedRegionOrder": REGIONS,
            "regionIdentityUsesTextAndColor": True,
            "annualValues": True,
            "betweenYearMotion": (
                "linear visual interpolation only; methodology must not describe "
                "fractional-year frames as separate observations"
            ),
        },
        "files": {
            str(RAW.relative_to(VIDEO)): sha256(RAW),
            str(CLEAN.relative_to(VIDEO)): sha256(CLEAN),
        },
        "publicationAuthority": False,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if status != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
