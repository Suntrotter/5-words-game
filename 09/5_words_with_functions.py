list_words = ["orange", "lemon", "pear", "plum", "peach"]
word1 = "******"
word2 = "*****"
word3 = "****"
word4 = "****"
word5 = "*****"
list1 = ["o", "r", "a", "n", "g", "e"]
list2 = ["l", "e", "m", "o", "n"]
list3 = ["p", "e", "a", "r"]
list4 = ["p", "l", "u", "m"]
list5 = ["p", "e", "a", "c", "h"]


def guessing_word(word, index):
    print("OK, here is the word: ", word)
    guess = input("Please type the word: ")
    if guess.lower() == list_words[index]:
        print("Congratulations! You score 20 points!")
    else:
        print("Unfortunately, that's a wrong guess. Better luck next time!")


def guessing_by_letters(word, list_index, list):
    print("OK, here is the word: ", word)
    flag = 0
    while word != list_words[list_index]:
        guess = input("Please enter a letter: ")
        if guess in list:
            index = list.index(guess)
            word = word[0:index] + guess + word[index + 1:]
            print("Correct: ", word)
            flag = 0
        if guess not in list:
            print("There is no such a letter in the word! Please try again.")
            flag = flag - 1
            if flag == -5:
                print("You've made five wrong guesses. Game over!")
                break
        if word == list_words[list_index]:
            print("Congratulations! You score 10 points!")


start = input("I've got five names of fruit for you to guess. Do you want to play? Type Yes or No: ")
if start.lower() != "yes" and start.lower() != "no":
    print("You've typed something strange, buddy.")
elif start.lower() == "no":
    print("Ok, maybe next time. Have a nice day!")
elif start.lower() == "yes":  # choose to guess a word or letters
    decision = input(
        "If you say the word at once, you will score 20 points. If you guess by letter, you will score 10 points. Type W if you want to say the word or L if you want to guess each letter: ")
    if decision.lower() == "w":  # guessing a word
        guessing_word(word1, 0)
    elif decision.lower() == "l":  # guessing letters
        guessing_by_letters(word1, 0, list1)
    if decision.lower() != "w" and decision.lower() != "l":
        print("You've typed something strange, buddy.")
        # guessing the second word
    start2 = input("Do you want to continue? I've got four more words to guess! Yes or No? ")
    if start2.lower() != "yes" and start2.lower() != "no":
        print("You've typed something strange, buddy.")
    elif start2.lower() == "no":
        print("Ok, maybe next time. Have a nice day!")
    elif start2.lower() == "yes":
        decision = input("Word and 20 points or letters and 10 points? W or L: ")
        if decision.lower() == "w":
            guessing_word(word2, 1)
        if decision.lower() == "l":
            guessing_by_letters(word2, 1, list2)
        if decision.lower() != "w" and decision.lower() != "l":
            print("You've typed something strange, buddy.")
            # guessing the third word
        start3 = input("Do you want to continue? I've got three more words to guess! Yes or No? ")
        if start3.lower() != "yes" and start3.lower() != "no":
            print("You've typed something strange, buddy.")
        elif start3.lower() == "no":
            print("Ok, maybe next time. Have a nice day!")
        elif start3.lower() == "yes":
            decision = input("Word and 20 points or letters and 10 points? W or L: ")
            if decision.lower() == "w":
                guessing_word(word3, 2)
            if decision.lower() == "l":
                guessing_by_letters(word3, 2, list3)
            if decision.lower() != "w" and decision.lower() != "l":
                print("You've typed something strange, buddy.")
                # guessing the fourth word
            start4 = input("Do you want to continue? I've got two more words to guess! Yes or No? ")
            if start4.lower() != "yes" and start4.lower() != "no":
                print("You've typed something strange, buddy.")
            elif start4.lower() == "no":
                print("Ok, maybe next time. Have a nice day!")
            elif start4.lower() == "yes":
                decision = input("Word and 20 points or letters and 10 points? W or L: ")
                if decision.lower() == "w":
                    guessing_word(word4, 3)
                if decision.lower() == "l":
                    guessing_by_letters(word4, 3, list4)
                if decision.lower() != "w" and decision.lower() != "l":
                    print("You've typed something strange, buddy.")
                    # guessing the fifth word
                start5 = input("Do you want to continue? I've got one more word to guess! Yes or No? ")
                if start5.lower() != "yes" and start5.lower() != "no":
                    print("You've typed something strange, buddy.")
                if start5.lower() == "no":
                    print("Ok, maybe next time. Have a nice day!")
                if start5.lower() == "yes":
                    decision = input("Word and 20 points or letters and 10 points? W or L: ")
                    if decision.lower() != "w" and decision.lower() != "l":
                        print("You've typed something strange, buddy.")
                    if decision.lower() == "w":
                        guessing_word(word5, 4)
                    if decision.lower() == "l":
                        guessing_by_letters(word5, 4, list5)





