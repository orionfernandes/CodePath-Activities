inventory = {"bananas": 5, "apples": 3, "oranges": 10, "bacon": 1, "sausages": 3}
threshold = 3
low =[]

key_list = list(inventory.keys())
val_list = list(inventory.values())

def maximum_count(inventory, threshold):
  for value in inventory.values():
    if value <= threshold:
      position = val_list.index(value)
      low.append(key_list[position])

  return low
  
 

print(maximum_count(inventory, threshold))
