def game():
    while True:
        rules = input("Do you wish to play this game: ").lower()
        if rules == "yes":
            print("Lets gooo!!!")
        elif rules == "no":
            print("Goodbye")
            break
        else:
            print("Please make a valid choice.")
            continue
        
        current_score = 0
        print("Question 1: What is the capital of Nigeria?")
        answer = input().lower()
        if answer == "abuja":
            print("Correct")
            current_score += 1
            print("Your score is: " + str(current_score))
        elif answer != "abuja":
            print("Wrong answer.")
            print("Your score is: " + str(current_score))
            

        print("Question 2: What is the capital of Ghana?")
        answer = input().lower()
        if answer == "accra":
            print("Correct")
            current_score += 1
            print("Your score is: " + str(current_score))
        elif answer != "accra":
            print("Wrong answer.")
            break


"""elif print("Question 1"):
    question1 = input("What is the capital of Nigeria: ")
        if question1 != "abuja":
        return input("Wrong answer. Try again")
        else:
        print("Question 2")
    question2 = input("what is the capital of Zimbabwe: ")
    if question2 != "harare":
        return input("Wrong answer. Try again")
    else:
        print("Question 3")
    question3 = input("What is the capital of Uganda: ")
    if question3 != "kampala":
        return print("Wrong answer. Try again")
    else:
        print("Question 4")
    question4 = input("What is the capital of Lesotho: ")
    if question4 != "maseru":
        return print("Wrong answer. Try again")
    else:
        print("Question 5")
    question5 = input("What is the capital of Mali: ")
    if question5 != "bamako":
        return print("Wrong answer. Try again")
    else:
        print("Question 6")
    question6 = input("what is the capital of Sudan: ")
    if question6 != "khartoum":
        return print("Wrong answer. Try again")
    else:
        print("Question 7")
    question7 = input("What is the capital of Niger: ")
    if question7 != "niamey":
        return print("Wrong answer. Try again")
    else:
        print("Question 8")
    question8 = input("What is the capital of Benin: ")
    if question8 != "porto-novo":
        return print("Wrong answer. Try again")
    else:
        print("Question 9")
    question9 = input("what is the capital of Ghana: ")
    if question9 != "accra":
        return print("Wrong answer. Try again")
    else:
        print("question 10")
    question10 = input("What is the capital of Rwanda: ")
    if question10 != "kigali":
        return print("Wrong answer. Try again")
    else:
        print("Nice!!! Game completed.")"""
game()
