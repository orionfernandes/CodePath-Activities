num = int(input("Enter Number: "))

def add_digits_2(num):
  if num == 0:
    return 0
  elif num%9 == 0:
    return 9
  
  return num%9


print("Output: ", add_digits_2(num))
