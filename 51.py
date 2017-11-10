import math
import itertools

def isPrime (num):
    if (num <=1 ):
        return False
    elif (num == 2 or num == 3):
        return True
    elif (num % 2 == 0):
        return False
    else:
        ub = math.ceil(math.sqrt(num))
        i = 3
        while (i <= ub):
            if(num % i == 0):
                return False
            i += 2
        return True

file_obj = open('primes.txt','r')
count = 0
sizeOfNum = 8
EightDigitPrimes = []
for line in file_obj:
    if(len(line) == 9):
        EightDigitPrimes.append(line)

print(len(EightDigitPrimes)

