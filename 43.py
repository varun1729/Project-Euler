import itertools
import time 
t1 = time.monotonic()
primeDivisors = [2,3,5,7,11,13,17]

def isDivisible (num):
	b = 1
	while(b<=7):
  		if (not (int(num[b:b+3])%primeDivisors[b-1] == 0)):
  			return False
  		b += 1
	return True 

gen = itertools.permutations('0123456789',10)
a = 0
for x in gen:
  	num = ''.join(x)
  	b = 1
  	if(isDivisible(num)):
	  	a += int(num)
	
 	

print(a,'\n','Execution time:', time.monotonic() - t1,'s')