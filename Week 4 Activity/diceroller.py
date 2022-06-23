import random

die = [1, 2, 3, 4, 5, 6]
die1 = []
die2 = []

def roller():
	dub = 0
	roll = 0
	throw1 = random.randint(1, 6)
	die1.append(throw1)
	throw2 = random.randint(1, 6)
	die2.append(throw2)
	roll+=1
	while True:
		
		throw1 = random.randint(1, 6)
		die1.append(throw1)

		throw2 = random.randint(1, 6)
		die2.append(throw2)

		roll+=1
		if throw1 == throw2 == 1:
			print("You got snake eyes !")
			print("die 1 = ", die1, "\n")
			print("Average of die 1 = ",sum(die1)/len(die1),"\n")
			print("die 2 = ", die2, "\n")
			print("Average of die 2 = ",sum(die2)/len(die2),"\n")
			print("Number of rolls = ", roll, "\n")
			print("Number of doubles rolled = ", dub)
			break

		elif(throw1 == throw2):
			dub+= 1

roller()

