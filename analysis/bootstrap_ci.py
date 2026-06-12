"""Compute bootstrap confidence intervals for reported study performance.

Uses only NumPy and the Python standard library for bootstrap calculations.
"""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data" / "included_studies.csv"
OUTPUT_PATH = ROOT / "results" / "bootstrap_confidence_intervals.csv"


def _parse_rows(path: Path) -> list[dict[str, str]]:
    """Load CSV rows as dictionaries."""
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _to_float(value: str) -> float | None:
    """Convert a value to float when possible, otherwise return None."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _bootstrap_ci(values: np.ndarray, n_iter: int = 10_000, seed: int = 42) -> tuple[float, float, float]:
    """Return mean and percentile bootstrap 95% confidence interval."""
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, len(values), size=(n_iter, len(values)))
    sampled_means = values[indices].mean(axis=1)
    return float(values.mean()), float(np.percentile(sampled_means, 2.5)), float(np.percentile(sampled_means, 97.5))


def main() -> None:
    """Run bootstrap analysis and save summary table."""
    rows = _parse_rows(INPUT_PATH)

    overall_values = [
        score for score in (_to_float(row.get("Key_Result", "")) for row in rows) if score is not None
    ]
    if not overall_values:
        raise ValueError("No numeric values found in Key_Result.")

    results: list[dict[str, object]] = []

    overall_array = np.array(overall_values, dtype=float)
    mean_value, ci_low, ci_high = _bootstrap_ci(overall_array)
    results.append(
        {
            "Group": "All Studies",
            "N": len(overall_array),
            "Mean_Best_Performance": round(mean_value, 4),
            "CI95_Lower": round(ci_low, 4),
            "CI95_Upper": round(ci_high, 4),
        }
    )

    # Compute per-domain bootstrap intervals.
    by_domain: dict[str, list[float]] = {}
    for row in rows:
        score = _to_float(row.get("Key_Result", ""))
        domain = row.get("Domain", "Unknown")
        if score is None:
            continue
        by_domain.setdefault(domain, []).append(score)

    for domain, values in sorted(by_domain.items()):
        arr = np.array(values, dtype=float)
        mean_value, ci_low, ci_high = _bootstrap_ci(arr)
        results.append(
            {
                "Group": domain,
                "N": len(arr),
                "Mean_Best_Performance": round(mean_value, 4),
                "CI95_Lower": round(ci_low, 4),
                "CI95_Upper": round(ci_high, 4),
            }
        )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["Group", "N", "Mean_Best_Performance", "CI95_Lower", "CI95_Upper"],
        )
        writer.writeheader()
        writer.writerows(results)

    print("Bootstrap confidence intervals saved to", OUTPUT_PATH)
    for row in results:
        print(row)


if __name__ == "__main__":
    main()
