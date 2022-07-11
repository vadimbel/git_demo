def exercise_one_a_b():
    # exercise 1.a part
    my_dict = {}
    reverse_dict = {}  # for 1.b part
    user_input = input("Please enter user input :")

    for ch in user_input:
        if ch in my_dict:
            my_dict[ch] += 1
        else:
            my_dict[ch] = 1

    print("\nExercise 1.a :")
    for key, amount in sorted(my_dict.items()):
        print(f"{key} - {amount}")

    # exercise 1.b part
    for key, amount in (my_dict.items()):
        if amount not in reverse_dict:          # if it is a new key
            reverse_dict[amount] = []           # then create a list for it
        reverse_dict[amount].append(key)        # add element to the list (anyway - new/old)

    print("\nExercise 1.b :")
    print(reverse_dict)


def exercise_two_a_b():
    lst1 = [11, 7, 5, 8, 5, 37, 11, 5, 14]
    lst2 = [22, 8, 10, 1, 11, 2]
    lst3 = [71, 3, 22, 8, 2, 14]

    # exercise 1.a part
    print("Exercise 1.a part :")

    # check if lst1 have duplicate values
    prev = None
    lst1_bool = False           # lst1 has no duplicate elements
    for i in sorted(lst1):
        if i == prev:
            lst1_bool = True    # there is a duplicate element
            break
        prev = i

    if lst1_bool:
        print("lst1 has duplicate elements !")

    # check if lst2 have duplicate elements
    prev = None
    lst2_bool = False           # lst1 has no duplicate elements
    for i in sorted(lst2):
        if i == prev:
            lst2_bool = True    # there is a duplicate element
            break
        prev = i

    if lst2_bool:
        print("lst2 has duplicate elements !")

    # check if lst3 have duplicate elements .
    prev = None
    lst3_bool = False           # lst1 has no duplicate elements
    for i in sorted(lst3):
        if i == prev:
            lst3_bool = True    # there is a duplicate element
            break
        prev = i

    if lst3_bool:
        print("lst3 has duplicate elements !")

    # Exercise 1.b part : the values I search -> from the lists that did not (!!) found on 1.a -> according the massage
    # was sent in the class group .
    print("\nExercise 2.b part :")

    # all 3 lists have duplicate elements -> nothing will be printed (return)
    if lst1_bool and lst2_bool and lst3_bool:
        return

    # lst1 have duplicate elements -> his elements not relevant
    if lst1_bool:
        my_set1 = set(lst2).union(set(lst3))
    # lst1 dont have duplicate elements -> his elements are relevant
    else:
        my_set1 = set(lst1)

    # same comments as above for lst2
    if lst2_bool:
        my_set2 = set(lst1).union(set(lst3))
    else:
        my_set2 = set(lst2)

    # same comments as above for lst3
    if lst3_bool:
        my_set3 = set(lst1).union(set(lst2))
    else:
        my_set3 = set(lst3)

    for val in my_set1.intersection(my_set2, my_set3):
        print(val, end=' ')


def exercise_three():
    lst = [31, 99, 3, 1943]
    my_set = set()
    s = ""

    # add every number to a string
    for number in lst:
        s += str(number)

    # add every digit to the set
    for ch in s:
        my_set.add(int(ch))

    # user choose the order
    user_input = input("Please choose one of the options :\n"
                       "1. asc .\n"
                       "2. desc .")

    # invalid input
    while user_input != "1" and user_input != "2":
        print("You entered invalid input .")
        user_input = input("Please choose one of the options :\n"
                           "1. asc .\n"
                           "2. desc .")

    if user_input == "1":
        my_set = sorted(my_set)
    else:
        my_set = sorted(my_set, reverse=True)

    for i in my_set:
        print(i, end=' ')


exercise_one_a_b()
exercise_two_a_b()
exercise_three()

