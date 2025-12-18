"""
INTERACTIVE MARKETING DASHBOARD WITH STREAMLIT
===============================================
This creates an interactive web dashboard for your marketing data!

HOW TO RUN:
1. Install Streamlit: pip install streamlit
2. Run this script: streamlit run 03_interactive_dashboard.py
3. Your browser will open with the interactive dashboard!

Prerequisites: Run 01_data_cleaning_tutorial.py first!
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import numpy as np

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="Influencer Marketing Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS FOR BETTER STYLING
# ============================================================================
st.markdown("""
    <style>
    .main-header {
        font-size: 42px;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        padding: 20px;
    }
    .metric-card {
        background-color: #F0F9FF;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
    }
    .insight-box {
        background-color: #FEF3C7;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #F59E0B;
        margin: 10px 0;
        color: #000000;
    }
    .insight-box h4 {
        color: #1F2937;
        font-weight: bold;
    }
    .insight-box ul {
        color: #1F2937;
    }
    .insight-box li {
        color: #1F2937;
    }
    .insight-box strong {
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# LOAD DATA
# ============================================================================
@st.cache_data
def load_data():
    """Load and cache the cleaned data"""
    try:
        df = pd.read_csv('influencer_marketing_cleaned.csv')
        df['start_date'] = pd.to_datetime(df['start_date'])
        df['end_date'] = pd.to_datetime(df['end_date'])
        return df
    except FileNotFoundError:
        st.error("❌ Error: Please run 01_data_cleaning_tutorial.py first!")
        st.stop()

df = load_data()

# ============================================================================
# HEADER
# ============================================================================
st.markdown('<p class="main-header">📊 Influencer Marketing ROI Dashboard</p>',
            unsafe_allow_html=True)

st.markdown("---")

# ============================================================================
# SIDEBAR FILTERS
# ============================================================================
st.sidebar.header("🔍 Filters")

# Date range filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(df['start_date'].min(), df['start_date'].max()),
    min_value=df['start_date'].min().date(),
    max_value=df['start_date'].max().date()
)

# Platform filter
platforms = st.sidebar.multiselect(
    "Select Platforms",
    options=df['platform'].unique(),
    default=df['platform'].unique()
)

# Campaign type filter
campaign_types = st.sidebar.multiselect(
    "Select Campaign Types",
    options=df['campaign_type'].unique(),
    default=df['campaign_type'].unique()
)

# Influencer category filter
categories = st.sidebar.multiselect(
    "Select Influencer Categories",
    options=df['influencer_category'].unique(),
    default=df['influencer_category'].unique()
)

# Apply filters
filtered_df = df[
    (df['start_date'].dt.date >= date_range[0]) &
    (df['start_date'].dt.date <= date_range[1]) &
    (df['platform'].isin(platforms)) &
    (df['campaign_type'].isin(campaign_types)) &
    (df['influencer_category'].isin(categories))
]

st.sidebar.markdown("---")
st.sidebar.info(f"📌 Showing {len(filtered_df):,} of {len(df):,} campaigns")

# ============================================================================
# KEY METRICS (TOP ROW)
# ============================================================================
st.header("📈 Key Performance Indicators")

col1, col2, col3, col4, col5 = st.columns(5)

total_spend = filtered_df['campaign_cost'].sum()
total_revenue = filtered_df['revenue'].sum()
overall_roas = total_revenue / total_spend if total_spend > 0 else 0
avg_cac = filtered_df['CAC'].mean()
total_sales = filtered_df['product_sales'].sum()

with col1:
    st.metric(
        label="💰 Total Spend",
        value=f"${total_spend:,.0f}",
        delta=None
    )

with col2:
    st.metric(
        label="📊 Total Revenue",
        value=f"${total_revenue:,.0f}",
        delta=f"{((total_revenue/total_spend - 1) * 100):.1f}% ROI" if total_spend > 0 else "N/A"
    )

with col3:
    st.metric(
        label="🎯 Overall ROAS",
        value=f"{overall_roas:.2f}",
        delta="Positive" if overall_roas > 1 else "Negative",
        delta_color="normal" if overall_roas > 1 else "inverse"
    )

with col4:
    st.metric(
        label="💵 Avg CAC",
        value=f"${avg_cac:.2f}",
        delta=None
    )

with col5:
    st.metric(
        label="🛒 Total Sales",
        value=f"{total_sales:,}",
        delta=None
    )

