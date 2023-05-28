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
from user_utils import *

def books_display_by_price(n, list):
    print("------------------------------------------------")
    print(list[n]["prod_id"])
    print("Price: UAH", list[n]["price"])
    if len(books_shop[n]["description"]) > 30:
        print(books_shop[n]["description"][:31] + "...Read more")
    elif len(books_shop[n]["description"]) <= 30:
        print(books_shop[n]["description"])
    print("Genre: ", list[n]["genre"])

def sort_cheap_to_expensive():
    my_list = sorted(books_shop, key=lambda k: k['price'])
    n = 0
    while n < len(my_list):
        books_display_by_price(n, my_list)
        n = n + 1
    choice = input("Do you want to do something else or quit? 1 to do or 2 to quit: ")
    if choice == "1":
        admin_or_user()
    elif choice == "2":
        print("Have a nice day!")


def sort_expensive_to_cheap():
    my_list = sorted(books_shop, key=lambda k: k['price'])
    n = - 1
    while abs(n) <= len(my_list):
        books_display_by_price(n, my_list)
        n = n - 1
    choice = input("Do you want to do something else or quit? 1 to do or 2 to quit: ")
    if choice == "1":
        admin_or_user()
    elif choice == "2":
        print("Have a nice day!")


def books_by_price():
    choice = input("""Please choose how you wanna see the books:
1. From cheap to expensive
2. From expensive to cheap
Please enter 1 or 2: """)
    if choice == "1":
        sort_cheap_to_expensive()
    elif choice == "2":
        sort_expensive_to_cheap()
    else:
        print("Wrong digit, buddy. Try again")
        books_by_price()
    choice = input("Do you want to do something else or quit? 1 to do or 2 to quit: ")
    if choice == "1":
        admin_or_user()
    elif choice == "2":
        print("Have a nice day!")


def books_display_by_genre(genre):
    n = 0
    while n < len(books_shop):
        if books_shop[n]["genre"] == genre:
            print("------------------------------------------------")
            print(books_shop[n]["prod_id"])
            print("Price: UAH", books_shop[n]["price"])
            if len(books_shop[n]["description"]) > 30:
                print(books_shop[n]["description"][:31] + "...Read more")
            elif len(books_shop[n]["description"]) <= 30:
                print(books_shop[n]["description"])
        n = n + 1


def books_by_genres():
    choice = input("""Please choose the genre:
1. love story
2. detective story
3. horror story
4. travel
5. historical book
Enter one digit from 1 to 5: """)
    if choice == "1":
        books_display_by_genre("love story")
    elif choice == "2":
        books_display_by_genre("detective story")
    elif choice == "3":
        books_display_by_genre("horror story")
    elif choice == "4":
        books_display_by_genre("travel")
    elif choice == "5":
        books_display_by_genre("historical book")
    else:
        print("Wrong digit, buddy. Please try again")
        books_by_genres()
    choice = input("Do you want to do something else or quit? 1 to do or 2 to quit: ")
    if choice == "1":
        admin_or_user()
    elif choice == "2":
        print("Have a nice day!")


def see_all_books():
    n = 0
    while n < len(books_shop):
        print("------------------------------------------------")
        print(n + 1)
        print(books_shop[n]["prod_id"])
        print("Price: UAH", books_shop[n]["price"])
        if len(books_shop[n]["description"]) > 30:
            print(books_shop[n]["description"][:31] + "...Read more")
        elif len(books_shop[n]["description"]) <= 30:
            print(books_shop[n]["description"])
        print("Genre: ", books_shop[n]["genre"])
        n = n + 1


def see_books():
    choice = input("""What exactly do you wanna see?
1. All books
2. Books by genres
3. Books sorted by price
Please enter a digit from 1 to 3: """)
    if choice == "1":
        see_all_books()
    elif choice == "2":
        books_by_genres()
    elif choice == "3":
        books_by_price()
    else:
        print("Wrong digit, buddy. Try again")
        see_books()
    choice = input("Do you want to do something else or quit? 1 to do or 2 to quit: ")
    if choice == "1":
        admin_or_user()
    elif choice == "2":
        print("Have a nice day!")


def admin_or_user():
    who = input("Type A if you are an admin or U if you are a user: ")
    who = who.lower()
    if who == "a":
        admin_panel()
    elif who == "u":
        user_panel()
    else:
        print("Wrong letter, buddy. Try again")
        admin_or_user()