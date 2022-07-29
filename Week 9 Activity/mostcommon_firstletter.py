word_list = ['cat', 'bat', 'rat', 'bar', 'car', 'can']

counter = {}

most_common = []


max = 0
for string in word_list:
  j = string[0]
  
  if j not in counter:
    counter[j] = 1:
  else:
    counter[j] += 1

for count in counter.values():
  if count > max:
    max = count

for letter, count in counter.items():
  if count == max:
    most_common.append(letter)

print("Input: ", counter)
print("Output: ", most_common)
