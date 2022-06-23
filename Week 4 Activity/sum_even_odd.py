
even = []
odd =[]
list = []

nums = [1, 2, 3, 4]

def sum_even_odds(nums):
	for i in nums:
		if i%2 ==0:
			even.append(i)
	for j in nums:
		if j%2 != 0:
			odd.append(j)

	a = sum(even)
	b = sum(odd)
	
	print("Sum of even = ", a)
	print("Sum of odd = ", b)

	list.insert(0, a)
	list.insert(1, b)

	print(list)

sum_even_odds(nums)
