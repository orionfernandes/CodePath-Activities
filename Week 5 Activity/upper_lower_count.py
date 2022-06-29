str1 = str(input("Enter string: "))

def upper_lower_count(string):
	up = 0
	low = 0
	for i in str1:
		if i.isupper() == True:
			up+=1
		elif i.islower() == True:
			low+=1

	print("Number of uppercase: ", up)
	print("Number of lowercase: ", low)

upper_lower_count(str1)
