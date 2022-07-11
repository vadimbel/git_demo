
class Date:
    def __init__(self, day: int, month: int, year: str):
        """
        Constructor of Class 'Date' .
        :param day: value for 'day' attribute .
        :param month: value for 'month' attribute .
        :param year: value for 'year' attribute .
        """
        # check for invalid values for class attributes according to the assignment
        message = ""
        if not 1 <= day <= 31 or not isinstance(day, int):
            message += "Invalid input for 'day' (valid range is 1-31 of type 'int') \n."
        if not 1 <= month <= 12 or not isinstance(month, int):
            message += "Invalid input for 'month' (valid range is 1-12 of type 'int') \n."
        if not len(year) == 4 or not year.isnumeric():
            message += "Invalid input for 'year' ."

        # one of the values for class attributes were not valid
        if message != "":
            raise Exception(message)

        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """
        Override __str__ .
        :return: the object attributes in this format below .
        """
        message = f"Day - {self.day} .\n" \
                  f"Month - {self.month} .\n" \
                  f"Year - {self.year} .\n"
        return message

    def isValid(self) -> bool:
        """
        This function checks if an object of class 'Date' attributes initialized with a valid date .
        :return: True or False .
        """

        # in april (4) , june (6) , september (9) , november (11) there is no 31 days
        if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
            if self.day == 31:
                print(f"object : {self.day}/{self.month}/{self.year} -> Is not valid -> "
                      f"{self.month}-th month have only 30 days .")
                return False

        elif self.month == 2:
            # leap year has 29 days in february
            if int(self.year) % 4 == 0:
                if self.day > 29:
                    print(f"object : {self.day}/{self.month}/{self.year} -> Is not valid -> "
                          f"in february during a leap year there is only 29 days .")
                    return False
            # regular year has 28 days in february
            else:
                if self.day > 28:
                    print(f"object : {self.day}/{self.month}/{self.year} -> Is not valid -> "
                          f"in february during a regular year there is only 28 days .")
                    return False

        return True

    def getNextDay(self):
        """
        This function returns a new object of class 'Date' with a date of the next day .
        :return:  new object of class 'Date' .
        """
        # check if object attributes are valid
        if not self.isValid():
            print("Invalid Date -> There is no next day .")
            return None

        # in april (4) , june (6) , september (9) , november (11) - there is 30 days
        if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
            # end of the month -> turn to next month
            if self.day == 30:
                day = 1
                month = self.month + 1
                year = self.year
            # turn to next day
            else:
                day = self.day + 1
                month = self.month
                year = self.year

        # february (2)
        elif self.month == 2:
            # in a leap year in february there is 29 days -> if day = 29 -> turn to next month
            if int(self.year) % 4 == 0 and self.day == 29:
                day = 1
                month = self.month + 1
                year = self.year

            # in a regular year in february there is 28 days -> if day = 28 -> turn to next month
            elif not int(self.year) % 4 == 0 and self.day == 28:
                day = 1
                month = self.month + 1
                year = self.year
            # not end of the month -> turn to next day
            else:
                day = self.day + 1
                month = self.month
                year = self.year

        # end of the month on all other month with 31 days
        elif self.day == 31:
            # month = 12 + day = 31 -> turn to next year
            if self.month == 12:
                day = 1
                month = 1
                year = str(int(self.year) + 1)
            # month < 12 + day = 31 -> turn to next month
            else:
                day = 1
                month = self.month + 1
                year = self.year

        # not end of the month/year -> turn to next day
        else:
            day = self.day + 1
            month = self.month
            year = self.year

        new_date = Date(day, month, year)
        return new_date

    def getNextDays(self, days_to_add: int):
        """
        This function using 'getNextDay' function 'days_to_add' times .
        The function will return a new object of class 'Date' with 'days_to_add' days further .

        :param days_to_add:
        :return: new object of class 'Date' .
        """
        # if the object of class 'Date' is not initialized properly -> this function will not be activated
        if not self.isValid():
            print("Invalid Date -> There is no next day .")
            return None

        # using 'getNextDay' , 'days_to_add' times to add 'days_to_add' amount of days to the date
        count = 0
        date = Date(self.day, self.month, self.year)

        # activate 'getNextDay' function 'days_to_add' times to get the required date
        while count < days_to_add:
            date = date.getNextDay()
            count += 1

        return date

    def __eq__(self, other):
        """
        Implementation of __eq__ function .
        checks if the two object of class 'Date' have the same values in their attributes .

        :param other:  other object of class 'Date' .
        :return: True or False
        """
        # 'other' is not 'Date' object
        if not isinstance(other, Date):
            return False

        # program will tell the user if one of the object has invalid date -> return false
        if not self.isValid() or not other.isValid():
            return False

        # same values -> equals .
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return True

        return False

    def __lt__(self, other):
        """
        Implementation of __lt__ function .
        This function check two objects of class 'Date' and returns bool value :
        if 'self' object of class 'Date' is lower than 'other' object of class 'Date' -> True
        and false otherwise .

        :param other: other object of class 'Date' .
        :return: True or False .
        """

        # 'other' is not 'Date' object
        if not isinstance(other, Date):
            return False

        # if one of the object has invalid date -> there is no lower/higher equivalence between them
        if not self.isValid() or not other.isValid():
            return False

        # if 'year' attributes of the two object are not equal , then we will check according to the 'year'
        if int(self.year) != int(other.year):
            return int(self.year) < int(other.year)
        # according to the 'month'
        elif self.month != other.month:
            return self.month < other.month
        # days
        elif self.day != other.day:
            return self.day < other.day
        # all attributes are equal -> no lower object
        else:
            return False

    def __gt__(self, other):
        """
        Implementation of __gt__ function .
        This function check the two objects of class 'Date' and returns bool value :
        if 'self' object of class 'Date' is greater than 'other' object of class 'Date' -> True
        and False otherwise .

        this function will use '__lt__' function and returns the opposite value .

        :param other: other object of class 'Date' .
        :return: True or False .
        """
        if not isinstance(other, Date):
            return False

        if self.day == other.day and self.month == other.month and self.year == other.year:
            return False

        return other < self

    def __le__(self, other):
        """
        Implementation of __le__ function .
        using __eq__ , __lt__ Implementation from above .

        :param other: other 'Date' object .
        :return: True or False .
        """
        # 'other' is not 'Date' object
        if not isinstance(other, Date):
            return False

        if self == other:
            return True

        return self < other

    def __ge__(self, other) -> bool:
        """
        Implementation of __ge__ function .
        using __eq__ , __gt__ Implementation from above .

        :param other: other 'Date' object .
        :return: True or False .
        """
        # 'other' is not 'Date' object
        if not isinstance(other, Date):
            return False

        if self == other:
            return True

        return self > other


    def __sub__(self, other):
        """
        Implementation of __sub__ function .
        This function calculates the days off every object , then returns the difference of days
        between the two objects .

        :param other: other object of class 'Date' .
        :return: difference of days .
        """

        # check if the 'other' is of class 'Date'
        if not isinstance(other, Date):
            return -1

        # at least one of the objects has Invalid date
        if not self.isValid() or not other.isValid():
            return -1

        # variables to count amount of days for each object
        self_days = self.day
        other_days = other.day

        # activate functions below
        self_days += calculate_years(self.year)
        self_days += calculate_months(self.month, self.year)
        other_days += calculate_years(other.year)
        other_days += calculate_months(other.month, other.year)

        return abs(self_days - other_days)


