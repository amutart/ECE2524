# ECE 2524 Homework 2 Problem 1 <Han Seung Lee>

with open('/etc/passwd', 'r') as f:
	for line in f:
		print line.split(":",1)[0] + "\t" + line.split(":",6)[6],
		 
