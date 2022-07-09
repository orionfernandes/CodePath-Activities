list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

k = int(input("Enter target number: "))

def search_list(list, k):
	
	result = any(k in sublist for sublist in list)
	print(str(result))
	
search_list(list, k)
