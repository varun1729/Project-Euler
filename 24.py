import sys
nums = ['0','1','2','3','4','5','6','7','8','9']

def swap(used,send,string):
	temp = string[send]
	string[send] = string[used]
	string[used] = temp
	return string

count = 0
for i in range (0,len(nums)):
    first =  nums[i]
    nums = swap(i,0,nums)
    t1 = nums[1:]
    for j in range (0, len(t1)):
    	second = t1[j]
    	t1 = swap (j,0, t1)
    	t2 = t1[1:]
    	for k in range (0, len(t2)):
    		third = t2[k]
    		t2 = swap(k,0,t2)
    		t3 = t2[1:]
    		for l in range (0, len(t3)):
    			fourth = t3[l]
    			t3 = swap(l,0,t3)
    			t4 = t3[1:]
    			for m in range (0,len(t4)):
    				fifth = t4[m]
    				t4 = swap(m,0,t4)
    				t5 = t4[1:]
    				for n in range (0, len(t5)):
        				sixth = t5[n]
        				t5 = swap(n,0,t5)
        				t6 = t5[1:]
        				for o in range (0, len(t6)):
	        				seventh = t6[o]
	        				t6 = swap(o,0,t6)
	        				t7 = t6[1:]
	        				for p in range (0, len(t7)):
		        				eighth = t7[p]
		        				t7 = swap(p,0,t7)
		        				t8 = t7[1:]
		        				for q in range (0, len(t8)):
		        					nineth = t8[q]
		        					t8 = swap(q,0,t8)
		        					t9 = t8[1:]
		        					for r in range (0, len(t9)):
		        						count+=1
		        						tenth = t9[r]
		        						if (count == 1000000):
		        							print(first+second+third+fourth+fifth+sixth+seventh+eighth+nineth+tenth)
		        						elif (count>1000000):
		        							sys.exit()
								













