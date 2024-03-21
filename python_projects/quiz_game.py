print("Welcome")
start = input("Do you wnat to play this quiz: ").lower()
score = 0
lives = 3
print("Your score is " + str(score))
print("You have " + str(lives) + " lives.") 

if start != "yes":
    quit()
else:
    print("Lets go!!!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
    lives = 3
    print("Your score is " + str(score))
    print("You have " + str(lives) + " lives.") 
else:
    print("Incorrect!")
    score = 0
    lives -= 1
    print("Your score is " + str(score))
    print("You have " + str(lives) + " lives.") 


answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
    lives = 3
    print("Your score is " + str(score))
    print("You have " + str(lives) + " lives.") 
else:
    print("Incorrect!")
    score = 0
    lives -= 1
    print("Your score is " + str(score))
    print("You have " + str(lives) + " lives.") 

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
    lives = 3
    print("Your score is " + str(score))
    print("You have " + str(lives) + " lives.") 
else:
    print("Incorrect!")
    score = 0
    lives -= 1
    print("Your score is " + str(score))
    print("You have " + str(lives) + " lives.") 

    
answer = input("What does I/O unit stand for? ")
if answer.lower() == "input/output unit":
    print("Correct!")
    score += 1
    lives = 3
    print("Your score is " + str(score))
    print("You have " + str(lives) + " lives.") 
else:
    print("Incorrect!")
    score = 0
    lives -= 1
    print("Your score is " + str(score))
    print("You have " + str(lives) + " lives.") 

answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    print("Correct!")
    score += 1
    lives = 3
    print("Your score is " + str(score))
    print("You have " + str(lives) + " lives.") 
else:
    print("Incorrect!")
    score = 0
    lives -= 1
    print("Your score is " + str(score))
    print("You have " + str(lives) + " lives.") 

print("You scored " + str(score) + " points.")


# Version 2
# create multiple quizes
#define functions for scores 
# be able to update the score in the else statement
