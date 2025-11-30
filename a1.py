# Program to find all substring of a string

import math

def printPowerSet(set,set_size):
	
	# Find total elements possible in the power set
	pow_set_size = (int) (math.pow(2, set_size))
	counter = 0
	j = 0
	num=0
	
	for counter in range(0, pow_set_size):
		for j in range(0, set_size):
			
			# Check if jth bit in the counter is set If set then print jth element from set
			if((counter & (1 << j)) > 0):
				print(set[j], end = "")
		num+=1		
		print("")
		
	print("size of power set: ",num)
size=int(input("Enter array size: "))
set=[]
for i in range(0,size):
	n=int(input("Enter element: "))
	set.append(n)

printPowerSet(set, len(set))


