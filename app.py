import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="CBAM Supply Chain Dashboard",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# Design system
# -----------------------------

BACKGROUND = "#F3F7FA"
CARD = "#FFFFFF"
TEXT = "#243044"
MUTED = "#7A8494"
GRID = "#E9EEF5"

ROUTE_COLORS = {
    "R1": "#4D7CFE",
    "R2": "#38E0B0",
    "R3": "#8B7CFF",
    "R4": "#FF9F43",
    "R5": "#FF5FA2",
}

COST_COLORS = {
    "Production Cost": "#4D7CFE",
    "Logistics Cost": "#38E0B0",
    "CBAM Cost": "#FF9F43",
    "생산비": "#4D7CFE",
    "물류비": "#38E0B0",
    "CBAM 비용": "#FF9F43",
}

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: #F3F7FA;
    }

    [data-testid="stHeader"] {
        background: rgba(243, 247, 250, 0);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1280px;
    }

    section[data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 1px solid #E9EEF5;
    }

    h1, h2, h3 {
        color: #243044;
        letter-spacing: -0.03em;
    }

    .hero-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FBFF 100%);
        border: 1px solid #E9EEF5;
        border-radius: 26px;
        padding: 30px 34px;
        box-shadow: 0 18px 45px rgba(120, 140, 170, 0.16);
        margin-bottom: 20px;
    }

    .hero-title {
        font-size: 42px;
        line-height: 1.08;
        font-weight: 800;
        color: #243044;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 17px;
        color: #7A8494;
        margin-bottom: 20px;
    }

    .hero-body {
        font-size: 15.5px;
        line-height: 1.72;
        color: #3A4658;
    }

    .metric-card {
        background: #FFFFFF;
        border: 1px solid #E9EEF5;
        border-radius: 22px;
        padding: 22px 24px;
        box-shadow: 0 16px 38px rgba(120, 140, 170, 0.14);
        min-height: 145px;
    }

    .metric-label {
        font-size: 13px;
        font-weight: 700;
        color: #7A8494;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 10px;
    }

    .metric-value {
        font-size: 30px;
        font-weight: 800;
        color: #243044;
        margin-bottom: 8px;
    }

    .metric-caption {
        font-size: 14px;
        color: #7A8494;
        line-height: 1.45;
    }

    .section-card {
        background: #FFFFFF;
        border: 1px solid #E9EEF5;
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 18px 42px rgba(120, 140, 170, 0.13);
        margin-top: 18px;
        margin-bottom: 18px;
    }

    .section-title {
        font-size: 23px;
        font-weight: 800;
        color: #243044;
        margin-bottom: 6px;
    }

    .section-subtitle {
        font-size: 14px;
        color: #7A8494;
        margin-bottom: 14px;
    }

    .route-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
        gap: 14px;
        margin-top: 18px;
    }

    .route-card {
        background: #FFFFFF;
        border: 1px solid #E9EEF5;
        border-radius: 18px;
        padding: 15px 16px;
        margin-bottom: 12px;
        box-shadow: 0 12px 30px rgba(120, 140, 170, 0.12);
    }

    .route-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 6px;
    }

    .route-id {
        font-size: 16px;
        font-weight: 800;
        color: #243044;
    }

    .route-flags {
        font-size: 18px;
    }

    .route-name {
        font-size: 14px;
        color: #3A4658;
        margin-bottom: 8px;
    }

    .route-meta {
        font-size: 12.5px;
        color: #7A8494;
        line-height: 1.5;
    }

    .note-box {
        background: #F8FBFF;
        border: 1px solid #E9EEF5;
        border-radius: 18px;
        padding: 14px 16px;
        color: #607086;
        font-size: 13.5px;
        line-height: 1.6;
        margin-top: 12px;
    }

    div[data-testid="stMetric"] {
        background: #FFFFFF;
        border-radius: 18px;
        padding: 16px;
        border: 1px solid #E9EEF5;
        box-shadow: 0 12px 30px rgba(120, 140, 170, 0.12);
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Data
# -----------------------------

df = pd.read_csv("data.csv")

# -----------------------------
# Sidebar controls
# -----------------------------

st.sidebar.title("Scenario Controls / 시나리오 설정")

language = st.sidebar.radio(
    "Language / 언어",
    ["English", "Korean"]
)

if language == "English":
    title = "CBAM Supply Chain Optimisation Dashboard"
    subtitle = "Carbon cost as a strategic variable in EU market entry"

    scenario_note = """
    This project explores how the EU Carbon Border Adjustment Mechanism (CBAM) could turn embedded emissions into a measurable supply chain cost.

    Using a hypothetical Korean EV battery components firm, the dashboard compares five possible supply chain routes for aluminium battery enclosure components entering the EU market. Each route is evaluated by production cost, logistics cost, embedded emissions, lead time, and risk.

    The figures used in this analysis are simplified assumptions for scenario comparison. They do not represent confidential company-level data.
    """

    carbon_price_slider_label = "Carbon price (USD per tCO2e)"
    logistics_slider_label = "Logistics cost increase (%)"
    emission_slider_label = "Emission reduction (%)"
    risk_slider_label = "Risk penalty weight"
    lead_time_slider_label = "Lead time penalty weight"

    carbon_metric_label = "Carbon Price"
    best_cost_label = "Lowest Final Cost Route"
    best_strategy_label = "Recommended Strategic Route"
    route_map_title = "World Supply Chain Route Map"
    route_map_subtitle = "Simplified scenario routes connecting production and market-entry points"
    final_cost_chart_title = "Final Cost by Supply Chain Route"
    breakdown_chart_title = "Cost Breakdown by Route"
    sensitivity_chart_title = "Carbon Price Sensitivity"
    table_title = "Route Ranking Table"
    data_note = "Data & Assumptions"

    route_label = "Route"
    final_cost_label = "Final Cost (USD)"
    cost_label = "Cost (USD)"
    cost_type_label = "Cost Type"
    carbon_price_label = "Carbon Price (USD per tCO2e)"

    map_note = "The map shows simplified scenario routes for visual comparison, not exact real-world shipping paths."

    tab_cost = "Cost Comparison"
    tab_breakdown = "Cost Breakdown"
    tab_sensitivity = "Carbon Sensitivity"
    tab_table = "Route Ranking"
    tab_data = "Data & Assumptions"

    cost_type_map = {
        "production_cost": "Production Cost",
        "adjusted_logistics_cost": "Logistics Cost",
        "cbam_cost": "CBAM Cost"
    }

    formula_text = """
    **Model Formula**

    Final Cost = Production Cost + Adjusted Logistics Cost + CBAM Cost

    CBAM Cost = Adjusted Embedded Emissions x Carbon Price

    Strategic Score = Final Cost + Risk Penalty + Lead Time Penalty

    ---

    **Important Note**

    This project uses a fact-based hypothetical scenario. Cost, emissions, lead time, and risk values are simplified assumptions created for scenario comparison and strategic analysis.
    """

else:
    title = "CBAM 공급망 최적화 대시보드"
    subtitle = "탄소비용을 EU 시장 진입 전략의 핵심 변수로 분석한 공급망 시나리오 대시보드"

    scenario_note = """
    이 프로젝트는 EU 탄소국경조정제도(CBAM)가 탄소 배출량을 어떻게 실제 공급망 비용으로 바꿀 수 있는지 분석한다.

    가상의 한국 EV 배터리 부품 기업을 설정하고, 알루미늄 배터리 외장 부품이 EU 시장에 진입하는 다섯 가지 공급망 경로를 비교했다. 각 경로는 생산비, 물류비, 내재 탄소배출량, 리드타임, 위험도를 기준으로 평가된다.

    이 분석에 사용된 수치는 경로 비교를 위한 단순화된 가정값이며, 실제 기업의 비공개 데이터를 의미하지 않는다.
    """

    carbon_price_slider_label = "탄소가격 (USD/tCO2e)"
    logistics_slider_label = "물류비 증가율 (%)"
    emission_slider_label = "배출량 감축률 (%)"
    risk_slider_label = "위험도 가중치"
    lead_time_slider_label = "리드타임 가중치"

    carbon_metric_label = "탄소가격"
    best_cost_label = "최종 비용 기준 최저 비용 경로"
    best_strategy_label = "전략 기준 추천 경로"
    route_map_title = "세계 공급망 경로 지도"
    route_map_subtitle = "생산 거점과 EU 시장 진입 경로를 단순화하여 시각화한 지도"
    final_cost_chart_title = "공급망 경로별 최종 비용"
    breakdown_chart_title = "경로별 비용 구조"
    sensitivity_chart_title = "탄소가격 변화에 따른 비용 민감도"
    table_title = "공급망 경로 순위표"
    data_note = "데이터 및 가정"

    route_label = "경로"
    final_cost_label = "최종 비용 (USD)"
    cost_label = "비용 (USD)"
    cost_type_label = "비용 유형"
    carbon_price_label = "탄소가격 (USD/tCO2e)"

    map_note = "이 지도는 실제 운송 경로가 아니라, 시나리오 비교를 위한 단순화된 경로 시각화입니다."

    tab_cost = "비용 비교"
    tab_breakdown = "비용 구조"
    tab_sensitivity = "탄소가격 민감도"
    tab_table = "경로 순위표"
    tab_data = "데이터 및 가정"

    cost_type_map = {
        "production_cost": "생산비",
        "adjusted_logistics_cost": "물류비",
        "cbam_cost": "CBAM 비용"
    }

    formula_text = """
    **계산 방식**

    최종 비용 = 생산비 + 조정된 물류비 + CBAM 비용

    CBAM 비용 = 조정된 내재 탄소배출량 x 탄소가격

    전략 점수 = 최종 비용 + 위험도 패널티 + 리드타임 패널티

    ---

    **데이터 사용 기준**

    이 프로젝트는 사실 기반의 가상 시나리오를 사용한다. 비용, 배출량, 리드타임, 위험도 수치는 경로 비교와 전략 분석을 위해 단순화한 가정값이다.
    """

carbon_price = st.sidebar.slider(
    carbon_price_slider_label,
    min_value=0,
    max_value=200,
    value=80,
    step=10
)

logistics_increase = st.sidebar.slider(
    logistics_slider_label,
    min_value=0,
    max_value=50,
    value=0,
    step=5
)

emission_reduction = st.sidebar.slider(
    emission_slider_label,
    min_value=0,
    max_value=40,
    value=0,
    step=5
)

risk_weight = st.sidebar.slider(
    risk_slider_label,
    min_value=0,
    max_value=100,
    value=20,
    step=5
)

lead_time_weight = st.sidebar.slider(
    lead_time_slider_label,
    min_value=0,
    max_value=20,
    value=2,
    step=1
)

# -----------------------------
# Calculations
# -----------------------------

df["adjusted_logistics_cost"] = df["logistics_cost"] * (1 + logistics_increase / 100)
df["adjusted_emissions"] = df["embedded_emissions"] * (1 - emission_reduction / 100)
df["cbam_cost"] = df["adjusted_emissions"] * carbon_price

df["final_cost"] = (
    df["production_cost"]
    + df["adjusted_logistics_cost"]
    + df["cbam_cost"]
)

df["strategic_score"] = (
    df["final_cost"]
    + df["risk_score"] * risk_weight
    + df["lead_time"] * lead_time_weight
)

best_cost_route = df.loc[df["final_cost"].idxmin()]
recommended_strategy_route = df.loc[df["strategic_score"].idxmin()]


# -----------------------------
# Helper functions
# -----------------------------

def format_money(value):
    return f"${value:,.0f}"


def scenario_to_html(text):
    paragraphs = [p.strip() for p in text.strip().split("\n\n") if p.strip()]
    return "".join([f"<p>{p}</p>" for p in paragraphs])


def style_plotly_figure(fig, height=470):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#FFFFFF",
        font=dict(family="Arial", color=TEXT, size=13),
        title=dict(
            font=dict(size=21, color=TEXT),
            x=0.02,
            xanchor="left",
            y=0.98,
            yanchor="top"
        ),
        margin=dict(l=35, r=30, t=95, b=105),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.20,
            xanchor="center",
            x=0.5,
            font=dict(size=12, color=MUTED)
        ),
        hoverlabel=dict(
            bgcolor="#FFFFFF",
            font_size=13,
            font_family="Arial",
            font_color=TEXT
        )
    )
    fig.update_xaxes(
        showgrid=False,
        linecolor=GRID,
        tickfont=dict(color=MUTED)
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor=GRID,
        zerolinecolor=GRID,
        tickfont=dict(color=MUTED)
    )
    return fig


