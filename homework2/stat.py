# ECE 2524 Homework 2 Problem 3 <Han Seung Lee>

total = 0
avg = 0
max = float("-inf")
min = float("inf")
cnt = 0

print "ACCOUNT SUMMARY"
with open('account', 'r') as f:
	for line in f:
		a = line.split()
		total += float(a[2])
		cnt += 1
		if(max < float(a[2])):
			max = float(a[2])
			max_name = a[1]

		if(min >= float(a[2])):
			min = float(a[2])
			min_name = a[1]
	
print "Total amount owed = " + str(total)
print "Average amount owed = " + str(total / cnt)
print "Maximum amount owed = " + str(max) + " by " + max_name
print "Minimum amount owed = " + str(min) + " by " + min_name


