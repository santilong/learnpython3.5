#!/usr/bin/env python
#

import paramiko
import sys,os

hostip = sys.argv[1]
cmd = sys.argv[2]
user = 'opsuser'
port = 22

def para_miko():
	paramiko.util.log_to_file('paramiko')
	s = paramiko.SSHClient()
	s.load_system_host_keys()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		s.connect(hostip,port,user)
	except Exception,e:
		print e
	else:
		stdin, stdout, stderr = s.exec_command(cmd)
		stdoutinfo = stdout.readlines()
		print "The command %s result is %s\n" % (cmd,stdoutinfo)
	finally:
		s.close()

if __name__ == '__main__':
	para_miko()