# -----------------------------
# Hero section
# -----------------------------

st.markdown(
    f"""
    <div class="hero-card">
        <div class="hero-title">{title}</div>
        <div class="hero-subtitle">{subtitle}</div>
        <div class="hero-body">{scenario_to_html(scenario_note)}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# KPI cards
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="metric-card" style="border-top: 5px solid #4D7CFE;">
            <div class="metric-label">{carbon_metric_label}</div>
            <div class="metric-value">${carbon_price}/tCO2e</div>
            <div class="metric-caption">Current carbon price scenario</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="metric-card" style="border-top: 5px solid #38E0B0;">
            <div class="metric-label">{best_cost_label}</div>
            <div class="metric-value">{best_cost_route["route_id"]}</div>
            <div class="metric-caption">{best_cost_route["route_name"]}<br>{format_money(best_cost_route["final_cost"])}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="metric-card" style="border-top: 5px solid #FF5FA2;">
            <div class="metric-label">{best_strategy_label}</div>
            <div class="metric-value">{recommended_strategy_route["route_id"]}</div>
            <div class="metric-caption">{recommended_strategy_route["route_name"]}<br>Score: {recommended_strategy_route["strategic_score"]:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Route map
# -----------------------------

locations = {
    "China": {"lat": 35.8617, "lon": 104.1954, "label": "🇨🇳 China"},
    "Vietnam": {"lat": 14.0583, "lon": 108.2772, "label": "🇻🇳 Vietnam"},
    "Korea": {"lat": 35.9078, "lon": 127.7669, "label": "🇰🇷 Korea"},
    "India": {"lat": 20.5937, "lon": 78.9629, "label": "🇮🇳 India"},
    "Germany/EU": {"lat": 51.1657, "lon": 10.4515, "label": "🇩🇪 Germany/EU"},
    "EU": {"lat": 50.8503, "lon": 4.3517, "label": "🇪🇺 EU Market"},
}

route_paths = {
    "R1": ["China", "Korea", "EU"],
    "R2": ["Vietnam", "Korea", "EU"],
    "R3": ["Korea", "EU"],
    "R4": ["India", "Korea", "EU"],
    "R5": ["Germany/EU", "EU"],
}

route_flags = {
    "R1": "🇨🇳 → 🇰🇷 → 🇪🇺",
    "R2": "🇻🇳 → 🇰🇷 → 🇪🇺",
    "R3": "🇰🇷 → 🇪🇺",
    "R4": "🇮🇳 → 🇰🇷 → 🇪🇺",
    "R5": "🇩🇪 → 🇪🇺",
}

fig_map = go.Figure()

for _, row in df.iterrows():
    route_id = row["route_id"]
    path = route_paths[route_id]
    lats = [locations[p]["lat"] for p in path]
    lons = [locations[p]["lon"] for p in path]

    fig_map.add_trace(
        go.Scattergeo(
            lon=lons,
            lat=lats,
            mode="lines",
            line=dict(
                width=7,
                color=ROUTE_COLORS[route_id]
            ),
            opacity=0.20,
            hoverinfo="skip",
            showlegend=False
        )
    )

    fig_map.add_trace(
        go.Scattergeo(
            lon=lons,
            lat=lats,
            mode="lines",
            line=dict(
                width=3,
                color=ROUTE_COLORS[route_id]
            ),
            opacity=0.95,
            name=f"{route_id}: {row['route_name']}",
            hovertemplate=(
                f"<b>{route_id}: {row['route_name']}</b><br>"
                f"Final Cost: {format_money(row['final_cost'])}<br>"
                f"Emissions: {row['adjusted_emissions']:.2f} tCO2e<br>"
                f"Risk Score: {row['risk_score']}<br>"
                "<extra></extra>"
            )
        )
    )

node_names = list(locations.keys())
fig_map.add_trace(
    go.Scattergeo(
        lon=[locations[n]["lon"] for n in node_names],
        lat=[locations[n]["lat"] for n in node_names],
        text=[locations[n]["label"] for n in node_names],
        mode="markers+text",
        marker=dict(
            size=12,
            color="#FFFFFF",
            line=dict(width=3, color="#4D7CFE")
        ),
        textposition="top center",
        textfont=dict(size=13, color=TEXT),
        hovertemplate="<b>%{text}</b><extra></extra>",
        showlegend=False
    )
)

fig_map.update_layout(
    height=540,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="#FFFFFF",
    margin=dict(l=0, r=0, t=10, b=0),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.06,
        xanchor="center",
        x=0.5,
        font=dict(size=11, color=MUTED)
    ),
    geo=dict(
        projection_type="natural earth",
        showland=True,
        landcolor="#EAF1F7",
        showocean=True,
        oceancolor="#F8FBFF",
        showcountries=True,
        countrycolor="#FFFFFF",
        showcoastlines=False,
        bgcolor="rgba(0,0,0,0)",
        lataxis_showgrid=False,
        lonaxis_showgrid=False
    )
)

st.markdown(
    f"""
    <div class="section-card">
        <div class="section-title">{route_map_title}</div>
        <div class="section-subtitle">{route_map_subtitle}</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.plotly_chart(fig_map, use_container_width=True)

route_cards_html = '<div class="route-grid">'

for _, row in df.sort_values("route_id").iterrows():
    route_id = row["route_id"]

    route_cards_html += f"""
    <div class="route-card" style="border-left: 6px solid {ROUTE_COLORS[route_id]};">
        <div class="route-top">
            <div class="route-id">{route_id}</div>
            <div class="route-flags">{route_flags[route_id]}</div>
        </div>
        <div class="route-name">{row["route_name"]}</div>
        <div class="route-meta">
            Final Cost: <b>{format_money(row["final_cost"])}</b><br>
            Emissions: <b>{row["adjusted_emissions"]:.2f} tCO2e</b><br>
            Risk: <b>{row["risk_score"]}</b> · Lead Time: <b>{row["lead_time"]} days</b>
        </div>
    </div>
    """

route_cards_html += "</div>"

st.markdown(route_cards_html, unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="note-box">{map_note}</div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Charts and table
# -----------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [tab_cost, tab_breakdown, tab_sensitivity, tab_table, tab_data]
)

with tab1:
    fig_final = px.bar(
        df.sort_values("final_cost"),
        x="route_name",
        y="final_cost",
        color="route_id",
        text="final_cost",
        title=final_cost_chart_title,
        color_discrete_map=ROUTE_COLORS,
        labels={
            "route_name": route_label,
            "final_cost": final_cost_label,
            "route_id": "Route ID"
        }
    )

    fig_final.update_traces(
        texttemplate="%{text:.0f}",
        textposition="outside",
        marker_line_width=0,
        opacity=0.95
    )

    fig_final.update_layout(
        xaxis_tickangle=-25,
        showlegend=False
    )

    fig_final = style_plotly_figure(fig_final, height=500)

    st.plotly_chart(fig_final, use_container_width=True)

with tab2:
    breakdown_df = df[
        [
            "route_name",
            "production_cost",
            "adjusted_logistics_cost",
            "cbam_cost"
        ]
    ].melt(
        id_vars="route_name",
        var_name="cost_type",
        value_name="cost"
    )

    breakdown_df["cost_type"] = breakdown_df["cost_type"].map(cost_type_map)

    fig_breakdown = px.bar(
        breakdown_df,
        x="route_name",
        y="cost",
        color="cost_type",
        title=breakdown_chart_title,
        color_discrete_map=COST_COLORS,
        labels={
            "route_name": route_label,
            "cost": cost_label,
            "cost_type": cost_type_label
        }
    )

    fig_breakdown.update_traces(
        marker_line_width=0,
        opacity=0.95
    )

    fig_breakdown.update_layout(
        xaxis_tickangle=-25,
        barmode="stack"
    )

    fig_breakdown = style_plotly_figure(fig_breakdown, height=500)

    st.plotly_chart(fig_breakdown, use_container_width=True)

with tab3:
    carbon_prices = np.arange(0, 210, 10)
    sensitivity_rows = []

    for price in carbon_prices:
        temp = df.copy()
        temp["sensitivity_final_cost"] = (
            temp["production_cost"]
            + temp["adjusted_logistics_cost"]
            + temp["adjusted_emissions"] * price
        )
        temp["carbon_price"] = price
        sensitivity_rows.append(
            temp[
                [
                    "route_id",
                    "route_name",
                    "carbon_price",
                    "sensitivity_final_cost"
                ]
            ]
        )

    sensitivity_df = pd.concat(sensitivity_rows)

    fig_sensitivity = go.Figure()

    for route_id, route_data in sensitivity_df.groupby("route_id"):
        route_name = route_data["route_name"].iloc[0]

        fig_sensitivity.add_trace(
            go.Scatter(
                x=route_data["carbon_price"],
                y=route_data["sensitivity_final_cost"],
                mode="lines",
                line=dict(
                    color=ROUTE_COLORS[route_id],
                    width=9
                ),
                opacity=0.18,
                hoverinfo="skip",
                showlegend=False
            )
        )

        fig_sensitivity.add_trace(
            go.Scatter(
                x=route_data["carbon_price"],
                y=route_data["sensitivity_final_cost"],
                mode="lines+markers",
                line=dict(
                    color=ROUTE_COLORS[route_id],
                    width=3
                ),
                marker=dict(
                    size=6,
                    color="#FFFFFF",
                    line=dict(width=2, color=ROUTE_COLORS[route_id])
                ),
                name=f"{route_id}: {route_name}",
                hovertemplate=(
                    f"<b>{route_id}: {route_name}</b><br>"
                    f"{carbon_price_label}: %{{x}}<br>"
                    f"{final_cost_label}: $%{{y:,.0f}}"
                    "<extra></extra>"
                )
            )
        )

    fig_sensitivity.update_layout(
        title=sensitivity_chart_title,
        xaxis_title=carbon_price_label,
        yaxis_title=final_cost_label
    )

    fig_sensitivity = style_plotly_figure(fig_sensitivity, height=500)

    st.plotly_chart(fig_sensitivity, use_container_width=True)

with tab4:
    st.subheader(table_title)

    ranking_df = df[
        [
            "route_id",
            "route_name",
            "route_type",
            "production_cost",
            "adjusted_logistics_cost",
            "adjusted_emissions",
            "cbam_cost",
            "final_cost",
            "risk_score",
            "lead_time",
            "strategic_score"
        ]
    ].sort_values("strategic_score")

    display_df = ranking_df.copy()
    numeric_cols = [
        "production_cost",
        "adjusted_logistics_cost",
        "adjusted_emissions",
        "cbam_cost",
        "final_cost",
        "strategic_score"
    ]

    for col in numeric_cols:
        display_df[col] = display_df[col].round(2)

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

with tab5:
    st.subheader(data_note)
    st.markdown(formula_text)
