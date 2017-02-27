#!/usr/bin/env python
#-*- coding: utf8 -*-

try:
    x = input("first number:")
    y = raw_input("second number:")
    print x / y

except (ZeroDivisionError, TypeError),e:
    print e

#except:
#    print "Something wrong happened..."
except Exception, e:
    print e
