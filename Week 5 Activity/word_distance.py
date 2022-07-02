word_list = ["cat", "dog", "abcd", "dog", "cat", "cat", "abcd", "dog", "wxyz"]

word1 = "abcd"

word2 = "wxyz"

def solve(word_list, word1, word2):
	ans = len(word_list)
	L = None
	for R in range(len(word_list)):
		if word_list[R] == word1 or word_list[R] == word2:
			if L is not None and word_list[R] != word_list[L]:
				ans = min(ans, R - L)
			L = R
	return -1 if ans == len(word_list) else ans

solve(word_list, word1, word2)
