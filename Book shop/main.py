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

from admin_user_utils import *
from user_utils import *
from admin_utils import *

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


def user_panel():
    case = input("""Do you wanna see or buy books?
1. See
2. Buy
Please enter 1 or 2: """)
    match case:
        case "1":
            see_books()
        case "2":
            buy_books()
        case _:
            print("Wrong choice, buddy. Please try again")
            user_panel()


def admin_authentication():
    login_OK = input("Please enter your login: ")
    n = 0
    success = ""
    while n <= len(admins):
        if n == len(admins) and success != "OK":
            print("Incorrect login! Please log in again")
            admin_authentication()
        if n < len(admins) and login_OK == admins[n]["login"]:
            password_OK = input("Please enter password: ")
            if password_OK == admins[n]["password"]:
                success = "OK"
                admin_panel()
                return success
            else:
                print("Incorrect password! Please log in again")
                admin_authentication()
        n = n + 1


def user_authentication():
    login_OK = input("Please enter your login: ")
    n = 0
    success = ""
    while n <= len(users):
        if n == len(users) and success != "OK":
            print("Incorrect login! Please log in again")
            user_authentication()
        if n < len(users) and login_OK == users[n]["login"]:
            password_OK = input("Please enter password: ")
            if password_OK == users[n]["password"]:
                success = "OK"
                user_panel()
                return success
            else:
                print("Incorrect password! Please log in again")
                user_authentication()
        n = n + 1


def user_registration():
    new_user = {}
    login = input("Please enter your login: ")
    password = input("Please enter your password: ")
    n = 0
    flag = 0
    while n < len(users):
        if users[n]["login"] == login and users[n]["password"] == password:
            flag = 1
        n = n + 1
    if flag == 1:
        print("Such a user already exists! Please try again")
        user_registration()
    elif flag == 0:
        new_user["login"] = login
        new_user["password"] = password
        new_user["ID"] = login[:3] + password[:4]
        users.append(new_user)
        print("Now please log in to access the user panel")
        user_authentication()


def user_database():
    new_or_old = input("Are you a registered or a new user? Print R or N: ")
    new_or_old = new_or_old.lower()
    if new_or_old == "r":
        user_authentication()
    elif new_or_old == "n":
        print("Welcome! Please register. It's quick")
        user_registration()
    elif new_or_old != "r" and new_or_old != "n":
        print("Wrong choice, buddy! Please try again")
        user_database()


def main():
    choice = input("Are you a user or an admin? U for user or A for admin: ")
    choice = choice.lower()
    if choice == "a":
        admin_authentication()
    elif choice == "u":
        user_database()
    elif choice != "a" and choice != "u":
        print("Wrong choice, buddy! Please try again")
        main()

if __name__ == "__main__":
    main()

















