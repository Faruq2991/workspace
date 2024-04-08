# This program compares two numbers and determines the bigger of the two and prints it out.

largest_so_far = 1
for number in [1,3,5,45,64,8,9,75]:
    if number > largest_so_far:
        largest_so_far = number
    print(largest_so_far, number)
print("After", largest_so_far)