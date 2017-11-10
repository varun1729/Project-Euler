
ub = 10000001
array = [0]*(ub+1)
array [1] = 1
array [89] = 89

def getDigits (num):
	digits = []
	while (num > 0):
		digits.append(num%10)
		num //= 10
	return digits

for num in range (2,ub):
	if(array[num] == 0):
		digits = getDigits(num)
		digits = [i**2 for i in digits]
		total = sum(digits)
		temp = [num, total]
		while (array[total] == 0):
			digits = getDigits(total)
			digits = [i**2 for i in digits] 
			total = sum(digits)
			temp.append(total)
		temp.pop()
		#print (temp)
		if (array[total] == 89):
			for n in temp:
				array[n] = 89
				'''
				nstr = str(n)
				permutations = itertools.permutations(nstr)
				for perm in permutations:
					p = int(''.join(perm))
					array[p] = 89
				'''
		else:
			for n in temp:
				array[n] = 1
				'''
				nstr = str(n)
				permutations = itertools.permutations(nstr)
				for perm in permutations:
					p = int(''.join(perm))
					array[p] = 1
				'''
	else:
		continue

count = 0
for element in array:
	if(element == 89):
		count += 1

print count

