def isPalindrome (num):
	binary = bin(num)
	binary = binary[2:]
	if ((binary == binary[::-1])and(str(num) == str(num)[::-1])):
		return True
	else:
		return False
total  = 0
for x in range (0,1000000):
	if(isPalindrome(x)):
		print(x)
		total += x

print(total)

