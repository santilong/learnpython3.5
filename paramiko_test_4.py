#!/usr/bin/env python

import paramiko
import sys,os
#hostip = sys.argv[1]
#cmd = sys.argv[2]
user = 'opsuser'
port = 22
def para_miko(hostip,optlist):
	paramiko.util.log_to_file('paramiko')
	s = paramiko.SSHClient()
	s.load_system_host_keys()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		s.connect(hostip,port,user)
	except Exception,e:
		print e
	stdin, stdout, stderr = s.exec_command(optlist)
	stdoutinfo = stdout.readlines()
	stderrinfo = stderr.readline()
	s.close()
	return stdoutinfo

def doSelect(hostip,selectSQL,dbname):
	dbStr = "mysql -uroot -p2Ycfsjd@ -s -N -e \"use %s;" % dbname
	optlist = dbStr + selectSQL + ';\"'
	global result 
	result = para_miko(hostip,optlist)
	#return result
	#writeSQL(result)

def set_hostip():
	hostip = raw_input('Enter a GW_IP address: ')
	hostip = hostip.strip()
	return hostip

def writeSQL(result):
	filedir = '/home/longyue/santi'
	filepath = filedir + '/SqlResult.txt' 
	print "Write the SQL result to a file !"
	f = open(filepath,'w')		
	for line in result:
		f.write(line + '\n')
	f.close()

def main():
	#selectSQL = raw_input('Enter a SQL: ')
	selectSQL = 'select * from servers limit 1'
	#dbname = raw_input('Enter a database name: ')
	dbname = 'galaxy_empire_gateway'
	#hostip = set_hostip()
	hostip = '54.200.253.122'
	doSelect(hostip,selectSQL,dbname)
	writeSQL(result)
	
if __name__ == '__main__':
	main()
