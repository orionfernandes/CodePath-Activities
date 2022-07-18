def most_similar_string(lst,str):
     
    max_string = ""
    max_chars = -1
 
    for word in lst:
      freq = 0
      for char in word.lower():
        if char in str.lower():
          freq += 1
      
      if (freq > max_chars):
        max_string = word
        max_chars = freq
        
    return max_string

             
test_1 = most_similar_string(["tangle", "charge", "ring"], "tangerine")
print(test_1)

test_2 = most_similar_string(["scrap", "sky", "pleasure"], "skyscraper")
print(test_2)
