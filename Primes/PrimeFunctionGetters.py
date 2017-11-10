import math
def isPrime (num):
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

primes = [2]
def isPrimeMemoization (num, primes):
	i = 0
	FC = 0
	while (i < len(primes)):
		if (num%primes[i] == 0):
			FC+=1
			return False
		i+=1
	if (FC == 0):
		primes.append(num)
		return True
a = 1
for x in range (3,100000):
	if(isPrimeMemoization(x,primes)):
		a +=1
print(a)
a = 0
for x in range (0,100000):
	if(isPrime(x)):
		a+=1
print (a)
	