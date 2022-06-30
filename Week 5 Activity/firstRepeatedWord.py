import re
from collections import Counter


def firstRepeatedWord(sentence):
    sentence = re.sub(r"[^a-zA-Z ]","",sentence)  #remove delimeters
    words = list(sentence.split(" "))	# take each word in list
    frequency = Counter(words) 	# get the frequency of each word
    for word in words: 	# loop all words
        if(frequency[word] > 1): 	# frequency of word is > 1
            return word



sentence = "Mary had a Little lamb little lamb"
print(firstRepeatedWord(sentence))
