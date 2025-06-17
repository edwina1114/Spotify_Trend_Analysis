from .chart_base import create_feature_bar_chart, create_feature_radar_chart


def calculate_language_feature_diff(df, col, language):
    """計算指定語言與其他語言的特徵差異"""
    # 計算各語言特徵平均值
    lang_stats = df.groupby("language")[col].mean()
    if "year" in lang_stats.columns:
        lang_stats = lang_stats.drop("year", axis=1)

    # 計算目標語言與其他語言的差異
    lang_avg = lang_stats.loc[language]
    others_avg = lang_stats.drop(language).mean()

    # 建立差異 DataFrame
    diff = (lang_avg - others_avg).abs().sort_values().reset_index()
    diff.columns = ["feature", "diff"]
    diff_threshold = diff["diff"].mean()

    # 添加顏色分類
    diff["color"] = diff["diff"].apply(
        lambda x: "highlight" if x > diff_threshold else "neutral"
    )

    return diff, diff_threshold, lang_avg, others_avg


def language_feature_diff(
    df,
    col,
    language,
    bar_title,
    radar_title,
    bar_main_color,
    bar_secondary_color,
    radar_main_color,
    radar_line_color,
):
    """分析語言特徵差異並建立長條圖和雷達圖（適用於 part2, part3）"""
    # 計算差異
    diff, diff_threshold, lang_avg, others_avg = calculate_language_feature_diff(
        df, col, language
    )

    # 建立圖表
    bar_fig = create_feature_bar_chart(
        diff, diff_threshold, bar_title, bar_main_color, bar_secondary_color
    )
    radar_fig = create_feature_radar_chart(
        diff,
        diff_threshold,
        lang_avg,
        others_avg,
        language,
        "Others",
        radar_title,
        radar_main_color,
        radar_line_color,
    )

    return bar_fig, radar_fig
