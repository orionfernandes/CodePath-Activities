
lst = [1, 2, 3, 1, 4, 5]
w = 3

def find_substring(lst, w):
	ptr1 = 0
	ptr2 = w
	maxi = 0
	lists =[]
	while ptr2 <= len(lst):
		if max(lst[ptr1:ptr2]) > maxi:
			maxi = max(lst[ptr1:ptr2])
			lists.append(maxi)
		else:
			maxi = maxi
			lists.append(maxi)

		ptr1 += 1
		ptr2 += 1

	print(lists)	


	print(" ".join(map(str,lists)))

find_substring(lst, w)
