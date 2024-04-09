print("Welcome ")

score = 0
lives = 5
start = input("Do you wish to play the Quiz: ").lower()

def life():
    print("You have " + str(lives) + " lives left")
    if lives == 0:
        print("Game Over")
        quit()

while True:
    if start == "yes":
        print("Lets Go!!!")
    else:
        print("Goodbye!!!")
        break

    print("Your score is:" + str(score))
    print("Lives:" + str(lives))

    question_1 = input("Who was the first wife of Prophet Muhammad SAW? ").lower()
    if question_1 == "khadija":
        print("Correct")
        score += 20
    else:
        print("Wrong answer")
        lives -= 1
        life()
    question_2 = input("What was the first chapter of the Qur'an revealed to Prophet Muhammad SAW? ").lower()
    if question_2 == "alaq":
        print("Correct")
        score += 20
    else:
        print("Wrong answer")
        lives -= 1
        life()

    question_3 = input("Who was the first man kill another man? ").lower()
    if question_3 == "cain":
        print("Correct")
        score += 20
    else:
        print("Wrong answer")
        lives -= 1
        life()
    question_4 = input("How many chapters are contained in The Qur'an? ").lower()
    if question_4 == str(114):
        print("Correct")
        score += 20
    else:
        print("Wrong answer")
        lives -= 1
        life()
    question_5 = input("How many children did Prophet Muhammad SAW birth? ").lower()
    if question_5 == "9":
        print("Correct")
        score += 20
    else:
        print("Wrong answer")
        lives -= 1
        life()
    question_6 = input("How many Prophets were mentioned in Holy Qur'an ").lower()
    if question_6 == str(25):
        print("Correct")
        score += 20
    else:
        print("Wrong answer")
        lives -= 1
        life()
    question_7 = input("Who did Allah refer to as a \"friend\" ").lower()
    if question_7 == "ibrahim":
        print("Correct")
        score += 20
    else:
        print("Wrong answer")
        lives -= 1
        life()
    question_8 = input("Which Prophet spoke to Allah? ").lower()
    if question_8 == "musa":
        print("Correct")
        score += 20
    else:
        print("Wrong answer")
        lives -= 1
        life()
    question_9 = input("What is the shortest chapter in the Qur'an? ").lower()
    if question_9 == "kauthar":
        print("Correct")
        score += 20
    else:
        print("Wrong answer")
        lives -= 1
        life()
    question_10 = input("What is the name of Prophet Muhammad's most beloved daughter? ").lower()
    if question_10 == "fatima":
        print("Correct")
        score += 20
        print(score)
    else:
        print("Wrong answer")
        lives -= 1
        life()
    break

print("Thank you for playing")


