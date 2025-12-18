"""
INFLUENCER MARKETING DATA CLEANING & EDA TUTORIAL
==================================================
This tutorial teaches you how to clean and explore marketing data for dashboard creation.

Topics Covered:
1. Loading and inspecting data
2. Data cleaning (missing values, duplicates, data types)
3. Feature engineering (creating new metrics)
4. Exploratory Data Analysis (EDA)
5. Preparing data for dashboard metrics: ROAS, CAC, Budget Allocation

Author: Tutorial for Beginners
"""

# ============================================================================
# STEP 1: IMPORT LIBRARIES
# ============================================================================
# These are the main libraries we'll use for data analysis

import pandas as pd  # For data manipulation
import numpy as np   # For numerical operations
import matplotlib.pyplot as plt  # For visualization
import seaborn as sns  # For beautiful statistical visualizations
from datetime import datetime  # For date handling

# Set display options to see more data
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Don't wrap output
pd.set_option('display.max_rows', 100)  # Show up to 100 rows

print("=" * 80)
print("INFLUENCER MARKETING DATA CLEANING & EDA TUTORIAL")
print("=" * 80)

# ============================================================================
# STEP 2: LOAD THE DATA
# ============================================================================
print("\n📊 STEP 1: LOADING DATA")
print("-" * 80)

# Load the CSV file
df = pd.read_csv('influencer_marketing_roi_dataset.csv')

# First look at the data
print(f"\n✓ Dataset loaded successfully!")
print(f"  - Total rows: {len(df):,}")
print(f"  - Total columns: {len(df.columns)}")
print(f"\nColumn names and types:")
print(df.dtypes)

print("\n📋 First 5 rows of data:")
print(df.head())

# ============================================================================
# STEP 3: INITIAL DATA INSPECTION
# ============================================================================
print("\n\n🔍 STEP 2: DATA INSPECTION")
print("-" * 80)

# Check the shape
print(f"\nDataset shape: {df.shape}")
print(f"  → This means: {df.shape[0]} rows and {df.shape[1]} columns")

# Get basic statistics
print("\n📈 Statistical Summary:")
print(df.describe())

# Check data types
print("\n🏷️  Data Types:")
print(df.dtypes)

# Check for missing values
print("\n❓ Missing Values:")
missing = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing_Count': missing,
    'Percentage': missing_pct
})
print(missing_df[missing_df['Missing_Count'] > 0])

if missing_df['Missing_Count'].sum() == 0:
    print("  ✓ No missing values found!")

# ============================================================================
# STEP 4: DATA CLEANING
# ============================================================================
print("\n\n🧹 STEP 3: DATA CLEANING")
print("-" * 80)

# Create a copy to work with (always keep original data safe!)
df_clean = df.copy()

# Convert date columns to datetime
print("\n1. Converting date columns to datetime format...")
df_clean['start_date'] = pd.to_datetime(df_clean['start_date'])
df_clean['end_date'] = pd.to_datetime(df_clean['end_date'])
print("   ✓ Dates converted!")

# Check for duplicates
print("\n2. Checking for duplicate rows...")
duplicates = df_clean.duplicated().sum()
print(f"   - Duplicate rows found: {duplicates}")
if duplicates > 0:
    df_clean = df_clean.drop_duplicates()
    print(f"   ✓ Removed {duplicates} duplicates")

# Check for negative values (shouldn't exist in metrics)
print("\n3. Checking for invalid values...")
numeric_cols = ['engagements', 'estimated_reach', 'product_sales', 'campaign_duration_days']
for col in numeric_cols:
    negative_count = (df_clean[col] < 0).sum()
    if negative_count > 0:
        print(f"   ⚠️  {col}: {negative_count} negative values found")
    else:
        print(f"   ✓ {col}: No negative values")

# ============================================================================
# STEP 5: FEATURE ENGINEERING
# ============================================================================
print("\n\n🔧 STEP 4: FEATURE ENGINEERING (Creating New Metrics)")
print("-" * 80)

