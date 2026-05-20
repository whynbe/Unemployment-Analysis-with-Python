# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv(r'C:\Users\Vector\Desktop\Boufti_Yassine_Activité\Internships Tasks\Task 2\Unemployment in India.csv')
print(f"Data shape : {df.shape}")
print(df)

# Strip leading/trailing spaces from column names (a common issue in these datasets)
df.columns = df.columns.str.strip()
print(df)

# Display the first few rows to understand the structure
print("First 5 rows of the dataset:")
print(df.head())

# 2. Data Cleaning
# Convert the 'Date' column to a datetime object
# (Update 'Date' to whatever your date column is actually named)
df['Date'] = pd.to_datetime(df['Date'],dayfirst=True)

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Drop columns with more than 40% of its cells are missing values for accuracy reasons
missing_percent=df.isnull().mean()
df=df.loc[:,missing_percent<0.4]

# Drop rows with missing values if any exist
df = df.dropna()

# 3. Exploratory Data Analysis & Visualization
# Set the visual style
sns.set_theme(style="whitegrid")

# Create a figure for the time series plot
plt.figure(figsize=(14, 7))

# Plot the unemployment rate over time
# (Update 'Estimated Unemployment Rate' to match your column name)
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)', errorbar=None, color='red')

# 4. Highlight the COVID-19 Impact
plt.title('Unemployment Rate Over Time (Highlighting COVID-19 Impact)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Unemployment Rate (%)', fontsize=12)

# Adding a vertical span to highlight the initial COVID-19 lockdown period (roughly March 2020 - July 2020)
plt.axvspan(pd.to_datetime('2020-03-01'), pd.to_datetime('2020-07-01'), color='gray', alpha=0.3, label='COVID-19 Lockdown')

plt.legend()
plt.tight_layout()
plt.show()