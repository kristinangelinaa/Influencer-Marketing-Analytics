# 📊 Influencer Marketing ROI Analytics Dashboard

An end-to-end data analytics project analyzing 87,743+ influencer marketing campaigns to optimize budget allocation and maximize ROI across social media platforms.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)](https://pandas.pydata.org/)

---

## 🎯 Project Overview

This project analyzes influencer marketing campaign performance across **Instagram, YouTube, TikTok, and Twitter** to provide data-driven insights for marketing budget optimization.

### Key Results

- **Total Campaigns Analyzed:** 87,743
- **Total Budget:** $329.5M
- **Total Revenue Generated:** $10.9B
- **Overall ROAS:** 33.14x (Every $1 spent returns $33.14)
- **Average CAC:** $7.23

### 🏆 Top Performing Platform: Twitter
- **ROAS:** 183.17x
- **CAC:** $5.11
- **Efficiency Score:** 35.85
- **Recommendation:** Increase budget allocation from 6.7% to 40.9%

---

## 📈 Dashboard Features

### Interactive Analytics
- **ROAS Analysis** - Return on Ad Spend by platform and campaign type
- **CAC Metrics** - Customer Acquisition Cost tracking
- **Trend Analysis** - Monthly revenue and performance trends
- **Budget Recommendations** - Data-driven allocation strategies

### Key Metrics Tracked
- Return on Ad Spend (ROAS)
- Customer Acquisition Cost (CAC)
- Engagement Rate
- Conversion Rate
- Revenue Trends
- Platform Performance

---

## 🛠️ Tech Stack

- **Python 3.8+** - Data processing and analysis
- **Pandas & NumPy** - Data manipulation
- **Plotly** - Interactive visualizations
- **Streamlit** - Web dashboard framework
- **Jupyter Notebook** - Analysis documentation

---

## 📁 Project Structure

```
influencer-marketing-analytics/
│
├── ROI_dataset.ipynb                      # Main analysis notebook
├── influencer_marketing_cleaned.csv       # Cleaned dataset
├── dashboard_summary_report.txt           # Executive summary
│
├── 2D visualization/                      # Static visualizations
│   ├── viz1_budget_allocation.png
│   ├── viz2_roas_analysis.png
│   ├── viz3_cac_analysis.png
│   ├── viz4_budget_recommendations.png
│   └── viz5_additional_insights.png
│
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn plotly streamlit
```

### Running the Analysis

1. **Clone the repository**
   ```bash
   git clone https://github.com/kristinangelinaa/influencer-marketing-analytics.git
   cd influencer-marketing-analytics
   ```

2. **Explore the Jupyter Notebook**
   ```bash
   jupyter notebook ROI_dataset.ipynb
   ```

---

## 📊 Key Insights

### Budget Allocation Recommendations

| Platform  | Current | Recommended | Change  |
|-----------|---------|-------------|---------|
| Twitter   | 6.7%    | 40.9%       | +34.2%  |
| TikTok    | 16.0%   | 28.5%       | +12.5%  |
| Instagram | 37.0%   | 21.0%       | -15.9%  |
| YouTube   | 40.4%   | 9.6%        | -30.8%  |

### Performance Highlights

1. **Best ROAS Platform:** Twitter (183.17x)
2. **Lowest CAC:** Twitter ($5.11)
3. **Best Campaign Type:** Seasonal Sale (ROAS: 124.75x)

---

## 📸 Visualizations

### Budget Allocation Analysis
![Budget Allocation](2D%20visualization/viz1_budget_allocation.png)

### ROAS Performance
![ROAS Analysis](2D%20visualization/viz2_roas_analysis.png)

### Customer Acquisition Cost
![CAC Analysis](2D%20visualization/viz3_cac_analysis.png)

### Budget Recommendations
![Recommendations](2D%20visualization/viz4_budget_recommendations.png)

---

## 💡 Methodology

### 1. Data Cleaning
- Handled missing values and duplicates
- Standardized date formats
- Validated numeric ranges

### 2. Feature Engineering
- Created ROAS metric (Revenue ÷ Cost)
- Calculated CAC (Cost ÷ Customers Acquired)
- Computed engagement and conversion rates
- Extracted temporal features (month, quarter, year)

### 3. Analysis
- Platform performance comparison
- Trend analysis over time
- Campaign type effectiveness
- Budget optimization modeling

### 4. Visualization
- Interactive Streamlit dashboard
- Static publication-quality charts
- Executive summary reports

---

## 📋 Dataset Description

### Original Features
- **Campaign ID** - Unique identifier
- **Platform** - Social media platform (Instagram, YouTube, TikTok, Twitter)
- **Influencer Category** - Content niche
- **Campaign Type** - Marketing campaign category
- **Start/End Date** - Campaign duration
- **Engagements** - Total interactions
- **Estimated Reach** - Impression count
- **Product Sales** - Conversions generated

### Calculated Metrics
- **ROAS** - Return on Ad Spend
- **CAC** - Customer Acquisition Cost
- **Revenue** - Total sales generated
- **Engagement Rate** - Engagement ÷ Reach
- **Conversion Rate** - Sales ÷ Reach
- **Efficiency Score** - ROAS ÷ CAC

---

## 🎓 Skills Demonstrated

### Technical Skills
- Data cleaning and preprocessing
- Feature engineering
- Statistical analysis
- Data visualization
- Dashboard development
- Python programming

### Business Skills
- Marketing analytics
- ROI optimization
- Budget allocation strategy
- Performance metrics analysis
- Data-driven decision making
- Stakeholder communication

---

## 📊 Business Impact

### Strategic Recommendations

1. **Reallocate Budget to Twitter**
   - Current allocation too low (6.7%)
   - Highest ROAS (183.17x) and lowest CAC ($5.11)
   - Recommended increase to 40.9% (+34.2%)

2. **Optimize TikTok Investment**
   - Strong performance with room for growth
   - Increase from 16.0% to 28.5%

3. **Reduce YouTube Spend**
   - Underperforming relative to cost
   - Decrease from 40.4% to 9.6%

4. **Focus on Seasonal Campaigns**
   - Best campaign type with 124.75x ROAS

### Projected Impact
Implementing these recommendations could optimize **$329.5M in annual marketing spend**, potentially increasing revenue generation while reducing customer acquisition costs.

---

## 👤 Author

**Kristin Angelina**
- GitHub: [@kristinangelinaa](https://github.com/kristinangelinaa)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/kristinangelinaa)
- Passionate about transforming data into actionable business insights

---

## 📄 License

This project is open source and available under the MIT License.

---

**⭐ If you found this project helpful, please consider giving it a star!**

---

*Last Updated: December 2024*
