list = [[1, 2, 3], [4, 5, 6, 1], [8, 9, 10, 12]]

def is_jagged(list):
	for i in range(len(list)-1):
		if len(list[i]) != len(list[i+1]):
			result = "True"
			
		elif len(list[i]) == len(list[i+1]):
			result = "False"
			
		
	print(result)


is_jagged(list)
