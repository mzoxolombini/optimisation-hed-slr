"""Perform sensitivity analysis for domain-level SLR statistics.

Scenarios:
1) Exclude low-quality studies.
2) Exclude studies before 2018.
3) Exclude studies without baseline comparisons.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
INCLUDED_PATH = ROOT / "data" / "included_studies.csv"
QUALITY_PATH = ROOT / "data" / "quality_assessment.csv"
OUTPUT_PATH = ROOT / "results" / "sensitivity_analysis.csv"


def _domain_summary(df: pd.DataFrame, scenario: str) -> pd.DataFrame:
    """Compute domain-level counts and means for a given filtered dataframe."""
    summary = (
        df.groupby("Domain")
        .agg(
            Study_Count=("Study_ID", "count"),
            Mean_Quality=("Total_Score (0-8)", "mean"),
            Mean_Key_Result=("Key_Result", "mean"),
        )
        .reset_index()
    )
    summary.insert(0, "Scenario", scenario)
    return summary


def main() -> None:
    """Run all sensitivity scenarios and save comparison output."""
    included_df = pd.read_csv(INCLUDED_PATH)
    quality_df = pd.read_csv(QUALITY_PATH)

    included_df["Key_Result"] = pd.to_numeric(included_df["Key_Result"], errors="coerce")

    merged = included_df.merge(quality_df, on="Study_ID", how="left")

    scenarios: list[tuple[str, pd.DataFrame]] = [
        ("All studies", merged),
        ("Exclude Quality_Band=Low", merged[merged["Quality_Band (High/Medium/Low)"] != "Low"]),
        ("Exclude Year<2018", merged[merged["Year"] >= 2018]),
        ("Exclude Q5_Baseline_Comparison=0", merged[merged["Q5_Baseline_Comparison"] > 0]),
    ]

    frames = [_domain_summary(frame.copy(), name) for name, frame in scenarios]
    result_df = pd.concat(frames, ignore_index=True)
    result_df[["Mean_Quality", "Mean_Key_Result"]] = result_df[["Mean_Quality", "Mean_Key_Result"]].round(3)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    result_df.to_csv(OUTPUT_PATH, index=False)

    print("Sensitivity analysis written to", OUTPUT_PATH)
    print(result_df.to_string(index=False))


if __name__ == "__main__":
    main()
