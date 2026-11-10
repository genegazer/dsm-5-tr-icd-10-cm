# DSM-5-TR to ICD-10-CM reference

This repository is intended to hold the supplied DSM-5-TR numerical listing and machine-readable representations of its diagnosis-to-code mappings.

## Data layout

- `DSM-5-TR_ICD-10-CM_numerical_listing.csv` — source listing with columns `ICD-10-CM` and `Disorder, condition, or problem`.
- `data/diagnoses.json` — JSON array generated from the CSV. Each source row remains a separate record, including repeated ICD-10-CM codes that map to multiple descriptions.
- `scripts/csv_to_json.py` — converts the CSV to JSON without grouping or dropping duplicate codes.
- `schema/diagnosis.schema.json` — JSON Schema for each diagnosis record.

## Generate JSON

From the repository root, run:

```bash
python scripts/csv_to_json.py
```

The script reads `DSM-5-TR_ICD-10-CM_numerical_listing.csv` and writes `data/diagnoses.json` as UTF-8 JSON.

## Data notes

This is a reference dataset, not clinical advice. Confirm coding decisions against the current official ICD-10-CM resources and applicable coding guidance. The CSV's original descriptions are retained as supplied; duplicate codes are intentional and should not be deduplicated.
