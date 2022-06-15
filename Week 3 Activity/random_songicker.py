import random

song_list = []

song_name = input("Enter song: ")

while (song_name != "stop"):
	song_list.append(song_name)

	song_name = input("Enter song: ")

	num = random.choice(song_list)
	print("Randomly Selected song: ", num)

	choice = input("Do you wish to pick another ? (Y/N): \n")
	
  if(choice == 'Y' or choice == 'y'):
		num = random.choice(song_list)
		print(" Randomly Selected song: ", num)
    
	else:
		continue
