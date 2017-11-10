from decimal import *
import math
'''
def isPrime (num):
	if (num <=1):
		return False
	if (num == 2 or num==3):
		return True
	elif (num%2 == 0):
		return False
	else:
		ub = math.ceil(num**(1/2))
		j = 3
		while (j<=ub):
			if (num%j == 0):
				return False 
			j+=2
		return Truen
'''
def RemainderApproach (num):
	array = []
	#array.append(a)
	counter = 1
	a = 1%num
	array.append(a)
	a *=10
	while (not(a%num in array)):
		a = a%num
		array.append(a)
		a *= 10
		counter +=1
	return counter

list_l = [0,1]
for x in range (2,1000):
	list_l.append(RemainderApproach(x))

top = list_l[0]
a = 0
for y in range (0, len(list_l)):
	if (list_l[y] > top):
		top = list_l[y]
		a = y

print(a)

print(max(list_l))
'''

	def getLargestRepeating (num):
		length = 0
		biggest = ''
		for x in range (0, len(num)):
			for y in range (x, len(num)):
				substr = num[x:y]
				length = len(substr)
				for z in range (y, len(num)):
					sub2 = num[z:z+length]
					if (substr == sub2):
						if (length > len(biggest)):
							biggest = substr
		return biggest

list_Reciprocals = [0]*1000

def getReciprocal (num):
	getcontext().prec = num*2
	ReciprocalDigits = str((Decimal(1)/Decimal(num)))
	ReciprocalDigits = ReciprocalDigits[2:]
	while (ReciprocalDigits[0]=='0'):
		ReciprocalDigits = ReciprocalDigits[1:]
	#ReciprocalDigits = ReciprocalDigits[0:num]
	return ReciprocalDigits.rstrip('0')


for x in range (2,1000):
	if (isPrime(x)):
		list_Reciprocals[x] = (getReciprocal(x))

for x in range (0,len(list_Reciprocals)):
	if (list_Reciprocals[x] != 0):
		print ('1/', x, len(list_Reciprocals[x]))


getcontext().prec = 1000
print(str(Decimal (1)/Decimal(7)))
'''

