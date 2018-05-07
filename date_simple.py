#!/usr/bin/env python
#DONE SUCCESS!! 

import sys
from datetime import datetime, date, time, timedelta
#ModuleNotFoundError: No module named 'date'

def get_date_object(date=None):
    """ takes an optional string date and returns a date object """
    #optional_string_date = input
    try:
        if date:
            dateobj1 = datetime.strptime(date, '%Y-%m-%d').date()
            #print(dateobj1)
        else:
            dateobj1 = datetime.today().date()
            #getting a syntax error on else when I indent..
    except ValueError:
        raise ValueError('please enter the date in format: year month day separated by a hyphen')
    except TypeError:
        raise TypeError('please enter a string')   
         #do i use raise or exit?

    #print(type(dateobj1))
    return(dateobj1)

def get_date_string(date_object=None): 
    """ takes an optional date object and returns a formatted string """
    try:
        if date_object:
            date_str = datetime.strftime(date_object, '%m/%d/%y')
            #print(date_str)
        else:
            #getting a syntax error on else when I indent..
            date_str = str(date.today())
    except TypeError:
        raise TypeError('please enter an date object')    
        
    #print(date_str)
    return(date_str)


if __name__ == '__main__': 
    get_date_object()
    #date='1776-7-4'
    #date='2018-2-26'
    get_date_string() 
    #date_object=date(1941, 2, 7)

#in this case, how should i structure so i have just main() called after this gateway?
