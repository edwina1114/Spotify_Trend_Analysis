import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_music_data
from utils.chart_base import display_chart, create_pie_chart
from utils.feature_diff import language_feature_diff

st.title("📈 Rise of K-pop After 2014 and Its Musical Features")
st.markdown(
    """
After 2014, K-pop rose to global prominence, becoming one of the most popular music genres—despite having fewer tracks than other languages.
This section analyzes the music features of K-pop and compares them to tracks in other languages released after 2014, the turning point in K-pop's global expansion.
"""
)

# Load the dataset
df = load_music_data()
numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns

# ---- 分析段落 1：Filter for songs released after 2014 ----
st.header("📊 Distribution of Songs by Language after 2014")

kpop_2014 = df[(df["year"] >= 2014) & (df["language"] != "Unknown")]
kpop_2014_count = kpop_2014["language"].value_counts().reset_index()

fig = create_pie_chart(
    kpop_2014_count,
    names="language",
    values="count",
    color_base="language",
    title="Overall Language Distribution of Songs After 2014",
)
display_chart(fig)

st.markdown(
    """
While **Korean songs (K-pop)** account for only **17.6%** of the dataset, their **cultural footprint is massive**.

- K-pop artists dominate global streaming charts.
- Despite not being the most common language, K-pop has reshaped global pop trends.
- This illustrates how **niche genres with strong fanbases** can outperform more common ones in influence.

"""
)

st.divider()

## ---- 分析段落 2：Highlight Key Differences in Hindi Music Features ----
st.header("🎯 Highlight Key Differences in Kpop Music Features")

bar_fig, radar_fig = language_feature_diff(
    kpop_2014,
    numerical_columns,
    "Korean",
    "Differences of K-pop Compare to Others After 2014",
    "Outstanding Music Features: K-pop vs Others",
    "rgba(255, 52, 120, 1)",
    "rgba(247, 193, 211, 1)",
    "rgba(255, 52, 120, 0.5)",
    "rgba(255, 52, 120, 1)",
)
display_chart(bar_fig)
display_chart(radar_fig)
# Radar chart of outstanding features
# bar_fig, radar_fig = language_feature_diff(
#     kpop_2014,
#     numerical_columns,
#     "Korean",
#     "Differences of K-pop Compare to Others After 2014",
#     "Outstanding Music Features: K-pop vs Others",
#     "rgba(255, 52, 120, 1)",
#     "rgba(247, 193, 211, 1)",
#     "rgba(255, 52, 120, 0.5)",
#     "rgba(255, 52, 120, 1)",
# )

# bar_fig = apply_transparent_plotly_layout(bar_fig)
# radar_fig = apply_transparent_plotly_layout(radar_fig)
# st.plotly_chart(bar_fig, use_container_width=True)
# st.plotly_chart(radar_fig, use_container_width=True)


st.header("📊 Key Insights")
st.subheader("⚡ 1. High Energy and Electronic Production")
st.markdown(
    """
- Top in `Energy`: K-pop tracks generally exhibit the highest energy levels across all languages. This creates a dynamic and powerful sound — ideal for choreographed performances and high-impact visuals.

- Low `Acousticness`: The relatively low acousticness indicates strong reliance on electronic production and studio effects, rather than traditional acoustic instruments.
"""
)

st.subheader("🎭 2. Designed for Performance and Stage Presence")
st.markdown(
    """
- High `Liveness`: K-pop shows a distinct focus on liveness, reflecting the genre’s strong connection to live performances, TV shows, and real-time fan events.

- Visual-Performance Synergy: This emphasis on live appeal sets K-pop apart from many genres that prioritize polished studio recordings over interactive or performative elements.
"""
)
