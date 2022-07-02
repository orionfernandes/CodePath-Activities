s = ["the", "quick", "brown", "fox", "quick"]

word1 = "the"

word2 = "fox"

def word_distance(word_list, word1, word2):
	
	for i in range(len(s)):
		for j in range(len(s)):
			if s[i] == word1 and s[j] == word2:
				answer = s.index(word2) - s.index(word1)

	print(answer)

word_distance(s, word1, word2)
