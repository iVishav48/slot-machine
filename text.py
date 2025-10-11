MAX_LINES = 3
MAX_BET = 500
MIN_BET = 10


"""step1: deposit function, keep asking until a valid amount is entered with while loop"""


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number. \n")

    return amount


"""step2: asking about number of lines function on which the user wants to bet on (1-3)"""


def number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" +
            str(MAX_LINES) + ")? \n"
        )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.\n")
        else:
            print("Please enter a number. \n")

    return lines


"""step3: bet function, keep asking until a valid bet is entered with while loop between min and max bet(f string used)"""


def get_bet():
    while True:
        amount = input("What would you like to bet on each line?\n $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.\n")
        else:
            print("Please enter a number. \n")

    return amount
