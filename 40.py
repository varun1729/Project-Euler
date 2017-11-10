import time 
t1 = time.monotonic()
irrational = '0'
x =1
while (len(irrational) < 1000000+1):
	irrational += str(x)
	x+=1
	
product = 1
for y in range (0,7):
  product *= int(irrational[10**y])

print(product)
print(time.monotonic()-t1,'s')