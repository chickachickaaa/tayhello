#!/usr/bin/env python

import pytest
import tayhello as th #make changes now instead of data_simple

TODAY_DATE = date.today()
OTHER_DATE = 2018-2-26
TODAY_DATE_STRING = str(date.today())
OTHER_DATE_STRING = ('2018-2-26')

def test_get_date_object():
        object_thing_none = th.get_date_object(date=None)
        object_thing_some =th.get_date_object(date='2018-2-26')

#1
        assert object_thing_none == TODAY_DATE 

#2
        assert isinstance(object_thing_some, ('datetime.date')) 


        assert isinstance(object_thing_none, ('datetime.date')) 

#7      
        
        with pytest.raises(TypeError):
            bad_object_thing = th.get_date_object(date='feb 26th') #not proper string format

        
#8        
        
        with pytest.raises(TypeError):
            other_bad_object_thing = data_simple.get_date_object(date=2012.00) #not a string



def test_get_date_string():
        string_thing_none = th.get_date_string(date=None)
        string_thing_some = th.get_date_string(date='2018-2-26')

#3
        assert string_thing_none == TODAY_DATE_STRING


#4
        assert string_thing_some == OTHER_DATE_STRING

#9

        
        with pytest.raises(TypeError):
            bad_string_thing = th.get_date_string(date_object='2018-09-09') #not a date object

    
#need help with this the slides are way too dense. 



