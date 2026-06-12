"""Compute aggregated statistics for included SLR studies.

This script reads the included-study metadata and quality-assessment sheets,
computes aggregate statistics, saves tabular summaries, and exports figures.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"


def _count_metrics(series: pd.Series) -> pd.Series:
    """Split semicolon-separated metric lists and count individual metrics."""
    metrics = (
        series.fillna("")
        .str.split(";")
        .explode()
        .str.strip()
    )
    metrics = metrics[metrics != ""]
    return metrics.value_counts()


def main() -> None:
    """Run aggregation and write results/figures."""
    included_df = pd.read_csv(DATA_DIR / "included_studies.csv")
    quality_df = pd.read_csv(DATA_DIR / "quality_assessment.csv")

    # Merge quality scores to support per-domain quality summaries.
    merged = included_df.merge(quality_df, on="Study_ID", how="left")

    domain_counts = included_df["Domain"].value_counts().sort_values(ascending=False)
    year_counts = included_df["Year"].value_counts().sort_index()
    backbone_counts = included_df["Backbone"].value_counts().sort_values(ascending=False)
    metric_counts = _count_metrics(included_df["Evaluation_Metrics"])

    overall_scores = merged["Total_Score (0-8)"]
    overall_summary = {
        "mean": round(float(overall_scores.mean()), 3),
        "median": round(float(overall_scores.median()), 3),
        "std": round(float(overall_scores.std(ddof=1)), 3),
    }

    per_domain_quality = (
        merged.groupby("Domain")["Total_Score (0-8)"]
        .agg(["mean", "median", "std"])  # type: ignore[arg-type]
        .round(3)
    )

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, object]] = []
    for domain, count in domain_counts.items():
        rows.append({"Category": "studies_per_domain", "Item": domain, "Statistic": "count", "Value": int(count)})
    for year, count in year_counts.items():
        rows.append({"Category": "studies_per_year", "Item": str(year), "Statistic": "count", "Value": int(count)})
    rows.extend([
        {"Category": "quality_overall", "Item": "all", "Statistic": "mean", "Value": overall_summary["mean"]},
        {"Category": "quality_overall", "Item": "all", "Statistic": "median", "Value": overall_summary["median"]},
        {"Category": "quality_overall", "Item": "all", "Statistic": "std", "Value": overall_summary["std"]},
    ])
    for domain, stats in per_domain_quality.iterrows():
        rows.append({"Category": "quality_per_domain", "Item": domain, "Statistic": "mean", "Value": stats["mean"]})
        rows.append({"Category": "quality_per_domain", "Item": domain, "Statistic": "median", "Value": stats["median"]})
        rows.append({"Category": "quality_per_domain", "Item": domain, "Statistic": "std", "Value": stats["std"]})
    for backbone, count in backbone_counts.items():
        rows.append({"Category": "studies_per_backbone", "Item": backbone, "Statistic": "count", "Value": int(count)})
    for metric, count in metric_counts.items():
        rows.append({"Category": "metric_usage", "Item": metric, "Statistic": "count", "Value": int(count)})

    summary_df = pd.DataFrame(rows)
    summary_df.to_csv(RESULTS_DIR / "aggregated_statistics.csv", index=False)

    print("Count of studies per domain:")
    print(domain_counts.to_string())
    print("\nCount of studies per year:")
    print(year_counts.to_string())
    print("\nQuality score summary (overall):")
    print(overall_summary)
    print("\nQuality score summary (per domain):")
    print(per_domain_quality.to_string())
    print("\nCount of studies per backbone:")
    print(backbone_counts.to_string())
    print("\nCount of studies per evaluation metric:")
    print(metric_counts.to_string())

    # Plot studies per domain.
    plt.figure(figsize=(10, 5))
    domain_counts.plot(kind="bar", color="#4C72B0")
    plt.title("Studies per Domain")
    plt.ylabel("Number of Studies")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "studies_per_domain.png", dpi=300)
    plt.close()

    # Plot studies per year.
    plt.figure(figsize=(10, 5))
    year_counts.plot(kind="bar", color="#55A868")
    plt.title("Studies per Year")
    plt.ylabel("Number of Studies")
    plt.xlabel("Year")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "studies_per_year.png", dpi=300)
    plt.close()

    # Plot quality score distribution.
    plt.figure(figsize=(8, 5))
    overall_scores.plot(kind="hist", bins=8, color="#C44E52", edgecolor="black")
    plt.title("Quality Scores Distribution")
    plt.xlabel("Total Score (0-8)")
    plt.ylabel("Number of Studies")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "quality_scores_distribution.png", dpi=300)
    plt.close()


if __name__ == "__main__":
    main()
