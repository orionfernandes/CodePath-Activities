str1 = input("Enter string: ")    # check number of digits in string and calculate average 
empty = ""
for i in str1:
	if i.isdigit():
		empty = empty + i

def getsum(n):
	count = 0
	sum = 0
	for digit in str(n):
		sum +=int(digit)
		count+=1
	print(sum)
	print("Average number of digits: ", sum/count)

getsum(empty)

def get_cons(string):    # check longest string of consecutive digits 
	count1 = 0
	longest = 0
	for i in range(len(string)):
		if string[i] in '0123456789':
			count1 +=1

		elif string[i] not in '0123456789':
			if count1>longest:
				longest = count1
				count1 = 0
			else:
				count1 = 0
	print("consecutive: ", longest)
		
get_cons(str1)
