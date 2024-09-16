# import pandas as pd

# # Load the two CSV files into DataFrames
# df1 = pd.read_csv(' BotData.csv')
# df2 = pd.read_csv('human.csv')

# # Combine the DataFrames
# # If you want to concatenate them vertically (one below the other):
# combined_df = pd.concat([df1, df2], ignore_index=True)

# # If you want to merge them horizontally (side by side), use:
# # combined_df = pd.merge(df1, df2, how='inner', on='common_column')

# # Save the combined DataFrame to a new CSV file
# combined_df.to_csv('data_without_mouse.csv', index=False)

# print("CSV files have been combined and saved to 'combined_file.csv'")
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('datak.csv')

# Drop the columns 'keystrokes[0]', 'keystrokes[1]', 'keystrokes[2]' if they exist
columns_to_drop = ['keystrokes[0]', 'keystrokes[1]', 'keystrokes[2]','ClickintervalAvg']
df = df.drop(columns=columns_to_drop, errors='ignore')  # Use 'ignore' to avoid errors if columns don't exist

# Save the updated DataFrame to a new CSV file
df.to_csv('datak1.csv', index=False)

print("Updated data saved as 'datak.csv'")
