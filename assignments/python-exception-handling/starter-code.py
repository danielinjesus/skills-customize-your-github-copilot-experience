# Task 1


def safe_divide(a, b):
    # Divide a by b, handling ZeroDivisionError and ValueError
    # Print a friendly message and return None if it fails
    pass

# Task 2


def get_positive_number():
    # Loop until the user enters a valid positive number
    # Catch ValueError for non-numeric input
    pass

# Task 3


class NegativeAmountError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


def withdraw(balance, amount):
    # Raise NegativeAmountError if amount is negative
    # Raise InsufficientFundsError if amount is greater than balance
    # Use try/except/else/finally to report the outcome
    pass

# Task 4 (stretch)


def atm_menu():
    # Build a menu-driven loop using the functions above
    pass
