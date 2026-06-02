-- create_tables.sql
-- DDL for DuckDB (local) or BigQuery.
-- DuckDB: duckdb gaming.duckdb < sql/create_tables.sql

CREATE TABLE IF NOT EXISTS gaming_students (
    student_id          INTEGER,
    age                 INTEGER,
    gender              VARCHAR,
    gaming_hours        DOUBLE,
    study_hours         DOUBLE,
    sleep_hours         DOUBLE,
    attendance          DOUBLE,
    gaming_genre        VARCHAR,
    social_activity     DOUBLE,
    device_usage        DOUBLE,
    reaction_time_ms    DOUBLE,
    addiction_score     DOUBLE,
    stress_level        VARCHAR,
    grades              DOUBLE,
    -- Engineered
    grade_tier          VARCHAR,
    addiction_level     VARCHAR,
    gaming_intensity    VARCHAR,
    sleep_quality       VARCHAR,
    age_group           VARCHAR,
    study_gaming_ratio  DOUBLE,
    total_screen_hours  DOUBLE,
    stress_encoded      INTEGER,
    PRIMARY KEY (student_id)
);

-- Load from processed CSV (DuckDB syntax)
-- COPY gaming_students FROM 'data/processed/gaming_clean.csv' (HEADER TRUE);