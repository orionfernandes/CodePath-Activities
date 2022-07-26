dic1 = {"apples": 2, "bananas": 3, "oranges": 5}
dic2 = {"pineapples": 3, "grapes": 6, "apples": 4}

item = str(input("Enter fruit from inventory: "))

def total_inventory(dic1, dic2, item):
  
  if item in dic1 and item in dic2:
    print(item,"=", dic1[item] + dic2[item]) 
  
  elif item in dic1:
    print(item,"=", dic1[item])
    
  elif item in dic2:
    print(item,"=", dic2[item])
    
  else:
    print("Item not found !")
  
  
total_inventory(dic1, dic2, item)
