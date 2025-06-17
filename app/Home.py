import streamlit as st
import plotly.express as px
from utils.data_loader import load_music_data
from utils.chart_base import (
    display_chart,
    create_pie_chart,
    create_line_chart,
)

st.set_page_config(page_title="Music Trends Analysis", layout="wide")

df = load_music_data()

st.title("🎵 Global Music Trends Explorer")
st.caption("📌 Use the left sidebar to navigate different analyses.")

# ---- 分析段落 1：語言分佈 ----
st.header("📊 Distribution of Songs by Language")
st.markdown(
    """
The dataset contains songs from multiple languages:
- **English Tracks Dominate:** English songs make up the largest portion of the dataset (37.5%), reflecting Spotify’s initial catalog and Western music's global reach.
- **K-pop Small but Impactful:** Although Korean songs represent a smaller fraction, they play a major role in global pop culture through the rise of K-pop.
"""
)

# Create a pie chart for language distribution
song_count = df["language"].value_counts().reset_index()
song_count.columns = ["language", "count"]

fig = create_pie_chart(
    song_count,
    names="language",
    values="count",
    color_base="language",
    title="Overall Language Distribution of Songs",
)
display_chart(fig)

# ---- 分析段落 2：時間趨勢 ----
st.header("⏳ Trends in Music Features Over Time")
st.markdown(
    """
- **🎧 Shorter Songs:** Song durations (`duration_ms`) have steadily declined since the 2000s, likely due to streaming and shorter attention spans.
- **💃 More Danceable & Energetic:** `danceability` and `energy` have risen, showing a trend toward upbeat, performance-oriented music.
- **🌫️ Lower Valence:** A drop in `valence` suggests a shift toward more neutral or melancholic tones.
These shifts help explain the rise of genres like K-pop during specific periods.
"""
)

# Create a Line chart with Select Box for Music Features Change Over Years
year_change = df.copy()

if "language" in year_change.columns:
    year_change = year_change.drop("language", axis=1)

yearly_avg = year_change.groupby("year").mean().reset_index()

feature_cols = [
    "duration_ms",
    "danceability",
    "energy",
    "valence",
    "acousticness",
    "instrumentalness",
    "key",
    "liveness",
    "loudness",
    "mode",
    "speechiness",
    "tempo",
    "time_signature",
]
selected_feature = st.selectbox("Choose a music feature to explore:", feature_cols)

fig = create_line_chart(
    yearly_avg,
    "year",
    selected_feature,
    None,
    f"Trend of {selected_feature.capitalize()} Over Time",
)

display_chart(fig)
