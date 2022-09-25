import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

###########  The following code is nearly identical to Day 3 Activity 10 
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
######  There are 2 tables in the db
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
###### Everything you need here can be found in Day 3 Activity 10
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>< and /api/v1.0/<start>/<end><br/>"
    )

###### the 'precipitation' route you will query and return the data Day 3 Activity 10
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    session = Session(engine)
    """Return the precipitation data for the last year"""
    # Calculate the date 1 year ago from last date in database
    last_date = dt.date(2017,8,23) - dt.timedelta(days=365)

    # Query for the date and precipitation for the last year
    prcp_query = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date>=last_date).\
        order_by(Measurement.date).all()

    #precipitation = session.query(Measurement.date, Measurement.prcp).\
        #filter(Measurement.date >= prev_year).all()

    # Dict with date as the key and prcp as the value
    prcp_data = []
    for date, prcp in prcp_query:
        prcp_dict = {}
        prcp_dict['date'] = date
        prcp_dict['prcp'] = prcp
        prcp_data.append(prcp_dict)

    return jsonify(prcp_data)


###### the 'stations' route you will query and return the data Day 3 Activity 10
@app.route("/api/v1.0/stations")
def stations():
    
    session = Session(engine)

    """Return a list of stations."""
    results = session.query(Station.name).all()

    # Unravel results into a 1D array and convert to a list
    list_station = list(np.ravel(results))

    return jsonify(list_station)

###### the 'tobs' route you will query and return the data Day 3 Activity 10
@app.route("/api/v1.0/tobs")
def temp_monthly():
    #Create a session(link)
    session = Session(engine)

    """Return the temperature observations (tobs) for previous year."""
    # Calculate the date 1 year ago from last date in database
    last_date = dt.date(2017,8,23) - dt.timedelta(days=365)

    active_station_list= session.query(Measurement.station,func.count(Measurement.station)).\
        group_by(Measurement.station).\
            order_by(func.count(Measurement.station).desc()).all()

    primary_station = active_station_list[0][0]
    print(primary_station)
        
    # Query the primary station for all tobs from the last year
    primary = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == primary_station ).\
        filter(Measurement.date >=last_date).\
        group_by(Measurement.date).all()

    # Unravel results into a 1D array and convert to a list
    yearly_temp = list(np.ravel(primary))

    # Return the results
    return jsonify(yearly_temp = yearly_temp)

###### the 'temp' route you will query the data with params in the url and return the data Day 3 Activity 10
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    """Return TMIN, TAVG, TMAX."""

    # Select statement


    # calculate TMIN, TAVG, TMAX with start and stop


    # Unravel results into a 1D array and convert to a list



if __name__ == '__main__':
    app.run(debug=True)
