def getDigitsSum (num):
	total = 0
	while (num > 0):
		total += num%10
		num //= 10
	return total


maximum = 0
for base in range (1,101):
	for exp in range (1,101):
		num = base**exp
		digitSum = getDigitsSum(num)
		if(digitSum > maximum):
			maximum = digitSum

print(maximum)

