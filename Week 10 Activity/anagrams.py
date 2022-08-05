def find_anagrams(word_list):
    anagram_list = []
    for word_1 in word_list: 
        for word_2 in word_list: 
            if word_1 != word_2 and (sorted(word_1)==sorted(word_2)):
                anagram_list.append(word_1)
    return (anagram_list)
    
