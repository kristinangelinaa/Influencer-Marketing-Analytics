# 📊 Tableau Dashboard Guide - Influencer Marketing ROI Analytics

## Complete Step-by-Step Tutorial to Recreate Your Streamlit Dashboard in Tableau

This guide will help you build a **professional, interactive Tableau dashboard** that matches (and enhances!) your Streamlit dashboard for portfolio presentation.

---

## 🎯 **What You'll Build**

A **3-page interactive Tableau dashboard** featuring:
- **Page 1:** Executive Overview with KPIs
- **Page 2:** ROAS Deep Dive Analysis
- **Page 3:** Budget Recommendations & Insights

All with **interactive filters, dynamic calculations, and professional design**.

---

## 📋 **Prerequisites**

### 1. Download Tableau
- **Tableau Public** (FREE): https://public.tableau.com/app/discover
- **Tableau Desktop** (14-day trial): https://www.tableau.com/products/trial

### 2. Prepare Your Data
You already have: `influencer_marketing_cleaned.csv` ✅

---

## 🚀 **PART 1: Getting Started (5 minutes)**

### Step 1: Open Tableau

1. Launch **Tableau Desktop** or **Tableau Public**
2. Click **"Connect"** → **"Text file"**
3. Navigate to your folder and select **`influencer_marketing_cleaned.csv`**
4. Click **"Open"**

### Step 2: Review Data Source

You should see the Data Source page with your data preview.

**Verify these columns are present:**
- `campaign_id`, `platform`, `campaign_type`, `topic`
- `start_date`, `end_date`, `timestamp`
- `revenue`, `campaign_cost`, `ROAS`, `CAC`
- `quality_score`, `engagement_rate`, `conversion_rate`
- `product_sales`, `engagements`, `estimated_reach`

### Step 3: Set Data Types

**Important:** Make sure data types are correct:

| Column | Correct Type |
|--------|-------------|
| `start_date`, `end_date`, `timestamp` | Date & Time |
| `revenue`, `campaign_cost`, `ROAS`, `CAC` | Number (decimal) |
| `platform`, `campaign_type`, `topic` | String |
| `product_sales`, `engagements` | Number (whole) |

**To change a data type:**
- Click the icon next to the column name
- Select the correct type (Date, Number, String)

### Step 4: Create Extract (Recommended)

For better performance:
1. Top-right corner: Click **"Extract"** (not "Live")
2. Click **"Sheet 1"** at the bottom to start building

---

## 🧮 **PART 2: Create Calculated Fields (30 minutes)**

Before building visualizations, create these essential calculated fields.

### **How to Create a Calculated Field:**
1. Right-click in the **Data pane** (left side)
2. Select **"Create Calculated Field..."**
3. Name it and paste the formula
4. Click **"OK"**

---

### **📊 Calculated Field #1: Total Records**

**Name:** `Total Records`
**Formula:**
```tableau
COUNT([Campaign Id])
```
**Purpose:** Count total campaigns

---

### **Calculated Field #2: Total Revenue**

**Name:** `Total Revenue`
**Formula:**
```tableau
SUM([Revenue])
```
**Purpose:** Sum all revenue

---

### **Calculated Field #3: Total Cost**

**Name:** `Total Cost`
**Formula:**
```tableau
SUM([Campaign Cost])
```
**Purpose:** Sum all campaign costs

---

### **Calculated Field #4: Overall ROAS**

**Name:** `Overall ROAS`
**Formula:**
```tableau
SUM([Revenue]) / SUM([Campaign Cost])
```
**Purpose:** Calculate overall return on ad spend

---

### **Calculated Field #5: Average CAC**

**Name:** `Average CAC`
**Formula:**
```tableau
AVG([Cac])
```
**Purpose:** Average customer acquisition cost

---

### **Calculated Field #6: ROI Percentage**

**Name:** `ROI %`
**Formula:**
```tableau
((SUM([Revenue]) - SUM([Campaign Cost])) / SUM([Campaign Cost])) * 100
```
**Purpose:** Return on investment as percentage

---

### **Calculated Field #7: Efficiency Score**

**Name:** `Efficiency Score`
**Formula:**
```tableau
AVG([Roas]) / AVG([Cac])
```
**Purpose:** Platform efficiency metric

---

### **Calculated Field #8: Best Platform Indicator**

**Name:** `Is Best Platform`
**Formula:**
```tableau
IF [Efficiency Score] = WINDOW_MAX([Efficiency Score])
THEN "Best"
ELSE "Other"
END
```
**Purpose:** Highlight top-performing platform
**Note:** After creating, right-click → Edit Table Calculation → Compute Using: Platform

