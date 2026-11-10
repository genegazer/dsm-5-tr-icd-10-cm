#!/usr/bin/env python3
"""Convert the DSM-5-TR ICD-10-CM CSV listing to a JSON array."""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "DSM-5-TR_ICD-10-CM_numerical_listing.csv"
DESTINATION = ROOT / "data" / "diagnoses.json"


def main() -> None:
    with SOURCE.open("r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        expected = ["ICD-10-CM", "Disorder, condition, or problem"]
        if reader.fieldnames != expected:
            raise ValueError(
                f"Expected CSV columns {expected!r}; found {reader.fieldnames!r}"
            )
        records = [
            {
                "icd10cm": row["ICD-10-CM"],
                "diagnosis": row["Disorder, condition, or problem"],
            }
            for row in reader
        ]

    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(records)} records to {DESTINATION.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
