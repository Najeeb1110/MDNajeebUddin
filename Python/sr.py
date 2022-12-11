
sorted = False  # We haven't started sorting yet

while not sorted:
    sorted = True  # Assume the list is now sorted
    for element in range(0, length):
        if badList[element] > badList[element + 1]:
            sorted = False  # We found two elements in the wrong order
            hold = badList[element + 1]
            badList[element + 1] = badList[element]
            badList[element] = hold
    # We went through the whole list. At this point, if there were no elements
    # in the wrong order, sorted is still True. Otherwise, it's false, and the
    # while loop executes again.


for i in range(0, length):

 for i in range(length):


 def bubble(bad_list):


bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]


my_list = [12, 5, 13, 8, 9, 65]

def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]

bubble(my_list)
print  (my_list)


