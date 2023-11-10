# Import the dependencies.
from flask import Flask, jsonify
import datetime as dt

app = Flask(__name__)

# Define the home route
@app.route("/")
def home():
    return (
        f"Welcome to the Climate App!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )

# Define the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Perform your precipitation query here and jsonify the result
    # Example: results = session.query(Measurement.date, Measurement.prcp).all()
    # Convert the results to a dictionary
    # Return the JSON representation of your dictionary
    return jsonify(results_dict)

# Define the stations route
@app.route("/api/v1.0/stations")
def stations():
    # Perform your stations query here and jsonify the result
    # Example: results = session.query(Station.station).all()
    # Convert the results to a list
    # Return the JSON representation of your list
    return jsonify(results_list)

# Define the temperature observation route
@app.route("/api/v1.0/tobs")
def tobs():
    # Perform your temperature observation query here and jsonify the result
    # Example: results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station).all()
    # Convert the results to a list
    # Return the JSON representation of your list
    return jsonify(results_list)

# Define the start date route
@app.route("/api/v1.0/<start_date>")
def start_date(start_date):
    # Perform your query for statistics using the start_date and jsonify the result
    # Example: results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start_date).all()
    # Convert the results to a dictionary
    # Return the JSON representation of your dictionary
    return jsonify(results_dict)

# Define the start date and end date route
@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end_date(start_date, end_date):
    # Perform your query for statistics using both start_date and end_date and jsonify the result
    # Example: results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    # Convert the results to a dictionary
    # Return the JSON representation of your dictionary
    return jsonify(results_dict)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)



#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
