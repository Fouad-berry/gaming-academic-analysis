# Data Dictionary

## Source: `gaming_academic_performance.csv`

8 000 rows · 14 raw columns + 8 engineered columns

---

### Raw columns

| Column | Type | Range / Values | Description |
|---|---|---|---|
| `student_id` | int | 1 – 8 000 | Unique student identifier |
| `age` | int | 16 – 24 | Age of the student |
| `gender` | str | Male / Female / Other | Gender identity |
| `gaming_hours` | float | 0 – 24 | Average daily gaming hours |
| `study_hours` | float | 0 – 24 | Average daily study hours |
| `sleep_hours` | float | 0 – 24 | Average daily sleep hours |
| `attendance` | float | 0 – 100 | Class attendance rate % |
| `gaming_genre` | str | FPS / RPG / Casual | Primary gaming genre |
| `social_activity` | float | 0 – 10 | Social engagement score |
| `device_usage` | float | 0 – 24 | Daily device (non-gaming) usage hours |
| `reaction_time_ms` | float | ms | Average reaction time in milliseconds |
| `addiction_score` | float | 0 – 25 | Gaming addiction score |
| `stress_level` | str | Low / Medium / High | Self-reported stress level |
| `grades` | float | 0 – 100 | Final academic grade (clipped to 100) |

---

### Engineered columns (added in `clean_transform.py`)

| Column | Type | Bins / Values | Description |
|---|---|---|---|
| `grade_tier` | str | Failing / Below Average / Average / Good / Excellent | Grade bucket (0–40 / 40–55 / 55–70 / 70–85 / 85–100) |
| `addiction_level` | str | Minimal / Moderate / High / Severe | Addiction bucket (0–5 / 5–10 / 10–15 / 15+) |
| `gaming_intensity` | str | Light / Casual / Moderate / Heavy | Gaming hours bucket |
| `sleep_quality` | str | Poor / Insufficient / Adequate / Oversleeping | Sleep hours bucket |
| `age_group` | str | 16-17 / 18-19 / 20-21 / 22-24 | Age bracket |
| `study_gaming_ratio` | float | — | `study_hours / (gaming_hours + 1)` — balance proxy |
| `total_screen_hours` | float | — | `gaming_hours + device_usage` |
| `stress_encoded` | int | 1 / 2 / 3 | Low=1, Medium=2, High=3 (for ordering in Looker) |