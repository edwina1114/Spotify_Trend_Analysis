import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_music_data
from utils.chart_base import display_chart, create_bar_chart
from utils.feature_diff import (
    language_feature_diff,
)

st.title("📈 Sharp Rise of Hindi Music in 2007")
st.markdown(
    """
This section explores the musical characteristics of Hindi tracks and compared them with other languages released in 2007 which was the year Hindi songs experienced a dramatic surge in popularity.
"""
)

# Load the dataset
df = load_music_data()
numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns

# ---- 分析段落 1：Filter for songs released in 2007 ----
st.header("📊 Distribution of Songs by Language in 2007")

sp_2007 = df[(df["language"] != "Unknown") & (df["year"] == 2007)]
sp_2007_count = sp_2007["language"].value_counts().reset_index()

# Bar chart for language distribution in 2007
fig = create_bar_chart(
    sp_2007_count,
    x_col="language",
    y_col="count",
    color_base="language",
    title="Overall Language Distribution of Songs in 2007",
)
display_chart(fig)

st.markdown(
    """     
In 2007, Hindi songs achieved unprecedented popularity despite <span style="color:	#FF0000"> only three songs </span>
being in the dataset compared to 344 English songs. 
<span style="color:	#FF0000"> This success highlights the cultural power of Bollywood, 
as all three songs were tied to blockbuster films. </span>
Their immense popularity, driven by the success of these movies and 
the growing accessibility of online music platforms, 
<b> marked a pivotal moment when Bollywood's influence expanded beyond India. </b>
""",
    unsafe_allow_html=True,
)

st.divider()

## ---- 分析段落 2：Highlight Key Differences in Hindi Music Features ----
st.header("🎯 Highlight Key Differences in Hindi Music Features")

bar_fig, radar_fig = language_feature_diff(
    sp_2007,
    numerical_columns,
    "Hindi",
    "Differences of Hindi Compare to Others in 2007",
    "Outstanding Music Features: Hindi vs Others",
    "rgba(247, 128, 9, 1)",
    "rgba(255, 239, 184, 1)",
    "rgba(247, 128, 9, 0.5)",
    "rgba(247, 128, 9, 1)",
)
display_chart(bar_fig)
display_chart(radar_fig)

st.header("📊 Key Insights")
st.subheader("🎵 1. Energetic and Upbeat Style")
st.markdown(
    """
- High `Danceability` & `Valence` Lead: Hindi tracks had significantly higher danceability and valence than other languages in 2007.

- Bollywood Influence: This reflects Bollywood’s tradition of using lively, rhythmic music that emphasizes joy and entertainment — often tied to dance-heavy film sequences.
"""
)

st.subheader("🎛️ 2. Simpler Musical Structure")
st.markdown(
    """
- Low `Liveness` & `Mode`: Hindi songs showed lower liveness and mode values, suggesting a focus on studio production rather than live performance elements.

- Minor Tonality Preference: Despite their energetic feel, the lower mode scores may indicate more frequent use of minor keys, adding emotional depth beneath the upbeat rhythm.
"""
)