def calculate_years(years: str) -> int:
    """
    This function will be activated inside '__sub__' override in class 'Date' .
    the function will calculate total days in 'year' attribute of class 'Date' .

    :param years: attribute of class 'Date' .
    :return: total days in 'year' attribute of class 'Date' .
    """
    count = 1
    total_days = 0

    # count all days in years except the last one
    while count < int(years):
        if count % 4 == 0:          # leap year has 366 days
            total_days += 366
        else:
            total_days += 365       # regular year has 365 days

        count += 1

    return total_days


def calculate_months(months: int, year: str) -> int:
    """
    This function will be activated inside '__sub__' override in class 'Date' .
    the function will calculate total days in 'month' attribute of class 'Date' .

    :param months: attribute of class 'Date' .
    :param year: attribute of class 'Date' .
    :return: total days in 'month' attribute of class 'Date' .
    """
    count = 1
    total_days = 0

    # count all days in months except the last one
    while count < months:
        if count == 4 or count == 6 or count == 9 or count == 11:       # 30 days a month
            total_days += 30
        elif count == 2:
            if int(year) % 4 == 0:      # leap year -> 29 days on february
                total_days += 29
            else:
                total_days += 28        # regular year -> 28 days om february
        else:
            total_days += 31

        count += 1

    return total_days