---

### **Calculated Field #9: ROAS Color Coding**

**Name:** `ROAS Status`
**Formula:**
```tableau
IF AVG([Roas]) >= 10 THEN "Excellent (≥10x)"
ELSEIF AVG([Roas]) >= 5 THEN "Good (5-10x)"
ELSEIF AVG([Roas]) >= 2 THEN "Fair (2-5x)"
ELSE "Poor (<2x)"
END
```
**Purpose:** Categorize ROAS performance

---

### **Calculated Field #10: Month Name**

**Name:** `Month Name`
**Formula:**
```tableau
DATENAME('month', [Start Date])
```
**Purpose:** Extract month name for trending

---

### **Calculated Field #11: Year-Month**

**Name:** `Year-Month`
**Formula:**
```tableau
STR(YEAR([Start Date])) + "-" +
RIGHT("0" + STR(MONTH([Start Date])), 2)
```
**Purpose:** Create YYYY-MM format for time series

---

### **Calculated Field #12: Budget Recommendation**

**Name:** `Budget Recommendation`
**Formula:**
```tableau
IF [Efficiency Score] >= 30 THEN "Increase Budget"
ELSEIF [Efficiency Score] >= 20 THEN "Maintain"
ELSE "Decrease Budget"
END
```
**Purpose:** Automated recommendations

---

✅ **Checkpoint:** You should now have 12 calculated fields created!

---

## 📊 **PART 3: Build Dashboard Page 1 - Executive Overview (45 minutes)**

### **Layout Structure:**

```
┌─────────────────────────────────────────────────────┐
│          INFLUENCER MARKETING ROI DASHBOARD         │
├──────────┬──────────┬──────────┬──────────┬─────────┤
│ Total    │ Total    │ Total    │ Overall  │ Avg     │
│ Campaigns│ Cost     │ Revenue  │ ROAS     │ CAC     │
├──────────┴──────────┴──────────┴──────────┴─────────┤
│                                                      │
│         Budget Allocation by Platform (Pie)         │
│                                                      │
├──────────────────────────────────┬──────────────────┤
│                                  │                  │
│   ROAS by Platform (Bar)         │  Cost vs Revenue │
│                                  │  (Grouped Bar)   │
│                                  │                  │
├──────────────────────────────────┴──────────────────┤
│                                                      │
│         Revenue Trend Over Time (Line Chart)        │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

### **Sheet 1: KPI - Total Campaigns**

1. Create a new sheet (click **"+"** at bottom, rename to "KPI Total Campaigns")
2. Drag **`Total Records`** to **Text** on Marks card
3. Format:
   - Click on the number → **Format**
   - Numbers → **Number (Custom)** → `#,##0`
   - Font size: **36pt**, Bold
   - Alignment: Center
4. Add label:
   - Drag a blank field to **Rows**
   - Double-click on the column header → Type: **"Total Campaigns"**
   - Format font: 14pt, Gray

---

### **Sheet 2: KPI - Total Cost**

