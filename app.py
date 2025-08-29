import pandas as pd

# Load Excel file
file_path = "Azure and Melbi4  Object comparison.xlsx"

# Read only Sheet5
df = pd.read_excel('C:\Users\maina\OneDrive\Desktop\BI Task\Azure and Melbi4  Object comparison.xlsx', sheet_name="Sheet5")

# Extract Column A and Column E
col_A = df.iloc[:, 0]
col_E = df.iloc[:, 4]

# Create comparison DataFrame
comparison_df = pd.DataFrame({
    "Column_A": col_A,
    "Column_E": col_E,
    "Match": col_A == col_E
})

# Keep only rows where they differ (ignoring NaN-to-NaN matches)
differences_df = comparison_df[comparison_df["Match"] == False].dropna(how='all')

# Display the differences
print(differences_df.to_string(index=False))
