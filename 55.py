def reverseNum (num):
	remainder = 0
	while (num>0):
		remainder = remainder*10 + num%10
		num //= 10
	return remainder

def isLychrelNum (num):
	for x in range (1,51):
		reverse = reverseNum(num)
		sumNumRev = num+reverse
		if (sumNumRev == reverseNum(sumNumRev)):
			return False
		else:
			num = sumNumRev
	return True

count = 0
for x in range (1,10001):
	if(isLychrelNum(x)):
		count += 1

print(count)