import math
import time
import itertools 

def isPrime (num):
	if (num%2 == 0):
		return False
	else:
		ub = math.ceil(num**(1/2))
		j = 3
		while (j<=ub):
			if (num%j == 0):
				return False 
			j+=2
		return True

t1 = time.monotonic()
maximum = 0
permut = itertools.permutations('1234567',7)
for z in permut:
	num = (int(''.join(z)))
	if(isPrime(num)):
		if ('1234567' == ''.join(sorted(str(num)))):
			if (num>maximum):
				maximum = num

print(maximum,'\n','Execution time', time.monotonic()-t1,'s')

'''
#Sieve of Eratosthenes
def PrimeSieve (n):
	primesSieveList = [True for i in range (n+2)]
	divisor = 2
	while (divisor*divisor < n):
		if (primesSieveList[divisor] == True):	
			for x in range(divisor*2,n+1,divisor):
				primesSieveList[x] = False
		divisor+=1
	for p in range (2,n+1):
		if(primesSieveList[p]):
			yield p

#8 digit and 9 digit pandigital numbers cannot be primes, 
#cause (1+2+3+4+5+6+7+8 = 36) ans (1+...+9 = 45) --> divisible by 3)
#Therefore only check up to the largest 7 digit number: 9,999,999

def isPalindrome (num):
	if(num>=1000):
		length = math.floor(math.log(num,10) + 1)
		if (length == 4):
			return '1234' == ''.join(sorted(str(num)))
		elif (length == 5):
			return '12345' == ''.join(sorted(str(num)))
		elif (length == 6):
			return '123456' == ''.join(sorted(str(num)))
		elif (length == 7):
			return '1234567' == ''.join(sorted(str(num)))
		elif (length == 8):
			return '12345678' == ''.join(sorted(str(num)))
		else:
			return '123456789' == ''.join(sorted(str(num)))
'''


'''
t2 = time.monotonic()
maximum = 0
primeGen = PrimeSieve(10000)
for x in primeGen:
	if(isPalindrome(x)):
	  if(x > maximum):
	    maximum = x
print(maximum,'\n','Execution time', time.monotonic()-t2,'s')
'''