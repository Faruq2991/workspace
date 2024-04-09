floor_number = input("Enter a floor number: ")
location = input("Enter your location: ").lower()
if location == "europe":
    floor_number = floor_number
    print("Your should be in the: " + int(floor_number + " floor."))
elif location == "usa":
    floor_number = floor_number +1
    print("Your should be in the: " + int(floor_number + " floor."))
else:
    print("Wrong location")