name = input("Player!!! Enter your name: ").title()
print("Welcome", name + ", this is your adventure.")

prompt_1 = input("You are on a dirt road, it has come to an end. You need to left or right to continue on you journey: ").lower()

if prompt_1 == "left":
    prompt_1 = input("You come to a river you must cross. Do you walk or swim: ").lower()
    
    if prompt_1 == "swim":
        print("You swam and were a eaten by a crocodile. ")
    elif prompt_1 == "walk":
        print("You walked for 10 miles and died of exhaustion. ")
    else:
        print("Wrong option. You lose")

elif prompt_1 == "right":
    prompt_1 = input("You arrived at an old wobbly bridge. Do you wish to cross (Yes/No): ").lower()
    
    if prompt_1 == "yes":
        
        prompt_1 = input("You crossed and met an old man at the other side. Do you engage or ignore him (engage/ignore): ").lower()
        if prompt_1 == "engage":
            print("You greeted the stranger and he gave you a gold chest. ")
        elif prompt_1 == "ignore":
            print("You ignore the stranger and he was offended he cast a spell on you and you bacame a pumpkin which he ate.")
    
    elif prompt_1 == "no":
        print("You went back and were eaten by a wild Boar. ")
        quit()
    else:
        print("Wrong option. You lose")
        quit()
else:
    print("Not a valid option. You lose")
    quit()