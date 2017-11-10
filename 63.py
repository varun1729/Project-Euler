import math
def lengthOfNum (base, exp):
	num  = x**y
	length = int(math.log(num,10) + 1)
	return (length == y)

count = 0
for x in range (1,100):
	for y in range (1,100):
		if(lengthOfNum(x,y)):
			count += 1
		else:
			break

print(count)