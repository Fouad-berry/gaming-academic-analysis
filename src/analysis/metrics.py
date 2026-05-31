"""
metrics.py
----------
Compute KPIs and aggregated tables for Looker export.
"""

import logging
from pathlib import Path

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger(__name__)

PROCESSED_PATH = Path(__file__).parents[2] / "data" / "processed" / "gaming_clean.csv"
EXPORTS_DIR    = Path(__file__).parents[2] / "data" / "exports"


def load_processed() -> pd.DataFrame:
    return pd.read_csv(PROCESSED_PATH)


# ─── KPI helpers ──────────────────────────────────────────────────────────────

def avg_grades(df: pd.DataFrame) -> float:
    return round(df["grades"].mean(), 2)


def avg_gaming_hours(df: pd.DataFrame) -> float:
    return round(df["gaming_hours"].mean(), 2)


def pct_high_addiction(df: pd.DataFrame) -> float:
    return round((df["addiction_level"].isin(["High", "Severe"])).mean() * 100, 2)


def correlation_gaming_grades(df: pd.DataFrame) -> float:
    return round(df["gaming_hours"].corr(df["grades"]), 3)


def correlation_study_grades(df: pd.DataFrame) -> float:
    return round(df["study_hours"].corr(df["grades"]), 3)


# ─── Aggregated export tables ─────────────────────────────────────────────────

def agg_by_genre(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("gaming_genre")
        .agg(
            avg_grades=("grades", "mean"),
            avg_gaming_hours=("gaming_hours", "mean"),
            avg_study_hours=("study_hours", "mean"),
            avg_addiction=("addiction_score", "mean"),
            avg_reaction_time=("reaction_time_ms", "mean"),
            avg_attendance=("attendance", "mean"),
            student_count=("student_id", "count"),
        )
        .round(2)
        .reset_index()
    )


def agg_by_stress(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("stress_level")
        .agg(
            avg_grades=("grades", "mean"),
            avg_gaming_hours=("gaming_hours", "mean"),
            avg_study_hours=("study_hours", "mean"),
            avg_sleep_hours=("sleep_hours", "mean"),
            avg_attendance=("attendance", "mean"),
            student_count=("student_id", "count"),
        )
        .round(2)
        .reset_index()
    )


def agg_by_addiction_level(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("addiction_level", observed=True)
        .agg(
            avg_grades=("grades", "mean"),
            avg_gaming_hours=("gaming_hours", "mean"),
            avg_study_hours=("study_hours", "mean"),
            avg_attendance=("attendance", "mean"),
            avg_sleep=("sleep_hours", "mean"),
            avg_social=("social_activity", "mean"),
            student_count=("student_id", "count"),
        )
        .round(2)
        .reset_index()
    )


def agg_by_gaming_intensity(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("gaming_intensity", observed=True)
        .agg(
            avg_grades=("grades", "mean"),
            avg_study_hours=("study_hours", "mean"),
            avg_sleep=("sleep_hours", "mean"),
            avg_attendance=("attendance", "mean"),
            avg_addiction=("addiction_score", "mean"),
            avg_reaction_time=("reaction_time_ms", "mean"),
            student_count=("student_id", "count"),
        )
        .round(2)
        .reset_index()
    )


def agg_by_gender_genre(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["gender", "gaming_genre"])
        .agg(
            avg_grades=("grades", "mean"),
            avg_gaming_hours=("gaming_hours", "mean"),
            avg_addiction=("addiction_score", "mean"),
            student_count=("student_id", "count"),
        )
        .round(2)
        .reset_index()
    )


def agg_by_sleep_quality(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("sleep_quality", observed=True)
        .agg(
            avg_grades=("grades", "mean"),
            avg_gaming_hours=("gaming_hours", "mean"),
            avg_stress=("stress_encoded", "mean"),
            avg_reaction_time=("reaction_time_ms", "mean"),
            student_count=("student_id", "count"),
        )
        .round(2)
        .reset_index()
    )


def agg_grade_distribution(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["grade_tier", "gaming_genre"], observed=True)
        .agg(student_count=("student_id", "count"))
        .reset_index()
    )


# ─── Main ─────────────────────────────────────────────────────────────────────

def run_all():
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    df = load_processed()

    tables = {
        "agg_genre.csv":            agg_by_genre(df),
        "agg_stress.csv":           agg_by_stress(df),
        "agg_addiction_level.csv":  agg_by_addiction_level(df),
        "agg_gaming_intensity.csv": agg_by_gaming_intensity(df),
        "agg_gender_genre.csv":     agg_by_gender_genre(df),
        "agg_sleep_quality.csv":    agg_by_sleep_quality(df),
        "agg_grade_dist.csv":       agg_grade_distribution(df),
    }

    for fname, table in tables.items():
        path = EXPORTS_DIR / fname
        table.to_csv(path, index=False)
        log.info(f"Exported {fname} ({len(table)} rows) → {path}")

    print("\n" + "=" * 42)
    print("📊  KEY METRICS SUMMARY")
    print("=" * 42)
    print(f"Students analysed:          {len(df):>8,}")
    print(f"Avg grades:                 {avg_grades(df):>8.2f}")
    print(f"Avg gaming hours/day:       {avg_gaming_hours(df):>8.2f}h")
    print(f"High/Severe addiction:      {pct_high_addiction(df):>7.1f}%")
    print(f"Corr gaming ↔ grades:       {correlation_gaming_grades(df):>8.3f}")
    print(f"Corr study  ↔ grades:       {correlation_study_grades(df):>8.3f}")


if __name__ == "__main__":
    run_all()