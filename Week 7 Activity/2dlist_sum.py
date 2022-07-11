n = [[0, 0, 1], [1, 1, 1], [4, 0, 0]]


def max_sum(n):

	result = list(map(sum, n))
	
	print("Sum of row " , result)

	print(f"Max value of sum is {max(result)}")

max_sum(n)
