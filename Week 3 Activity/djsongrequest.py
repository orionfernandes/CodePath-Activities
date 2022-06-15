
print("Welcome to the DJ Request !")

song_list = []

song_name = input("Enter Song: ")

song_list.append(song_name)

print("The song", song_name, "has been added. It is song number ", (song_list.index(song_name)+1), "on the list \n")



while (song_name != "quit"):
	
	song_name = input("Enter Song: ")

	song_list.append(song_name)

	print("The song", song_name, "has been added. It is song number ", (song_list.index(song_name)+1), "on the list \n")

	song_name = input("Enter Song: ")

	song_list.append(song_name)

	if( song_name in song_list):
		print("The song", song_name, "has already been requested. It is song number ", (song_list.index(song_name)+1)," on the list \n")

	else:

		song_list.append(song_name)

		print("The song", song_name, "has been added. It is song number ", (song_list.index(song_name)+1), "on the list \n")
		
		continue
