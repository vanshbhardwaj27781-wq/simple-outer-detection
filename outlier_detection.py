import pandas as pd

# Load the retail sales dataset
df = pd.read_csv("retail_sales.csv")

# Column used for outlier detection
column = "Sales"

# Calculate Q1, Q3 and IQR
Q1 = df[column].quantile(0.25)
Q3 = df[column].quantile(0.75)
IQR = Q3 - Q1

# Calculate the lower and upper limits
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Create an outlier table
outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)].copy()

# Add a simple status column
outliers["Outlier_Type"] = outliers[column].apply(
    lambda x: "Low Outlier" if x < lower_bound else "High Outlier"
)

# Save the result
outliers.to_csv("outlier_table.csv", index=False)

print("Simple Outlier Detection")
print("------------------------")
print(f"Q1: {Q1:.2f}")
print(f"Q3: {Q3:.2f}")
print(f"IQR: {IQR:.2f}")
print(f"Lower Bound: {lower_bound:.2f}")
print(f"Upper Bound: {upper_bound:.2f}")
print(f"Number of outliers: {len(outliers)}")
print("\nOutlier Table:")
print(outliers[["Date", "Category", "Product", "Sales", "Outlier_Type"]].to_string(index=False))
print("\nSaved: outlier_table.csv")
