"""
clean_transform.py
------------------
Clean the raw dataset and engineer features for analysis.
"""

import logging
from pathlib import Path

import numpy as np
import pandas as pd

from src.ingestion.load_data import load_raw

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger(__name__)

PROCESSED_PATH = Path(__file__).parents[2] / "data" / "processed" / "gaming_clean.csv"
EXPORT_PATH    = Path(__file__).parents[2] / "data" / "exports"   / "gaming_looker.csv"


def clean(df: pd.DataFrame) -> pd.DataFrame:
    log.info("Cleaning data …")
    df = df.copy()

    # Standardise strings
    for col in ["gender", "gaming_genre", "stress_level"]:
        df[col] = df[col].str.strip().str.title()

    # Clip grades to [0, 100] — dataset contains a few values above 100
    df["grades"] = df["grades"].clip(0, 100)

    # Clip hours to non-negative
    for col in ["gaming_hours", "study_hours", "sleep_hours", "device_usage"]:
        df[col] = df[col].clip(lower=0)

    # Clip attendance to [0, 100]
    df["attendance"] = df["attendance"].clip(0, 100)

    # Clip addiction_score to [0, 25] (dataset min is slightly negative)
    df["addiction_score"] = df["addiction_score"].clip(lower=0)

    log.info("Cleaning done ✓")
    return df


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    log.info("Engineering features …")
    df = df.copy()

    # Grade tier
    df["grade_tier"] = pd.cut(
        df["grades"],
        bins=[0, 40, 55, 70, 85, 100],
        labels=["Failing", "Below Average", "Average", "Good", "Excellent"],
        right=True,
    )

    # Addiction level bucket
    df["addiction_level"] = pd.cut(
        df["addiction_score"],
        bins=[0, 5, 10, 15, 25],
        labels=["Minimal", "Moderate", "High", "Severe"],
        right=True,
    )

    # Gaming intensity (hours per day)
    df["gaming_intensity"] = pd.cut(
        df["gaming_hours"],
        bins=[-0.1, 1, 3, 6, 24],
        labels=["Light (<1h)", "Casual (1-3h)", "Moderate (3-6h)", "Heavy (6h+)"],
    )

    # Sleep quality bucket
    df["sleep_quality"] = pd.cut(
        df["sleep_hours"],
        bins=[0, 5, 7, 9, 24],
        labels=["Poor (<5h)", "Insufficient (5-7h)", "Adequate (7-9h)", "Oversleeping (9h+)"],
    )

    # Balance ratio: study / (gaming + 1) — higher = more study-focused
    df["study_gaming_ratio"] = (df["study_hours"] / (df["gaming_hours"] + 1)).round(3)

    # Total screen time: gaming + device_usage (proxy)
    df["total_screen_hours"] = (df["gaming_hours"] + df["device_usage"]).round(2)

    # Age group
    df["age_group"] = pd.cut(
        df["age"],
        bins=[15, 17, 19, 21, 24],
        labels=["16-17", "18-19", "20-21", "22-24"],
    )

    # Stress encoded (for numeric comparisons)
    stress_map = {"Low": 1, "Medium": 2, "High": 3}
    df["stress_encoded"] = df["stress_level"].map(stress_map)

    log.info("Feature engineering done ✓")
    return df


def save(df: pd.DataFrame) -> None:
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    EXPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(PROCESSED_PATH, index=False)
    log.info(f"Saved processed → {PROCESSED_PATH}")

    export_cols = [c for c in df.columns]
    df[export_cols].to_csv(EXPORT_PATH, index=False)
    log.info(f"Saved Looker export → {EXPORT_PATH}")


def run_pipeline() -> pd.DataFrame:
    df = load_raw()
    df = clean(df)
    df = feature_engineering(df)
    save(df)
    log.info(f"Pipeline complete — {len(df):,} rows ready.")
    return df


if __name__ == "__main__":
    run_pipeline()