print("\n⚠️  IMPORTANT NOTE:")
print("   The dataset is missing 'campaign_cost' or 'budget' column.")
print("   We'll create a simulated cost for educational purposes.")
print("   In real scenarios, you would have actual budget data!\n")

# Simulate campaign costs based on platform and reach (for educational purposes)
# This is just an example - real data would have actual costs
np.random.seed(42)  # For reproducibility

# Base costs by platform (example CPM - Cost Per Mille/thousand impressions)
platform_cpm = {
    'Instagram': 7,  # $7 per 1000 impressions
    'YouTube': 10,   # $10 per 1000 impressions
    'TikTok': 6,     # $6 per 1000 impressions
    'Twitter': 5     # $5 per 1000 impressions
}

# Calculate simulated campaign cost
df_clean['campaign_cost'] = df_clean.apply(
    lambda row: (row['estimated_reach'] / 1000) * platform_cpm[row['platform']] *
                (1 + np.random.uniform(-0.2, 0.2)),  # Add some randomness
    axis=1
).round(2)

print("1. Created 'campaign_cost' column (simulated for tutorial)")

# Calculate ROAS (Return on Ad Spend)
# Formula: Revenue / Cost
# We'll use product_sales as revenue proxy (assuming each sale = $1 for simplicity)
# In reality, you'd multiply product_sales by average order value

# For this tutorial, let's assume average order value of $50
AVERAGE_ORDER_VALUE = 50

df_clean['revenue'] = df_clean['product_sales'] * AVERAGE_ORDER_VALUE
df_clean['ROAS'] = (df_clean['revenue'] / df_clean['campaign_cost']).round(2)

print("2. Created 'revenue' column (product_sales × $50 average order value)")
print("3. Created 'ROAS' column (Revenue ÷ Campaign Cost)")

# Calculate CAC (Customer Acquisition Cost)
# Formula: Campaign Cost / Number of Customers Acquired
df_clean['CAC'] = (df_clean['campaign_cost'] / df_clean['product_sales'].replace(0, 1)).round(2)
# Note: We replace 0 with 1 to avoid division by zero

print("4. Created 'CAC' column (Cost ÷ Product Sales)")

# Calculate Engagement Rate
# Formula: Engagements / Reach
df_clean['engagement_rate'] = (df_clean['engagements'] / df_clean['estimated_reach'] * 100).round(2)

print("5. Created 'engagement_rate' column (Engagements ÷ Reach × 100)")

# Calculate Conversion Rate
# Formula: Sales / Reach
df_clean['conversion_rate'] = (df_clean['product_sales'] / df_clean['estimated_reach'] * 100).round(2)

print("6. Created 'conversion_rate' column (Sales ÷ Reach × 100)")

# Extract date features
df_clean['year'] = df_clean['start_date'].dt.year
df_clean['month'] = df_clean['start_date'].dt.month
df_clean['quarter'] = df_clean['start_date'].dt.quarter
df_clean['day_of_week'] = df_clean['start_date'].dt.day_name()

print("7. Created date features: year, month, quarter, day_of_week")

print("\n✓ Feature engineering complete!")
print(f"  New dataset shape: {df_clean.shape}")

# ============================================================================
# STEP 6: EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================================
print("\n\n📊 STEP 5: EXPLORATORY DATA ANALYSIS")
print("-" * 80)

print("\n1. PLATFORM ANALYSIS")
print("   " + "-" * 40)
platform_stats = df_clean.groupby('platform').agg({
    'campaign_cost': 'sum',
    'revenue': 'sum',
    'product_sales': 'sum',
    'ROAS': 'mean',
    'CAC': 'mean',
    'engagement_rate': 'mean'
}).round(2)

platform_stats['total_campaigns'] = df_clean.groupby('platform').size()
platform_stats = platform_stats.sort_values('revenue', ascending=False)

print("\n   Platform Performance Summary:")
print(platform_stats)

