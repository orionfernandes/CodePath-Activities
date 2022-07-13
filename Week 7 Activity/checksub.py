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
