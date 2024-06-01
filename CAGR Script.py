import pandas as pd

# Load the CSV file
file_path = 'path_to_your_file/india_trade_data.csv'
df = pd.read_csv(file_path)

# Filter data to include only Export data (if needed)
export_df = df[df['Type of Trade'] == 'Export']

# Calculate the start and end values
start_values = export_df.groupby('Commodity').first().reset_index()
end_values = export_df.groupby('Commodity').last().reset_index()

# Merge the start and end values
merged_df = pd.merge(start_values, end_values, on='Commodity', suffixes=('_start', '_end'))

# Calculate the number of years
merged_df['Years'] = merged_df['year_end'] - merged_df['year_start']

# Calculate the CAGR
merged_df['CAGR'] = ((merged_df['sum USD_end'] / merged_df['sum USD_start']) ** (1 / merged_df['Years'])) - 1

# Display the resulting DataFrame
print(merged_df[['Commodity', 'sum USD_start', 'sum USD_end', 'Years', 'CAGR']])
