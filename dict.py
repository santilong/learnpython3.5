#!/usr/bin/env python
#-*- coding: utf-8 -*-

people = {
	
	'alice':{
		'phone':'2341',
		'addr':'foo drive 23'
		},

	'beth':{
		'phone':'9102',
		'addr':'bar street 42'
		},

	'cecil':{
		'phone':'3158',
		'addr':'baz avenue 90'
		}
	}

labels = {
	'phone':'phone number',
	'addr':'address'
	}

name = raw_input('Name: ')

request = raw_input('Phone number (p) or address (a)? ')

if request == 'p':
	key = 'phone'
if request == 'a':
	key = 'addr'

if name in people:
	print "%s's %s is %s." % (name,labels[key],people[name][key])






