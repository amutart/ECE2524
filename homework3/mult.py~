#!/usr/bin/env python2
import argparse
import sys

ret = 1
parser = argparse.ArgumentParser(description='Process some numbers.')
args = parser.parse_args()

try:
	for line in iter(sys.stdin.readline, ''):
		if(line == '\n') :
			print >> sys.stdout, ret
			ret = 1
		else :
			ret = ret * float(line)
	print >> sys.stdout, ret
except ValueError as e:
	print >> sys.stderr, e
	sys.exit(1)
	
