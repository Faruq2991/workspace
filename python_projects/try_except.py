
ferh = float(input("Enter a Fahrenheite Value: "))

try:
    cel = (ferh - 32.0)*5.0 / 9.0
    print(cel)
except:
    print("Enter a number: ")