print("\n2. INFLUENCER CATEGORY ANALYSIS")
print("   " + "-" * 40)
category_stats = df_clean.groupby('influencer_category').agg({
    'campaign_cost': 'sum',
    'revenue': 'sum',
    'ROAS': 'mean',
    'CAC': 'mean',
    'engagement_rate': 'mean'
}).round(2)

category_stats = category_stats.sort_values('ROAS', ascending=False)
print("\n   Top Categories by ROAS:")
print(category_stats.head(10))

print("\n3. CAMPAIGN TYPE ANALYSIS")
print("   " + "-" * 40)
campaign_type_stats = df_clean.groupby('campaign_type').agg({
    'revenue': 'sum',
    'ROAS': 'mean',
    'CAC': 'mean',
    'product_sales': 'sum'
}).round(2)

campaign_type_stats = campaign_type_stats.sort_values('ROAS', ascending=False)
print("\n   Campaign Type Performance:")
print(campaign_type_stats)

print("\n4. KEY INSIGHTS FOR BUDGET ALLOCATION")
print("   " + "-" * 40)

# Best performing platform by ROAS
best_platform = platform_stats.sort_values('ROAS', ascending=False).index[0]
best_platform_roas = platform_stats.loc[best_platform, 'ROAS']

print(f"\n   🏆 Best Platform: {best_platform}")
print(f"      - ROAS: {best_platform_roas:.2f}")
print(f"      - Average CAC: ${platform_stats.loc[best_platform, 'CAC']:.2f}")

# Best performing category
best_category = category_stats.sort_values('ROAS', ascending=False).index[0]
best_category_roas = category_stats.loc[best_category, 'ROAS']

print(f"\n   🏆 Best Influencer Category: {best_category}")
print(f"      - ROAS: {best_category_roas:.2f}")
print(f"      - Average CAC: ${category_stats.loc[best_category, 'CAC']:.2f}")

# Best performing campaign type
best_campaign = campaign_type_stats.sort_values('ROAS', ascending=False).index[0]
print(f"\n   🏆 Best Campaign Type: {best_campaign}")
print(f"      - ROAS: {campaign_type_stats.loc[best_campaign, 'ROAS']:.2f}")

# ============================================================================
# STEP 7: SAVE CLEANED DATA
# ============================================================================
print("\n\n💾 STEP 6: SAVING CLEANED DATA")
print("-" * 80)

output_file = 'influencer_marketing_cleaned.csv'
df_clean.to_csv(output_file, index=False)
print(f"\n✓ Cleaned data saved to: {output_file}")

# Also save summary statistics for dashboard
summary_by_platform = platform_stats.to_csv('summary_by_platform.csv')
print(f"✓ Platform summary saved to: summary_by_platform.csv")

# ============================================================================
# STEP 8: DASHBOARD PREPARATION TIPS
# ============================================================================
print("\n\n📈 STEP 7: NEXT STEPS FOR DASHBOARD")
print("-" * 80)
print("""
For your dashboard, you can now visualize:

1. BUDGET ALLOCATION RECOMMENDATIONS:
   - Show spend by platform (pie chart or bar chart)
   - Recommend allocating more budget to high-ROAS platforms
   - Display ROI by influencer category

2. ROAS ANALYSIS:
   - Line chart showing ROAS trends over time
   - Comparison by platform (bar chart)
   - Heatmap of ROAS by platform × campaign type

3. CAC BY CHANNEL:
   - Bar chart of average CAC by platform
   - Comparison with industry benchmarks
   - CAC trends over time

4. ADDITIONAL METRICS:
   - Engagement rate by platform
   - Conversion rate analysis
   - Campaign duration impact on performance

Tools you can use for dashboards:
   - Streamlit (easiest for beginners)
   - Plotly Dash
   - Power BI / Tableau (import the cleaned CSV)
   - matplotlib/seaborn for static reports
""")

print("\n" + "=" * 80)
print("✅ TUTORIAL COMPLETE!")
print("=" * 80)
print(f"\nYou've successfully cleaned {len(df_clean):,} records!")
print("The cleaned data is ready for dashboard creation.")
print("\nNext: Run the visualization script (02_create_visualizations.py)")
