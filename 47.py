ub = 1000000
import math
import sys
import time 
#import sympy
target = 4
t1 = time.monotonic()
def getprimeFactors (num,primes):
	'''
	factors = sympy.factorint()
	return len(factors) == 4
	'''
	primeFactors = 0
	counter = 0
	while (primes[counter] <= num//2 ):
		if(num % primes[counter] == 0):
			primeFactors += 1
		#if(count > target):
			#return False
		counter += 1
	return (primeFactors == target)
	

def sieveOfEratosthenesPrimes (ub):
	num = 2
	array = [True]*(ub)
	while (num*num < ub):
		for x in range (2*num,ub,num):
			array[x] = False
		num += 1
		while (array[num] == False):
			num+=1
	primes = []
	for x in range (2, len(array)):
		if(array[x] == True):
			primes.append(x)
	return (primes)


primes = sieveOfEratosthenesPrimes(ub)
count = 0
#print(getprimeFactors(644,primes))
for x in range (0,primes[len(primes) - 1]):
	if (count == target):
		for y in range (0,target):
			print(x-y-1, ' ', end = ' ')
		print('\n',time.monotonic()-t1, 's')
		break
	else:
		if(getprimeFactors(x,primes)):
			count += 1
		else:
			count = 0

