
word_list = ['car', 'bat', 'rat']

counter = {}

most_common = []

max = 0

def letter_count(word_list):
  max = 0
  for i in range(len(word_list)):
    for j in word_list[i]:
      if j not in counter:
        counter[j] = 1
      else:
        counter[j] +=1

  for count in counter.values():
    if count > max:
      max = count

  for letter, count in counter.items():
    if count == max:
      most_common.append(letter)
  

  print("Input: ", counter)
  print("Output: ", most_common)
  

letter_count(word_list)







