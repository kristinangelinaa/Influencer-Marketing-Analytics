# 📊 TABLEAU DASHBOARD VISUALIZATION SKETCH

## Dashboard Overview
**3-Page Interactive Dashboard for Influencer Marketing ROI Analytics**

---

## 🎨 PAGE 1: EXECUTIVE OVERVIEW

### Layout Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     INFLUENCER MARKETING ROI DASHBOARD                       │
│                          EXECUTIVE OVERVIEW                                  │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│ TOTAL        │ TOTAL        │ TOTAL        │ OVERALL      │ AVERAGE      │
│ CAMPAIGNS    │ BUDGET       │ REVENUE      │ ROAS         │ CAC          │
│              │              │              │              │              │
│   87,743     │  $329.5M     │  $10.9B      │   33.14x     │   $7.23      │
│              │              │              │              │              │
│   📊         │   💰         │   💵         │   📈         │   🎯         │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────┘

┌─────────────────────────────────┬──────────────────────────────────────────┐
│ PLATFORM PERFORMANCE TABLE      │ ROAS BY PLATFORM (BAR CHART)             │
│                                 │                                          │
│  Platform  │ ROAS  │ CAC  │Scr │          ┌─┐                             │
│  ─────────┼───────┼──────┼─── │          │█│                             │
│  Twitter   │183.17 │ $5.11│35.9│          │█│                             │
│  TikTok    │ 47.62 │ $6.84│6.96│          │█│                             │
│  Instagram │  9.89 │ $8.24│1.20│          │█│         ┌─┐                 │
│  YouTube   │  8.77 │ $7.75│1.13│          │█│         │█│  ┌─┐  ┌─┐      │
│                                 │          │█│         │█│  │█│  │█│      │
│  🏆 Best: Twitter               │          └─┘         └─┘  └─┘  └─┘      │
│     ROAS: 183.17x               │        Twitter    TikTok Inst  YouTube   │
│     CAC: $5.11                  │                                          │
└─────────────────────────────────┴──────────────────────────────────────────┘

┌─────────────────────────────────┬──────────────────────────────────────────┐
│ CAC ANALYSIS (HORIZONTAL BARS)  │ REVENUE TREND (LINE CHART)               │
│                                 │                                          │
│  Twitter    ███████ $5.11       │                            ╱Twitter      │
│  TikTok     █████████ $6.84     │                        ╱╱╱              │
│  YouTube    ██████████ $7.75    │                    ╱╱╱  ╱TikTok         │
│  Instagram  ███████████ $8.24   │                ╱╱╱   ╱╱╱                │
│                                 │            ╱╱╱    ╱╱Instagram           │
│  Lower CAC = Better             │        ╱╱╱    ╱╱╱  YouTube              │
│                                 │    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱                      │
└─────────────────────────────────┴──────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ BUDGET ALLOCATION (PIE CHART)                                               │
│                                                                             │
│                      ╱──────╲                                               │
│                   ╱            ╲                                            │
│                 │  YouTube 40.4% │                                          │
│                 │  Instagram 37% │                                          │
│                  │  TikTok 16%  │                                           │
│                   │ Twitter 6.7%│                                           │
│                     ╲──────╱                                                │
│                                                                             │
│  ⚠️ Twitter is underallocated despite best performance                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Visual Components

1. **KPI Cards (Top Row)**
   - Type: Big Number + Icon
   - Metrics: Total Campaigns, Budget, Revenue, ROAS, CAC
   - Color: Light backgrounds with border highlights
   - Font: Large numbers, small labels

2. **Platform Performance Table (Left Middle)**
   - Type: Cross-tab table with conditional formatting
   - Columns: Platform, ROAS, CAC, Efficiency Score
   - Sorting: By Efficiency Score (descending)
   - Highlight: Best performer (Twitter) in green

3. **ROAS Bar Chart (Center Middle)**
   - Type: Vertical bar chart
   - X-Axis: Platform
   - Y-Axis: ROAS value
   - Color: Color-coded by platform
   - Labels: Value on top of each bar

4. **CAC Horizontal Bar Chart (Right Middle)**
   - Type: Horizontal bar chart
   - Y-Axis: Platform
   - X-Axis: CAC ($)
   - Color: Green (low) to Red (high)
   - Sorting: Ascending (lowest CAC at top)

5. **Revenue Trend Line Chart (Left Bottom)**
   - Type: Multi-line chart
   - X-Axis: Month
   - Y-Axis: Revenue
   - Lines: 4 lines (one per platform)
   - Markers: Points on each data point

6. **Budget Allocation Pie Chart (Right Bottom)**
   - Type: Pie chart with labels
   - Segments: 4 platforms
   - Labels: Platform name + percentage
   - Colors: Distinct colors per platform

---