st.markdown("---")

# ============================================================================
# MAIN DASHBOARD - TWO COLUMNS
# ============================================================================

# TAB LAYOUT
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "💰 ROAS Analysis", "👥 CAC Analysis", "💡 Recommendations"])

# ============================================================================
# TAB 1: OVERVIEW
# ============================================================================
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Budget Allocation by Platform")

        budget_by_platform = filtered_df.groupby('platform')['campaign_cost'].sum().reset_index()
        budget_by_platform = budget_by_platform.sort_values('campaign_cost', ascending=False)

        fig = px.pie(
            budget_by_platform,
            values='campaign_cost',
            names='platform',
            title='Current Budget Distribution',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Revenue by Platform")

        revenue_by_platform = filtered_df.groupby('platform').agg({
            'campaign_cost': 'sum',
            'revenue': 'sum'
        }).reset_index()

        fig = go.Figure(data=[
            go.Bar(name='Cost', x=revenue_by_platform['platform'],
                   y=revenue_by_platform['campaign_cost'], marker_color='#FF6B6B'),
            go.Bar(name='Revenue', x=revenue_by_platform['platform'],
                   y=revenue_by_platform['revenue'], marker_color='#4ECDC4')
        ])
        fig.update_layout(
            title='Cost vs Revenue Comparison',
            barmode='group',
            xaxis_title='Platform',
            yaxis_title='Amount ($)'
        )
        st.plotly_chart(fig, use_container_width=True)

    # Full width chart - Trend over time
    st.subheader("Revenue Trend Over Time")

    monthly_data = filtered_df.groupby([
        filtered_df['start_date'].dt.to_period('M'),
        'platform'
    ]).agg({
        'revenue': 'sum',
        'campaign_cost': 'sum'
    }).reset_index()
    monthly_data['start_date'] = monthly_data['start_date'].dt.to_timestamp()

    fig = px.line(
        monthly_data,
        x='start_date',
        y='revenue',
        color='platform',
        title='Revenue Trend by Platform (Monthly Aggregated)',
        markers=True
    )
    fig.update_layout(
        xaxis_title='Month',
        yaxis_title='Revenue ($)',
        hovermode='x unified',
        height=500,
        font=dict(size=12),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        plot_bgcolor='white',
        yaxis=dict(
            gridcolor='lightgray',
            tickformat='$,.0f'
        ),
        xaxis=dict(
            gridcolor='lightgray'
        )
    )
    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=8)
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# TAB 2: ROAS ANALYSIS
# ============================================================================
with tab2:
    st.header("🎯 Return on Ad Spend (ROAS) Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("ROAS by Platform")

        roas_by_platform = filtered_df.groupby('platform')['ROAS'].mean().reset_index()
        roas_by_platform = roas_by_platform.sort_values('ROAS', ascending=False)

        # Create color based on ROAS (green if >1, red if <1)
        colors = ['#2ECC71' if x > 1 else '#E74C3C' for x in roas_by_platform['ROAS']]

        fig = go.Figure(data=[
            go.Bar(
                x=roas_by_platform['platform'],
                y=roas_by_platform['ROAS'],
                marker_color=colors,
                text=roas_by_platform['ROAS'].round(2),
                textposition='outside'
            )
        ])
        fig.add_hline(y=1, line_dash="dash", line_color="black",
                      annotation_text="Break-even (ROAS=1)")
        fig.update_layout(
            title='Average ROAS by Platform',
            xaxis_title='Platform',
            yaxis_title='ROAS (Revenue/Cost)',
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("ROAS by Campaign Type")

        roas_by_campaign = filtered_df.groupby('campaign_type')['ROAS'].mean().reset_index()
        roas_by_campaign = roas_by_campaign.sort_values('ROAS', ascending=True)

        fig = px.bar(
            roas_by_campaign,
            x='ROAS',
            y='campaign_type',
            orientation='h',
            title='Average ROAS by Campaign Type',
            color='ROAS',
            color_continuous_scale='RdYlGn'
        )
        fig.add_vline(x=1, line_dash="dash", line_color="black")
        st.plotly_chart(fig, use_container_width=True)

    # ROAS Heatmap
    st.subheader("ROAS Heatmap: Platform × Campaign Type")

    heatmap_data = filtered_df.pivot_table(
        values='ROAS',
        index='platform',
        columns='campaign_type',
        aggfunc='mean'
    )

    fig = px.imshow(
        heatmap_data,
        labels=dict(x="Campaign Type", y="Platform", color="ROAS"),
        x=heatmap_data.columns,
        y=heatmap_data.index,
        color_continuous_scale='RdYlGn',
        aspect="auto",
        text_auto='.2f'
    )
    fig.update_layout(title='ROAS Performance Matrix')
    st.plotly_chart(fig, use_container_width=True)

    # ROAS Distribution
    st.subheader("ROAS Distribution by Platform")

    fig = px.box(
        filtered_df,
        x='platform',
        y='ROAS',
        color='platform',
        title='ROAS Distribution (Box Plot)',
        points='outliers'
    )
    fig.add_hline(y=1, line_dash="dash", line_color="red", opacity=0.5)
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# TAB 3: CAC ANALYSIS
# ============================================================================
with tab3:
    st.header("💵 Customer Acquisition Cost (CAC) Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("CAC by Platform")

        cac_by_platform = filtered_df.groupby('platform')['CAC'].mean().reset_index()
        cac_by_platform = cac_by_platform.sort_values('CAC')

        fig = px.bar(
            cac_by_platform,
            x='platform',
            y='CAC',
            title='Average Customer Acquisition Cost',
            color='CAC',
            color_continuous_scale='RdYlGn_r',
            text='CAC'
        )
        fig.update_traces(texttemplate='$%{text:.2f}', textposition='outside')
        fig.update_layout(
            xaxis_title='Platform',
            yaxis_title='CAC ($)',
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("CAC by Influencer Category")

        cac_by_category = filtered_df.groupby('influencer_category')['CAC'].mean().reset_index()
        cac_by_category = cac_by_category.sort_values('CAC', ascending=True)

        fig = px.bar(
            cac_by_category,
            x='CAC',
            y='influencer_category',
            orientation='h',
            title='Average CAC by Category',
            color='CAC',
            color_continuous_scale='Reds'
        )
        st.plotly_chart(fig, use_container_width=True)

    # CAC vs ROAS Scatter
    st.subheader("CAC vs ROAS Performance Matrix")

    fig = px.scatter(
        filtered_df,
        x='CAC',
        y='ROAS',
        color='platform',
        size='revenue',
        hover_data=['campaign_type', 'influencer_category'],
        title='CAC vs ROAS by Platform (bubble size = revenue)',
        opacity=0.6
    )
    fig.add_hline(y=1, line_dash="dash", line_color="red", opacity=0.3)
    fig.update_layout(
        xaxis_title='Customer Acquisition Cost ($)',
        yaxis_title='Return on Ad Spend (ROAS)'
    )
    st.plotly_chart(fig, use_container_width=True)

    # CAC Trend
    st.subheader("CAC Trend Over Time")

    cac_trend = filtered_df.groupby([
        filtered_df['start_date'].dt.to_period('M'),
        'platform'
    ])['CAC'].mean().reset_index()
    cac_trend['start_date'] = cac_trend['start_date'].dt.to_timestamp()

    fig = px.line(
        cac_trend,
        x='start_date',
        y='CAC',
        color='platform',
        markers=True,
        title='CAC Trend by Platform (Monthly Average)'
    )
    fig.update_layout(
        xaxis_title='Month',
        yaxis_title='Average CAC ($)',
        height=500,
        font=dict(size=12),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        plot_bgcolor='white',
        yaxis=dict(
            gridcolor='lightgray',
            tickformat='$,.2f'
        ),
        xaxis=dict(
            gridcolor='lightgray'
        ),
        hovermode='x unified'
    )
    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=8)
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# TAB 4: RECOMMENDATIONS
# ============================================================================
with tab4:
    st.header("💡 Budget Allocation Recommendations")

    # Calculate performance metrics
    platform_performance = filtered_df.groupby('platform').agg({
        'ROAS': 'mean',
        'CAC': 'mean',
        'campaign_cost': 'sum',
        'revenue': 'sum',
        'engagement_rate': 'mean',
        'conversion_rate': 'mean'
    }).round(2)

    platform_performance['efficiency_score'] = (
        platform_performance['ROAS'] / platform_performance['CAC']
    ).round(2)

    platform_performance = platform_performance.sort_values('efficiency_score', ascending=False)

    # Current vs Recommended Allocation
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Platform Efficiency Scores")

        fig = px.bar(
            platform_performance.reset_index(),
            x='platform',
            y='efficiency_score',
            title='Efficiency Score (ROAS/CAC)',
            color='efficiency_score',
            color_continuous_scale='Viridis',
            text='efficiency_score'
        )
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Budget Reallocation Suggestion")

        # Calculate recommended allocation
        current_total = platform_performance['campaign_cost'].sum()
        weights = platform_performance['efficiency_score'] / platform_performance['efficiency_score'].sum()
        platform_performance['recommended_budget'] = weights * current_total

        allocation_comparison = pd.DataFrame({
            'Platform': platform_performance.index,
            'Current': platform_performance['campaign_cost'],
            'Recommended': platform_performance['recommended_budget']
        })

        fig = go.Figure(data=[
            go.Bar(name='Current', x=allocation_comparison['Platform'],
                   y=allocation_comparison['Current'], marker_color='#FF6B6B'),
            go.Bar(name='Recommended', x=allocation_comparison['Platform'],
                   y=allocation_comparison['Recommended'], marker_color='#4ECDC4')
        ])
        fig.update_layout(
            title='Current vs Recommended Budget',
            barmode='group',
            xaxis_title='Platform',
            yaxis_title='Budget ($)'
        )
        st.plotly_chart(fig, use_container_width=True)

    # Insights and Recommendations
    st.subheader("📋 Key Insights & Action Items")

    best_platform = platform_performance.index[0]
    best_roas = platform_performance.loc[best_platform, 'ROAS']
    best_efficiency = platform_performance.loc[best_platform, 'efficiency_score']

    st.markdown(f"""
    <div class="insight-box">
    <h4>🏆 Top Performing Platform: {best_platform}</h4>
    <ul>
        <li><strong>ROAS:</strong> {best_roas:.2f} (${best_roas:.2f} revenue per $1 spent)</li>
        <li><strong>Efficiency Score:</strong> {best_efficiency:.2f}</li>
        <li><strong>Recommendation:</strong> Increase budget allocation by {((platform_performance.loc[best_platform, 'recommended_budget'] / platform_performance.loc[best_platform, 'campaign_cost'] - 1) * 100):.1f}%</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # Performance Table
    st.subheader("📊 Detailed Performance Metrics by Platform")

    display_df = platform_performance[['ROAS', 'CAC', 'efficiency_score',
                                       'engagement_rate', 'conversion_rate', 'revenue']].copy()
    display_df.columns = ['Avg ROAS', 'Avg CAC ($)', 'Efficiency Score',
                          'Engagement Rate (%)', 'Conversion Rate (%)', 'Total Revenue ($)']

    # Style the dataframe
    st.dataframe(
        display_df.style.background_gradient(subset=['Avg ROAS', 'Efficiency Score'], cmap='Greens')
                       .background_gradient(subset=['Avg CAC ($)'], cmap='Reds_r')
                       .format({
                           'Avg ROAS': '{:.2f}',
                           'Avg CAC ($)': '${:.2f}',
                           'Efficiency Score': '{:.2f}',
                           'Engagement Rate (%)': '{:.2f}%',
                           'Conversion Rate (%)': '{:.4f}%',
                           'Total Revenue ($)': '${:,.0f}'
                       }),
        use_container_width=True
    )

    # Action items
    st.subheader("✅ Recommended Actions")

    for i, (platform, row) in enumerate(platform_performance.iterrows(), 1):
        change_pct = ((row['recommended_budget'] / row['campaign_cost']) - 1) * 100

        if change_pct > 10:
            action = f"📈 **Increase** budget for {platform} by {change_pct:.1f}%"
            reason = f"High efficiency score ({row['efficiency_score']:.2f}) and strong ROAS ({row['ROAS']:.2f})"
        elif change_pct < -10:
            action = f"📉 **Decrease** budget for {platform} by {abs(change_pct):.1f}%"
            reason = f"Lower efficiency compared to other platforms"
        else:
            action = f"➡️ **Maintain** current budget for {platform}"
            reason = "Performance is balanced with current allocation"

        st.markdown(f"{i}. {action}")
        st.caption(f"   Reason: {reason}")

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
    📊 Influencer Marketing ROI Dashboard | Built with Streamlit & Python
    </div>
""", unsafe_allow_html=True)
