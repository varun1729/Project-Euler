def getDigits (num):
	list_digits = list()
	while (num >0):
		list_digits.append(num%10)
		num //=10
	list_digits = list(reversed(list_digits))
	return list_digits

def getDigitsGen (num):
	while (num >0):
		yield num%10
		num //=10

def getUB (power):
	base = 9**power
	i = 1
	while (i*base > 10**i):
		i+=1
	return i*base

total = 0
for x in range (10,getUB(5)):
	val = 0
	for y in getDigitsGen(x):
		val += y**5
	if (val == x):
		print(val)
		total += val

print(total)
		
