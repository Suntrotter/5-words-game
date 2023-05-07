list1 = ["o", "r", "a", "n", "g", "e"]
list2 = ["l", "e", "m", "o", "n"]
list3 = ["p", "e", "a", "r"]
list4 = ["p", "l", "u", "m"]
list5 = ["p", "e", "a", "c", "h"]
word1 = "******"
word2 = "*****"
word3 = "****"
word4 = "****"
word5 = "*****"
score = 0
# Guessing the first word
# Want to play or not?
start = input("I've got five names of fruit for you to guess. Do you want to play? Type Yes or No: ")
if start.lower() != "yes" and start.lower() != "no":
    print("You've typed something strange, buddy.")
elif start.lower() == "no":
    print("Ok, maybe next time. Have a nice day!")
elif start.lower() == "yes":  # choose to guess a word or letters
    decision = input(
        "If you say the word at once, you will score 20 points. If you guess by letter, you will score 10 points. Type W if you want to say the word or L if you want to guess each letter: ")
    if decision.lower() == "w":  # guessing a word
        print("OK, here is the first word: ", word1)
        guess = input("Please type the word: ")
        if guess.lower() == "orange":
            print("Congratulations! It REALLY is an orange! You score 20 points!")
            score = 20
        else:
            print("Unfortunately, that's a wrong guess. Better luck next time!")
    elif decision.lower() == "l":  # guessing letters
        print("OK, here is the first word: ", word1)
        flag = 0
        while word1 != "orange":
            guess = input("Please enter a letter: ")
            if guess in list1:
                index = list1.index(guess)
                word1 = word1[0:index] + guess + word1[index + 1:]
                print("Correct: ", word1)
                flag = 0
            if guess not in list1:
                print("There is no such a letter in the word! Please try again.")
                flag = flag - 1
                if flag == -5:
                    print("You've made five wrong guesses. Game over!")
                    break
            if word1 == "orange":
                print("Congratulations! It REALLY is an orange! You score 10 points!")
                score = 10
    else:
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
            print("OK, here is the word: ", word2)
            guess = input("Please type the word: ")
            if guess.lower() == "lemon":
                print("Congratulations! It REALLY is a lemon! You score 20 points!")
                score = score + 20
            else:
                print("Unfortunately, that's a wrong guess. Better luck next time!")
        if decision.lower() == "l":
            print("OK, here is the word: ", word2)
            flag = 0
            while word2 != "lemon":
                guess = input("Please enter a letter: ")
                if guess in list2:
                    index = list2.index(guess)
                    word2 = word2[0:index] + guess + word2[index + 1:]
                    print("Correct: ", word2)
                    flag = 0
                if guess not in list2:
                    print("There is no such a letter in the word! Please try again.")
                    flag = flag - 1
                    if flag == -5:
                        print("You've made five wrong guesses. Game over!")
                        break
                if word2 == "lemon":
                    print("Congratulations! It REALLY is a lemon! You score 10 points!")
                    score = score + 10
                    break
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
                print("OK, here is the word: ", word3)
                guess = input("Please type the word: ")
                if guess.lower() == "pear":
                    print("Congratulations! It REALLY is a pear! You score 20 points!")
                    score = score + 20
                else:
                    print("Unfortunately, that's a wrong guess. Better luck next time!")
            if decision.lower() == "l":
                print("OK, here is the word: ", word3)
                flag = 0
                while word3 != "pear":
                    guess = input("Please enter a letter: ")
                    if guess in list3:
                        index = list3.index(guess)
                        word3 = word3[0:index] + guess + word3[index + 1:]
                        print("Correct: ", word3)
                        flag = 0
                    if guess not in list3:
                        print("There is no such a letter in the word! Please try again.")
                        flag = flag - 1
                        if flag == -5:
                            print("You've made five wrong guesses. Game over!")
                            break
                    if word3 == "pear":
                        print("Congratulations! It REALLY is a pear! You score 10 points!")
                        score = score + 10
                        break
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
                    print("OK, here is the word: ", word4)
                    guess = input("Please type the word: ")
                    if guess.lower() == "plum":
                        print("Congratulations! It REALLY is a plum! You score 20 points!")
                        score = score + 20
                    else:
                        print("Unfortunately, that's a wrong guess. Better luck next time!")
                if decision.lower() == "l":
                    print("OK, here is the word: ", word4)
                    flag = 0
                    while word4 != "plum":
                        guess = input("Please enter a letter: ")
                        if guess in list4:
                            index = list4.index(guess)
                            word4 = word4[0:index] + guess + word4[index + 1:]
                            print("Correct: ", word4)
                            flag = 0
                        if guess not in list4:
                            print("There is no such a letter in the word! Please try again.")
                            flag = flag - 1
                            if flag == -5:
                                print("You've made five wrong guesses. Game over!")
                                break
                        if word4 == "plum":
                            print("Congratulations! It REALLY is a plum! You score 10 points!")
                            score = score + 10
                            break
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
                    if decision.lower() != "w" and decision.lower != "l":
                        print("You've typed something strange, buddy.")
                    if decision.lower() == "w":
                        print("OK, here is the word: ", word5)
                        guess = input("Please type the word: ")
                        if guess.lower() == "peach":
                            print("Congratulations! It REALLY is a peach! You score 20 points!")
                            score = score + 20
                        else:
                            print("Unfortunately, that's a wrong guess. Better luck next time!")
                    if decision.lower() == "l":
                        print("OK, here is the word: ", word5)
                        flag = 0
                        while word5 != "peach":
                            guess = input("Please enter a letter: ")
                            if guess in list5:
                                index = list5.index(guess)
                                word5 = word5[0:index] + guess + word5[index + 1:]
                                print("Correct: ", word5)
                                flag = 0
                            if guess not in list5:
                                print("There is no such a letter in the word! Please try again.")
                                flag = flag - 1
                                if flag == -5:
                                    print("You've made five wrong guesses. Game over!")
                                    break
                            if word5 == "peach":
                                print("Congratulations! It REALLY is a peach! You score 10 points!")
                                score = score + 10
                                break
print("Your total score is:", score)













