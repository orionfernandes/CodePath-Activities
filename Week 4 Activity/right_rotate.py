nums = [1, 2, 3, 4, 5]

n = 1   #defines how many indices to rotate by

if n>len(nums):
   n = int(n%len(nums))
nums = (nums[-n:] + nums[:-n])

print(nums)
