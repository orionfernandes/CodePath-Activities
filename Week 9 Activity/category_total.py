a = []

total = 0

def category_total(inventory, categories, category):
  total = 0
  for values in categories.values():
    l = list(categories[category])

  for i in range(len(l)):
    a.append(inventory.get(l[i]))

  for val in a:
    if val is not None:
      total += val

  return total
