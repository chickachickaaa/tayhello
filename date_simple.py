#!/usr/bin/env python

import sys
from datetime import datetime, date, time, timedelta
#ModuleNotFoundError: No module named 'date'

def get_date_object(date=None):
    """ takes an optional string date and returns a date object """
    #optional_string_date = input
    try:
        if date:
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date() 
    except ValueError:
        raise ValueError('please enter a proper format')
    except TypeError:
        raise TypeError('please enter a string argument')	
        #do i use raise or exit?
    else:
            #getting a syntax error on else when I indent..
        date_obj = date.today()
        #AttributeError: 'NoneType' object has no attribute 'today'
        print(date_obj)
        print(type(date_obj))
    return(date_obj)

def get_date_string(date_object=None): 
    """ takes an optional date object and returns a formatted string """
    try:
        if date_object:
            #format string
            date_str = datetime.datetime.strptime(date_object, '%m/%d/%y')
    except TypeError:
        raise TypeError('please enter an date object')    
    else:
        #getting a syntax error on else when I indent..
        date_str = str(date.today())
        # print(date_str)
        # print(type(date_str))
    return(date_str)


if __name__ == '__main__': 
    get_date_object()
    get_date_string() #ValueError: unconverted data remains: 18 

#in this case, how should i structure so i have just main() called after this gateway?



