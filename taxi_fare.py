import csv
import sqlite3 as lite
from dateutil.parser import parse
import time
import datetime
import sys

def convert_to_timestamp(str):
    if str == '':
        return 0
    else:
        stamp = int(time.mktime(parse(str).timetuple()))
        return stamp

con = None
file = None
words = None
message = None
files = ("trip_fare_1.csv","trip_fare_2.csv","trip_fare_3.csv","trip_fare_4.csv","trip_fare_5.csv","trip_fare_6.csv","trip_fare_7.csv","trip_fare_8.csv"
         ,"trip_fare_9.csv","trip_fare_10.csv","trip_fare_11.csv","trip_fare_12.csv")

try:
    #open database and create table
    con = lite.connect('Taxi_Fare.db')
    cur = con.cursor()    
    cur.execute("DROP TABLE IF EXISTS Taxi_Fare")
    cur.execute("""CREATE TABLE Taxi_Fare(medallion TEXT, hack_license TEXT, vendor_id TEXT, pickup_datetime TIMESTAMP, payment_type TEXT, fare_amount REAL, 
                   surcharge REAL, mta_tax REAL, tip_amount REAL, tolls_amount REAL, total_amount REAL)""")
    #open file and read first line
    file_number = 0
    for f in files:
        file_number += 1
        file = open(f, 'r') #opens a file at the beginning
        lines = csv.reader(file, delimiter=',', quotechar='"')
        lines.next()
        n = 0
        #read all lines
        for words in lines:
            n += 1
            #clean data
            words[3] = convert_to_timestamp(words[3])
            for i in range(5,11):
                try:
                    words[i] = float(words[i])
                except:
                    words[i] = 0
            #insert values into database
            message = r"INSERT INTO Taxi_Fare VALUES({!r},{!r},{!r},{!r},{!r},{!r},{!r},{!r},{!r},{!r},{!r})".format(*words)
            cur.execute(message)
            if n%1000000 == 0:
                print(n)
                con.commit()
                
        con.commit()
        print str(file_number)+' file finished with '+str(i)+' data entries'
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
        
except IOError as e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
except ValueError as e:
    print(str(e))
    
finally:   
    if con:
        con.commit()
        con.close()
    if file:
        file.close()
    if words:
        print words
    if message:
        print message
    