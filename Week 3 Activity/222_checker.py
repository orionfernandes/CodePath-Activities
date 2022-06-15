passing_test = [2, 2, 2]
failing_test = [2, 1, 4, 2, 3]
failing_test = [1, 3, 5, 2, 22, 222, 1, 3, 2]

def has_222(nums):
	# nums = [2, 2, 3, 2]

	for index in range(len(nums)-2):    # list within limits
		curr = nums[index]
		sec = nums[index+1]
		third = nums[index+2]

	if (curr == sec == third == 2):
		print("True")
	else:
		print("False")


has_222(passing_test)
	
