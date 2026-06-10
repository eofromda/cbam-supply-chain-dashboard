import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(
page_title=“CBAM Supply Chain Dashboard”,
page_icon=“🌍”,
layout=“wide”
)

df = pd.read_csv(“data.csv”)

st.sidebar.title(“Scenario Controls / 시나리오 설정”)

language = st.sidebar.radio(
“Language / 언어”,
[“English”, “Korean”]
)

if language == “English”:
title = “CBAM Supply Chain Optimisation Dashboard”
subtitle = “A scenario-based analysis of carbon costs and supply chain strategy for EU market entry”

scenario_note = """
This project explores how the EU's Carbon Border Adjustment Mechanism (CBAM) could turn embedded emissions into a measurable supply chain cost.
Using a hypothetical Korean EV battery components firm, the dashboard compares five possible supply chain routes for aluminium battery enclosure components entering the EU market. Each route is evaluated by production cost, logistics cost, embedded emissions, lead time, and risk.
The figures used in this analysis are simplified assumptions for scenario comparison. They do not represent confidential company-level data.
"""
carbon_price_slider_label = "Carbon price (USD per tCO₂e)"
logistics_slider_label = "Logistics cost increase (%)"
emission_slider_label = "Emission reduction (%)"
risk_slider_label = "Risk penalty weight"
lead_time_slider_label = "Lead time penalty weight"
best_cost_label = "Lowest Final Cost Route"
best_strategy_label = "Recommended Strategic Route"
final_cost_chart_title = "Final Cost by Supply Chain Route"
breakdown_chart_title = "Cost Breakdown by Route"
sensitivity_chart_title = "Carbon Price Sensitivity"
table_title = "Route Ranking Table"
data_note = "Data & Assumptions"
route_label = "Route"
final_cost_label = "Final Cost (USD)"
cost_label = "Cost (USD)"
cost_type_label = "Cost Type"
carbon_price_label = "Carbon Price (USD per tCO₂e)"
cost_type_map = {
    "production_cost": "Production Cost",
    "adjusted_logistics_cost": "Logistics Cost",
    "cbam_cost": "CBAM Cost"
}
formula_text = """
**Model Formula**
Final Cost = Production Cost + Adjusted Logistics Cost + CBAM Cost
CBAM Cost = Adjusted Embedded Emissions × Carbon Price
Strategic Score = Final Cost + Risk Penalty + Lead Time Penalty
---
**Important Note**
This project uses a fact-based hypothetical scenario. Cost, emissions, lead time, and risk values are simplified assumptions created for scenario comparison and strategic analysis.
"""

else:
title = “CBAM 공급망 최적화 대시보드”
subtitle = “탄소비용이 EU 시장 진입 전략과 공급망 선택에 미치는 영향을 비교한 시나리오 분석”

