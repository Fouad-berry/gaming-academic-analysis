-- genre_analysis.sql
-- Performance and habit differences across gaming genres.

SELECT
    gaming_genre,
    gender,
    COUNT(*)                                AS student_count,
    ROUND(AVG(grades), 2)                   AS avg_grades,
    ROUND(AVG(gaming_hours), 2)             AS avg_gaming_hours,
    ROUND(AVG(study_hours), 2)              AS avg_study_hours,
    ROUND(AVG(addiction_score), 2)          AS avg_addiction,
    ROUND(AVG(reaction_time_ms), 1)         AS avg_reaction_ms,
    ROUND(AVG(social_activity), 2)          AS avg_social_activity,
    ROUND(AVG(attendance), 2)               AS avg_attendance
FROM gaming_students
GROUP BY gaming_genre, gender
ORDER BY gaming_genre, gender;

-- Genre × stress level
SELECT
    gaming_genre,
    stress_level,
    COUNT(*)                                AS student_count,
    ROUND(AVG(grades), 2)                   AS avg_grades
FROM gaming_students
GROUP BY gaming_genre, stress_level
ORDER BY gaming_genre,
         CASE stress_level WHEN 'Low' THEN 1 WHEN 'Medium' THEN 2 ELSE 3 END;