1. New sheet: "KPI Total Cost"
2. Drag **`Total Cost`** to **Text**
3. Format:
   - Number format: **Currency (Custom)** → `$#,##0,,.0M` (shows as millions)
   - Font: 36pt, Bold, Color: **Red (#FF6B6B)**
4. Add label: "Total Budget Spent"

---

### **Sheet 3: KPI - Total Revenue**

1. New sheet: "KPI Total Revenue"
2. Drag **`Total Revenue`** to **Text**
3. Format:
   - Number format: `$#,##0,,.0M`
   - Font: 36pt, Bold, Color: **Green (#2ECC71)**
4. Add label: "Total Revenue"

---

### **Sheet 4: KPI - Overall ROAS**

1. New sheet: "KPI ROAS"
2. Drag **`Overall ROAS`** to **Text**
3. Format:
   - Number format: `0.00`
   - Font: 36pt, Bold, Color: **Blue (#3B82F6)**
4. Add label: "Overall ROAS"
5. Add suffix:
   - Click on **AGG(Overall ROAS)** in Marks → **Format**
   - Custom → Suffix: "x"

---

### **Sheet 5: KPI - Average CAC**

1. New sheet: "KPI CAC"
2. Drag **`Average CAC`** to **Text**
3. Format:
   - Number format: `$0.00`
   - Font: 36pt, Bold
4. Add label: "Average CAC"

---

### **Sheet 6: Budget Allocation Pie Chart**

1. New sheet: "Budget Allocation"
2. Drag **`Platform`** to **Color** (on Marks card)
3. Drag **`Total Cost`** to **Angle**
4. Change mark type to **Pie** (dropdown at top of Marks card)
5. Drag **`Total Cost`** to **Label**
6. Format labels:
   - Right-click label → **Format** → Add **Percentage of Total**
   - Show: Value and Percentage
7. Colors:
   - Right-click **Platform** in Color → **Edit Colors**
   - Assign colors:
     - Instagram: `#E4405F` (Pink)
     - YouTube: `#FF0000` (Red)
     - TikTok: `#000000` (Black)
     - Twitter: `#1DA1F2` (Blue)
8. Title: "Budget Allocation by Platform"

---

### **Sheet 7: ROAS by Platform Bar Chart**

1. New sheet: "ROAS by Platform"
2. Drag **`Platform`** to **Rows**
3. Drag **`ROAS`** to **Columns**
4. Right-click `ROAS` → **Measure** → **Average**
5. Sort descending (toolbar icon)
6. Add color:
   - Drag **`ROAS Status`** to **Color**
   - Edit colors: Green (Excellent), Yellow (Good), Orange (Fair), Red (Poor)
7. Add data labels:
   - Drag **`AVG(ROAS)`** to **Label**
   - Format: `0.00`
8. Format axes:
   - Right-click Y-axis → **Format**
   - Title: "Average ROAS"
9. Add reference line:
   - Analytics pane → Drag **Reference Line** to chart
   - Value: **Constant = 1**
   - Label: "Break-even"
   - Line: Dashed, Black
10. Title: "Average ROAS by Platform"

---

### **Sheet 8: Cost vs Revenue Comparison**

1. New sheet: "Cost vs Revenue"
2. Drag **`Platform`** to **Columns**
3. Drag **`Total Cost`** to **Rows**
4. Drag **`Measure Names`** to **Color**
5. On Marks card:
   - Change to **Bar**
6. Drag **`Total Revenue`** next to `Total Cost` in Rows
7. Right-click axis → **Dual Axis**
8. Synchronize axes (right-click → **Synchronize Axis**)
9. Format:
   - Cost bars: Red
   - Revenue bars: Green
10. Title: "Cost vs Revenue by Platform"

---

### **Sheet 9: Revenue Trend Over Time**

1. New sheet: "Revenue Trend"
2. Drag **`Start Date`** to **Columns**
   - Right-click → Change to **Month**
3. Drag **`Revenue`** to **Rows** → Change to **SUM**
4. Drag **`Platform`** to **Color**
5. Change mark type to **Line**
6. Add markers:
   - Click **Color** → **Markers** → Select circle
7. Format:
   - Line width: 3
8. Add trend line (optional):
   - Analytics pane → **Trend Line**
9. Format axes:
   - Y-axis: Currency format `$#,##0,,M`
   - X-axis: "Month"
10. Title: "Revenue Trend Over Time by Platform"

---

### **Assemble Dashboard Page 1:**

1. Click **Dashboard** menu → **New Dashboard**
2. Rename: "1 - Executive Overview"
3. Set size: **Automatic** or **1200 x 800**
4. Drag sheets in this order:

   **Top Row (KPIs):**
   - Drag each KPI sheet horizontally
   - Make them equal width
   - Remove titles (right-click sheet → **Hide Title**)

   **Second Row:**
   - Drag "Budget Allocation" pie chart
   - Make it centered, medium size

   **Third Row:**
   - Drag "ROAS by Platform" (left, 50%)
   - Drag "Cost vs Revenue" (right, 50%)

   **Bottom Row:**
   - Drag "Revenue Trend" (full width)

5. Add title:
   - Drag **Text** object from left panel
   - Type: "📊 Influencer Marketing ROI Dashboard"
   - Format: 24pt, Bold, Center-aligned

6. Add filters:
   - Click on any sheet in dashboard → **Filter icon** (funnel) → Add these filters:
     - **Platform** (multi-select dropdown)
     - **Campaign Type** (multi-select)
     - **Start Date** (range slider)
   - Drag filters to right side
   - Format: **Single Value (dropdown)**

---

✅ **Checkpoint:** Page 1 complete! You should have a professional executive dashboard.

---

## 🎯 **PART 4: Build Dashboard Page 2 - ROAS Analysis (30 minutes)**

### **Sheets to Create:**

### **Sheet 10: ROAS Heatmap (Platform × Campaign Type)**

1. New sheet: "ROAS Heatmap"
2. Drag **`Platform`** to **Rows**
3. Drag **`Campaign Type`** to **Columns**
4. Drag **`ROAS`** to **Color** and **Label**
5. Change to **AVG(ROAS)**
6. Format:
   - Color: **Orange-Blue Diverging** (center at 10)
   - Labels: Show values, format `0.00`
   - Mark type: **Square**
7. Title: "ROAS Performance Matrix: Platform × Campaign Type"

---

### **Sheet 11: ROAS Distribution Box Plot**

1. New sheet: "ROAS Distribution"
2. Drag **`Platform`** to **Columns**
3. Drag **`ROAS`** to **Rows**
4. Change mark type to **Circle**
5. Analytics → **Box Plot**
6. Add reference line at ROAS = 1
7. Title: "ROAS Distribution by Platform"

---

### **Sheet 12: Top 10 Campaigns**

1. New sheet: "Top Campaigns"
2. Drag **`Campaign Id`** to **Rows**
3. Drag **`ROAS`** to **Columns**
4. Filter: Top 10 by ROAS
5. Add **`Platform`** to **Color**
6. Sort descending
7. Title: "Top 10 Campaigns by ROAS"

---

### **Assemble Dashboard Page 2:**

1. New dashboard: "2 - ROAS Deep Dive"
2. Layout:
   - Top: ROAS Heatmap (60% height)
   - Bottom left: Box Plot (40% width)
   - Bottom right: Top 10 Campaigns (60% width)
3. Add same filters as Page 1
4. Add navigation: Button to Page 1 and Page 3

---

## 💡 **PART 5: Build Dashboard Page 3 - Recommendations (40 minutes)**

### **Sheet 13: Platform Efficiency Score**

1. New sheet: "Efficiency Score"
2. Drag **`Platform`** to **Rows**
3. Drag **`Efficiency Score`** to **Columns**
4. Sort descending
5. Color: Gradient (green = high, red = low)
6. Add data labels
7. Title: "Platform Efficiency Score (ROAS/CAC)"

---

### **Sheet 14: Current vs Recommended Budget**

**This requires a custom calculation:**

1. Create calculated field: **`Current Budget %`**
```tableau
SUM([Campaign Cost]) / TOTAL(SUM([Campaign Cost]))
```

2. Create calculated field: **`Recommended Budget %`**
```tableau
// Based on efficiency score
[Efficiency Score] / TOTAL([Efficiency Score])
```

3. New sheet: "Budget Comparison"
4. Drag **`Platform`** to **Rows**
5. Drag both **`Current Budget %`** and **`Recommended Budget %`** to **Columns**
6. Format as **Percentage** (0%)
7. Change to **Bar** chart
8. Color: Current (Red), Recommended (Green)
9. Add difference labels

---

### **Sheet 15: Performance Summary Table**

1. New sheet: "Performance Table"
2. Drag **`Platform`** to **Rows**
3. Drag these to **Text** (in order):
   - **`AVG(ROAS)`**
   - **`AVG(CAC)`**
   - **`Efficiency Score`**
   - **`Total Revenue`**
4. Format as table
5. Add color coding:
   - Right-click each measure → **Format**
   - Add **color scales** (green = good, red = bad)
6. Title: "Platform Performance Summary"

---

### **Sheet 16: Action Items Text**

1. New sheet: "Recommendations"
2. Add calculated field: **`Top Platform`**
```tableau
WINDOW_MAX(MAX([Efficiency Score]))
```
3. Create text box with insights:
   - Use dashboard text object
   - Write key recommendations based on data

---

### **Assemble Dashboard Page 3:**

1. New dashboard: "3 - Budget Recommendations"
2. Layout:
   - Top left: Efficiency Score (40%)
   - Top right: Budget Comparison (60%)
   - Middle: Performance Table (full width)
   - Bottom: Action Items / Insights text box
3. Add filters
4. Add navigation buttons

---

## 🎨 **PART 6: Design & Polish (20 minutes)**

### **Global Formatting:**

1. **Font Family:** Tableau Book or Segoe UI
2. **Color Palette:**
   - Primary: `#3B82F6` (Blue)
   - Success: `#2ECC71` (Green)
   - Warning: `#F59E0B` (Orange)
   - Danger: `#E74C3C` (Red)

### **Dashboard Design Tips:**

1. **Consistent spacing:** 10px padding around all elements
2. **Remove clutter:** Hide unnecessary field labels
3. **Align elements:** Use dashboard layout containers
4. **Add context:** Tooltips with detailed information
5. **White space:** Don't overcrowd

---

## 🔄 **PART 7: Add Interactivity (15 minutes)**

### **Dashboard Actions:**

#### **1. Highlight Action**
```
Dashboard → Actions → Add Action → Highlight
- Name: "Highlight Related"
- Source: All sheets
- Target: All sheets
- Clearing: Show all values
```

#### **2. Filter Action**
```
Dashboard → Actions → Add Action → Filter
- Name: "Click to Filter"
- Source: ROAS by Platform
- Target: All sheets except source
- Clearing: Show all values
```

#### **3. URL Action (to GitHub)**
```
Dashboard → Actions → Add Action → Go to URL
- Name: "View GitHub"
- URL: https://github.com/kristinangelinaa/Influencer-Marketing-Analytics
```

---

## 📱 **PART 8: Publish to Tableau Public (10 minutes)**

### **Step 1: Optimize for Web**

1. Dashboard → Device Preview
2. Create **Mobile Layout** (optional but impressive!)
3. Simplify for smaller screens

### **Step 2: Publish**

1. **Server** → **Tableau Public** → **Save to Tableau Public As...**
2. Sign in (create free account if needed)
3. Name: "Influencer Marketing ROI Dashboard"
4. Description: "Interactive analytics dashboard analyzing 87K+ campaigns"
5. Add tags: data-analytics, marketing, roi, python
6. Click **Save**

### **Step 3: Configure Settings**

1. On Tableau Public website, click **Edit Details**
2. Make it **Public**
3. Allow **Download** (shows confidence!)
4. Add **Thumbnail** (screenshot of dashboard)

### **Step 4: Get Share Link**

Copy the embed code and share URL!

---

## 🎯 **Advanced Features (Optional)**

### **1. Dynamic Parameters**

Create a parameter to switch metrics:
```tableau
Parameter: Selected Metric
Values: ROAS, CAC, Revenue, Engagement Rate

Calculated Field: Dynamic Metric
CASE [Selected Metric]
WHEN "ROAS" THEN [Roas]
WHEN "CAC" THEN [Cac]
WHEN "Revenue" THEN [Revenue]
WHEN "Engagement Rate" THEN [Engagement Rate]
END
```

### **2. Forecasting**

On your trend chart:
- Analytics → Forecast
- 6 months into future

### **3. Clustering**

On scatter plots:
- Analytics → Cluster
- Show natural groupings

---

## 📋 **Checklist Before Publishing**

- [ ] All KPIs showing correct values
- [ ] Filters work across all dashboards
- [ ] Colors are consistent and meaningful
- [ ] Tooltips are informative
- [ ] No blank/error sheets
- [ ] Mobile layout created (optional)
- [ ] Dashboard loads quickly (< 5 seconds)
- [ ] All charts have titles
- [ ] Axes are labeled
- [ ] Tested click interactions

---

## 🔗 **After Publishing**

### **Update Your GitHub README:**

Add this section:
```markdown
## 📊 Interactive Dashboard

Explore the live Tableau dashboard:

[View Interactive Dashboard →](YOUR_TABLEAU_PUBLIC_LINK)

Features:
- Real-time filtering across 87K+ campaigns
- ROAS and CAC analysis by platform
- Budget optimization recommendations
- Mobile-responsive design
```

### **Update LinkedIn Post:**

Add:
```
🎉 UPDATE: The interactive Tableau dashboard is now live!

Explore the data yourself: [Your Tableau Link]

You can now filter by platform, date, and campaign type to see how different factors impact ROI.
```

---

## 🚀 **Your Final Deliverable**

After completing this guide, you'll have:

✅ **3-page professional Tableau dashboard**
✅ **12+ calculated fields for advanced analytics**
✅ **Interactive filters and actions**
✅ **Published on Tableau Public** (shareable link)
✅ **Mobile-responsive** (optional)
✅ **Portfolio-ready presentation**

---

## 💡 **Pro Tips**

1. **Save often** (Ctrl/Cmd + S)
2. **Test on different screen sizes**
3. **Get feedback** before final publish
4. **Update with new insights** over time
5. **Share on LinkedIn** with screenshots

---

## 🆘 **Common Issues & Solutions**

### Issue: "Calculations not working"
- Check data types are correct
- Verify field names match exactly
- Use AGG() or SUM() appropriately

### Issue: "Dashboard is slow"
- Use extracts instead of live connections
- Limit data with filters
- Simplify calculations

### Issue: "Can't publish to Tableau Public"
- Data must be < 15 million rows ✅ (you have 87K)
- Remove sensitive information
- Check internet connection

---

## 📚 **Resources**

- **Tableau Public Gallery:** https://public.tableau.com/gallery
- **Tableau Training:** https://www.tableau.com/learn/training
- **Color Picker:** https://colorbrewer2.org

---

**Estimated Total Time: 3-4 hours**

**Difficulty: Intermediate**

**Result: Professional portfolio-quality dashboard!** 🎉

---

Good luck! Let me know if you get stuck on any step! 🚀
