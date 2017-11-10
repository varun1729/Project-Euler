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

primeNums = list()
for x in range(1000):
	if(isPrime(x)):
		primeNums.append(x)

a_max = 0
b_max = 0
n_max = 0
for b in primeNums:
	for a in range (-1000,1000):
		n = 0
		prime = (n**2) + (a*n) + b
		while (isPrime(prime)):
			n+=1
			prime = n**2 + a*n + b
		if (n>n_max):
			n_max = n
			b_max = b
			a_max = a

print(a_max, " ", b_max, " ", n_max)
print('a_max * b_max = ', a_max * b_max)

for x in range (0,71):
	print((x**2) + (-61*x) + 971, " ", end = " ")
