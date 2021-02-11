#!/usr/bin/python
import sys

try:
    IntegerArgument = int(sys.argv[1])

    DayOfWeek = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
    }

    print ("At least one argument")
    print (DayOfWeek.get(IntegerArgument, "Not a valid day"))

    
except:
    print ("No integer argument")