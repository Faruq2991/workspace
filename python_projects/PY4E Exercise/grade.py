
grade_input = float(input("Enter a score between 0.0 and 1.0: "))

if grade_input < 0.0 and grade_input > 1.0:
    print("Out of scope. try again!!!")
if grade_input >= 0.9:
    print("A")
elif grade_input >= 0.8:
    print("B")
elif grade_input >= 0.7:
    print("C")
elif grade_input >= 0.6:
    print("D")
else:
    print("F")

        
