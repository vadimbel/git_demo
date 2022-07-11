
def add_to_dict(data_set: dict, key_id: int, name: str, sex: str, age: int, *values) -> None:
    """
    This function will add a new 'element' to 'data_set' dict .
    if extra - fields are entered , then user will input what they represent .
    'element' - is a dict itself , contains :

    :param data_set: The dict that we add new elements to .
    :param key_id: id of the new element .
    :param name: Name of the new element .
    :param sex: Gender of the new element .
    :param age: Age of the new element .
    :param values: Extra-fields of the new element .
    :return: None .
    """

    # if the id entered by the user already exists , then update his elements .
    if key_id in data_set.keys():
        print(f"Update id : {key_id} .\n")

    # update 'data_set' with id + 3 must be params .
    data_set.update({key_id: {"Name": name, "Sex": sex, "Age": age}})

    if len(values) > 0:
        print(f"ID - {key_id} has extra - fields .")

    # loop on the optional extra-fields , and add them to the new value .
    for ind, val in enumerate(values):
        extra_field = input(f"Please enter what is the {ind+1} extra-field represents :")
        data_set[key_id][extra_field] = val


def split_male_female(data_set: dict) -> tuple:
    """
    This function will split the 'data_set' to 2 different dictionaries by their gender .
    :param data_set: main 'data_set' .
    :return: a tuple contains 2 dictionaries .
    """

    male_dict = {}
    female_dict = {}

    # according to the assay - 'sex' param is valid (male or female) .
    for key, values in data_set.items():
        if values["Sex"] == "male":             # if male , add it to male dict .
            male_dict.update({key: values})
        else:                                   # else add it to female dict .
            female_dict.update({key: values})

    return male_dict, female_dict


def find_median_average(data_set: dict) -> tuple:
    """
    This function will calculate the medial and the average age of the elements in 'data_set' .
    :param data_set: main 'data_set' .
    :return: a tuple contains - average age , median age - in a tuple .
    """
    age_avg = 0
    age_lst = []

    # sum the ages and add them to a list .
    for values in data_set.values():
        age_avg += values["Age"]
        age_lst.append(values["Age"])

    # calculate the avg .
    age_avg /= len(data_set)

    # sort the list with the ages , then take the median .
    age_lst.sort()
    median_age = age_lst[len(data_set)//2]

    return round(age_avg, 4), median_age


def print_values_above(data_set: dict, age: int = 0) -> None:
    """
    This function will print all the elements with a greater 'Age' then 'age' .
    If 'age' is not entered by the user , then all the elements will be printed .
    :param data_set: main 'data_set' .
    :param age: user input .
    :return: None .
    """
    for key, values in data_set.items():
        if values["Age"] > age:
            print(f"Id number : {key} - ")
            for inside_key, value in values.items():
                print(f"{inside_key} - {value}")
            print()


def print_elements(data_tuple: tuple) -> None:
    """
    This function created to print the 2 dictionaries after 'split_male_female' activated .
    :param data_tuple: tuple contains the 2 dictionaries .
    :return: None .
    """
    for item in data_tuple:
        print_values_above(item)


def main():
    data_set = {}

    # add values to the 'data_set' manually using 'add_to_dict' function .
    # according to the assay - input in valid .
    add_to_dict(data_set, 123456789, "vadim", "male", 28, 1.89, "bel")
    add_to_dict(data_set, 123333, "vad", "male", 11)
    add_to_dict(data_set, 55455555, "vanda", "female", 34)
    add_to_dict(data_set, 545345211, "artiom", "male", 29, 1.92, "tall man")
    add_to_dict(data_set, 292929, "liora", "female", 30)
    add_to_dict(data_set, 22321, "dana", "female", 27)
    add_to_dict(data_set, 112312, "adi", "male", 40)

    # using 'split_male_female' function , then print the two dictionaries .
    print("-"*50)
    split_data_set = split_male_female(data_set)
    print_elements(split_data_set)
    print("-" * 50)

    # using 'find_median_average' function and print the values .
    print("-" * 50)
    print(find_median_average(data_set))
    print("-" * 50)

    # using 'print_values_above' function .
    print("-" * 50)
    print_values_above(data_set, 27)
    print("-" * 50)

# comment for tamir (or the one who check the assignment) -
# if user update existing key (id) -> then the function 'find_median_average' will calculate the values will the
# updated 'age' fields .

main()
