#!/usr/bin/env python
#
try:
    while True:
        d1 = raw_input('An integer: ')
        if d1 == 'quit': break
        d2 = raw_input('Another integr: ')
        print int(d1) / int(d2)
except ZeroDivisionError, e:
    print 'can not use 0', e
except ValueError:
    print 'only intger'
except:
    print 'unknow error' 
