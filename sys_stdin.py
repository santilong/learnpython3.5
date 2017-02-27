#!/usr/bin/env python
# use cat sys_stdin_text | python sys_stdin.py 
import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print 'wordcount: ', wordcount
