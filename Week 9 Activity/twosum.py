nums = [12, 0, 12, 24] 
target = 24

def pair_sum(list, target):
  p1 = 0
  p2 = 1

  while p1 < p2:
    
    sum = list[p1] + list[p2]

    if sum == target:
      return(p1, p2)

    else:
      p2 +=1
      if p2 == len(nums)-1:
        p1 +=1

  
    
print(pair_sum(nums, target))
