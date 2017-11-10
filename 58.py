import math
import sys
def isPrime (num):
	#ignore that num <=1 is not prime
	if (num == 2 or num == 3):
		return True
	elif (num % 2 == 0):
		return False
	else:
		ub = math.ceil(math.sqrt(num)) + 1
		j = 3
		for j in range (3,ub,2):
			if (num % j == 0):
				return False
		return True

count = 0
d4 = 1
diagonal = 1
for x in range (3,100000,2):
	diagonal += 4
	start = d4
	d1 = start + (x-2)+1
	d2 = d1 + x - 1
	d3 = d2 + x - 1
	d4 = d3 + x - 1
	temp = [d1,d2,d3,d4]
	#print (x, d1, isPrime(d1), d2, isPrime(d2), d3 , isPrime(d3), d4, isPrime(d4))
	for num in temp:
		if (isPrime(num)):
			count += 1
	criticalValue = count/diagonal
	if (criticalValue < 0.1):
		print (x, criticalValue)
		sys.exit()


