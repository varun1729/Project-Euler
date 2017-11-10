import math
import time
import sys
t1 = time.monotonic()
pentagonNumbers = []
def verifyPentagonal (num):
	return(((1 + math.sqrt(1 + 24*num))/ 6) % 1 == 0)
	
ub = 2200
for x in range (0,ub):
	 pentagonNumbers.append(((3*math.pow(x,2) - x)/2))
	 #print(verifyPentagonal(pentagonNumbers[x]))

for x in range (1,ub):
	y = x+1
	while (y < ub):
		if (verifyPentagonal(pentagonNumbers[y] + pentagonNumbers[x])):
			if(verifyPentagonal(pentagonNumbers[y] - pentagonNumbers[x])):
				print(x,y)
				print(pentagonNumbers[y] - pentagonNumbers[x])
				print('Execution time:', time.monotonic()- t1,'s')
				sys.exit()
		y+=1

