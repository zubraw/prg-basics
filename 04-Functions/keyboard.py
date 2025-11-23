# keyboard.py

def input_string(prompt):
    return input(prompt)

def input_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer!")

def input_real(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def input_boolean(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        print("Please enter 'y' or 'n'")