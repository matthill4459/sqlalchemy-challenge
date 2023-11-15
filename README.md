# sqlalchemy-challenge
The is a repository for module 10

## Purpose of code
This code will use the resources of hawaii.sqlite, hawaii_measurements.csv and hawwii_stations.csv.
it will then use SQLAlchemy ORM to do an explotatory analysis on Precipitation. It will then create a graph that measures the precipitation over a 12 month period between 2016-08-23 - 2017-07-10 in inches. It will grab the summary stats of the precipitation. After mesuring the precipitation it will then analize the staions and the temp observations over a 12 month period. after all of that data has been found. I will create a climate app using Flasks. this app will allow for specified within the exsiting python data base to be accessed. it will then jsonify the data. the routes created will be 

`/api/v1.0/precipitation`

`/api/v1.0/stations`

`/api/v1.0/tobs`

`/api/v1.0/<start>`

`/api/v1.0/<start>/<end>`

