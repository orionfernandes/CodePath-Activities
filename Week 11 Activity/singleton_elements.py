lst= [1, 2, 2, 6, 1, 3, 2]

a = []

def singelton_elements(lst):
  for i in lst:
    if lst.count(i) == 1:
      a.append(i)
  return a
  
print(singelton_elements(lst))
  
