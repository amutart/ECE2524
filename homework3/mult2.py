#!/usr/bin/env python2
import argparse
import sys
import fileinput

ret = 1
parser = argparse.ArgumentParser(description='Process some numbers.')
parser.add_argument('files', nargs='*')
parser.add_argument('--ignore-blank', dest='blank', action='store_true', help='ignore blank lines in the input' )
parser.add_argument('--ignore-non-numeric', dest='nonnumeric', action='store_true', help='ignore lines that do not contain numeric input')
args = parser.parse_args()

try:
	if(args.blank):
		if(args.nonnumeric):
			for line in fileinput.input(args.files):
				if(line == '\n'):
					ret = ret
				else:
					try:
						ret = ret * float(line)
					except ValueError as e:
						pass
			#print(ret)
			print >> sys.stdout, ret
		else:
			for line in fileinput.input(args.files):
				if(line == '\n'):
					ret = ret
				else:
					ret = ret * float(line)
			print >> sys.stdout, ret
	else:
		if(args.nonnumeric):
			for line in fileinput.input(args.files):
				if(line == '\n'):
					print >> sys.stdout, ret
					ret = 1
				else:
					try:
						ret = ret * float(line)
					except ValueError as e:
						pass
			print >> sys.stdout, ret
		else: 
			for line in fileinput.input():
				if(line == '\n'):
					print >> sys.stdout, ret
					ret = 1
				else:
					ret = ret * float(line)
			print >> sys.stdout, ret

except ValueError as e:
	print >> sys.stderr, e
	sys.exit(1)
	
