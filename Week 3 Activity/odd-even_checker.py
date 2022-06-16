list = []

inp = input("Enter numbers to list: (n to stop): ")
list.append(inp)


if not list:
	print(list)

def count_even_odd(list):
	e = 0  	# even counter set to 0
	o = 0	# odd counter set to 0
	for i in range(len(list)):
		if i%2 ==0:
			e += 1		# even counter increment
		else:
			o+= 1		# odd counter increment

	print("Number of even numbers in the list: ", e)
	print("Number of odd numbers in the list: ", o)



while (inp!='n'):
	inp = input("Enter numbers to list: (n to stop): ")
	list.append(inp)
	
	
if inp == 'n':
	list.pop(-1)
	print("Your list is: ", list)
	count_even_odd(list)

