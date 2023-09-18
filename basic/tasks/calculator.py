# Calculator

while True:
    first_value = input('Enter a value: ').strip()
    second_value = input('Enter another value: ').strip()
    operator = input('Enter a operator (+-/*): ').strip()
    valid_numbers = None

    # Makes an assessment if the entered numbers are valid so as not to break the program
    try:
        first_value = float(first_value)
        second_value = float(second_value)
        valid_numbers = True
        valid_operators = '+-/*'

    # The values ​​being invalid, it goes back to None
    except Exception as error:
        valid_numbers = False
        print(error)

    # If they are valid it continues the program for the operations, if it is invalid or None it goes back to try to evaluate the new numbers
    if valid_numbers is None:
        print('One or both numbers entered are invalid.')
        continue

    # Check if the operator is in the allowed operators
    if operator not in valid_operators:
        print('Invalid operator.')
        continue

    # Check if more than one operator was entered
    if len(operator) > 1:
        print('Enter only one operator.')
        continue

    # Calculator Operators
    if operator == '+':
        print(first_value + second_value)

    elif operator == '-':
        print(first_value - second_value)

    elif operator == '*':
        print(first_value * second_value)

    elif operator == '/':
        print(first_value / second_value)

    # Check if you want to stop the program
    exit = input('Wanna go out? [y]yep: ').lower().startswith('y')

    if exit is True:
        break