n = [10, 20, 35, 50, 75, 80]

target = 70

def pair_sum(list):
  p1 = 0
  p2 = len(list) - 1

  while p1 < p2:
    
  	sum = list[p1] + list[p2]

  	if sum == target:
  		return True

  	elif sum < target:
  		p1 += 1

  	elif sum > target:
  		p2 -= 1

  return False
    
print(pair_sum(n))
