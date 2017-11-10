import math
def isSpecial (num1):
	num = num1
	total = 0
	while (num > 0):
		total += math.factorial(num%10)
		num //= 10
	if (num1 == total):
		return True

for x in range (10,1000000):
	if(isSpecial(x)):
		print(x)
