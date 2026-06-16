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
                        +--> Full-text articles excluded, with reasons (n = 24)
                        |       - Wrong study type: 4
                        |       - Wrong intervention: 4
                        |       - Wrong outcome measure: 4
                        |       - Inaccessible full text: 4
                        |       - Duplicate: 4
                        |       - Conference abstract only: 4
                        |
                        v
Studies included in qualitative/quantitative synthesis (n = 48)
```

## Notes on Screening Totals

- The reduction from **2,051** to **204** reflects both **deduplication** and **source filtering** as reported in `data/search_strings.md`.
- The step from **204** to **200** indicates that four records were removed prior to title/abstract screening during source-filtering cleanup.

## Full-text Exclusion Reasons

| Exclusion category | Count |
|---|---:|
| Wrong study type | 4 |
| Wrong intervention | 4 |
| Wrong outcome measure | 4 |
| Inaccessible full text | 4 |
| Duplicate | 4 |
| Conference abstract only | 4 |
| **Total full-text exclusions** | **24** |
