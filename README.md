# CBAM Supply Chain Optimisation Dashboard

**Author:** Haeun Eo
**Project Type:** Global Business Strategy · Supply Chain Analytics · Carbon Regulation · Interactive Dashboard

## Live Dashboard

Streamlit App: https://cbam-supply-chain-dashboard-vbh639qxaqt7rapplh4zaze.streamlit.app/

## Code Repository

GitHub Repository: https://github.com/eofromda/cbam-supply-chain-dashboard

## Project Overview

This project aims at the influence that carbon regulations may have on supply chain management practices by companies on a global scale.

Taking into consideration a hypothetical company called **K-EV Components Co.**, which manufactures EV battery components in South Korea, this dashboard will analyse five alternative paths in the global supply chain concerning aluminium EV battery enclosure components, which will be supplied to the EU market. Factors such as production cost, logistics cost, emissions of greenhouse gases, lead time, and risks associated with supply chains will be considered in this analysis.

The analysis will be conducted according to the EU's Carbon Border Adjustment Mechanism (CBAM), which was intended to reflect carbon emissions that are embedded into the selected imported goods. As aluminium belongs to those products for which the CBAM will apply, this product will serve as an example for our project.

The main idea of this project is:

> How much carbon something produces is not about the environment anymore. When there are rules about carbon it can also become a cost that companies have to think about when they do business, around the world.

## Research Question

How could carbon costs under CBAM influence supply chain route selection for a Korean EV battery components firm entering the EU market?

## Business Scenario

K-EV Components Co. is a hypothetical Korean company producing battery components for EVs considering entering the European market.

The company is analysing various supply chain paths for its products that will be aluminium enclosures of batteries of EVs. Different supply chain paths have various cost structures, carbon footprints, lead times, and risks associated with them.

The dashboard allows one to experiment with different prices of carbon, transportation costs, reduction of carbon footprint, weight of risk, and lead time.

The analysis is not intended as a compliance exercise or a business decision tool. It serves as an example of translating carbon regulation into supply chain management strategy.

## Supply Chain Routes

The dashboard compares five scenario routes:

| Route ID | Route                  | Strategic Meaning                 |
| -------- | ---------------------- | --------------------------------- |
| R1       | China -> Korea -> EU   | Low-cost, high-carbon route       |
| R2       | Vietnam -> Korea -> EU | Balanced cost and emissions route |
| R3       | Korea -> EU            | Stable home-base export route     |
| R4       | India -> Korea -> EU   | Low-cost, higher-risk route       |
| R5       | Germany/EU -> EU       | High-cost, low-carbon local route |

These routes are simplified scenarios. They are designed to compare different strategic trade-offs, not to represent the actual supplier network of a real company.

## Dashboard Features

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

## Model Formula

### Final Cost

Final Cost = Production Cost + Adjusted Logistics Cost + CBAM Cost

### CBAM Cost

CBAM Cost = Adjusted Embedded Emissions x Carbon Price

### Strategic Score

Strategic Score = Final Cost + Risk Penalty + Lead Time Penalty

The dashboard separates the lowest final cost route from the recommended strategic route because the cheapest option is not always the strongest strategic option.

## Data Assumptions

This project uses simplified scenario assumptions for comparison.

The cost, emissions, lead time, and risk values do not represent confidential company-level data. They were created to demonstrate how carbon pricing can be incorporated into supply chain decision-making.

The model is intended to show relationships between variables rather than predict the exact cost of a real company’s supply chain.

## Key Findings

It is evident from the above dashboard that carbon pricing has the ability to affect the order of preference of supply chain routes.

For instance, although one route might seem superior compared to another because of its lower production cost, this is not necessarily the case because of its greater embedded emissions, while another route, despite having a higher production cost, becomes more strategically favourable in consideration of carbon price, transportation time, and risks involved.

This means that CBAM has the capacity of converting emissions into a strategic business variable.

## Limitations

This model is a simplified scenario analysis.

It does not consider all the elements that can affect the real-life environment like supply contract, customs, exchange rates, individual emission for products, difference in energy sources, or even product-level CBAM classification.

The dashboard is to be considered as a strategic simulation tool, and not as an actual recommendation.

## Tools Used

* Python
* Streamlit
* Pandas
* Plotly
* NumPy
* GitHub
* Google Sheets

## AI Use Statement

I used Artificial Intelligence as a tool to help me with coding and finding mistakes during this project. It assisted me with the Streamlit code structure it reviewed my code it checked for syntax errors. It helped me troubleshoot problems when I was deploying the project.

I was the one who did all the research I picked the sources I came up with the project concept I thought of the business scenario I designed the supply chain route I figured out the dashboard structure I made assumptions about the data I decided on the direction I did the analysis and I made the final decisions, about the Artificial Intelligence project and the Streamlit project.

## Official Sources

* [European Commission - Carbon Border Adjustment Mechanism](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en)
* [European Commission - CBAM Legislation and Guidance](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en)
* [European Commission - CBAM Communication and FAQs](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-communication-and-faqs_en)
* [European Commission - EU Trade Relations with South Korea](https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/south-korea_en)
* [Streamlit Documentation - App Dependencies for Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)
* [Streamlit Documentation - File Organisation for Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization)
* [GitHub Docs - About Repository README Files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
