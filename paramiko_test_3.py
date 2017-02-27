#!/usr/bin/env python
#

import paramiko
import sys,os
#hostip = sys.argv[1]
#cmd = sys.argv[2]
user = 'opsuser'
port = 22
def para_miko(hostip,cmd):
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
		stdoutinfo = stdout.read()
		print "The command %s result is \n%s\n" % (cmd,stdoutinfo)
	
	finally:
		s.close()
def set_hostip():
	hostip = raw_input('Enter a IP address: ')
	hostip = hostip.strip()
	return hostip
def set_cmd():
	cmd = raw_input('Enter a Command: ')
	cmd = cmd.strip().lower()
	return cmd

def main():
	hostip = set_hostip()
	print hostip
	cmd = set_cmd()
	print cmd
	para_miko(hostip,cmd)
	
if __name__ == '__main__':
	main()
