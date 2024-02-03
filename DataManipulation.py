import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV file into a Pandas dataframe
df = pd.read_csv('data.csv')
print("Statistics of Data:\n{} \n".format(df.describe()))
# Check for null values
print("Number of null Values in data per column: \n{} \n".format(df.isnull().sum()))

# Replace null values with the mean
df.fillna(df.mean(), inplace=True)

# Aggregate data for two columns
columns = ['Duration', 'Calories']
agg = df[columns].agg(['min', 'max', 'count', 'mean'])
print("Aggregate data of two columns (Duration, Calories) : \n {} \n".format(agg))

# Filter data with calories between 500 and 1000
df_500_1000 = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]
print("Data with calories between 500 and 1000: \n {} \n".format(df_500_1000))

# Filter data with calories > 500 and pulse < 100
df_500_pulse = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]
print("Data with calories > 500 and pulse < 100: \n {} \n".format(df_500_pulse))

# Create new dataframe without "Maxpulse" column
df_modified = df.drop('Maxpulse', axis=1)

# Delete "Maxpulse" column from the main df dataframe
df.drop('Maxpulse', axis=1, inplace=True)

# Convert "Calories" column to int datatype
df['Calories'] = df['Calories'].astype(int)

# Scatter plot for "Duration" and "Calories"

plt.scatter(df['Duration'], df['Calories'])
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.show()