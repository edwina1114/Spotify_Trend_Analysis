import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_music_data
from utils.chart_base import (
    display_chart,
    create_line_chart,
)

st.title("📈 Language Popularity Trends in Global Music")
st.markdown(
    """
This section explores how different song languages have trended in popularity over the years.
"""
)

# Line Plot: Popularity by Year and Language
df = load_music_data()

popularity_year_language = (
    df.groupby(["year", "language"])["popularity"].mean().reset_index()
)

fig = create_line_chart(
    popularity_year_language,
    x_col="year",
    y_col="popularity",
    color_base="language",
    title="Popularity by Year and Language",
)
display_chart(fig)

st.header("📊 Key Insights from Language Popularity Trends")

st.subheader("🇬🇧 1. Early Dominance of English Songs")
st.markdown(
    """
- English songs led in the early years.
- May reflect Spotify's early catalog bias.
"""
)

st.subheader("🇮🇳 2. Sharp Rise of Hindi Music in 2007")
st.markdown(
    """
- Hindi tracks peaked in 2007.
- Likely boosted by Bollywood hits.
"""
)

st.subheader("🌍 3. Decline in English Popularity")
st.markdown(
    """
- English remains common but less dominant.
- Other languages gained visibility over time.
"""
)

st.subheader("🎤 4. Rise of K-pop After 2014")
st.markdown(
    """
- K-pop surged after 2014.
- Fewer tracks, but high impact and popularity.
"""
)