scenario_note = """
이 프로젝트는 EU 탄소국경조정제도(CBAM)가 탄소 배출량을 어떻게 실제 공급망 비용으로 바꿀 수 있는지 분석한다.
가상의 한국 EV 배터리 부품 기업을 설정하고, 알루미늄 배터리 외장 부품이 EU 시장에 진입하는 다섯 가지 공급망 경로를 비교했다. 각 경로는 생산비, 물류비, 내재 탄소배출량, 리드타임, 위험도를 기준으로 평가된다.
이 분석에 사용된 수치는 경로 비교를 위한 단순화된 가정값이며, 실제 기업의 비공개 데이터를 의미하지 않는다.
"""
carbon_price_slider_label = "탄소가격 (USD/tCO₂e)"
logistics_slider_label = "물류비 증가율 (%)"
emission_slider_label = "배출량 감축률 (%)"
risk_slider_label = "위험도 가중치"
lead_time_slider_label = "리드타임 가중치"
best_cost_label = "최종 비용 기준 최저 비용 경로"
best_strategy_label = "전략 기준 추천 경로"
final_cost_chart_title = "공급망 경로별 최종 비용"
breakdown_chart_title = "경로별 비용 구조"
sensitivity_chart_title = "탄소가격 변화에 따른 비용 민감도"
table_title = "공급망 경로 순위표"
data_note = "데이터 및 가정"
route_label = "경로"
final_cost_label = "최종 비용 (USD)"
cost_label = "비용 (USD)"
cost_type_label = "비용 유형"
carbon_price_label = "탄소가격 (USD/tCO₂e)"
cost_type_map = {
    "production_cost": "생산비",
    "adjusted_logistics_cost": "물류비",
    "cbam_cost": "CBAM 비용"
}
formula_text = """
**계산 방식**
최종 비용 = 생산비 + 조정된 물류비 + CBAM 비용
CBAM 비용 = 조정된 내재 탄소배출량 × 탄소가격
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

df[“adjusted_logistics_cost”] = df[“logistics_cost”] * (1 + logistics_increase / 100)

df[“adjusted_emissions”] = df[“embedded_emissions”] * (1 - emission_reduction / 100)

df[“cbam_cost”] = df[“adjusted_emissions”] * carbon_price

df[“final_cost”] = (
df[“production_cost”]
+ df[“adjusted_logistics_cost”]
+ df[“cbam_cost”]
)

df[“strategic_score”] = (
df[“final_cost”]
+ df[“risk_score”] * risk_weight
+ df[“lead_time”] * lead_time_weight
)

best_cost_route = df.loc[df[“final_cost”].idxmin()]
recommended_strategy_route = df.loc[df[“strategic_score”].idxmin()]

st.title(title)
st.caption(subtitle)
st.info(scenario_note)

col1, col2, col3 = st.columns(3)

with col1:
st.metric(
label=“Carbon Price”,
value=f”${carbon_price}/tCO₂e”
)

with col2:
st.metric(
label=best_cost_label,
value=best_cost_route[“route_id”]
)
st.write(best_cost_route[“route_name”])

with col3:
st.metric(
label=best_strategy_label,
value=recommended_strategy_route[“route_id”]
)
st.write(recommended_strategy_route[“route_name”])

st.divider()

fig_final = px.bar(
df.sort_values(“final_cost”),
x=“route_name”,
y=“final_cost”,
text=“final_cost”,
title=final_cost_chart_title,
labels={
“route_name”: route_label,
“final_cost”: final_cost_label
}
)

fig_final.update_traces(
texttemplate=”%{text:.0f}”,
textposition=“outside”
)

fig_final.update_layout(
xaxis_tickangle=-30
)

st.plotly_chart(
fig_final,
use_container_width=True
)

breakdown_df = df[
[
“route_name”,
“production_cost”,
“adjusted_logistics_cost”,
“cbam_cost”
]
].melt(
id_vars=“route_name”,
var_name=“cost_type”,
value_name=“cost”
)

breakdown_df[“cost_type”] = breakdown_df[“cost_type”].map(cost_type_map)

fig_breakdown = px.bar(
breakdown_df,
x=“route_name”,
y=“cost”,
color=“cost_type”,
title=breakdown_chart_title,
labels={
“route_name”: route_label,
“cost”: cost_label,
“cost_type”: cost_type_label
}
)

fig_breakdown.update_layout(
xaxis_tickangle=-30
)

st.plotly_chart(
fig_breakdown,
use_container_width=True
)

carbon_prices = np.arange(0, 210, 10)
sensitivity_rows = []

for price in carbon_prices:
temp = df.copy()
temp[“sensitivity_final_cost”] = (
temp[“production_cost”]
+ temp[“adjusted_logistics_cost”]
+ temp[“adjusted_emissions”] * price
)
temp[“carbon_price”] = price
sensitivity_rows.append(
temp[
[
“route_name”,
“carbon_price”,
“sensitivity_final_cost”
]
]
)

sensitivity_df = pd.concat(sensitivity_rows)

fig_sensitivity = px.line(
sensitivity_df,
x=“carbon_price”,
y=“sensitivity_final_cost”,
color=“route_name”,
title=sensitivity_chart_title,
labels={
“carbon_price”: carbon_price_label,
“sensitivity_final_cost”: final_cost_label,
“route_name”: route_label
}
)

st.plotly_chart(
fig_sensitivity,
use_container_width=True
)

st.subheader(table_title)

ranking_df = df[
[
“route_id”,
“route_name”,
“route_type”,
“production_cost”,
“adjusted_logistics_cost”,
“adjusted_emissions”,
“cbam_cost”,
“final_cost”,
“risk_score”,
“lead_time”,
“strategic_score”
]
].sort_values(“strategic_score”)

st.dataframe(
ranking_df,
use_container_width=True,
hide_index=True
)

st.subheader(data_note)

st.markdown(formula_text)
