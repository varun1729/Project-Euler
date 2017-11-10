import sys
import math
import time

t1 = time.monotonic()

def getNumDenomGen (ub):
	
	ub -= 1
	num = 3
	denom = 2
	yield [num,denom]
	
	num1 = 7
	denom1 = 5
	ub -= 1
	yield [num1, denom1]
	
	while (ub >= 1):
		tn = num1
		td = denom1
		num1 = 2*num1 + num
		denom1 = 2*denom1 + denom
		num = tn
		denom = td
		ub -= 1
		yield [num1,denom1]

counter = 0
gen = getNumDenomGen(1000)
for x in gen:
	if (int(math.log(x[0],10)) > int(math.log(x[1],10))):
		counter += 1

print(counter)
t2 = time.monotonic()
print(t2 - t1)

####

print()

####

from fractions import Fraction
sys.setrecursionlimit(2000)

def getsqrt2aprox (x):
	if (x == 1):
		return 2
	else:
		return 2 + Fraction (1,getsqrt2aprox(x-1))

counter = 0
for x in range (1,1001):
	approx = Fraction((1/getsqrt2aprox(x) + 1))
	numerator = approx.numerator
	denominator = approx.denominator
	if(int(math.log(numerator,10)) > int(math.log(denominator,10))):
		counter += 1

print(counter)
print(time.monotonic() - t2)