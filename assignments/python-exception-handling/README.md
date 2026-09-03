# 📘 Assignment: Robust Python: Exception Handling & Input Validation

## 🎯 Objective

Learn how to handle errors gracefully in Python using `try`/`except`/`else`/`finally` and custom exception classes so programs don't crash on bad input.

## 📝 Tasks

### 🛠️	Handle Basic Exceptions

#### Description
Using the provided starter code, write a `safe_divide(a, b)` function that divides two numbers and handles the case where the user divides by zero or provides a non-numeric value.

#### Requirements
Completed program should:

- Use a `try`/`except` block to catch `ZeroDivisionError` and `ValueError`
- Print a friendly error message instead of crashing
- Return `None` when the division fails

### 🛠️	Validate User Input in a Loop

#### Description
Write a `get_positive_number()` function that repeatedly asks the user for a number until they enter a valid positive number.

#### Requirements
Completed program should:

- Loop until valid input is received
- Catch `ValueError` when the input isn't a number
- Re-prompt with a clear message when the number is zero or negative
- Return the valid number once entered

### 🛠️	Create a Custom Exception

#### Description
Define a custom exception class named `NegativeAmountError` and use it in a `withdraw(balance, amount)` function that simulates withdrawing money from a bank account.

#### Requirements
Completed program should:

- Define `NegativeAmountError` as a subclass of `Exception`
- Raise `NegativeAmountError` when `amount` is negative
- Raise a custom `InsufficientFundsError` when `amount` is greater than `balance`
- Use `try`/`except`/`else`/`finally` to print whether the withdrawal succeeded, and always print a "transaction complete" message at the end

### 🛠️	Combine Validation Across Functions (Stretch Goal)

#### Description
Build a small "ATM" script that uses all three functions above together in a menu-driven loop, ensuring no invalid input ever crashes the program.

#### Requirements
Completed program should:

- Present a menu to check balance, withdraw, or exit
- Reuse `get_positive_number()` to collect the withdrawal amount
- Catch and handle every custom and built-in exception raised by the other functions
- Keep running until the user chooses to exit, even after invalid input or errors
