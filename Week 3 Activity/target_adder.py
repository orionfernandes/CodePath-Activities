menu=[1,2, 3, 4, 5]
t = 6


def count(i, target):
	for i in range(len(menu)):
		for j in range(len(menu)):
			curr = menu[i]
			sec = menu[j]

		if( t - curr == sec):
			print("number 1: ", curr, " number 2: ", sec)
    else:
      print("False")


count(menu, t)
