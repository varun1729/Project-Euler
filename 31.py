
import time
t1 = time.clock()
val = [200,100,50,20,10,5,2,1]

target = 200
def getUb (val):
	return target//val + 1

ways = 0
#2pound
for a in range (0, getUb(val[0])):
	if (a*val[0] >target):
		break
	#1pound
	for b in range (0,getUb(val[1])):
		if (a*val[0] + b*val[1] >target):
			break
		#50cent
		for c in range (0, getUb(val[2])):
			if (a*val[0] + b*val[1] + c*val[2] >target):
				break
			#20cent
			for d in range (0, getUb(val[3])):
				if (a*val[0] + b*val[1] + c*val[2] + d*val[3] >target):
					break
				#10cent
				for e in range(0, getUb(val[4])):
					if (a*val[0] + b*val[1] + c*val[2] + d*val[3] + e*val[4]>target):
						break
					#5cent
					for f in range(0, getUb(val[5])):
						if (a*val[0] + b*val[1] + c*val[2] + d*val[3] + e*val[4] + f*val[5] >target):
							break
						#2cent
						for g in range(0, getUb(val[6])):
							if (a*val[0] + b*val[1] + c*val[2] + d*val[3] + e*val[4] + f*val[5] + g*val[6] >target):
								break
							#1dent
							for h in range(0,getUb(val[7])):
								if (a*val[0] + b*val[1] + c*val[2] + d*val[3] + e*val[4] + f*val[5] + g*val[6] + h*val[7] >target):
									break
								else:
									if((a*val[0] + b*val[1] + c*val[2] + d*val[3] + e*val[4] + f*val[5] + g*val[6] + h*val[7]) == target):
										ways +=1
print('Execution time: ', time.clock() - t1)
print(ways)

'''

import time
t1 = time.clock()
val = [200,100,50,20,10,5,2,1]
ub = 7
target = 200
def ways (target, ub, val):
	if (ub == 0):
		return 1
	result = 0
	while (target >= 0):
		result += ways(target, ub-1,val)
		target -= val[ub-1]
	return result
print(ways(target,ub,val))

print('Execution time: ', time.clock() - t1)

'''
