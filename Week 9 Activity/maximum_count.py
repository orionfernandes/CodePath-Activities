def maximum_count(inventory):
    
  inventory = {"bananas": 5, "apples": 3, "cherries": 100}
  max = 0

  fruits = list(inventory.keys())
  amount = list(inventory.values())
  
  for value in inventory.values():
    if value > max:
      max = value
    else:
      continue

  position = amount.index(value)
  return fruits[position]


maximum_count(inventory)
