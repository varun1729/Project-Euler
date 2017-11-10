import time
import math
t1 = time.monotonic()
testing = '123456789'
pandigitals =[]
for x in range (1,10000):
	num = ''
	i = 1
	while(len(num) <= 9):
		product = x*i
		num += str(product)
		#print(num)
		i+=1
		if(len(num) == 9 and ''.join(sorted(num)) == testing):
			pandigitals.append(int(num))
print((pandigitals))
print('Execution time:',time.monotonic()-t1,'s')

