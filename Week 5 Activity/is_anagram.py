def is_anagram(str1, str2):

	for char in str1:
		if char in str2:
			print("True")
			break

		else:
			print("False")
			break

is_anagram("dog", "cat")
