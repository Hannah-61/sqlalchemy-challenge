# Import the dependencies
import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Flask setup
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables using the updated parameter
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session (link) from Python to the database
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the last 12 months of precipitation data"""
    # Calculate the date one year from the last date in the dataset
    latest_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(latest_date, "%Y-%m-%d") - dt.timedelta(days=365)
    
    # Query for the last 12 months of precipitation data
    precipitation_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    
    # Convert to dictionary
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""
    results = session.query(Station.station).all()
    # Convert list of tuples into normal list
    stations_list = [station[0] for station in results]
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the temperature observations (TOBS) for the previous year for the most active station."""
    # Calculate the date one year from the last date in the dataset
    latest_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(latest_date, "%Y-%m-%d") - dt.timedelta(days=365)

    # Find the most active station
    most_active_station = session.query(Measurement.station).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()[0]

    # Query the last 12 months of temperature observation data for this station
    tobs_data = session.query(Measurement.tobs).filter(Measurement.station == most_active_station).filter(Measurement.date >= one_year_ago).all()
    # Unpack results
    tobs_list = [tobs[0] for tobs in tobs_data]
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_stats(start, end=None):
    """Return TMIN, TAVG, and TMAX for a given start or start-end range."""
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).filter(Measurement.date >= start).all()
    else:
        results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Unpack results
    temp_stats = list(results[0])
    return jsonify(temp_stats)

# Close session when the app stops
@app.teardown_appcontext
def close_session(exception=None):
    session.close()

if __name__ == "__main__":
    app.run(debug=True)
