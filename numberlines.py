#!/usr/bin/env python                                                  
                                                                       
import fileinput                                                       
for line in fileinput.input():

if fileinput.isstdin:
	print "finish!!!"
