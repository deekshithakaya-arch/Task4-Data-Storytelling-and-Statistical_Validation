import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# ==================================
# LOAD DATASET
# ==================================

df = pd.read_csv("Superstore data.csv")

print("=" * 60)
print("SUPERSTORE DATA STORYTELLING & STATISTICAL VALIDATION")
print("=" * 60)

print("\nDataset Preview:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

# ==================================
# DATA STORYTELLING
# ==================================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\n" + "=" * 60)
print("BUSINESS STORY")
print("=" * 60)

print(f"Total Sales  : ${total_sales:,.2f}")
print(f"Total Profit : ${total_profit:,.2f}")

print("""
Objective:
Analyze Superstore sales performance and identify
the best-performing categories, states, regions,
segments, and shipping modes.

Goal:
Improve sales, profitability, and business growth.
""")

# ==================================
# SALES BY CATEGORY
# ==================================

sales_category = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
sales_category.plot(kind="bar")
plt.title("Total Sales by Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ==================================
# PROFIT BY CATEGORY
# ==================================

profit_category = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
profit_category.plot(kind="bar")
plt.title("Total Profit by Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

# ==================================
# SALES BY REGION
# ==================================

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(7,7))
plt.pie(
    region_sales,
    labels=region_sales.index,
    autopct="%1.1f%%"
)
plt.title("Sales Distribution by Region")
plt.show()

# TOP 10 STATES BY SALES

top_states = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

sns.barplot(
    x=top_states.index,
    y=top_states.values
)

plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# SALES BY CUSTOMER SEGMENT

segment_sales = (
    df.groupby("Segment")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
sns.barplot(
    x=segment_sales.index,
    y=segment_sales.values
)

plt.title("Sales by Customer Segment")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# SALES BY SHIP MODE

ship_sales = (
    df.groupby("Ship Mode")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
sns.barplot(
    x=ship_sales.index,
    y=ship_sales.values
)

plt.title("Sales by Ship Mode")
plt.ylabel("Sales")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# CORRELATION HEATMAP

plt.figure(figsize=(8,6))

corr = df[
    ["Sales", "Quantity", "Discount", "Profit"]
].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# HYPOTHESIS TESTING

print("\n" + "=" * 60)
print("HYPOTHESIS TESTING")
print("=" * 60)

print("""
Null Hypothesis (H0):
There is no significant difference in profit
between Technology and Furniture categories.

Alternative Hypothesis (H1):
There is a significant difference in profit
between Technology and Furniture categories.
""")

tech_profit = df[df["Category"] == "Technology"]["Profit"]
furniture_profit = df[df["Category"] == "Furniture"]["Profit"]

t_stat, p_value = ttest_ind(
    tech_profit,
    furniture_profit,
    equal_var=False
)

print(f"T Statistic : {t_stat:.4f}")
print(f"P Value     : {p_value:.4f}")

if p_value < 0.05:
    print("\nResult: Reject Null Hypothesis")
    print("Significant difference exists.")
else:
    print("\nResult: Fail to Reject Null Hypothesis")
    print("No significant difference exists.")

# BUSINESS INSIGHTS

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

highest_sales_category = sales_category.idxmax()
highest_profit_category = profit_category.idxmax()
best_region = region_sales.idxmax()
best_segment = segment_sales.idxmax()
best_ship_mode = ship_sales.idxmax()
best_state = top_states.idxmax()

print(f"Highest Sales Category : {highest_sales_category}")
print(f"Highest Profit Category: {highest_profit_category}")
print(f"Best Region            : {best_region}")
print(f"Best Customer Segment  : {best_segment}")
print(f"Best Ship Mode         : {best_ship_mode}")
print(f"Top State              : {best_state}")

print("""
Recommendations:

1. Increase investment in high-profit categories.

2. Focus marketing efforts on top-performing regions.

3. Strengthen customer acquisition in profitable segments.

4. Promote efficient shipping methods.

5. Review discount strategy to improve profit margins.

6. Expand business in top-performing states.
""")

print("\nPROJECT TASK 4 COMPLETED SUCCESSFULLY")