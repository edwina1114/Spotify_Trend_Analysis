# 🎵 Spotify Trend Analysis Dashboard

This project combines **exploratory data analysis (EDA)** and an **interactive Streamlit dashboard** to explore global music trends based on Spotify song data from Kaggle.

It analyzes changes in music features over time, language shifts, and compares the musical characteristics of **K-pop**, **Hindi music**, and **popular vs non-popular songs**.

> 📁 **Dataset Source**: [Spotify Tracks Dataset (Updated every week)
](https://www.kaggle.com/datasets/gauthamvijayaraj/spotify-tracks-dataset-updated-every-week)

---

## 🌍 Live Demo

> 👉 [Open the dashboard](https://spotifytrendanalysis-mcvc9zrf5bbua8mvkfgpj9.streamlit.app/)

---

## 📁 Project Structure

| Path                | Description |
|---------------------|-------------|
| `.devcontainer/`     | (Optional) VSCode Dev Container setup (if used) |
| `app/`              | Streamlit dashboard app (see details below) |
| `notebooks/`        | Jupyter notebook for Kaggle-style EDA |
| `README.md`         | Project documentation |
| `requirements.txt`  | For pip or Streamlit Cloud deployment |
| `environment.yml`   | Conda environment file (for local or Docker setup) |

### 📂 Inside `app/`

| Subpath            | Description |
|--------------------|-------------|
| `Home.py`          | Dashboard entry point |
| `pages/`           | Subpages for each analysis part (K-pop, language trends, popularity, etc.) |
| `utils/`           | Modular functions: chart creation, feature diff logic, data loader |
| `data/` (optional) | Dataset folder if you're loading local CSVs |
| `config.py` (optional) | App-wide constants (e.g., color mapping, thresholds) |


---

## 📊 Features

### 🔍 EDA Highlights ([`spotify-popular-track.ipynb`](notebooks/spotify-popular-track.ipynb))
- Handled missing values, normalization
- Music trends Analysis by language and year
- Feature differences during the rise of **Hindi music (2007)** and **K-pop (2014+)**
- Comparative analysis of **popular vs non-popular songs** in Recent 5 Years

### 🖥️ Interactive Dashboard via Streamlit ([`app`](app))
- **Overall Language Distribution of Songs** (Pie Chart)
- **Music Feature Trends Over Time** (Line Chart)
- **Language Popularity Trends Over Time** (Line Chart)
- **Hindi vs Other Genres** (Bar + Radar Chart)
- **K-pop vs Other Genres** (Pie + Bar + Radar Chart)
- **Popular vs Non-Popular Songs** (Feature Differences, Bar + Radar Chart)

---

##  🧠 Relevant Skills & Techniques

- Python for data cleaning, transformation, outlier handling, feature engineering
- Plotly for rich interactive charting
- Streamlit for lightweight web app development
- GitHub project structuring & documentation
- Kaggle-based exploratory development
  
---

## 🚀 How to Run Locally

```bash
### ▶️ Option 1: With pip (recommended for Streamlit)
pip install -r requirements.txt
streamlit run app/Home.py

###▶️ Option 2: With conda
conda env create -f environment.yml
conda activate streamlit_practice
streamlit run app/Home.py
```

