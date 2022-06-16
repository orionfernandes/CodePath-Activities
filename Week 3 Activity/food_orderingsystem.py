print("Welcome to the Food Ordering System !")
print("STARBUCKS MENU \n")

menu = ["1 Iced Coffee", "2 Blonde Roast", "3 Matcha Latte", "4 Cold Brew", "5 Caramel Macchiato", "6 Pumpkin Spice Latte", "7 Peppermint Mocha", "8 Iced Green Lemonade", "9 Mango Dragonfruit Refresher", "10 Iced Dirty Chai Latte"]

for i in range(len(menu)):
	print(menu[i],"\n")

order = []

user_order = str(input("What would you like today ? (1 - 10) - "))

if user_order == '1':
	order.append("Iced Coffee")

if user_order == '2':
	order.append("Blonde Roast")

if user_order == '3':
	order.append("Matcha Latte")

if user_order == '4':
	order.append("Cold Brew")

if user_order == '5':
	order.append("Caramel Macchiato")

if user_order == '6':
	order.append("Pumpkin Spice Latte")

if user_order == '7':
	order.append("Peppermint Mocha")

if user_order == '8':
	order.append("Iced Green Lemonade")

if user_order == '9':
	order.append("Mango Dragonfruit Refresher")

if user_order == '10':
	order.append("Iced Dirty Chai Latte")


while (user_order != "done"):

	user_order = str(input("Anything else to order ?: "))

	if user_order == '1':
		order.append("Iced Coffee")

	if user_order == '2':
		order.append("Blonde Roast")

	if user_order == '3':
		order.append("Matcha Latte")

	if user_order == '4':
		order.append("Cold Brew")

	if user_order == '5':
		order.append("Caramel Macchiato")

	if user_order == '6':
		order.append("Pumpkin Spice Latte")

	if user_order == '7':
		order.append("Peppermint Mocha")

	if user_order == '8':
		order.append("Iced Green Lemonade")

	if user_order == '9':
		order.append("Mango Dragonfruit Refresher")

	if user_order == '10':
		order.append("Iced Dirty Chai Latte")

	if (user_order == "done"):
    	
		print("Goodbye ! Thnx for ordering. \n")
		print("Your order: \n")
		for i in range(len(order)):
			print(order[i])

	else:
		continue
