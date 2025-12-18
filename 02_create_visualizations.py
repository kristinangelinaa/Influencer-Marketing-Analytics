"""
INFLUENCER MARKETING DATA VISUALIZATION TUTORIAL
=================================================
This script creates visualizations for your marketing dashboard.

Prerequisites: Run 01_data_cleaning_tutorial.py first!

Topics Covered:
1. Creating charts for ROAS analysis
2. Visualizing CAC by channel
3. Budget allocation recommendations
4. Interactive dashboard concepts
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

print("=" * 80)
print("CREATING VISUALIZATIONS FOR MARKETING DASHBOARD")
print("=" * 80)

# ============================================================================
# LOAD CLEANED DATA
# ============================================================================
print("\n📊 Loading cleaned data...")

try:
    df = pd.read_csv('influencer_marketing_cleaned.csv')
    print(f"✓ Loaded {len(df):,} records")
except FileNotFoundError:
    print("❌ Error: Please run 01_data_cleaning_tutorial.py first!")
    exit()

# Convert dates back to datetime
df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])

# ============================================================================
# VISUALIZATION 1: BUDGET ALLOCATION BY PLATFORM
# ============================================================================
print("\n📈 Creating Visualization 1: Budget Allocation by Platform")

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Pie chart of budget allocation
budget_by_platform = df.groupby('platform')['campaign_cost'].sum().sort_values(ascending=False)
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']

axes[0].pie(budget_by_platform, labels=budget_by_platform.index, autopct='%1.1f%%',
            startangle=90, colors=colors)
axes[0].set_title('Current Budget Allocation by Platform', fontsize=14, fontweight='bold')

# Bar chart with revenue comparison
platform_metrics = df.groupby('platform').agg({
    'campaign_cost': 'sum',
    'revenue': 'sum'
}).round(2)

x = np.arange(len(platform_metrics))
width = 0.35

axes[1].bar(x - width/2, platform_metrics['campaign_cost'], width,
            label='Cost', color='#FF6B6B', alpha=0.8)
axes[1].bar(x + width/2, platform_metrics['revenue'], width,
            label='Revenue', color='#4ECDC4', alpha=0.8)

axes[1].set_xlabel('Platform', fontweight='bold')
axes[1].set_ylabel('Amount ($)', fontweight='bold')
axes[1].set_title('Cost vs Revenue by Platform', fontsize=14, fontweight='bold')
axes[1].set_xticks(x)
axes[1].set_xticklabels(platform_metrics.index)
axes[1].legend()
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('viz1_budget_allocation.png', dpi=300, bbox_inches='tight')
print("✓ Saved: viz1_budget_allocation.png")
plt.close()

# ============================================================================
# VISUALIZATION 2: ROAS BY CHANNEL
# ============================================================================
print("📈 Creating Visualization 2: ROAS Analysis by Channel")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 2.1: ROAS by Platform (Bar Chart)
roas_by_platform = df.groupby('platform')['ROAS'].mean().sort_values(ascending=False)
colors_roas = ['#2ECC71' if x > 1 else '#E74C3C' for x in roas_by_platform]

axes[0, 0].bar(roas_by_platform.index, roas_by_platform.values, color=colors_roas, alpha=0.8)
axes[0, 0].axhline(y=1, color='black', linestyle='--', linewidth=2, label='Break-even (ROAS=1)')
axes[0, 0].set_title('Average ROAS by Platform', fontsize=14, fontweight='bold')
axes[0, 0].set_ylabel('ROAS (Revenue/Cost)', fontweight='bold')
axes[0, 0].legend()
axes[0, 0].grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, v in enumerate(roas_by_platform.values):
    axes[0, 0].text(i, v + 0.1, f'{v:.2f}', ha='center', fontweight='bold')

# 2.2: ROAS by Campaign Type
roas_by_campaign = df.groupby('campaign_type')['ROAS'].mean().sort_values(ascending=False)
colors_campaign = ['#3498DB', '#9B59B6', '#E67E22', '#1ABC9C', '#F39C12']

axes[0, 1].barh(roas_by_campaign.index, roas_by_campaign.values, color=colors_campaign, alpha=0.8)
axes[0, 1].axvline(x=1, color='black', linestyle='--', linewidth=2)
axes[0, 1].set_title('Average ROAS by Campaign Type', fontsize=14, fontweight='bold')
axes[0, 1].set_xlabel('ROAS (Revenue/Cost)', fontweight='bold')
axes[0, 1].grid(axis='x', alpha=0.3)

# 2.3: ROAS Distribution by Platform (Box Plot)
platform_order = roas_by_platform.index
sns.boxplot(data=df, y='platform', x='ROAS', order=platform_order,
            palette='Set2', ax=axes[1, 0])
axes[1, 0].set_title('ROAS Distribution by Platform', fontsize=14, fontweight='bold')
axes[1, 0].set_xlabel('ROAS', fontweight='bold')
axes[1, 0].set_ylabel('Platform', fontweight='bold')
axes[1, 0].axvline(x=1, color='red', linestyle='--', linewidth=2, alpha=0.5)

# 2.4: Heatmap - ROAS by Platform x Campaign Type
heatmap_data = df.pivot_table(values='ROAS', index='platform',
                                columns='campaign_type', aggfunc='mean')
sns.heatmap(heatmap_data, annot=True, fmt='.2f', cmap='RdYlGn', center=1,
            cbar_kws={'label': 'ROAS'}, ax=axes[1, 1])
axes[1, 1].set_title('ROAS Heatmap: Platform × Campaign Type', fontsize=14, fontweight='bold')
axes[1, 1].set_ylabel('Platform', fontweight='bold')
axes[1, 1].set_xlabel('Campaign Type', fontweight='bold')

plt.tight_layout()
plt.savefig('viz2_roas_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Saved: viz2_roas_analysis.png")
plt.close()

# ============================================================================
# VISUALIZATION 3: CAC BY CHANNEL
# ============================================================================
print("📈 Creating Visualization 3: Customer Acquisition Cost Analysis")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 3.1: Average CAC by Platform
cac_by_platform = df.groupby('platform')['CAC'].mean().sort_values()
colors_cac = ['#2ECC71', '#3498DB', '#F39C12', '#E74C3C']

axes[0, 0].bar(cac_by_platform.index, cac_by_platform.values, color=colors_cac, alpha=0.8)
axes[0, 0].set_title('Average Customer Acquisition Cost by Platform', fontsize=14, fontweight='bold')
axes[0, 0].set_ylabel('CAC ($)', fontweight='bold')
axes[0, 0].grid(axis='y', alpha=0.3)

# Add value labels
for i, v in enumerate(cac_by_platform.values):
    axes[0, 0].text(i, v + 0.5, f'${v:.2f}', ha='center', fontweight='bold')

# 3.2: CAC by Influencer Category
cac_by_category = df.groupby('influencer_category')['CAC'].mean().sort_values()
axes[0, 1].barh(cac_by_category.index, cac_by_category.values,
                color=sns.color_palette('coolwarm', len(cac_by_category)), alpha=0.8)
axes[0, 1].set_title('Average CAC by Influencer Category', fontsize=14, fontweight='bold')
axes[0, 1].set_xlabel('CAC ($)', fontweight='bold')
axes[0, 1].grid(axis='x', alpha=0.3)

# 3.3: CAC vs ROAS Scatter Plot (Platform)
for platform in df['platform'].unique():
    platform_data = df[df['platform'] == platform]
    axes[1, 0].scatter(platform_data['CAC'], platform_data['ROAS'],
                       label=platform, alpha=0.6, s=50)

axes[1, 0].set_xlabel('CAC ($)', fontweight='bold')
axes[1, 0].set_ylabel('ROAS', fontweight='bold')
axes[1, 0].set_title('CAC vs ROAS by Platform', fontsize=14, fontweight='bold')
axes[1, 0].axhline(y=1, color='red', linestyle='--', alpha=0.5, label='ROAS=1')
axes[1, 0].legend()
axes[1, 0].grid(alpha=0.3)

# 3.4: CAC Trend Over Time
df_monthly = df.groupby([df['start_date'].dt.to_period('M'), 'platform'])['CAC'].mean().reset_index()
df_monthly['start_date'] = df_monthly['start_date'].dt.to_timestamp()

for platform in df['platform'].unique():
    platform_trend = df_monthly[df_monthly['platform'] == platform]
    axes[1, 1].plot(platform_trend['start_date'], platform_trend['CAC'],
                    marker='o', label=platform, linewidth=2)

axes[1, 1].set_xlabel('Date', fontweight='bold')
axes[1, 1].set_ylabel('Average CAC ($)', fontweight='bold')
axes[1, 1].set_title('CAC Trend Over Time by Platform', fontsize=14, fontweight='bold')
axes[1, 1].legend()
axes[1, 1].grid(alpha=0.3)
plt.setp(axes[1, 1].xaxis.get_majorticklabels(), rotation=45)

plt.tight_layout()
plt.savefig('viz3_cac_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Saved: viz3_cac_analysis.png")
plt.close()

# ============================================================================
# VISUALIZATION 4: BUDGET ALLOCATION RECOMMENDATIONS
# ============================================================================
print("📈 Creating Visualization 4: Budget Allocation Recommendations")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Calculate efficiency score (ROAS / CAC)
platform_performance = df.groupby('platform').agg({
    'ROAS': 'mean',
    'CAC': 'mean',
    'campaign_cost': 'sum',
    'revenue': 'sum'
}).round(2)

platform_performance['efficiency_score'] = (
    platform_performance['ROAS'] / platform_performance['CAC']
).round(2)
platform_performance = platform_performance.sort_values('efficiency_score', ascending=False)

# 4.1: Efficiency Score
axes[0, 0].bar(platform_performance.index, platform_performance['efficiency_score'],
               color=sns.color_palette('viridis', len(platform_performance)), alpha=0.8)
axes[0, 0].set_title('Platform Efficiency Score (ROAS/CAC)', fontsize=14, fontweight='bold')
axes[0, 0].set_ylabel('Efficiency Score', fontweight='bold')
axes[0, 0].grid(axis='y', alpha=0.3)

for i, v in enumerate(platform_performance['efficiency_score'].values):
    axes[0, 0].text(i, v + 0.05, f'{v:.2f}', ha='center', fontweight='bold')

# 4.2: Current vs Recommended Budget Allocation
current_allocation = df.groupby('platform')['campaign_cost'].sum()
total_budget = current_allocation.sum()

# Recommended allocation based on efficiency score
weights = platform_performance['efficiency_score'] / platform_performance['efficiency_score'].sum()
recommended_allocation = weights * total_budget

allocation_df = pd.DataFrame({
    'Current': current_allocation,
    'Recommended': recommended_allocation
})

allocation_df.plot(kind='bar', ax=axes[0, 1], color=['#FF6B6B', '#4ECDC4'], alpha=0.8)
axes[0, 1].set_title('Current vs Recommended Budget Allocation', fontsize=14, fontweight='bold')
axes[0, 1].set_ylabel('Budget ($)', fontweight='bold')
axes[0, 1].set_xlabel('Platform', fontweight='bold')
axes[0, 1].legend()
axes[0, 1].grid(axis='y', alpha=0.3)
plt.setp(axes[0, 1].xaxis.get_majorticklabels(), rotation=45)

# 4.3: Performance Matrix
axes[1, 0].scatter(platform_performance['CAC'], platform_performance['ROAS'],
                   s=platform_performance['campaign_cost']/100,
                   alpha=0.6, c=range(len(platform_performance)),
                   cmap='viridis')

for idx, row in platform_performance.iterrows():
    axes[1, 0].annotate(idx, (row['CAC'], row['ROAS']),
                        fontweight='bold', fontsize=11)

axes[1, 0].set_xlabel('Average CAC ($)', fontweight='bold')
axes[1, 0].set_ylabel('Average ROAS', fontweight='bold')
axes[1, 0].set_title('Performance Matrix (bubble size = total spend)', fontsize=14, fontweight='bold')
axes[1, 0].axhline(y=1, color='red', linestyle='--', alpha=0.3)
axes[1, 0].grid(alpha=0.3)

# Add quadrants
cac_median = platform_performance['CAC'].median()
axes[1, 0].axvline(x=cac_median, color='gray', linestyle='--', alpha=0.3)
axes[1, 0].text(cac_median * 0.5, platform_performance['ROAS'].max() * 0.95,
                'Low CAC\nHigh ROAS\n(INVEST)', ha='center',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

# 4.4: ROI Comparison Table (as image)
axes[1, 1].axis('tight')
axes[1, 1].axis('off')

summary_table = platform_performance[['ROAS', 'CAC', 'efficiency_score', 'revenue']].copy()
summary_table['revenue'] = summary_table['revenue'].apply(lambda x: f'${x:,.0f}')
summary_table = summary_table.round(2)

table = axes[1, 1].table(cellText=summary_table.values,
                         rowLabels=summary_table.index,
                         colLabels=['Avg ROAS', 'Avg CAC ($)', 'Efficiency', 'Total Revenue'],
                         cellLoc='center',
                         loc='center',
                         bbox=[0, 0, 1, 1])

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2)

# Color code the efficiency column
for i in range(1, len(summary_table) + 1):
    table[(i, 2)].set_facecolor('#90EE90' if i == 1 else '#FFE4B5')

axes[1, 1].set_title('Platform Performance Summary', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('viz4_budget_recommendations.png', dpi=300, bbox_inches='tight')
print("✓ Saved: viz4_budget_recommendations.png")
plt.close()

# ============================================================================
# VISUALIZATION 5: ADDITIONAL INSIGHTS
# ============================================================================
print("📈 Creating Visualization 5: Additional Marketing Insights")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 5.1: Engagement Rate by Platform
engagement_by_platform = df.groupby('platform')['engagement_rate'].mean().sort_values(ascending=False)
axes[0, 0].bar(engagement_by_platform.index, engagement_by_platform.values,
               color=sns.color_palette('magma', len(engagement_by_platform)), alpha=0.8)
axes[0, 0].set_title('Average Engagement Rate by Platform', fontsize=14, fontweight='bold')
axes[0, 0].set_ylabel('Engagement Rate (%)', fontweight='bold')
axes[0, 0].grid(axis='y', alpha=0.3)

# 5.2: Conversion Rate by Platform
conversion_by_platform = df.groupby('platform')['conversion_rate'].mean().sort_values(ascending=False)
axes[0, 1].bar(conversion_by_platform.index, conversion_by_platform.values,
               color=sns.color_palette('rocket', len(conversion_by_platform)), alpha=0.8)
axes[0, 1].set_title('Average Conversion Rate by Platform', fontsize=14, fontweight='bold')
axes[0, 1].set_ylabel('Conversion Rate (%)', fontweight='bold')
axes[0, 1].grid(axis='y', alpha=0.3)

# 5.3: Campaign Type Distribution
campaign_counts = df['campaign_type'].value_counts()
axes[1, 0].pie(campaign_counts, labels=campaign_counts.index, autopct='%1.1f%%',
               startangle=90, colors=sns.color_palette('Set3'))
axes[1, 0].set_title('Campaign Type Distribution', fontsize=14, fontweight='bold')

# 5.4: Revenue Trend Over Time
monthly_revenue = df.groupby(df['start_date'].dt.to_period('M'))['revenue'].sum().reset_index()
monthly_revenue['start_date'] = monthly_revenue['start_date'].dt.to_timestamp()

axes[1, 1].plot(monthly_revenue['start_date'], monthly_revenue['revenue'],
                marker='o', linewidth=2, color='#2ECC71', markersize=8)
axes[1, 1].fill_between(monthly_revenue['start_date'], monthly_revenue['revenue'],
                         alpha=0.3, color='#2ECC71')
axes[1, 1].set_xlabel('Date', fontweight='bold')
axes[1, 1].set_ylabel('Revenue ($)', fontweight='bold')
axes[1, 1].set_title('Revenue Trend Over Time', fontsize=14, fontweight='bold')
axes[1, 1].grid(alpha=0.3)
plt.setp(axes[1, 1].xaxis.get_majorticklabels(), rotation=45)

plt.tight_layout()
plt.savefig('viz5_additional_insights.png', dpi=300, bbox_inches='tight')
print("✓ Saved: viz5_additional_insights.png")
plt.close()

# ============================================================================
# GENERATE SUMMARY REPORT
# ============================================================================
print("\n📋 Generating Summary Report...")

report = f"""
{'='*80}
INFLUENCER MARKETING DASHBOARD - EXECUTIVE SUMMARY
{'='*80}

