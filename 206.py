import math
import sys
number = "1_2_3_4_5_6_7_8_9_0"

lb = 1000000000
ub = 1414213562

def isConcealed (x):
	square = str(int(x**2))
	i = 2
	for y in range (2,17,2):
		if (square[y] == str(i)):
			i += 1
		else:
			return False
	return True

for x in range (1000000000,1414213562,10):
	if (isConcealed(x)):
		print (x)
		sys.exit()
