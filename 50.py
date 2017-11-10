import math
import itertools
ub = 10000000
def primeSeive (ub):
	ub+=1
	array = [True]*(ub)
	array[0] = False
	array[1] = False
	x = 2
	while(x<ub):
		if(array[x] == True):
			for a in range (2*x,ub,x):
				array[a] = False
			x+=1
		else:
			x+=1
	return array

def isPrime (num):
	if (num <=1 ):
		return False
	elif (num == 2 or num == 3):
		return True
	elif (num % 2 == 0):
		return False
	else:
		ub = math.ceil(math.sqrt(num))
		i = 3
		while (i <= ub):
			if(num % i == 0):
				return False
			i += 2
		return True

primes = []
array = primeSeive(ub)
'''
for a in range(2,len(array)):
	if(array[a] == True):
		primes.append(a)

sumConsecArray = []
for a in range (0, len(primes)-1):
	sumConsec = 0
	i = a
	while (sumConsec < ub):
		
		if(isPrime(sumConsec) and (i - a > 1)):
			sumConsecArray.append([i - a, sumConsec])
								   #terms, primeNum
		sumConsec += primes[i]
		i += 1

def isInSumConsecArray (num, array):
	for item in array:
		if (item[1] == num):
			return True
	return False

sumConsecArray = sorted(sumConsecArray)

print ((sumConsecArray[len(sumConsecArray)-1]))
#print (sumConsecArray)
'''