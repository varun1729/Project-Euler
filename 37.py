import resource
import math
import time
t1 = time.monotonic()
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

def rightTrucatedPrimes (num):
	if (num in [2,3,5,7]):
		return True
	elif(isPrime(num)):
		return(rightTrucatedPrimes(num//10))
	else:
		return False

def leftTruncatedPrimes (num,exp):
	if (num in [2,3,5,7]):
		return True
	elif(isPrime(num)):
		return leftTruncatedPrimes(num%(10**exp), exp-1)
	else:
		return False

def getExp (num):
	exp = math.floor(math.log(num,10)) + 1
	return exp

twoSidedPrimes = 0
num = 11
total = 0
while (twoSidedPrimes <=10):
	if (rightTrucatedPrimes(num)):
		if(leftTruncatedPrimes(num,getExp(num))):
			twoSidedPrimes += 1
			total += num
			print(num)
	num += 2

print('Sum is',total)
print(time.monotonic() - t1,'s')
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000 , 'KB')
    
'''
#Failed recursive approach
array = list(range(1,10))
def RemoveFromLtoRTruncPrimes (num):
	i = 0
	if (isPrime(num) and counter <5):
		num = num*10 + array[i]
		i+=1
		return (RemoveFromLtoRTruncPrimes(num))
	elif(num>=10):
		num //= 10
		return (RemoveFromLtoRTruncPrimes (num))
	else:


counter = 0
print(RemoveFromLtoRTruncPrimes(2))
'''
