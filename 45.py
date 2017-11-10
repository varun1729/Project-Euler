import math
import sys
import time

def genHexagonal():
	n = 144
	while True:
		yield 2*math.pow(n,2) - n
		n+=1

def verifyPentagonal (num):
	return(((1 + math.sqrt(1 + 24*num))/ 6) % 1 == 0)

def verifyTriangular (num):
	return (((-1 + math.sqrt(1 + 8*num)) / 2) % 1 == 0)

t1 = time.monotonic()
hexNums = genHexagonal()
counter = 144
for x in hexNums:
	if(verifyPentagonal(x)):
		if(verifyTriangular(x)):
			print('Hex ',counter, ':' ,int(x))
			print('Execution time:',  time.monotonic()-t1, 's')
			sys.exit()
	counter += 1
