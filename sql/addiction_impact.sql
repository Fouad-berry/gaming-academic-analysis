-- addiction_impact.sql
-- Impact of gaming addiction score on academic and wellbeing metrics.

SELECT
    addiction_level,
    COUNT(*)                                AS student_count,
    ROUND(AVG(grades), 2)                   AS avg_grades,
    ROUND(AVG(gaming_hours), 2)             AS avg_gaming_hours,
    ROUND(AVG(study_hours), 2)              AS avg_study_hours,
    ROUND(AVG(sleep_hours), 2)              AS avg_sleep,
    ROUND(AVG(attendance), 2)               AS avg_attendance,
    ROUND(AVG(reaction_time_ms), 1)         AS avg_reaction_ms,
    ROUND(AVG(social_activity), 2)          AS avg_social,
    ROUND(AVG(stress_encoded), 2)           AS avg_stress_score
FROM gaming_students
GROUP BY addiction_level
ORDER BY addiction_level;

-- Stress level distribution within each addiction tier
SELECT
    addiction_level,
    stress_level,
    COUNT(*)                                AS student_count,
    ROUND(AVG(grades), 2)                   AS avg_grades
FROM gaming_students
GROUP BY addiction_level, stress_level
ORDER BY addiction_level, stress_level;