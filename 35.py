import math
import time

t1 = time.clock()
def isPrime (num):
	ub = math.ceil(num**(1/2))
	j = 3
	while (j<=ub):
		if (num%j == 0):
			return False 
		j+=2
	return True
def isPrimeT (num):
	if (num <=1):
		return False
	if (num == 2 or num==3):
		return True
	elif (num%2 == 0):
		return False
	else:
		ub = math.ceil(num**(1/2))
		j = 3
		while (j<=ub):
			if (num%j == 0):
				return False 
			j+=2
		return True
def getCircularGen (num):
	temp = str(num)
	i = 0
	while (i < len(temp)-1):
		temp = temp[1:] + temp[0]
		yield int(temp)
		i+=1

array = [2,3,5,7]
for x in range (11,1000000,2):
	if (isPrime(x)):
		array.append(x)

t2 = time.clock()
print('Time to initialize array of primes:', t2 - t1)

def getTrueRotations (num):
	rotations = getCircularGen(num)
	tempExempt = [num]
	for z in rotations:
		if (isPrimeT(z)):
			tempExempt.append(z)
		else:
			return False
	return tempExempt

exempt = [2,3,5,7,11]
for y in array:
	if (y not in exempt):
		tempExempt = getTrueRotations(y)
		if (tempExempt != False):

			'''
			rotations = getCircularGen(y)
			tempExempt = [y]
			for z in rotations:
				if (isPrimeT(z)):
					tempExempt.append(z)
			'''
			if (len(tempExempt) == len(str(y))):
				for a in tempExempt:
					exempt.append(a)

t3 = time.clock()
print('Time to check circular', t3 -  t2)
print(len(exempt))
print(exempt)

