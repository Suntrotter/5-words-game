books_shop = [
    {
        "prod_id": "Esmeralda",
        "amount": 10,
        "label": "A truly captivating love story",
        "price": 233,
        "description": "The girl relocates to a new country and falls in love with a local",
        "genre": "love story"
    },
    {
        "prod_id": "Killer's Color",
        "amount": 15,
        "label": "A thrilling detective story",
        "price": 155,
        "description": "A killer appears in a small town whose victims are women dressed in white",
        "genre": "detective story"
    },
    {
        "prod_id": "Ghost's Blood",
        "amount": 20,
        "label": "A blood-freezing ghost story",
        "price": 100,
        "description": "The house is haunted, and ghosts leave blood on the walls once a month",
        "genre": "horror story"
    },
    {
        "prod_id": "Discover Uruguay",
        "amount": 25,
        "label": "Read the unknown facts on Uruguay that will fascinate you",
        "price": 300,
        "description": "A blogger relocates to Uruguay for three months to explore the country's life",
        "genre": "travel"
    },
    {
        "prod_id": "Dictatorship: Curse or Blessing?",
        "amount": 30,
        "label": "An overview of the most prominent dictators in the world's history",
        "price": 200,
        "description": "Read about the rule of the best-known dictators in history",
        "genre": "historical book"
    },

    {
        "prod_id": "Kingdom of Lust",
        "amount": 100,
        "label": "A practical manual of sensual pleasures",
        "price": 500,
        "description": "Love story and sex",
        "genre": "love story"
    }

]

admins = [{"login": "sun", "password": "moon"}, {"login": "sky", "password": "star"}]
users = [{"login": "first", "password": "stunning"}, {"login": "second", "password": "unearthly"}]
cart = []

from main import *
from admin_utils import *
from admin_user_utils import *

def bill(cart):
    if len(cart) == 1:
        print("Your bill is UAH", cart[0])
    elif len(cart) > 1:
        print("You get a 10% discount.")
        bill = 0
        n = 0
        while n < len(cart):
            bill = bill + cart[n]
            n = n + 1
        print("Your bill is UAH", bill + bill * 0.1)
    choice = input("Do you want to do something else or quit? 1 to do or 2 to quit: ")
    if choice == "1":
        user_panel()
    elif choice == "2":
        print("Have a nice day!")


def buy_books():
    print("If you buy at least 2 books, you will get a 10% discount")
    print("We have the following books: ")
    n = 0
    while n < len(books_shop):
        print(n + 1, books_shop[n]["prod_id"])
        n = n + 1
    choice = input("Please type the number of book you wanna buy: ")
    cart.append(books_shop[int(choice) - 1]['price'])
    continue_shopping = input("Wanna buy more? Y or N: ")
    continue_shopping = continue_shopping.lower()
    if continue_shopping == "n":
        bill(cart)
    elif continue_shopping == "y":
        buy_books()
    return cart

def quit_continue_user():
    choice = input("Do you want to do something else or quit? 1 to do or 2 to quit: ")
    if choice == "1":
        user_panel()
    elif choice == "2":
        print("Have a nice day!")
    else:
        print("Wrong letter, buddy. Try again")
        quit_continue_user()

