def reverseNumStr(numStr):
	num = int(numStr)
	reverse = 0
	while (num > 0):
		reverse = reverse*10 + num%10
		num//= 10
	return reverse

num = 28433*(2**7830457) + 1
numStr = ''
for x in range (0,10):
	temp = num%10
	numStr += str(temp)
	num //= 10
print(reverseNumStr(numStr))


print((28433 * 2**7830457 + 1) % 10000000000)

