#!/usr/bin/env python2
# ECE2524
# Han Seung Lee

import argparse
import sys
import fileinput
import ast
from operator import itemgetter
import csv

parser = argparse.ArgumentParser(description='Managing the Inventory')
parser.add_argument("-f, --data-file", action='store', dest= 'file', help="path to the data file to read at startup")
args = parser.parse_args()

def insert_data(strQuery):
	data.append(ast.literal_eval(strQuery))
	print "Insert OK"
	print "."
	
def delete_data(strQuery):
	(fld, tmp, val) = strQuery.partition("=")
	flag = False # flag for delete command
	
	for item in data:
		if item[fld] == val:
			del data[data.index(item)]
			flag = True
			print "Delete OK"

	if flag == False:
		print "{}_{} was not deleted.".format(fld, val)
	
	print "."
		
def update_data(strQuery):
	(new, tmp, old) = strQuery.partition(" where ") # new where old
	(new_fld, tmp, new_val) = new.partition("=")	# new_fld=new_val
	(old_fld, tmp, old_val) = old.partition("=")	# old_fld=old_val
	try:
		for item in data:
			if item[old_fld] == old_val:
				data[data.index(item)][new_fld] = new_val
				print "Update OK"
	except KeyError as e:
		sys.stderr.write("Not a valid field name\n")

	print "."
	
def select_data(strQuery):
	w = csv.DictWriter(sys.stdout, fieldnames = data[0].keys(), delimiter='|')
	
	qry = strQuery.split()	# check '*' for select all

	try:
		if strQuery.find("where") > 0:
			(pre, tmp, where) = strQuery.partition(" where ")
			(fld, tmp, val) = where.partition("=")
			
			w.writeheader()
			
			for item in data:
				if item[fld] == val:
					w.writerow(item)
			
		if strQuery.find("order") > 0:
			(pre, tmp, fld) = strQuery.partition(" order by ")
		
			if fld == "Quantity":
				sort = sorted(data, key=lambda t:int(t["Quantity"]))
			else:
				sort = sorted(data, key=itemgetter(fld))

			w.writeheader()
			w.writerows(sort)
		else:
			if qry[0] == "*":
				w.writeheader()
				w.writerows(data)
	except KeyError as e:
		sys.stderr.write("Not a valid field name\n")

	print "."

myDict = {'insert': insert_data, 'delete': delete_data, 'update':update_data, 'select': select_data}

data=[]

# open file / make data dictionary
try:
	with open(args.file, 'rb') as f:
		r = csv.DictReader(f, delimiter='|', skipinitialspace=True)
		for i in r:
			i={k.strip():v for k, v in i.items()}	#For remove space from each key.
			data.append(i)
			
except IOError as e:
	sys.stderr.write("{} was not found.\n".format(args.file))
	sys.exit(1)

# enter commnads
for cmd in iter(sys.stdin.readline, ''):
	(action, space, strQuery) = cmd.partition(" ")
	strQuery = strQuery.strip("\n")
	
	try:
		myDict[action](strQuery)

		if action == "insert" or action == "update" or action == "delete":
			with open(args.file, 'wb') as output:
				w = csv.DictWriter(output, fieldnames = data[0].keys(), delimiter='|')
				w.writeheader()
				w.writerows(data)
	except KeyError as e:
		sys.stderr.write("{} is not right command\n".format(action))

#for run with actions chk must be in each functions.
#commit y/n
#if action == "insert" or action == "update" or action == "delete":
	#chk = raw_input("Commit y/n? ")
#	chk = "Y"
#	if chk == "Y" or chk == "y":
#		with open(args.file, 'wb') as output:
#			w = csv.DictWriter(output, fieldnames = data[0].keys(), delimiter='|')
#			w.writeheader()
#			w.writerows(data)
#		
#		print "Committed"
#	else:
#		print "Rollbacked"

