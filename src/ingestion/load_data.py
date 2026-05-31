"""
load_data.py
------------
Load and validate the raw Gaming & Academic Performance CSV.
"""

import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger(__name__)

RAW_PATH = Path(__file__).parents[2] / "data" / "raw" / "gaming_academic_performance.csv"

EXPECTED_COLUMNS = [
    "student_id", "age", "gender", "gaming_hours", "study_hours",
    "sleep_hours", "attendance", "gaming_genre", "social_activity",
    "device_usage", "reaction_time_ms", "addiction_score", "stress_level", "grades",
]

DTYPES = {
    "student_id":       int,
    "age":              int,
    "gender":           str,
    "gaming_hours":     float,
    "study_hours":      float,
    "sleep_hours":      float,
    "attendance":       float,
    "gaming_genre":     str,
    "social_activity":  float,
    "device_usage":     float,
    "reaction_time_ms": float,
    "addiction_score":  float,
    "stress_level":     str,
    "grades":           float,
}

VALID_GENDERS  = {"Male", "Female", "Other"}
VALID_GENRES   = {"FPS", "RPG", "Casual"}
VALID_STRESS   = {"Low", "Medium", "High"}


def load_raw(path: Path = RAW_PATH) -> pd.DataFrame:
    """Load the raw CSV and run basic validation."""
    log.info(f"Loading data from {path}")
    df = pd.read_csv(path, dtype=str)

    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")
    df = df[EXPECTED_COLUMNS]

    for col, dtype in DTYPES.items():
        try:
            df[col] = df[col].astype(dtype)
        except Exception as e:
            log.warning(f"Could not cast '{col}' to {dtype}: {e}")

    log.info(f"Loaded {len(df):,} rows × {len(df.columns)} columns")
    _validate(df)
    return df


def _validate(df: pd.DataFrame) -> None:
    null_counts = df.isnull().sum()
    nulls = null_counts[null_counts > 0]
    if not nulls.empty:
        log.warning(f"Null values:\n{nulls}")

    dupes = df["student_id"].duplicated().sum()
    if dupes:
        log.warning(f"{dupes} duplicate student_ids")

    bad_gender = (~df["gender"].isin(VALID_GENDERS)).sum()
    if bad_gender:
        log.warning(f"{bad_gender} unexpected gender values")

    bad_genre = (~df["gaming_genre"].isin(VALID_GENRES)).sum()
    if bad_genre:
        log.warning(f"{bad_genre} unexpected gaming_genre values")

    bad_grades = ((df["grades"] < 0) | (df["grades"] > 100)).sum()
    if bad_grades:
        log.warning(f"{bad_grades} grades outside [0, 100]")

    log.info("Validation complete ✓")


if __name__ == "__main__":
    df = load_raw()
    print(df.head())
    print(df.dtypes)