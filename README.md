# 🎮 Gaming & Academic Performance — Data Analysis Project

End-to-end data analysis pipeline exploring the relationship between gaming habits and student academic performance, with Python ETL, SQL analytics, and Looker Studio dashboards.

---

## 📁 Project Structure

```
gaming-academic-analysis/
│
├── data/
│   ├── raw/                              # Original CSV (do not modify)
│   ├── processed/                        # Cleaned & feature-engineered data
│   └── exports/                          # Aggregated CSVs ready for Looker
│
├── notebooks/
│   ├── 01_exploration.ipynb              # EDA — distributions, nulls, correlations
│   ├── 02_cleaning.ipynb                 # Cleaning walkthrough
│   └── 03_analysis.ipynb                 # Business insights & visualisations
│
├── sql/
│   ├── create_tables.sql                 # DDL for DuckDB / BigQuery
│   ├── grades_by_gaming.sql              # Grades vs gaming hours
│   ├── addiction_impact.sql              # Addiction score breakdowns
│   ├── genre_analysis.sql                # Performance by gaming genre
│   └── sleep_stress_grades.sql           # Sleep & stress vs academic output
│
├── src/
│   ├── ingestion/load_data.py            # Load & validate raw CSV
│   ├── transformation/clean_transform.py # Cleaning + feature engineering
│   └── analysis/metrics.py              # KPI computation + export tables
│
├── looker/
│   ├── models/gaming_academic.model.lkml
│   ├── views/gaming_academic.view.lkml
│   ├── explores/gaming_explore.lkml
│   └── dashboards/student_overview.dashboard.lookml
│
├── docs/
│   ├── data_dictionary.md                # Column descriptions & types
│   └── looker_setup.md                   # Connect Looker to this project
│
├── .github/workflows/ci.yml              # Lint + tests on push
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🗂️ Dataset

**File:** `data/raw/gaming_academic_performance.csv`
**Rows:** 8 000 | **Columns:** 14
**Subjects:** Students aged 16–24

| Column | Type | Description |
|---|---|---|
| `student_id` | int | Unique identifier |
| `age` | int | Age of the student (16–24) |
| `gender` | str | Male / Female / Other |
| `gaming_hours` | float | Daily gaming hours |
| `study_hours` | float | Daily study hours |
| `sleep_hours` | float | Daily sleep hours |
| `attendance` | float | Attendance rate % |
| `gaming_genre` | str | FPS / RPG / Casual |
| `social_activity` | float | Social activity score (0–10) |
| `device_usage` | float | Daily device usage (hours) |
| `reaction_time_ms` | float | Reaction time in ms |
| `addiction_score` | float | Gaming addiction score |
| `stress_level` | str | Low / Medium / High |
| `grades` | float | Final academic grade (0–100) |

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/gaming-academic-analysis.git
cd gaming-academic-analysis
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the pipeline
```bash
python src/transformation/clean_transform.py
python src/analysis/metrics.py
```

### 5. Explore notebooks
```bash
jupyter lab
```

---

## 📊 Looker Studio Dashboards

See [`docs/looker_setup.md`](docs/looker_setup.md) for full connection instructions.

| Dashboard | Key charts |
|---|---|
| 🎓 Student Overview | Grade distribution, avg grades by genre, stress vs grades |
| 🎮 Gaming Habits | Hours by genre, addiction score distribution, device usage |
| 😴 Sleep & Wellness | Sleep hours vs grades, stress levels, reaction time |
| 📈 Correlation Explorer | Study hours vs grades, gaming vs attendance, multi-scatter |

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.11 |
| Data manipulation | pandas, numpy |
| Visualisation | matplotlib, seaborn, plotly |
| SQL analytics | DuckDB (local) / BigQuery (cloud) |
| BI / Dashboards | Looker Studio |
| CI | GitHub Actions |

---

## 📄 License

Réalisé par Fouad MOUTAIROU

MIT