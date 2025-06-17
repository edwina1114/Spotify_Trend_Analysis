import pandas as pd
import streamlit as st
import os
from pathlib import Path


@st.cache_data
def load_music_data():
    """載入音樂資料，支援多種路徑配置"""
    possible_paths = [
        "data/Spotify_Normalized.csv",
        "./data/Spotify_Normalized.csv",
        os.path.join(os.path.dirname(__file__), "../data/Spotify_Normalized.csv"),
    ]

    for path in possible_paths:
        if os.path.exists(path):
            try:
                df = pd.read_csv(path)
                return df
            except Exception as e:
                st.error(f"載入資料時發生錯誤: {e}")
                return None

    st.error("找不到資料檔案，請確認 data/Spotify_Normalized.csv 存在")
    return None
