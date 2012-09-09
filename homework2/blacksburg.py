# ECE 2524 Homework 2 Problem 2 <Han Seung Lee>
print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
with open('account', 'r') as f:

	for line in f:
		a = line.split()
		#print (",".join(a))
		if a[3] == "Blacksburg":
			ret = [a[4], a[1], a[0], a[2]]
			print ", ".join(ret)
			
		






		 

