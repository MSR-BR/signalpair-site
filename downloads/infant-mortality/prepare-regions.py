#!/usr/bin/env python3
"""Extract official World Bank regional aggregates from the frozen V006 snapshot."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path


VIDEO = Path(__file__).resolve().parents[1]
RAW = VIDEO / "raw/v000/worldbank-SP.DYN.IMRT.IN-1960-2024.json"
CLEAN = VIDEO / "clean/v004-world-bank-regions.csv"
MANIFEST = VIDEO / "manifests/v004-regional-data-validation.json"

REGIONS = [
    ("SSF", "Sub-Saharan Africa"),
    ("SAS", "South Asia"),
    ("MEA", "Middle East, North Africa, Afghanistan & Pakistan"),
    ("EAS", "East Asia & Pacific"),
    ("LCN", "Latin America & Caribbean"),
    ("ECS", "Europe & Central Asia"),
    ("NAC", "North America"),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    metadata, observations = json.loads(RAW.read_text(encoding="utf-8"))
    expected = {code: name for code, name in REGIONS}
    rows = []
    by_code: dict[str, list[dict[str, object]]] = defaultdict(list)
    source_names: dict[str, str] = {}

    for observation in observations:
        code = observation.get("countryiso3code") or ""
        value = observation.get("value")
        if code not in expected or value is None:
            continue
        year = int(observation["date"])
        if not 1990 <= year <= 2024:
            continue
        source_name = observation["country"]["value"]
        source_names[code] = source_name
        row = {
            "region_code": code,
            "region": expected[code],
            "source_region_name": source_name,
            "year": year,
            "infant_mortality_per_1000": float(value),
        }
        rows.append(row)
        by_code[code].append(row)

    order = {code: index for index, (code, _) in enumerate(REGIONS)}
    rows.sort(key=lambda row: (int(row["year"]), order[str(row["region_code"])]))
    if len(rows) != 7 * 35:
        raise RuntimeError(f"Expected 245 complete region-year rows, found {len(rows)}")

    coverage = {}
    for code, display_name in REGIONS:
        region_rows = sorted(by_code[code], key=lambda row: int(row["year"]))
        years = [int(row["year"]) for row in region_rows]
        if years != list(range(1990, 2025)):
            raise RuntimeError(f"Incomplete annual coverage for {code}")
        coverage[code] = {
            "displayName": display_name,
            "sourceName": source_names[code],
            "years": len(years),
            "firstYear": years[0],
            "firstValue": region_rows[0]["infant_mortality_per_1000"],
            "lastYear": years[-1],
            "lastValue": region_rows[-1]["infant_mortality_per_1000"],
        }

    CLEAN.parent.mkdir(parents=True, exist_ok=True)
    with CLEAN.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    manifest = {
        "status": "PASS",
        "change": "C-009/L05-region-bars-pilot",
        "indicator": "SP.DYN.IMRT.IN",
        "unit": "deaths before age 1 per 1,000 live births",
        "source": "World Bank WDI; upstream producer UN IGME",
        "sourceLastUpdated": metadata.get("lastupdated"),
        "period": [1990, 2024],
        "aggregation": "official World Bank regional aggregates; no arithmetic country mean",
        "rows": len(rows),
        "regions": coverage,
        "files": {
            str(RAW.relative_to(VIDEO)): sha256(RAW),
            str(CLEAN.relative_to(VIDEO)): sha256(CLEAN),
        },
        "publicationAuthority": False,
    }
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