## 📈 PAGE 2: ROAS DEEP DIVE ANALYSIS

### Layout Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          ROAS DEEP DIVE ANALYSIS                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ ROAS BY CAMPAIGN TYPE (GROUPED BAR CHART)                                   │
│                                                                             │
│  ┌─┐┌─┐┌─┐┌─┐   ┌─┐┌─┐┌─┐┌─┐   ┌─┐┌─┐┌─┐┌─┐   ┌─┐┌─┐┌─┐┌─┐   ┌─┐┌─┐┌─┐┌─┐│
│  │█││█││█││█│   │█││█││█││█│   │█││█││█││█│   │█││█││█││█│   │█││█││█││█││
│  │█││█││█││█│   │█││█││█││█│   │█││█││█││█│   │█││█││█││█│   │█││█││█││█││
│  └─┘└─┘└─┘└─┘   └─┘└─┘└─┘└─┘   └─┘└─┘└─┘└─┘   └─┘└─┘└─┘└─┘   └─┘└─┘└─┘└─┘│
│ Seasonal Sale  Product Launch Brand Awareness  Flash Sale      Giveaway     │
│                                                                             │
│ Legend: ■ Twitter  ■ TikTok  ■ Instagram  ■ YouTube                         │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────┬──────────────────────────────────────┐
│ ROAS HEATMAP                         │ TOP 10 CAMPAIGNS BY ROAS             │
│ Platform × Influencer Category       │                                      │
│                                      │  Rank │ Campaign │ Platform │ ROAS  │
│         Fashion Tech Fitness Food... │  ──────────────────────────────────  │
│ Twitter   █████  ████  █████  ████  │  🥇 1 │ C12345  │ Twitter  │ 245.6x │
│ TikTok    ████   ████  ████   ████  │  🥈 2 │ C67890  │ Twitter  │ 198.3x │
│ Instagram ███    ███   ███    ███   │  🥉 3 │ C45678  │ TikTok   │ 187.4x │
│ YouTube   ███    ██    ███    ██    │    4  │ C23456  │ Twitter  │ 176.2x │
│                                      │    5  │ C78901  │ TikTok   │ 165.8x │
│ Color Scale:                         │    6  │ C34567  │ Twitter  │ 159.1x │
│ ███ High (>100)                      │    7  │ C89012  │ TikTok   │ 152.7x │
│ ███ Medium (50-100)                  │    8  │ C56789  │ Twitter  │ 148.3x │
│ ███ Low (<50)                        │    9  │ C01234  │ Instagram│ 142.9x │
│                                      │   10  │ C12340  │ Twitter  │ 138.5x │
└──────────────────────────────────────┴──────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ ROAS DISTRIBUTION BY PLATFORM (BOX PLOT)                                    │
│                                                                             │
│           ○                         ○                                       │
│           │                         ○                                       │
│         ┌───┐                     ┌───┐                                     │
│         │███│           ○         │   │           ○         ○               │
│      ○  │███│         ┌───┐       │   │         ┌───┐     ┌───┐            │
│      │  │███│         │███│       │   │         │   │     │   │            │
│      │  └───┘         │███│       └───┘         │   │     │   │            │
│                       └───┘                     └───┘     └───┘            │
│     Twitter         TikTok      Instagram      YouTube                      │
│                                                                             │
│  Higher box = Higher ROAS    ○ = Outliers                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Visual Components

1. **ROAS by Campaign Type (Top)**
   - Type: Grouped/clustered bar chart
   - X-Axis: Campaign Type (5 categories)
   - Y-Axis: ROAS
   - Groups: 4 bars per campaign type (one per platform)
   - Colors: Platform colors
   - Legend: Platform names

2. **ROAS Heatmap (Bottom Left)**
   - Type: Highlight table / heatmap
   - Rows: Platforms (4)
   - Columns: Influencer Categories (Fashion, Tech, Fitness, Food, Travel)
   - Color: Gradient from red (low) to dark green (high)
   - Values: ROAS displayed in each cell

3. **Top 10 Campaigns Table (Bottom Right)**
   - Type: Ranked table with icons
   - Columns: Rank, Campaign ID, Platform, ROAS, Revenue
   - Sorting: By ROAS (descending)
   - Formatting: Top 3 with medal icons
   - Conditional formatting: ROAS values color-coded

4. **ROAS Distribution Box Plot (Bottom)**
   - Type: Box and whisker plot
   - X-Axis: Platform
   - Y-Axis: ROAS distribution
   - Elements: Box (IQR), median line, whiskers, outliers
   - Color: Platform colors with transparency

---

## 💡 PAGE 3: BUDGET RECOMMENDATIONS & OPTIMIZATION

