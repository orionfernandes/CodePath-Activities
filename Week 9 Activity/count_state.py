locations = {"Bob": "San Francisco", "Anna": "Los Angeles", "Charlie": "Detroit"}
states = {"San Francisco": "California", "Los Angeles": "California", "Ann Arbor": "Michigan", "Detroit": "Michigan"}
state = "California"



def count_by_state(locations, states, state):
  total = 0
  for name, city in locations.items():
    if states[city] == state:
      total += 1
    return total

print(count_by_state(locations, states, state))

