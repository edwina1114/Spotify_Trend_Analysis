# 🎵 Spotify Trend Analysis Dashboard

This project combines **exploratory data analysis (EDA)** and an **interactive Streamlit dashboard** to explore global music trends based on Spotify song data from Kaggle.

It analyzes changes in music features over time, language shifts, and compares the musical characteristics of **K-pop**, **Hindi music**, and **popular vs non-popular songs**.

> 📁 **Dataset Source**: [Spotify Tracks Dataset (Updated every week)
](https://www.kaggle.com/datasets/gauthamvijayaraj/spotify-tracks-dataset-updated-every-week)

---

## 🌍 Live Demo

> 👉 [Open the dashboard](https://spotifytrendanalysis-mcvc9zrf5bbua8mvkfgpj9.streamlit.app/)

---

## 📌 Project Structure

| Component      | Description |
|----------------|-------------|
| `notebooks/`   | Jupyter notebook with full EDA on Kaggle |
| `app/`         | Streamlit dashboard with multi-page design |
| `utils/`       | Modular code: data loader, chart builders, feature analysis |
| `requirements.txt` | For deployment on Streamlit Cloud |
| `environment.yml` | Conda environment file (for local or Docker-based deployment) |
| `README.md`    | Project documentation (you’re reading it!) |

---

## 📊 Features

### 🔍 EDA Highlights ([`spotify-popular-track.ipynb`](notebooks/spotify-popular-track.ipynb))
- Handled missing values, normalization
- Language trends Analysis
- Feature differences during the rise of **Hindi music (2007)** and **K-pop (2014+)**
- Comparative analysis of **popular vs non-popular songs**

### 🖥️ Streamlit Dashboard ([`app`](app))
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
git clone https://github.com/your-username/Spotify_Trend_Analysis.git
cd Spotify_Trend_Analysis
pip install -r requirements.txt
streamlit run app/Home.py
