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
from admin_user_utils import *
from user_utils import *

def quit_continue_admin():
    choice = input("Do you want to do something else or quit? 1 to do or 2 to quit: ")
    if choice == "1":
        admin_panel()
    elif choice == "2":
        print("Have a nice day!")
    else:
        print("Wrong letter, buddy. Try again")
        quit_continue_admin()


def total_book_price():
    n = 0
    total_price = 0
    while n < len(books_shop):
        total_price = total_price + books_shop[n]['price'] * books_shop[n]['amount']
        n = n + 1
    print("The total cost of books in the shop is UAH", total_price)
    quit_continue_admin()


def total_book_number():
    n = 0
    total_number = 0
    while n < len(books_shop):
        total_number = total_number + int(books_shop[n]['amount'])
        n = n + 1
    print("The total number of books in the shop is:", total_number)
    quit_continue_admin()


def delete_book():
    book = input("PLease enter the name of the book you wanna delete: ")
    n = 0
    while n < len(books_shop):
        if books_shop[n]['prod_id'] == book:
            books_shop.remove(books_shop[n])
            print("The book has been successfully deleted!")
            break
        n = n + 1
    quit_continue_admin()


def price_update():
    book = input("Please enter the book name: ")
    price = input("Please enter the book price: ")
    n = 0
    while n < len(books_shop):
        if books_shop[n]['prod_id'] == book:
            books_shop[n]['price'] = price
            print("The price has been successfully updated!")
        n = n + 1
    quit_continue_admin()


def amount_update():
    book = input("Please enter the book name: ")
    amount = input("Please enter the book quantity: ")
    n = 0
    while n < len(books_shop):
        if books_shop[n]['prod_id'] == book:
            books_shop[n]['amount'] = amount
            print("The amount has been successfully updated!")
        n = n + 1
    quit_continue_admin()


def update_books():
    choice = input("Do you wanna update Price or Amount? Enter P or A: ")
    choice = choice.lower()
    if choice == "p":
        price_update()
    elif choice == "a":
        amount_update()
    else:
        print("Wrong choice, buddy. Please try again...")
        update_books()
    quit_continue_admin()


def add_new_book():
    new_book = {}
    title = input("Please enter the book title: ")
    new_book["prod_id"] = title
    amount = input("Please enter how many books we have: ")
    new_book["amount"] = amount
    label = input("Please enter the book label: ")
    new_book["label"] = label
    price = input("Please enter the book price: ")
    new_book["price"] = price
    description = input("Please enter the book description: ")
    new_book["description"] = description
    genre = input("Please enter the book genre: ")
    new_book["genre"] = genre
    books_shop.append(new_book)
    print("The book has been successfully added!")
    choice = input("Type 1 to see books by genres or 2 to continue work: ")
    if choice == "1":
        books_by_genres()
    if choice == "2":
        admin_panel()


def reset_password():
    old_password = input("Please enter your old password: ")
    new_password = input("Please enter your new password: ")
    n = 0
    while n < len(users):
        if admins[n]["password"] == old_password:
            admins[n]["password"] = new_password
            print("Your password has been successfully updated")
        n = n + 1
    quit_continue_admin()

def admin_panel():
    case = input("""Choose what you wanna do:
1. Reset password
2. Add a new book
3. See the available books
4. Update the list of books
5. Delete a book
6. Count all books
7. Total the price of all books

Please enter a digit from 1 to 7: """)
    match case:
        case "1":
            reset_password()
        case "2":
                add_new_book()
        case "3":
                see_books()
        case "4":
                update_books()
        case "5":
                delete_book()
        case "6":
                total_book_number()
        case "7":
                total_book_price()
        case _:
                print('\033[1m' + "Wrong digit. Please choose from 1 to 7" + '\033[0m')
                admin_panel()