
lst = [[1, 2, 3], [4, 5, 6, 1, 2], [8, 9, 10, 12, 2]]

target = int(input("Enter target number: "))

def search_list(list, target):
	
	count = 0
	for i in range(len(lst)):
		if target in list[i]:
			count += 1

	print(count)
		
	
search_list(lst, target)
