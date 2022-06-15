print("Welcome to the Food Ordering System !")

order = []

user_order = input("What would you like today ? \n")

order.append(user_order)

while (user_order != "done"):

	user_order = input("Anything else to order ?: ")

	order.append(user_order)

	if (user_order == "done"):
    order.pop(-1)
		print("Goodbye ! Thnx for ordering. \n")
		print("Your order includes: ")
		print(order)

	else:
		continue
