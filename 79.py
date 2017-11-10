import time

succesfulAtempts1 = [319,680,180,690,129,620,762,689,762,318,368,710,720,710,629,168,160,689,716,731,736,729,316,729,729,710,769,290,719,680,318,389,162,289,162,718,729,319,790,680,890,362,319,760,316,729,380,319,728,716]
succesfulAtempts = []
for succesfulAtempt in succesfulAtempts1:
	if(succesfulAtempt not in succesfulAtempts):
		succesfulAtempts.append(succesfulAtempt)


def reverseNum (num):
	reverse = 0
	while (num >0):
		reverse = reverse*10 + num%10
		num //= 10
	return reverse

def getDigitsGen (num):
	num = reverseNum(num)
	digits = []
	while(len(digits) < 3):
		digits.append(num%10)
		num //= 10
	for digit in digits:
		yield digit

def digitIndex (num, digit):
	num = str(num)
	digit = str(digit)
	for x in range (0, len(num)):
		if (num[x] == digit):
			return x
	return -1

def getIndexList (num, array):
	for x in range (0, len(array)):
		if (array[x] == num):
			return x

def comesAfterMe (digit, succesfulAtempts):
	comesAfterMeList = []
	for succesfulAtempt in succesfulAtempts:
		digitGen = getDigitsGen(succesfulAtempt) 
		for value in digitGen:
			if(value == digit):
				index = digitIndex(succesfulAtempt, digit)
				index += 1
				num = str(succesfulAtempt)
				while (index < len(num)):
					t = num[index]
					if (t not in comesAfterMeList):
						comesAfterMeList.append(t)
					index += 1
				break
	return len(comesAfterMeList)


def getDigitsPresent(succesfulAtempts):
	presentDigit = [ ]
	for succesfulAtempt in succesfulAtempts:
		digitGen = getDigitsGen(succesfulAtempt)
		for digit in digitGen:
			if(digit not in presentDigit):
				presentDigit.append(digit)
	return presentDigit


array = []
for x in range (0,10):
	array.append(comesAfterMe(x,succesfulAtempts))

presentDigits = getDigitsPresent(succesfulAtempts)
printed = []
for y in range (0,10):
	num = max(array) 
	index = getIndexList(num, array)
	if (index in presentDigits and str(index) not in printed):
		printed.append(str(index))
	array[index] = 0

print(''.join(printed))

#print(succesfulAtempts) 
