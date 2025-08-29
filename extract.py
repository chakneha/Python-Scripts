import pandas as pd

# Try with ISO-8859-1 encoding (commonly works for Windows CSVs)
df = pd.read_csv("Book1.csv", encoding="ISO-8859-1")

# Extract last part of path
df["last_part"] = df["Path"].apply(lambda x: str(x).split("/")[-1])

# Get only unique items
unique_items = df["last_part"].unique()

# Convert to DataFrame
unique_df = pd.DataFrame(unique_items, columns=["unique_last_part"])

# Save to CSV
unique_df.to_csv("unique_last_parts.csv", index=False, encoding="utf-8")

print(unique_df)
