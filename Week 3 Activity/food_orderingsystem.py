print("Welcome to the Food Ordering System !")
print("1 - Pizza \n 2 - Coke \n 3 - Diet Pepsi \n 4 - Donut \n 5- Fries")

order = []

user_order = str(input("What would you like today ? \n"))

if user_order == '1':
	order.append("Pizza")

if user_order == '2':
	order.append("Coke")

if user_order == '3':
	order.append("Diet Pepsi")

if user_order == '4':
	order.append("Donut")

if user_order == '5':
	order.append("Fries")


while (user_order != "done"):

	user_order = str(input("Anything else to order ?: "))

	if user_order == '1':
		order.append("Pizza")

	if user_order == '2':
		order.append("Coke")

	if user_order == '3':
		order.append("Diet Pepsi")

	if user_order == '4':
		order.append("Donut")

	if user_order == '5':
		order.append("Fries")

	if (user_order == "done"):
    	
		print("Goodbye ! Thnx for ordering. \n")
		print("Your order: ", order)

	else:
		continue
