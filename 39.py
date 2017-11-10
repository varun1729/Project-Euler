'''

byRayfill from the forum
As a starter, based on the relation
   a^2+b^2 = c^2  (1)
If both a and b are even, c will also be even and P (the perimeter) will be even.
If both a and b are odd, c will be even and P will be even.
If one is even and the other is odd, c will be odd and P will again be even.
Therefore, only even values of P need to be checked.
'''
'''
import time
t1 = time.monotonic()
def getRightTrianglePoss (perimeter):
	ways = 0
	for x in range (1,(perimeter)//2):
		for y in range (1, (perimeter - x +1)//2):
			z = perimeter-x-y
			if (x**2 == y**2 + z**2):
				ways+=1
				print(x,y,z)
	return ways

print(getRightTrianglePoss(840))

maximum = 0
index = 0
for a in range (2,1001,2):
  val = getRightTrianglePoss(a)
  if(val > maximum):
    maximum = val
    index = a

print('Execution time:', time.monotonic() - t1,'s')
print(index, maximum)
'''
import time 
t1 = time.monotonic()
def getRightTrianglePossAlgebraic (perimeter):
	ways = 0
	array = [ ]
	a = 1
	
	'''
	Note: this needs to be 'while( a<perimeter//2 and a not in array)', but searching the array takes too long. Twice as many results are given so we need to cut it by dividing by 2. Because, at some point the 'b' equals previously looped over values of a
	'''
	
	while (a < perimeter//2 and a not in array):
  		b = perimeter*(perimeter - 2*a)/(2*(perimeter-a))
  		array.append(b)
  		if (b%1 == 0):
  	  		ways+=1
  		a+=1
	return ways

maximum = 0 
index = 0
for x in range (12,1001,2):
  val = getRightTrianglePossAlgebraic(x)
  if(val > maximum):
    maximum = val
    index = x
print('Execution time:', time.monotonic()-t1,'s')
print(index, maximum)
  
		








