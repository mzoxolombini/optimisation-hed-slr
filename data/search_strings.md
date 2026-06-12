# Search Strings and Retrieval Summary

The following Boolean strings were used during the SLR search stage.

- **Date range searched:** January 2015 – December 2024
- **Search window executed:** January 2025
- **Topic focus:** Holistically-Nested Edge Detection (HED), deep edge/boundary detection, optimisation, and downstream segmentation/application tasks.

## IEEE Xplore

**Query**
```
(("Document Title":"Holistically-Nested Edge Detection" OR "Abstract":"Holistically-Nested Edge Detection" OR "Abstract":"HED")
 AND ("Abstract":"edge detection" OR "Abstract":"boundary detection" OR "Abstract":"image segmentation")
 AND ("Abstract":"optimization" OR "Abstract":"improved" OR "Abstract":"hybrid" OR "Abstract":"multi-scale"))
```

**Results returned:** 286

## ScienceDirect / Scopus

**Query**
```
(TITLE-ABS-KEY("Holistically-Nested Edge Detection" OR "HED" OR "deep edge detection" OR "boundary detection")
 AND TITLE-ABS-KEY("image segmentation" OR "salient object detection" OR "medical imaging" OR "remote sensing" OR "crack detection")
 AND TITLE-ABS-KEY("optimization" OR "improved" OR "attention" OR "fusion" OR "U-Net" OR "Mask R-CNN"))
 AND PUBYEAR > 2014 AND PUBYEAR < 2025
```

**Results returned:** 412

## Web of Science

**Query**
```
TS=(("Holistically-Nested Edge Detection" OR HED OR "deep edge detection" OR "boundary-aware")
    AND ("image segmentation" OR "semantic segmentation" OR "edge map" OR "contour extraction")
    AND ("medical" OR "remote sensing" OR "industrial" OR "saliency" OR "agriculture"))
Timespan=2015-2024
Indexes=SCI-EXPANDED, ESCI
```

**Results returned:** 233

## Google Scholar

**Query**
```
("Holistically-Nested Edge Detection" OR "HED")
("edge detection" OR "boundary detection" OR "image segmentation")
("improved" OR "hybrid" OR "attention" OR "multi-scale" OR "application")
2015..2024
```

**Results returned:** ~1,120 (first 300 screened due ranking/noise)

## Deduplication and Screening Totals

- **Initial retrieval (all databases combined):** 2,051
- **After deduplication and source filtering:** 204
- **Title/abstract screened:** 200
- **Included for full-text eligibility:** 72
- **Final included studies:** 42
