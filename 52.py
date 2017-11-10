import sys
for x in range (10,100000000):
	numString = sorted(str(x))
	loop = True
	i = 1
	target = 6
	while (loop == True):
		if(sorted(str(x*i)) == numString):
			if(i == target):
				result = []
				while(i > 0):
					result.append(x*i)
					i -= 1
				print(result)
				sys.exit()
			i += 1
		else:
			loop = False