### Layout Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  BUDGET RECOMMENDATIONS & OPTIMIZATION                       │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────┬──────────────────────────────────────┐
│ BUDGET ALLOCATION COMPARISON         │ PLATFORM EFFICIENCY RANKINGS         │
│                                      │                                      │
│   CURRENT      →      RECOMMENDED    │  🥇 1st Twitter  ████████████ 35.85 │
│     ╱───╲            ╱───╲          │  🥈 2nd TikTok   ██ 6.96             │
│    │40.4%│          │40.9%│         │  🥉 3rd Instagram █ 1.20             │
│    │ YT  │          │ TW  │         │     4th YouTube  █ 1.13             │
│    │37%IG│          │28.5%│         │                                      │
│    │16%TT│          │ TT  │         │  Efficiency = ROAS ÷ CAC            │
│    │6.7%│           │21%IG│         │                                      │
│     ╲───╱            ╲9.6%╱         │  Higher score = Better performance   │
│                        YT            │                                      │
│                                      │                                      │
│ Platform Changes:                    │                                      │
│ • YouTube:   40.4% → 9.6%  (-30.8%) │                                      │
│ • Instagram: 37.0% → 21.0% (-15.9%) │                                      │
│ • TikTok:    16.0% → 28.5% (+12.5%) │                                      │
│ • Twitter:    6.7% → 40.9% (+34.2%) │                                      │
└──────────────────────────────────────┴──────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ PROJECTED IMPACT OF BUDGET REALLOCATION (WATERFALL CHART)                   │
│                                                                             │
│                                                                  ┌────┐     │
│                                              ┌────┐              │    │     │
│                           ┌────┐             │    │              │    │     │
│          ┌────┐           │    │             │    │              │130M│     │
│          │    │           │    │       ╱─╲   │    │        ╱─╲   │    │     │
│          │100M│     ╱─╲   │    │      │-8M│  │    │       │-12M│ │    │     │
│          │    │    │+35M│ │    │       ╲─╱   │    │        ╲─╱   │    │     │
│          └────┘     ╲─╱   │    │             │    │              │    │     │
│                            │+15M│             │    │              │    │     │
│                             ╲─╱               │    │              │    │     │
│        Current    Twitter  TikTok  Instagram YouTube           Projected    │
│        Revenue   Increase Increase Reduction Reduction          Revenue     │
│                                                                             │
│  Net Impact: +$30M projected revenue increase (+30%)                        │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────┬──────────────────────────────────────┐
│ KEY RECOMMENDATIONS                  │ EXPECTED OUTCOMES                    │
│                                      │                                      │
│ ① Increase Twitter budget from       │ Revenue Increase      +30%  $3.3B   │
│   6.7% to 40.9%                      │                                      │
│   Reason: Highest ROAS (183.17x)     │ ROAS Improvement      +45%  48.1x   │
│          Lowest CAC ($5.11)          │                                      │
│                                      │ CAC Reduction         -25%  $5.42   │
│ ② Scale TikTok investment from       │                                      │
│   16.0% to 28.5%                     │ ROI Growth            +52%  4,710%  │
│   Reason: Strong ROAS (47.62x)       │                                      │
│          Growing platform            │ ✅ Based on historical performance   │
│                                      │ ✅ Conservative estimates            │
│ ③ Reduce YouTube allocation from     │ ✅ Quarterly review recommended      │
│   40.4% to 9.6%                      │                                      │
│   Reason: Low ROAS (8.77x)           │                                      │
│          High CAC ($7.75)            │                                      │
│                                      │                                      │
│ ④ Focus on Seasonal Sale campaigns   │                                      │
│   Reason: Best campaign type         │                                      │
│          ROAS: 124.75x               │                                      │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

### Visual Components

1. **Budget Allocation Comparison (Top Left)**
   - Type: Side-by-side pie charts
   - Left pie: Current allocation
   - Right pie: Recommended allocation
   - Below: Change table showing % shifts
   - Colors: Consistent platform colors
   - Annotations: Change percentages with +/- indicators

2. **Efficiency Rankings (Top Right)**
   - Type: Horizontal bar chart with icons
   - Y-Axis: Platform (ranked)
   - X-Axis: Efficiency Score
   - Icons: Medal icons for top 3
   - Colors: Platform colors
   - Formula displayed below

3. **Waterfall Chart (Middle)**
   - Type: Waterfall/bridge chart
   - Shows: Current → Changes → Projected
   - Bars: Green for increases, red for decreases
   - Connecting lines between bars
   - Total bars in blue
   - Labels: Dollar amounts on each bar

4. **Recommendations Panel (Bottom Left)**
   - Type: Text box with numbered list
   - Format: Action item + reasoning
   - Icons: Numbers in circles
   - Highlighting: Key metrics in bold

