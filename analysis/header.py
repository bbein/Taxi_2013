'''
common header file for the analysis scripts
'''

import sqlite3 as lite 
import sys
import numpy as np
from dateutil.parser import parse
import time
import datetime
import csv
import matplotlib.pyplot as plt #plotting
import math as ma
import json

def week_based_timestamp(timestamp):
    '''
    Converts a timestamp into a list index with enteries for every minute of every day in one week.
    index 0 coresponds to 12am Monday morning and the largest index is 11:59pm on Sunday night.
    
    Inputs:
    timestamp: int
    
    Returns:
    index: int
    '''
    
    date=datetime.datetime.fromtimestamp(timestamp)
    #date.weekday() == 0 for Mondays and == 6 for Sundays
    return date.weekday()*24*60+date.hour*60+date.minute