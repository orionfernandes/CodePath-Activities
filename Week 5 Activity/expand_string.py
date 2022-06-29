list = []

n = int(input("Enter number of elements: "))

for i in range(0, n):
	inp = input("Enter element: ")

	list.append(inp)

def expand_string(list):

	b = ''.join(list).upper()
  
	print(list)
	print(b*5)

expand_string(list)
