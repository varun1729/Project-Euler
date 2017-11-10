import math
import sys
import time
ub = 1000
total = 0
def powMe (num):
	counter = 1
	product = 1
	while (counter <= num):
		product *= num
		counter += 1
	return product

for x in range (1,ub+1):
	total += powMe(x)

print(len(str(total)),'\n', str(total))
