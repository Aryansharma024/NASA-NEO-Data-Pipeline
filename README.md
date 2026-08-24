# NASA-NEO-Data-Pipeline

☄️ NASA Near-Earth Object (NEO) Data Pipeline & Analytics

Power BI Dashboard](IMG-20260823-WA0008.jpg)

Project Overview
This project is an *end-to-end ETL data pipeline* designed to extract, transform, and visualize live data regarding Near-Earth Objects (asteroids) tracked by NASA. The goal of this analysis is to categorize potential planetary threats based on size, brightness (magnitude), and proximity, translating raw JSON API data into an interactive, actionable Power BI dashboard.

Technical Stack
  Python (Extraction & Loading): `requests`, `pandas`, `sqlalchemy`, `pymysql`
MySQL (Data Transformation): Relational database design, analytical window functions, logical categorization, and view creation.
Power BI (Visualization):Data modeling, interactive filtering, and custom visualization design (Scatter Plots, Clustered Bar Charts, KPI Cards).

Architecture & Pipeline Flow

1. Extract (Python)
* Connected to the *NASA Open Data REST API* (`/neo/rest/v1/neo/browse`).
* Parsed complex, nested JSON responses into a flattened list of dictionaries.
* Converted the structured data into a Pandas DataFrame for pre-processing.

2. Load (Python to MySQL)
* Established a localized connection to a MySQL database (`ASTRO_DB`) utilizing SQLAlchemy.
* Programmatically loaded the Pandas DataFrame directly into a staging table (`RAW_NEO_DATA`) for secure storage.

3. Transform (MySQL)
Rather than performing heavy transformations in Power BI, I utilized MySQL to shift the processing load to the database layer. I engineered an analytical view (`VW_NEO_ANALYTICS`) that:
* Calculated the precise average diameter of each object based on minimum and maximum estimates.
* Cleaned boolean text fields for readable hazard classifications ("Hazardous" vs. "Safe").
* Utilized SQL Window Functions. (RANK() OVER(PARTITION BY...) to rank asteroids by size within their specific hazard categories.

4. Visualize (Power BI)
Connected Power BI directly to the MySQL analytical view to build an interactive threat-tracking dashboard featuring:
Threat Matrix (Scatter Plot):Mapping the correlation between an object's brightness (magnitude) and its estimated diameter.
*Hazard Breakdown (Donut Chart):* Displaying the overall proportion of tracked objects that pose a potential threat.
*Top 10 Action List (Bar Chart):* A dynamic, filtered visual isolating the 10 largest hazardous asteroids for immediate identification (highlighting massive objects like 1036 Ganymed).

Repository Files
*`01_extract_load_neo.py`: The Python script responsible for hitting the NASA API and loading the data into MySQL.
* `02_transform_neo.sql`: The SQL script used to create the database schema and the analytical views.


How to Run Locally
1. Clone this repository.
2. Ensure you have MySQL Server installed and running locally on port `3306`.
3. Create a database named `ASTRO_DB` in your MySQL environment.
4. Install required Python packages: `pip install requests pandas sqlalchemy pymysql`.
5. Update the MySQL connection string in `01_extract_load_neo.py` with your local credentials and execute the script.
6. Run `02_transform_neo.sql` in your MySQL environment to generate the analytical views.
7. Open Power BI, connect to your local MySQL database, and load the `VW_NEO_ANALYTICS` view.


Aryan Sharma 
Connect with me:[Insert your LinkedIn Profile URL here]
