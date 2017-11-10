import itertools
import math
import time
t1 = time.monotonic()
def isPrime(num):
	if(num <= 1):
		return False
	elif(num%2 == 0):
		return False
	elif (num == 3):
		return False
	else:
		divisor = 3
		while(divisor <= math.sqrt(num) +1):
			if(num % divisor == 0):
				return False
			divisor += 2
		return True

def isPermutofEachother(num1, num2):
    digits = sorted(list(str(num1)))
    digits2 = sorted(list(str(num2)))
    return (digits2 == digits)

def getSol (num):
    
    perms = itertools.permutations(num,4)
    temp = []

    for y in perms:
        val = int(''.join(y))
        if(isPrime(val)):
            temp.append(val)


        for z in range (0, len(temp)):
            for z1 in range(z+1, len(temp)):
                diff = temp[z1] - temp[z]
                if(diff > 0 and temp[z] + diff  >1000  and temp[z] + 2*diff > 1000 and temp[z] > 1000):
                    if ((temp[z] + diff in temp) and (temp[z] + 2*diff in temp)):
                        return(temp[z], temp[z] + diff, temp[z] + 2*diff)

'''
def isPermut (num,array):
	i = 0
	temp = []
	diff = []
	for i in range (0, len(array)):
		if (sorted(num) == sorted(array[i])):
			temp.append(array[i])
	return temp

permutGen = itertools.permutations('0123456789',4)

array = []
for x in permutGen:
	val = (''.join(x))
	if(isPrime(int(val))):
		array.append(val)

combGen = itertools.combinations('0123456789',4)

combs = itertools.combinations('0123456789', 4)
for y in combGen:
	if (y[0] != '0'):
		y = ''.join(y)
		temp = isPermut(y,array)
		if (len(temp) >= 3):
			temp2 = []
			for y in temp:
			    temp2.append(int(y))
			#print(temp2)
			print(temp2)
			subPerms = itertools.combinations(temp, 2)
			arrayDiff = []
			for y in subPerms:
			    difference = int(y[1]) - int(y[0])
			    t = [difference, int(y[0])]
			    arrayDiff.append(t)

			for i in range (0, len(arrayDiff)):
			    counter = 0
			    val = arrayDiff[i][1] + arrayDiff[i][0]
			    if (val in temp2):
			        val += arrayDiff[i][0]
			        if(val in temp2):
			            #print(val)
			            print(val, val- arrayDiff[i][0], val - 2*arrayDiff[i][0])
'''
primes = []
for x in range(1000,10000):
	if(isPrime(x)):
		primes.append(str(x))

for z in primes:
	if not(getSol(z) == None):
		print(getSol(z))




'''
arrayDiff = []
for y in range (0, len(primes)):
	for z in range (y, len(primes)):
		difference = primes[z] - primes[y]
		t = [difference, primes[y]]
		arrayDiff.append(t)
t = 0
for i in range (0, len(arrayDiff)):
	val = arrayDiff[i][1] + arrayDiff[i][0]
	if (isPrime(val) and isPermutofEachother(val, arrayDiff[i][1]) and arrayDiff[i][0] != 0):
		val += arrayDiff[i][0]
		if (isPrime(val) and isPermutofEachother(val, arrayDiff[i][1])):
			t+=1
			print(val, val - arrayDiff[i][0], val -2*arrayDiff[i][0])
			print(val -2*arrayDiff[i][0],val - arrayDiff[i][0],val)
			if (t==2):
				break

print(time.monotonic() - t1,'s')
'''