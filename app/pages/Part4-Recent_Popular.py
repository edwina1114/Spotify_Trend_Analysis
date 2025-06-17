import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from utils.data_loader import load_music_data
from utils.chart_base import (
    display_chart,
    create_feature_bar_chart,
    create_feature_radar_chart,
)


st.title("📈 Characteristics of Recent Popular Songs (2018–2023)")
st.markdown(
    """
This section analyzes the top 5% most popular tracks between 2018 and 2023 and compared their musical features with all other songs during the same period.
"""
)

# Load the dataset
df = load_music_data()
numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns

# Filter for songs released in recent years (2018–2023)
recent_years = df[(df["year"] >= 2018) & (df["language"] != "Unknown")]
# Calculate the popularity threshold for the top 5%
threshold = recent_years["popularity"].quantile(0.95)

# Separate popular and non-popular tracks
popular_tracks = recent_years[recent_years["popularity"] >= threshold]
non_popular_tracks = recent_years[recent_years["popularity"] < threshold]

feature_cols = [col for col in numerical_columns if col not in ["popularity", "year"]]
popular_avg = popular_tracks[feature_cols].mean()
non_popular_avg = non_popular_tracks[feature_cols].mean()

feature_diff = (popular_avg - non_popular_avg).abs().sort_values().reset_index()
feature_diff.columns = ["feature", "diff"]
diff_avg = feature_diff["diff"].mean()

# Add color category
feature_diff["color"] = feature_diff["diff"].apply(
    lambda x: "highlight" if x > diff_avg else "neutral"
)

bar_fig = create_feature_bar_chart(
    feature_diff,
    diff_avg,
    "Differences of Popular Songs Compared to Non-Popular Songs in Recent Years",
    "rgba(255, 197, 0, 1)",
    "rgba(239, 222, 167, 1)",
)
display_chart(bar_fig)

radar_fig = create_feature_radar_chart(
    feature_diff,
    diff_avg,
    popular_avg,
    non_popular_avg,
    "Popular",
    "Non-Popular",
    "Outstanding Music Features: Popular vs Non-Popular",
    "rgba(255, 197, 0, 0.5)",
    "rgba(255, 197, 0, 1)",
)
display_chart(radar_fig)

st.header("📊 Key Insights")
st.subheader("🔥 1. More Danceable, More Energetic")
st.markdown(
    """
- High `Danceability` & `Energy`: Popular tracks tend to have significantly higher danceability and energy, suggesting a strong preference for rhythmic and upbeat music.

- This aligns with current streaming and short-form content trends (e.g., TikTok), where catchy, performance-ready music thrives.
"""
)

st.subheader("🎸 2. Less Acoustic, Less Instrumental")
st.markdown(
    """
- Low `Acousticness` & `Instrumentalness`: Popular songs show noticeably lower values in these features, indicating fewer traditional or acoustic elements and a strong tilt toward electronic production.

- These results reflect the dominance of studio-produced pop, hip-hop, and dance genres in recent years.
"""
)
