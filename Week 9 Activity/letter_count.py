
word_list = ['car', 'bat', 'rat']

counter = {}

def letter_count(word_list):

  for i in range(len(word_list)):
    for j in word_list[i]:
      if j not in counter:
        counter[j] = 1
      else:
        counter[j] +=1

  print("Input: ", word_list)
  print(counter)
  

letter_count(word_list)







