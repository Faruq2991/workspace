smallest = None
print("Before")
for value in [3,2,4,-1,5,34,78,54,100]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)