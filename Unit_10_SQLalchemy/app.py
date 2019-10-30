import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
#set up db and tables
engine = create_engine("sqlite:///Resources\hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
#create a flask app
app= Flask(__name__)
#create home page
@app.route('/')
def origin():
    return(
        'Welcome<br/>'
        'Precipitation data /api/v1.0/precipitation<br/>'
        'Station data /api/v1.0/stations<br/>'
        'Temperature data /api/v1.0/tobs<br/>'
        'Start date & Years /api/v1.0/<start><br/>'
        'End date /api/v1.0/<start>/<end><br/>'
    )
@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    prcp=session.query(Measurement.date, Measurement.prcp).\
    group_by(Measurement.date).all
    results = list(np.ravel(prcp))
    session.close()
    return jsonify(results)
@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    stations=session.query(Measurement.station).group_by(Measurement.station).all()
    results = list(np.ravel(stations))
    session.close()
    return jsonify(results)
@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    tobs=session.query(Measurement.date, Measurement.tobs).group_by(Measurement.date).all()
    results = list(np.ravel(tobs))
    session.close()
    return jsonify(results)
@app.route('/api/v1.0/<start>')
def start(start):
    session = Session(engine)
    begin=session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    results = list(np.ravel(begin))
    session.close()
    return jsonify(results)
@app.route('/api/v1.0/<start>/<end>')
def end(start, end):
    session = Session(engine)
    begin=session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    results = list(np.ravel(begin))
    session.close()
    return jsonify(results)
if __name__ == '__main__':
    app.run(debug=True)

    