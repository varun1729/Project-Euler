import math
import time

t1 = time.clock()

def isPandigital (num):
	size = len(str(num))
	if(num > (size+1)*10**size):
		return False
	else:
		digits = list()
		while (num>0):
			val = num%10
			if not(val in digits):
				digits.append(val)
			num //= 10
		count = 0
		for x in range(1,size + 1):
			if(x in digits):
				count+=1
			else:
				return False
		if(count == size):
			return True

result = []
for x in range (1000,10000):
	upperBound = math.ceil(x**0.5)
	for y in range (1,upperBound+1):
		if(x%y == 0):
			numString = str(x) + str(y) + str(x//y)
			num = int(numString)
			if (isPandigital(num) and (len(numString)==9)):
				if not(x in result):
					result.append(x)
					print(num, ": ", x, "=", y,"*", x//y)


print('\n', sum(result))


