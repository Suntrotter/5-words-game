user_wallet = {"John": 48}
food_store = {"Snickers": 23, "Pepsi": 13, "Car": 10, "Fish": 11}
user_bag = []
user = input("Please enter the user's name: ")
if user in user_wallet:  # checking if the user exists
    pass
else:
    print("This user does not exist. Please try again.")
    user = input("Please enter the user's name: ")


def purchases(user, food_store):
    purchase = input("Please enter the purchase or enter q to quit: ")
    purchase = purchase.capitalize()
    if purchase == "Q":
        print("Bye then, have a nice day!")
    if purchase not in food_store and purchase != "Q":
        print("Sorry, we have no", purchase, "but we have other products.")
        purchases(user, food_store)
    if purchase in food_store:
        purchase_cost = food_store[purchase]
        money = user_wallet[user]
        change = money - purchase_cost
        user_wallet[user] = user_wallet[user] - purchase_cost  # updating the money in the wallet
        if change < 0:
            print("Sorry, you don't have enough money.")
        elif change >= 0:
            del food_store[purchase]
            print("Here is your", purchase, "and you still have", change, "dollars left.")
            user_bag.append(purchase)
            buy_more = input("Do you want to buy something else? Yes or No: ")
            buy_more = buy_more.lower()
            if buy_more == "yes":
                purchases(user, food_store)
            if buy_more == "no":
                print("Bye then, have a nice day!")
            if buy_more != "yes" and buy_more != "no":
                print("You've typed something strange!")
    return user_bag


purchases(user, food_store)


def show_bag(user_bag):
    answer = input("Have you bought something? Yes or No? ")
    answer = answer.capitalize()
    if answer == "No":
        print("It's a pity!")
    if answer == "Yes":
        print("Show it to me!")
        print("OK, here it is: ")
        n = 0
        while n < len(user_bag):
            print(user_bag[n], end=' ')
            n = n + 1
        print("\nWow! Thank you!")


show_bag(user_bag)
