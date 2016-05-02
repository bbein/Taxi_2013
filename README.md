# New York City Taxi Fare data for 2013

These are the suporrting files for the [blog post](https://benbein.wordpress.com/2016/05/02/Taxi) on the analysis of Taxi Fare date in NY City from 2013.

## Instructions

### 1. Install [python](https://www.python.org/) and [sqlite](https://www.sqlite.org/)

I use 'sqlite3' and 'python 2.7+'. It is important to also get the 'sqlite3 package for python'.

### 2. Download raw Taxi data

The raw data can be found [here](http://www.andresmh.com/nyctaxitrips/). One needs to download and unpack the 12 Fare data files.

### 3. Initialize database and set up schema

In the folder with the 'taxi_fare.py' run the console comands:
'sqlite3 Taxi_Fare.dp'
'.tables'
'.exit'

This will create the sqlite database file.

Now run the python script to load all the raw data into the database:
'python taxi_fare.py'

All done 
