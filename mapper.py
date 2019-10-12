#!/usr/bin/env python                
import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split(",")

    if (len(words)==5):
              infoUsers = words[0]+" "+words[1]+" "+words[3]+" "+words[4]
              print '%s^%s'%(words[2], infoUsers)
    else:
              infoCalls=words[1]+" "+words[2]
              print '%s^%s'% (words[0],infoCalls)
