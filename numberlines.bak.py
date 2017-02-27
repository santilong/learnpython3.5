#!/usr/bin/env python                                                  
                                                                       
import fileinput                                                       
                                                                       
for line in fileinput.input(inplace=True):                             
	line = line.rstrip()                                                  
	num = fileinput.lineno()                                              
	print "%-70s # %2i" % (line,num)                                      
