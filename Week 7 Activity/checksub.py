string = "catdogcatdog"
sub = "dog"

def check(l, m):
	a = list(l)
	b = list(m)

	for i in range(len(a)):
		for j in range(len(b)):
			if a[i] == b[0]:
				print("Found substring at index ", i)
				break
			elif j == len(a):
				break
		i+=1
		j+=1		

check(string, sub)



#def find_substring(str, sub):
#  ptr1 = 0
#  ptr2 = len(sub)
#
#  while ptr2 <= len(str):
#    if str[ptr1:ptr2] == sub:
#       print("Found Substring at Index", ptr1)
#    ptr1 += 1
#    ptr2 += 1
#
#find_substring("catdogcat", "dog")
