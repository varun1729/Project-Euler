list_nums = list()
ub = 100+1
for a in range (2,ub):
	for b in range (2,ub):
		val = a**b
		if (not(val in list_nums)):
			list_nums.append(val)

print (len(list_nums))