OVERALL PERFORMANCE:
-------------------
Total Campaigns:        {len(df):,}
Total Budget Spent:     ${df['campaign_cost'].sum():,.2f}
Total Revenue:          ${df['revenue'].sum():,.2f}
Overall ROAS:           {(df['revenue'].sum() / df['campaign_cost'].sum()):.2f}
Average CAC:            ${df['CAC'].mean():.2f}

TOP PERFORMING PLATFORM:
-----------------------
Platform:               {platform_performance.index[0]}
ROAS:                   {platform_performance.iloc[0]['ROAS']:.2f}
CAC:                    ${platform_performance.iloc[0]['CAC']:.2f}
Efficiency Score:       {platform_performance.iloc[0]['efficiency_score']:.2f}

BUDGET ALLOCATION RECOMMENDATIONS:
---------------------------------
"""

for platform in platform_performance.index:
    current_pct = (allocation_df.loc[platform, 'Current'] / total_budget) * 100
    recommended_pct = (allocation_df.loc[platform, 'Recommended'] / total_budget) * 100
    change = recommended_pct - current_pct

    report += f"\n{platform:12} | Current: {current_pct:5.1f}% → Recommended: {recommended_pct:5.1f}% "
    report += f"({change:+.1f}%)"

report += f"""

KEY INSIGHTS:
------------
1. Best ROAS Platform: {roas_by_platform.index[0]} ({roas_by_platform.iloc[0]:.2f})
2. Lowest CAC Platform: {cac_by_platform.index[0]} (${cac_by_platform.iloc[0]:.2f})
3. Best Campaign Type: {roas_by_campaign.index[0]} (ROAS: {roas_by_campaign.iloc[0]:.2f})

VISUALIZATIONS CREATED:
----------------------
✓ viz1_budget_allocation.png - Current budget distribution
✓ viz2_roas_analysis.png - ROAS performance by channel
✓ viz3_cac_analysis.png - Customer acquisition cost analysis
✓ viz4_budget_recommendations.png - Data-driven budget recommendations
✓ viz5_additional_insights.png - Engagement & conversion metrics

{'='*80}
"""

print(report)

# Save report to file
with open('dashboard_summary_report.txt', 'w') as f:
    f.write(report)

print("✓ Saved: dashboard_summary_report.txt")

print("\n" + "="*80)
print("✅ ALL VISUALIZATIONS CREATED SUCCESSFULLY!")
print("="*80)
print("\nNext steps:")
print("1. Review all the PNG files generated")
print("2. Read the dashboard_summary_report.txt for insights")
print("3. Optional: Create an interactive dashboard with Streamlit")
print("   (See: 03_interactive_dashboard.py)")
