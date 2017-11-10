def getSumSpiral(num):
	if (num == 3):
		return 3+5+7+9+1
	else:
		result = (num-2)*(num-2)+(num-1)
		i = 0
		value = result
		while (i<=2):
			value += num-1
			result += value
			i+=1
		return result + getSumSpiral(num -2)

print(getSumSpiral(1001))

		