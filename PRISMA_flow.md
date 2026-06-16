# PRISMA Flow Summary

This text-based PRISMA/ROSES-style flow summary is derived from:
- `data/search_strings.md`
- `data/screening/fulltext_exclusion_reasons.csv`

## Flow Diagram (ASCII)

```text
Records identified through database searching (n = 2,051)
                        |
                        v
Records after deduplication and source filtering (n = 204)
                        |
                        v
Records screened (title/abstract) (n = 200)
                        |
                        v
Full-text articles assessed for eligibility (n = 72)
                        |
                        +--> Full-text articles excluded, with reasons (n = 30)
                        |       - Wrong study type: 5
                        |       - Wrong intervention: 5
                        |       - Wrong outcome measure: 5
                        |       - Inaccessible full text: 5
                        |       - Duplicate: 5
                        |       - Conference abstract only: 5
                        |
                        v
Studies included in qualitative/quantitative synthesis (n = 42)
```

## Notes on Screening Totals

- The reduction from **2,051** to **204** reflects both **deduplication** and **source filtering** as reported in `data/search_strings.md`.
- The step from **204** to **200** indicates that four records were removed prior to title/abstract screening during source-filtering cleanup.

## Full-text Exclusion Reasons

| Exclusion category | Count |
|---|---:|
| Wrong study type | 5 |
| Wrong intervention | 5 |
| Wrong outcome measure | 5 |
| Inaccessible full text | 5 |
| Duplicate | 5 |
| Conference abstract only | 5 |
| **Total full-text exclusions** | **30** |
