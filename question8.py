import re
import pandas as pd

# Define regular expression pattern to match URL format
url_pattern = r'^[a-z]+:\/\/[a-z0-9_]+\.[a-z0-9_\.]+$'

# Load database into a Pandas dataframe
data = pd.read_csv('database.csv')

# Loop through each device type
for device_type in data['Device_Type'].unique():
    
    # Filter dataframe to access links for this device type
    access_links = data.loc[data['Device_Type'] == device_type, 'Stats_Access_Link']
    
    # Apply regular expression pattern to each access link
    urls = []
    for link in access_links:
        match = re.match(url_pattern, link.lower())
        if match:
            urls.append(match.group())
    
    # Print the list of URLs for this device type
    print(f'{device_type}: {urls}')




