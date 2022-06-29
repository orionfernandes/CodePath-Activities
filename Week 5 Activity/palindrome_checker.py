s = str(input("Enter word: "))

empty = ""

for i in s:
	if i.isalpha():
		empty = empty + i
b = empty.lower()
reverse = b[::-1]

print("Input: ",b, "\n")
print("Reverse: "reverse, "\n")

if reverse == b:
	print("Palindrome")
else:
	print("Not a Palindrome")
