import pandas as pd

# Read the imputed CSV file into a Pandas dataframe
df = pd.read_csv('country_vaccination_stats_imputed.csv')

# Group the data by country, and calculate the median daily vaccination number per country
median_daily_vaccinations = df.groupby('country')['daily_vaccinations'].median().reset_index()

# Sort the median daily vaccination numbers in descending order, and select the top-3 countries
top_3_countries = median_daily_vaccinations.sort_values(by='daily_vaccinations', ascending=False).head(3)

# Print the top-3 countries with highest median daily vaccination numbers
print("Top-3 countries with highest median daily vaccination numbers (imputed version):")
print(top_3_countries.to_string(index=False))
