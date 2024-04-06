

def binary_search(list, element):

    start = 0
    middle = 0
    ending = len(list) - 1
    steps = 1


    while start <= ending:
        print("Steps", steps, ":", str(list[start:ending + 1]))

        steps = steps + 1
        middle = (start + ending) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            ending = middle -1
        else: 
            start = middle + 1
    return -1

my_list = [1,2,3,4,5,6,7,8,9]
target = 6
binary_search(my_list, target)