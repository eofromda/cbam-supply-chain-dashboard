CBAM Supply Chain Optimisation Dashboard

Author: Haeun Eo
Project Type: Global Business Strategy · Supply Chain Analytics · Carbon Regulation · Interactive Dashboard

Live Dashboard

Streamlit App: https://cbam-supply-chain-dashboard-vbh639qxaqt7rapplh4zaze.streamlit.app/

Code Repository

GitHub Repository: https://github.com/eofromda/cbam-supply-chain-dashboard

Project Overview

This project explores how carbon regulation can influence global supply chain strategy.

I built this dashboard to examine how companies may need to rethink supply chain decisions when carbon emissions become part of business cost. Instead of looking only at production cost, the project compares how carbon price, logistics cost, embedded emissions, lead time, and supply chain risk can affect route selection.

The project is based on K-EV Components Co., a hypothetical Korean EV battery components firm preparing to enter the EU market. The dashboard compares five possible supply chain routes for aluminium EV battery enclosure components supplied to Europe.

The analysis uses the EU Carbon Border Adjustment Mechanism (CBAM) as the regulatory background. Since aluminium is included in the CBAM framework, this project uses an aluminium-intensive EV battery component as a scenario product to show how carbon-related costs can become part of business decision-making.

The main idea behind this project is:

Carbon emissions are no longer only an environmental issue. Under carbon regulation, they can become a strategic cost variable in global trade.

Research Question

How could carbon costs under CBAM influence supply chain route selection for a Korean EV battery components firm entering the EU market?

Business Scenario

K-EV Components Co. is a hypothetical Korean EV battery components firm considering entry into the European market.

In this scenario, the company is comparing several supply chain routes for aluminium EV battery enclosure components. Each route has a different combination of production cost, logistics cost, embedded emissions, lead time, and supply chain risk.

The dashboard allows users to adjust carbon price, logistics cost increase, emissions reduction, risk weighting, and lead time weighting. By changing these variables, users can observe how the lowest-cost route and the strategic recommendation may change under different conditions.

This project is not intended to be a legal compliance tool or a commercial recommendation. It is a scenario-based business strategy model designed to show how carbon regulation can be translated into supply chain decision-making.

Supply Chain Routes

The dashboard compares five scenario routes:

Route ID	Route	Strategic Meaning
R1	China -> Korea -> EU	Low-cost, high-carbon route
R2	Vietnam -> Korea -> EU	Balanced cost and emissions route
R3	Korea -> EU	Stable home-base export route
R4	India -> Korea -> EU	Low-cost, higher-risk route
R5	Germany/EU -> EU	High-cost, low-carbon local route

These routes are simplified scenarios. They are designed to compare different strategic trade-offs, not to represent the actual supplier network of a real company.

Dashboard Features

The dashboard includes:

* Carbon price slider
* Logistics cost increase slider
* Emissions reduction slider
* Supply chain risk weighting
* Lead time weighting
* Lowest final cost route recommendation
* Strategic route recommendation
* Final cost comparison chart
* Cost breakdown chart
* Carbon price sensitivity chart
* Route ranking table
* English and Korean language toggle

Model Formula

Final Cost

Final Cost = Production Cost + Adjusted Logistics Cost + CBAM Cost

CBAM Cost

CBAM Cost = Adjusted Embedded Emissions x Carbon Price

Strategic Score

Strategic Score = Final Cost + Risk Penalty + Lead Time Penalty

The dashboard separates the lowest final cost route from the recommended strategic route because the cheapest option is not always the strongest strategic choice when risk and delivery time are also considered.

Data Assumptions

This project uses simplified scenario assumptions for comparison.

The cost, emissions, lead time, and risk values do not represent confidential company-level data. They were created to demonstrate how carbon pricing can be incorporated into supply chain decision-making.

The model is intended to show relationships between variables rather than predict the exact cost of a real company’s supply chain.

Key Findings

The dashboard shows that carbon pricing can change the ranking of supply chain routes.

A route with low production cost may look attractive at first, but its advantage can weaken if it has higher embedded emissions. In contrast, a route with higher production cost may become more strategically competitive when carbon cost, delivery time, and supply chain risk are considered together.

This suggests that carbon intensity can become a measurable business variable. Under carbon regulation, emissions data can affect sourcing decisions, logistics planning, and EU market-entry strategy.

Limitations

This model is a simplified scenario analysis.

It does not include every real-world factor, such as supplier contracts, customs procedures, exchange rate changes, detailed product-level emissions, energy source differences, or official product-level CBAM classification.

The dashboard should be understood as a strategic simulation tool, not as a legal, compliance, or commercial recommendation.

Tools Used

* Python
* Streamlit
* Pandas
* Plotly
* NumPy
* GitHub
* Google Sheets

AI Use Statement

AI was used only as a coding and debugging support tool during the development of this project. It helped with Streamlit code structure, code review, syntax error checking, and deployment troubleshooting.

The research process, source selection, project concept, business scenario, supply chain route design, dashboard structure, data assumptions, visual direction, analysis, and final decisions were designed, reviewed, and directed by me.

Official Sources

* European Commission - Carbon Border Adjustment Mechanism
* European Commission - CBAM Legislation and Guidance
* European Commission - CBAM Communication and FAQs
* European Commission - EU Trade Relations with South Korea
* Streamlit Documentation - App Dependencies for Community Cloud
* Streamlit Documentation - File Organisation for Community Cloud
* GitHub Docs - About Repository README Files
