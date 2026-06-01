# Looker Studio Setup Guide

---

## Option A — Looker Studio (free, via Google)

### Steps

1. **Run the pipeline:**
   ```bash
   python src/transformation/clean_transform.py
   python src/analysis/metrics.py
   ```

2. **Upload to Google Sheets:**  
   Upload `data/exports/gaming_looker.csv` and the `agg_*.csv` files to a Google Drive folder.

3. **Open Looker Studio** → [lookerstudio.google.com](https://lookerstudio.google.com)

4. **Create a new report** → Add data source → Google Sheets → select your file.

5. **Suggested pages:**

| Page | Primary source | Charts |
|---|---|---|
| Student Overview | `gaming_looker.csv` | Scorecards, grade distribution, genre comparison |
| Gaming Habits | `agg_gaming_intensity.csv` | Bar: intensity vs grades, donut: genres |
| Addiction & Stress | `agg_addiction_level.csv` | Bar: addiction vs grades, stacked stress |
| Sleep & Wellness | `agg_sleep_quality.csv` | Line: sleep vs grades, reaction time |
| Correlations | `gaming_looker.csv` | Scatter: study_hours vs grades, gaming vs attendance |

---

## Option B — Looker (enterprise) via BigQuery

### 1. Load data into BigQuery

```python
from google.cloud import bigquery
import pandas as pd

client = bigquery.Client(project="your-project")
df = pd.read_csv("data/processed/gaming_clean.csv")

job = client.load_table_from_dataframe(
    df,
    "your-project.gaming_academic.gaming_students",
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE"),
)
job.result()
print("Loaded", job.output_rows, "rows")
```

### 2. Connect Looker
- Admin → Connections → New → BigQuery
- Set connection name to `gaming_academic_bq`
- Deploy the `looker/` folder to your Looker project

---

## Key Metrics to Build

| Metric | Formula |
|---|---|
| Avg grades | AVG(grades) |
| Avg gaming hours | AVG(gaming_hours) |
| Study/gaming ratio | AVG(study_gaming_ratio) |
| Addiction rate (High+Severe) | COUNT WHERE addiction_level IN ('High','Severe') / total |
| Avg reaction time | AVG(reaction_time_ms) |
| Sleep adequacy rate | COUNT WHERE sleep_quality = 'Adequate' / total |