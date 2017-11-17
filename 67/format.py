file = open("triangle.txt","r+")

nums = []
for line in file:
	nums.append(line)

#print (nums)
final = []
for row in nums:
	temp = 0
	finalRow = []
	for char in row:
		if (char == ' '):
			finalRow.append(temp)
			temp = 0
			continue;
		elif (char == '\n'):
			finalRow.append(temp)
			temp = 0			
			break;
		else:
			temp = temp*10 + int(char)
	final.append(finalRow)

for row in final:
	print (row)