import requests
import pandas as pd
from sqlalchemy import create_engine

# 1. Fetch Data from NASA API
url = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=DEMO_KEY"
response = requests.get(url)
data = response.json()

# 2. Parse the nested JSON into a flat list of dictionaries
neo_list = []
for neo in data['near_earth_objects']:
    neo_list.append({
        'NEO_REFERENCE_ID': neo['neo_reference_id'],
        'NAME': neo['name'],
        'ABSOLUTE_MAGNITUDE_H': neo['absolute_magnitude_h'],
        'ESTIMATED_DIAMETER_MIN_KM': neo['estimated_diameter']['kilometers']['estimated_diameter_min'],
        'ESTIMATED_DIAMETER_MAX_KM': neo['estimated_diameter']['kilometers']['estimated_diameter_max'],
        'IS_POTENTIALLY_HAZARDOUS': str(neo['is_potentially_hazardous_asteroid']) # Cast boolean to string
    })

# 3. Convert to a Pandas DataFrame
df = pd.DataFrame(neo_list)

# 4. Connect to local MySQL using SQLAlchemy
# Format: mysql+pymysql://<username>:<password>@localhost/<database_name>
# Replace 'YOUR_PASSWORD' with your actual MySQL Workbench root password
engine = create_engine("mysql+pymysql://root:Jimmy256%40@localhost/ASTRO_DB")

# 5. Write the DataFrame directly into a new MySQL table
df.to_sql(name='RAW_NEO_DATA', con=engine, if_exists='replace', index=False)

print(f"Pipeline Success: Loaded {len(df)} rows into the RAW_NEO_DATA table in MySQL.")