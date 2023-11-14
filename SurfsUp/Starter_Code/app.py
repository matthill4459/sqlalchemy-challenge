
#################################################
# Database Setup
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, request
import datetime as dt
app = Flask(__name__)
#################################################
# Create SQLAlchemy engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    # reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Define the home route
@app.route("/")
def home():
    return (
        "Welcome to the Climate App!<br/><br/>"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/start_date<br/>"
        "/api/v1.0/start_date/end_date"
    )

# Define the /api/v1.0/precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
        # Calculate the date one year ago from the most recent date
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = (dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365)).strftime('%Y-%m-%d')

    # Perform precipitation query for the last 12 months
    results = session.query(Measurement.date, Measurement.prcp)\
        .filter(Measurement.date >= one_year_ago)\
        .filter(Measurement.date <= most_recent_date)\
        .all()

    # Convert the results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}

    # Return the JSON representation of the precipitation data
    return jsonify(precipitation_data)

# Define the /api/v1.0/stations route
@app.route("/api/v1.0/stations")
def starions():
    results = session.query(Station.station).all()

    #convert to a list
    station_list = [station[0] for station in results]

    #JSON representation as list
    return jsonify(station_list)

# Define the /api/v1.0/tobs route
@app.route("/api/v1.0/tobs")
def tobs():
        # Find the most active station
    most_active_station = session.query(Measurement.station, func.count(Measurement.station))\
        .group_by(Measurement.station)\
        .order_by(func.count(Measurement.station).desc())\
        .first()[0]
    
    # grab data 1 year from most recent date
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = (dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365)).strftime('%Y-%m-%d')

    #temp query for last 12 months
    results = session.query(Measurement.date, Measurement.tobs)\
        .filter(Measurement.station == most_active_station)\
        .filter(Measurement.date >= one_year_ago)\
        .filter(Measurement.date <= most_recent_date)\
        .all()
    
    #convert to list of dict
    tobs_list = [{"Date": date, "Temperature": tobs} for date, tobs in results]

    # jsonify it
    return jsonify(tobs_list)

# Define the start_date route with a default start date
@app.route("/api/v1.0/start_date")
def start_date():
    start_date = request.args.get("start", "2010-01-01")

    try:
        # Perform query for statistics using the start_date
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
            .filter(Measurement.date >= start_date)\
            .all()

        # Check if results contain any values
        if results and results[0][0] is not None and results[0][1] is not None and results[0][2] is not None:
            # Convert the results to a dictionary
            stats_dict = {
                "Start Date": start_date,
                "Minimum Temperature": float(results[0][0]),
                "Average Temperature": float(results[0][1]),
                "Maximum Temperature": float(results[0][2])
            }
        else:
            stats_dict = {"message": "No data available for the specified date range."}

        # Return the JSON representation of the statistics with indentation for better readability
        return jsonify(stats_dict), 200, {'Content-Type': 'application/json; charset=utf-8'}

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define the start_date/end_date route
@app.route("/api/v1.0/start_date/end_date")
def start_date_end_date():
    start_date = request.args.get("start", "2010-01-01")
    end_date = request.args.get("end", "2017-08-23")

    try:
        # Perform query for statistics using the start_date and end_date
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
            .filter(Measurement.date >= start_date)\
            .filter(Measurement.date <= end_date)\
            .all()

        # Check if results contain any values
        if results and results[0][0] is not None and results[0][1] is not None and results[0][2] is not None:
            # Convert the results to a dictionary
            stats_dict = {
                "Start Date": start_date,
                "End Date": end_date,
                "Minimum Temperature": float(results[0][0]),
                "Average Temperature": float(results[0][1]),
                "Maximum Temperature": float(results[0][2])
            }
        else:
            stats_dict = {"message": "No data available for the specified date range."}

        # Return the JSON representation of the statistics with indentation for better readability
        return jsonify(stats_dict), 200, {'Content-Type': 'application/json; charset=utf-8'}

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(debug=True)