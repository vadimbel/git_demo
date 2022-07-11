
def print_colour(pass_fail: int, message: str) -> None:
    """
    This function created to print a message to the user with the right colour .
    if 'pass_fail' = 1 -> then the test failed -> print message in red colour .
    if 'pass_fail' = 0 -> then the test succeeded -> print message in green colour .

    :param pass_fail: Integer represents test failure/success .
    :param message: the message that will be printed to the user .
    :return: None .
    """
    import colorama
    colorama.init()

    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    RESET = '\u001b[0m'

    if pass_fail == 0:
        print(GREEN, message, RESET)
    elif pass_fail == 1:
        print(RED, message, RESET)


def check_password(password: str) -> int:
    """
    This function created to check the password entered by the user .
    The function will return :
        PASS = 0 -> if the Test succeeded .
        FAIL = 1 -> if the Test failed .

    :param password: password entered by the user .
    :return: PASS/FAIL .
    """
    LENGTH = 10         # password must contain at least 10 characters
    PASS = 0
    FAIL = 1

    # boolean variables to check if password sustain all conditions
    valid_length = False
    capital_letter = False
    small_letter = False
    integer = False

    # check password length
    if len(password) >= LENGTH:
        valid_length = True

    # check if password sustain all other conditions
    for ch in password:
        if ch.isnumeric():
            integer = True
        elif 'A' <= ch <= 'Z':
            capital_letter = True
        elif 'a' <= ch <= 'z':
            small_letter = True

    # if the password sustain all conditions -> then it passed the test -> print message in green colour
    if valid_length and capital_letter and small_letter and integer:
        message = f"TEST CASE : '{password}'    -    TEST PASSED ."
        print_colour(PASS, message)
        return PASS

    # password did not pass the test -> print the right messages to the user in red colour
    else:
        if not valid_length:
            message = f"TEST CASE : '{password}'    -    Password must contain at least {LENGTH} characters     -" \
                      f"    TEST FAILED ."
            print_colour(FAIL, message)
        if not capital_letter:
            message = f"TEST CASE : '{password}'    -    Password must contain at least one capital letter" \
                       f"    -    TEST FAILED ."
            print_colour(FAIL, message)
        if not small_letter:
            message = f"TEST CASE : '{password}'    -    Password must contain at least one small letter" \
                       f"    -    TEST FAILED ."
            print_colour(FAIL, message)
        if not integer:
            message = f"TEST CASE : '{password}'    -    Password must contain at least one Integer" \
                       f"    -    TEST FAILED ."
            print_colour(FAIL, message)

    return FAIL


def passwords_to_check(passwords: list) -> None:
    """
    This function will get a list of passwords to check .
    Every password will be checked using 'check_password' function .

    :param passwords: List of passwords .
    :return: None .
    """
    for password in passwords:
        exit_code = check_password(password)
        if exit_code == 0:
            print_colour(exit_code, f"EXIT CODE - {exit_code} - TEST PASS .\n")
        elif exit_code == 1:
            print_colour(exit_code, f"EXIT CODE - {exit_code} - TEST FAIL .\n")








