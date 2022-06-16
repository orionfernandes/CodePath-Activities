list = []

# with reverse()
inp = input("Enter numbers to list: (n to stop): ")
list.append(inp)


if not list:
	print(list)


while (inp!='n'):
	inp = input("Enter numbers to list: (n to stop): ")
	list.append(inp)
	
	
if inp == 'n':
	list.pop(-1)
	list.reverse()
	print("Reversed list is: ", list)

# without reverse()

list[::-1]
print("Reversed list is: ", list)
