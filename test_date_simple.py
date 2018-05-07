#!/usr/bin/env python

#i don't think i'm getting enough tests pass when I test it (only 2), but i tried testing each individually and they work. 

import pytest
from datetime import datetime, date, time, timedelta
import tayhello as th 


TODAY_DATE = date.today()
OTHER_DATE = date(2018, 2, 26)
TODAY_DATE_STRING = str(date.today())
OTHER_DATE_STRING = ('02/07/41')


def test_get_date_object():
        object_thing_none = th.get_date_object(date=None)
        object_thing_some = th.get_date_object(date='2018-2-26')

        assert object_thing_none == TODAY_DATE 


        assert object_thing_some == OTHER_DATE
        assert isinstance(object_thing_some, object) 
        assert isinstance(object_thing_none, object) 

        with pytest.raises(ValueError):
            th.get_date_object(date='2/222')

        with pytest.raises(TypeError):
            th.get_date_object(date=2012.00) #not a string



def test_get_date_string():
        string_thing_none = th.get_date_string(date_object=None)
        string_thing_some = th.get_date_string(date_object=date(1941, 2, 7))

        assert string_thing_none == TODAY_DATE_STRING

        assert string_thing_some == OTHER_DATE_STRING
 
        with pytest.raises(TypeError):
            th.get_date_string(date_object='1,2,3') 

if __name__ == '__main__': 

    test_get_date_object()

    test_get_date_string()