5. **Expected Outcomes Panel (Bottom Right)**
   - Type: Metric cards / KPI list
   - Format: Metric name | Change % | New value
   - Colors: Green for positive changes
   - Checkmarks: Validation notes

---

## 🎨 DESIGN SPECIFICATIONS

### Color Palette

**Platform Colors:**
- Twitter: #4CAF50 (Green)
- TikTok: #8BC34A (Light Green)
- Instagram: #FFC107 (Amber)
- YouTube: #FF9800 (Orange)

**UI Colors:**
- Background: #F5F5F5 (Light Gray)
- Text: #212121 (Dark Gray)
- Headers: #37474F (Blue Gray)
- Borders: #BDBDBD (Gray)

**Performance Colors:**
- High/Good: #1B5E20 (Dark Green)
- Medium: #FDD835 (Yellow)
- Low/Bad: #D32F2F (Red)

### Typography

- **Dashboard Title:** 24pt, Bold, Dark Gray
- **Section Headers:** 14pt, Bold, White on Dark Background
- **KPI Numbers:** 32pt, Bold, Platform Color
- **KPI Labels:** 10pt, Regular, Gray
- **Table Headers:** 10pt, Bold, Dark Gray
- **Table Values:** 9pt, Regular, Black
- **Annotations:** 8pt, Italic, Gray

### Interactivity

**Filters (Available on all pages):**
1. Platform (Multi-select)
2. Date Range (Slider)
3. Campaign Type (Dropdown)
4. Influencer Category (Multi-select)

**Actions:**
1. Click platform → Filter all charts
2. Hover on bars/lines → Show tooltip with details
3. Click on table row → Highlight in other charts
4. Export to PDF/Excel buttons

### Tooltips

**Should include:**
- Platform name
- Exact values (ROAS, Revenue, CAC)
- Date/Campaign name when relevant
- Comparison to average

### Mobile Responsiveness

- Automatic layout for tablets
- Stacked vertical layout for phones
- Touch-friendly filter controls
- Simplified charts on small screens

---

## 📋 IMPLEMENTATION CHECKLIST

### Before Building:
- [ ] Load influencer_marketing_cleaned.csv into Tableau
- [ ] Verify all calculated fields are created
- [ ] Set up data relationships if using multiple data sources

### Page 1 - Executive Overview:
- [ ] Create 5 KPI cards with big number formatting
- [ ] Build platform performance cross-tab table
- [ ] Create vertical ROAS bar chart
- [ ] Create horizontal CAC bar chart
- [ ] Build multi-line revenue trend chart
- [ ] Create budget allocation pie chart
- [ ] Add platform filter
- [ ] Add date range filter

### Page 2 - ROAS Analysis:
- [ ] Create grouped bar chart for campaign types
- [ ] Build ROAS heatmap with color gradient
- [ ] Create top 10 campaigns ranked table
- [ ] Build box plot for ROAS distribution
- [ ] Add campaign type filter
- [ ] Link filters to Page 1

### Page 3 - Budget Recommendations:
- [ ] Create side-by-side pie charts
- [ ] Build change comparison table
- [ ] Create efficiency horizontal bar chart
- [ ] Build waterfall/bridge chart
- [ ] Add recommendations text box
- [ ] Add outcomes metrics panel
- [ ] Ensure all filters work across pages

### Final Polish:
- [ ] Apply consistent color scheme
- [ ] Add dashboard title on each page
- [ ] Set up page navigation
- [ ] Test all interactive elements
- [ ] Add footer with data source info
- [ ] Preview on different screen sizes
- [ ] Export screenshots for documentation

---

## 🚀 QUICK START GUIDE

1. **Open Tableau Desktop**
2. **Connect to Data:** influencer_marketing_cleaned.csv
3. **Create Calculated Fields** (refer to TABLEAU_DASHBOARD_GUIDE.md)
4. **Build Page 1:** Start with KPIs, then charts
5. **Build Page 2:** Focus on ROAS deep dive
6. **Build Page 3:** Create recommendation views
7. **Add Filters:** Apply to all pages
8. **Format & Polish:** Colors, fonts, spacing
9. **Test:** All interactions and filters
10. **Publish:** To Tableau Public

---

## 💡 TIPS FOR SUCCESS

✓ **Use containers** for better layout control
✓ **Apply consistent spacing** between elements (10-15px)
✓ **Test filters** on all charts before proceeding
✓ **Save frequently** throughout the build process
✓ **Use tooltips** to provide additional context
✓ **Keep it simple** - don't overcrowd visualizations
✓ **Color code consistently** - same platform = same color
✓ **Add annotations** for key insights
✓ **Preview regularly** to check overall design
✓ **Document your work** - add comments in calculated fields

---

*This sketch provides a visual roadmap for building your Tableau dashboard. Follow the layout, implement the components, and customize as needed for your presentation.*
