
words = ["cat", "dog", "pig", "dog", "dog", "cat"]

word_dict = {}

def hash_freq(words):
  
  for word in words:
    if word in word_dict:
      word_dict[word] += 1
      print(word_dict)
    


    else:
      word_dict[word] = 1
      print("key created: ", word_dict)



hash_freq(words)




