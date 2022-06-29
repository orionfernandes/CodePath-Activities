s = str(input("Input string: "))

def fix_capitalization(s):
	
	temp = s.split('. ')
	finallist = []
	for i in temp:
		finallist.append(i.capitalize())
	

	print(". ".join(finallist))


fix_capitalization(s)
