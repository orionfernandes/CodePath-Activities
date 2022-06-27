str1 = input("Enter word: ")

count = 0
for i in range(len(str1)):
	if str1[i] in 'aeiou':
		count+=1

print("Number of vowels: ", count)
