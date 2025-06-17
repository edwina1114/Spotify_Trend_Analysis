# 🎵 Spotify Trend Analysis Dashboard

This project combines **exploratory data analysis (EDA)** and an **interactive Streamlit dashboard** to explore global music trends using Spotify track data from Kaggle.

It analyzes how music features have changed over time, tracks the rise of genres like **Hindi music** and **K-pop**, and compares the musical characteristics of **popular vs non-popular songs** in recent years.

> 📁 **Dataset Source**:  
> [Spotify Tracks Dataset (Updated Weekly) – by Gautham Vijayaraj](https://www.kaggle.com/datasets/gauthamvijayaraj/spotify-tracks-dataset-updated-every-week)

---

## 🌐 Live Demo

👉 [Open the Dashboard](https://spotifytrendanalysis-mcvc9zrf5bbua8mvkfgpj9.streamlit.app/)

---

## 📁 Project Structure

| Path               | Description |
|--------------------|-------------|
| `.devcontainer/`   | (Optional) VSCode Dev Container setup |
| `app/`             | Streamlit dashboard (main logic, pages, and utils) |
| `notebooks/`       | Jupyter notebook for Kaggle-style EDA |
| `README.md`        | Project documentation (you’re reading it!) |
| `requirements.txt` | Pip-based dependency file for Streamlit Cloud |
| `environment.yml`  | Conda environment for local or Docker-based deployment |

### 📂 Inside `app/`

| Subpath            | Description |
|--------------------|-------------|
| `Home.py`          | Dashboard entry point |
| `pages/`           | Multi-page dashboard sections (K-pop, language, popularity, etc.) |
| `utils/`           | Modular functions: data loader, chart builder, feature diff logic |
| `data/` *(optional)* | Local dataset folder (if applicable) |
| `config.py` *(optional)* | App-wide constants (color mapping) |

---

## 📊 Features

### 🔍 EDA Highlights ([`spotify-popular-track.ipynb`](notebooks/spotify-popular-track.ipynb))
- Handled missing values, outliers and normalization
- Trend analysis by language and release year
- Identified music feature shifts during the rise of **Hindi music (2007)** and **K-pop (2014+)**
- Compared **popular vs non-popular** songs based on music features in Recent 5 Years (2018–2023)

### 🖥️ Streamlit Dashboard ([`app/`](app))
- Language Distribution of Songs (Pie Chart)
- Music Feature Trends Over Time (Line Chart)
- Language Popularity Trends (Line Chart)
- Hindi Music vs Others (Bar + Radar Chart)
- K-pop vs Others (Pie + Bar + Radar Chart)
- Popular vs Non-Popular Songs (Bar + Radar Chart)

---

## 🧠 Relevant Skills & Techniques

- **Python**: data cleaning, transformation, outlier handling, feature engineering
- **Plotly**: interactive charting (pie, bar, line, radar)
- **Streamlit**: rapid dashboard development with multi-page layout
- **Jupyter Notebook**: exploratory analysis and hypothesis generation
- **Modular Programming**: reusable charting and feature comparison functions
- **Version Control**: GitHub project organization and documentation

---

## 🚀 How to Run Locally

### ▶️ Option 1: Pip (recommended for Streamlit Cloud)
```bash
pip install -r requirements.txt
streamlit run app/Home.py
```

### ▶️ Option 2: With conda
```bash
conda env create -f environment.yml
conda activate streamlit_practice
streamlit run app/Home.py
```

