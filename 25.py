import sys

def getFib(index,list_Fibs):
	if (index == 0 or index == 1):
		list_Fibs[index] = 1
	elif (list_Fibs[index] == 0):
		list_Fibs[index] = getFib(index-1,list_Fibs) + getFib(index-2,list_Fibs)
	return list_Fibs[index]

list_FibsSize = 10000
list_Fibs = [0]*list_FibsSize
counter = 0
for x in range (0,list_FibsSize):
	getFib(x, list_Fibs)
	
	if(list_Fibs[x] >= 10**999):
		counter+=1
		print(x + 1,'\n', list_Fibs[x])
		#our index starts at 0, PE starts its at 1 so x+=1b
	if (counter >=1):
		sys.exit()
	