
hours = int(input("enter hours: "))
mins = int(input("enter mins: "))

def miliary_to_standard(hours, mins):
	
	if hours == 12 and mins == 0:
		print("12:00PM")

	elif hours == 0 and mins == 0:
		print("12:00AM")

	elif hours >= 12:
		print(f"{hours-12}:{mins}PM") 

	elif hours <12:
		print(f"{12 - hours}:{mins}AM")


miliary_to_standard(hours, mins)
