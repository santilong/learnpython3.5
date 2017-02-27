#!/usr/bin/env python
#-*- coding:utf8 -*-

import shelve,sys

def store_person(db):
	pid = raw_input('Enter a unique number: ')
        person = {}
	person['name'] = raw_input('Eneter a person\'s name: ')
	person['age'] = raw_input('Enter a person\'s age: ')
	person['phone'] = raw_input('Enter a person\'s phone number: ')
	db[pid] = person

def lookup_person(db):
	pid = raw_input('Enter a unique number:')
	field = raw_input('choose (name,age,phone to search. )')
	field = field.strip().lower()
	print field.title() + ':' , db[pid][field]

def print_help():
	print 'This is help hint about Command: '
	print 'store : store the information of a person.'
	print 'lookup: lookup the information of a person.'
	print '  ?   : print this message.'
	print 'quit | q: exit the programe.'

def enter_cmd():
	cmd = raw_input('Enter a command: ')
	cmd = cmd.strip().lower()
	return cmd

def main():
	database = shelve.open('database.dat')
	try:
		while True:
			cmd = enter_cmd()
			if cmd == 'store': store_person(database)
			elif cmd == 'lookup': lookup_person(database)
			elif cmd == '?': print_help()
			elif cmd == 'quit' or cmd == 'q': return
	finally:
		database.close()
if __name__ == '__main__':
	main()
