import time
import math
import sys
ub = 100000

t1 = time.monotonic()

def sieveOfEratosthenesGenCompositeAndPrime (ub):
	num = 2
	array = [True]*(ub)
	while (num*num < ub):
		for x in range (2*num,ub,num):
			array[x] = False
		num += 1
		while (array[num] == False):
			num+=1
	primes = []
	composites = []
	for x in range (2, len(array)):
		if(array[x] == True):
			primes.append(x)
		else:
			composites.append(x)
	return (primes, composites)


def isGoldbachOtherConjectureTrue (num,primes):
	i = 0
	while(primes[i]<num):
		if(math.sqrt((num - primes[i])/2)%1 == 0):
			return True
		i += 1
	return False

primesAndComposites = sieveOfEratosthenesGenCompositeAndPrime(ub)

for x in range (0, len(primesAndComposites[1]) -10):
	val = primesAndComposites[1][x]
	if(val % 2 == 1):
		if(isGoldbachOtherConjectureTrue(val, primesAndComposites[0]) == False):
			print(val)


