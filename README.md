# Climate Analysis API Project

## Overview
This project is a data analysis and API development exercise focused on climate data for Honolulu, Hawaii. Using Python, SQLAlchemy, Flask, Pandas, and Matplotlib, we analyze historical weather data to uncover trends in temperature and precipitation. We then create a Flask API with several endpoints, allowing users to query this data dynamically.

## Project Files
The main components of this project are:

- **`climate_starter.ipynb`**: A Jupyter Notebook where climate data is analyzed and visualized. Here, we explore precipitation patterns and temperature trends over time.
- **`app.py`**: A Flask-based API that serves climate data based on SQL queries. This script defines several endpoints for accessing climate information in JSON format.
- **`Resources/`**: Contains the SQLite database (`hawaii.sqlite`) and related CSV files with climate data.

## Key Features

1. **Data Analysis**:
   - Uses SQLAlchemy to query a SQLite database for precipitation and temperature data.
   - Analyzes data to identify trends in temperature and precipitation over time.
   - Visualizations in `climate_starter.ipynb` reveal yearly and monthly weather patterns.

2. **Flask API**:
   - Develops a RESTful API with endpoints to retrieve climate information.
   - Allows users to specify date ranges for temperature and precipitation data.
   - Returns JSON responses that can be used in web applications or further data analysis.

## Installation and Setup

1. **Clone the Repository**:

   git clone https://github.com/Hannah-61/sqlalchemy-challenge.git
   cd sqlalchemy-challenge

2.Install Required Packages: This project requires Python 3.x and the following packages:

SQLAlchemy
Flask
Pandas
Matplotlib
datetime (Python standard library)

##You can install the required packages with:

pip install -r requirements.txt
Run the Flask API: Start the API by running the app.py script:

python app.py
The API will be accessible at http://127.0.0.1:5000/.

--API Endpoints
The following endpoints are available in the Flask API:

Homepage: /

Lists all available routes.
Precipitation Data: /api/v1.0/precipitation

Returns the last 12 months of precipitation data as JSON with dates as keys and precipitation values.
Station Data: /api/v1.0/stations

Returns a JSON list of all weather stations in the dataset.
Temperature Observations (TOBS): /api/v1.0/tobs

Returns temperature observations for the previous year from the most active station.
Temperature Stats by Start Date: /api/v1.0/<start>

Replace <start> with a start date in YYYY-MM-DD format.
Returns minimum, average, and maximum temperatures for all dates greater than or equal to the start date.
Temperature Stats by Start and End Dates: /api/v1.0/<start>/<end>

Replace <start> and <end> with dates in YYYY-MM-DD format.
Returns minimum, average, and maximum temperatures for dates between the specified start and end dates, inclusive.

--Example API Usage
After running app.py, use the following URLs in your browser or API client (like Postman) to retrieve data:

Precipitation Data: http://127.0.0.1:5000/api/v1.0/precipitation
Station Data: http://127.0.0.1:5000/api/v1.0/stations
Temperature Observations: http://127.0.0.1:5000/api/v1.0/tobs
Temperature Stats from Start Date: http://127.0.0.1:5000/api/v1.0/2017-01-01
Temperature Stats from Start to End Date: http://127.0.0.1:5000/api/v1.0/2017-01-01/2017-12-31

##Data Sources
The climate data used in this project is sourced from the Hawaii SQLite database, which contains daily weather observations.

--Technologies Used
Python 3: Core programming language for scripting and data analysis.
SQLAlchemy: ORM for interacting with the SQLite database.
Flask: Lightweight web framework to create RESTful APIs.
Pandas: Library for data manipulation and analysis.
Matplotlib: Library for data visualization in the Jupyter Notebook.

--Potential Improvements
Expanding the API to include additional climate metrics.
Deploying the Flask API to a cloud service like Heroku or Render for public access.
Adding user authentication to control access to certain endpoints.

--Author
Created by Hanife Sahin.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
