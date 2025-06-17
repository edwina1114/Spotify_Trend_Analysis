import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.config import language_color_map


def apply_transparent_plotly_layout(fig):
    """套用透明背景與一致樣式設定至 Plotly 圖表。"""
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor="rgba(0,0,0,0)"),
    )
    return fig


def display_chart(fig):
    st.plotly_chart(fig, use_container_width=True)


def create_pie_chart(df, names, values, color_base, title):
    fig = px.pie(
        df,
        names=names,
        values=values,
        color=color_base,
        color_discrete_map=language_color_map,
        title=title,
    )
    fig.update_traces(textinfo="label+percent")
    fig.update_layout(showlegend=False)
    fig = apply_transparent_plotly_layout(fig)
    return fig


def create_line_chart(df, x_col, y_col, color_base, title):
    fig = px.line(
        df,
        x=x_col,
        y=y_col,
        color=color_base,
        color_discrete_map=language_color_map,
        title=title,
        labels={x_col: x_col.capitalize(), y_col: y_col.capitalize()},
    )

    fig = apply_transparent_plotly_layout(fig)
    return fig


def create_bar_chart(df, x_col, y_col, color_base, title):
    fig = px.bar(
        df,
        x=x_col,
        y=y_col,
        color=color_base,
        color_discrete_map=language_color_map,
        title=title,
        labels={x_col: x_col.capitalize(), y_col: y_col.capitalize()},
    )

    fig.update_traces(texttemplate="%{y}", textposition="outside")
    fig.update_layout(showlegend=False)
    fig = apply_transparent_plotly_layout(fig)
    return fig


def create_feature_bar_chart(
    diff, diff_threshold, bar_title, bar_main_color, bar_secondary_color
):
    """建立特徵差異長條圖"""
    color_map = {"highlight": bar_main_color, "neutral": bar_secondary_color}

    fig = px.bar(
        diff,
        x="diff",
        y="feature",
        color="color",
        orientation="h",
        color_discrete_map=color_map,
        labels={"diff": "Difference", "feature": "Feature"},
        title=bar_title,
    )

    fig.add_vline(
        x=diff_threshold,
        line_dash="dash",
        line_color="blue",
        annotation_text=f"Mean diff: {diff_threshold:.3f}",
    )
    fig.update_layout(showlegend=False)

    return fig


def create_feature_radar_chart(
    diff,
    diff_threshold,
    group1_avg,
    group2_avg,
    group1_name,
    group2_name,
    radar_title,
    radar_main_color,
    radar_line_color,
):
    """建立特徵雷達圖"""
    # 找出突出特徵
    outstanding_features = diff[diff["diff"] > diff_threshold]["feature"].tolist()

    if not outstanding_features:
        fig = go.Figure()
        fig.update_layout(title=f"{radar_title} (無突出特徵)")
        return fig

    group1_values = group1_avg.loc[outstanding_features]
    group2_values = group2_avg.loc[outstanding_features]

    fig = go.Figure()

    # 添加第一組軌跡
    fig.add_trace(
        go.Scatterpolar(
            r=group1_values.values,
            theta=group1_values.index,
            fill="toself",
            name=group1_name,
            fillcolor=radar_main_color,
            line=dict(color=radar_line_color),
            marker=dict(size=6),
        )
    )

    # 添加第二組軌跡
    fig.add_trace(
        go.Scatterpolar(
            r=group2_values.values,
            theta=group2_values.index,
            fill="toself",
            name=group2_name,
            fillcolor="rgba(17, 12, 15, 0.25)",
            line=dict(color="rgba(17, 12, 15, 0.5)"),
            marker=dict(size=6),
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, tickvals=[0.2, 0.4, 0.6, 0.8, 1.0]),
            angularaxis=dict(
                tickfont=dict(size=12), rotation=90, direction="clockwise"
            ),
        ),
        showlegend=True,
        title=dict(text=radar_title, font=dict(size=16)),
    )

    return fig
