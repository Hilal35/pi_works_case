import pandas as pd

# Read the CSV file into a Pandas dataframe
df = pd.read_csv('country_vaccination_stats.csv')

# Group the data by country and date, and calculate the minimum daily vaccination number per country
min_daily_vaccinations = df.groupby(['country', 'date'])['daily_vaccinations'].min().reset_index()

# Group the data by country, and fill the missing values in daily_vaccinations column with the minimum daily vaccination number of relevant countries
df['daily_vaccinations'] = df.groupby('country')['daily_vaccinations'].apply(lambda x: x.fillna(x.min()))

# Fill remaining missing values with 0
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)

# Write the resulting dataframe to a new CSV file
df.to_csv('country_vaccination_stats_imputed.csv', index=False)
