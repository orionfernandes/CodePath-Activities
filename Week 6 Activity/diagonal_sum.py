def diagonal_sum(m):
  sum = 0
  for i in range(len(m)):
    sum += m[i][i]
  return sum

# Test Cases
m = [ [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]] 



print("Input: ", m)
print("Output: ", diagonal_sum(m)) #15

m = [[1]]
print("\nInput: ", m)
print("Output: ", diagonal_sum(m)) #1
