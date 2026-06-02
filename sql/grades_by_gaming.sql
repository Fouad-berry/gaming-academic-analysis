-- grades_by_gaming.sql
-- How do gaming hours and intensity relate to academic performance?

-- 1. Avg grades by gaming intensity bucket
SELECT
    gaming_intensity,
    COUNT(*)                                AS student_count,
    ROUND(AVG(grades), 2)                   AS avg_grades,
    ROUND(AVG(study_hours), 2)              AS avg_study_hours,
    ROUND(AVG(attendance), 2)               AS avg_attendance,
    ROUND(AVG(sleep_hours), 2)              AS avg_sleep,
    ROUND(AVG(addiction_score), 2)          AS avg_addiction
FROM gaming_students
GROUP BY gaming_intensity
ORDER BY gaming_intensity;

-- 2. Grade tier breakdown by gaming genre
SELECT
    gaming_genre,
    grade_tier,
    COUNT(*)                                AS student_count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY gaming_genre), 2) AS pct_in_genre
FROM gaming_students
GROUP BY gaming_genre, grade_tier
ORDER BY gaming_genre, grade_tier;

-- 3. Top vs bottom quartile gamers — academic comparison
SELECT
    CASE
        WHEN gaming_hours <= PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY gaming_hours)
             OVER ()  THEN 'Q1 — Lowest 25% gamers'
        WHEN gaming_hours >= PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY gaming_hours)
             OVER ()  THEN 'Q4 — Top 25% gamers'
        ELSE 'Middle 50%'
    END                                     AS gamer_quartile,
    COUNT(*)                                AS student_count,
    ROUND(AVG(grades), 2)                   AS avg_grades,
    ROUND(AVG(study_hours), 2)              AS avg_study_hours,
    ROUND(AVG(attendance), 2)               AS avg_attendance
FROM gaming_students
GROUP BY gamer_quartile
ORDER BY avg_grades DESC;