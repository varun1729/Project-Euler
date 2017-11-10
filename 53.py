import math

def genPascalTriangle (num):
	triangle = [[1]]
	ub = num+1
	for i in range (1,ub):
		row = [1]
		prevRow = i-1
		for j in range (0,prevRow):
			row.append(triangle[prevRow][j] + triangle[prevRow][j+1])
		row.append(1)
		triangle.append(row)
	return triangle

count = 0
triangle = genPascalTriangle(100)
for x in triangle:
	for y in x:
		if(y>1000000):
			count+=1

print(triangle)
print(count)
