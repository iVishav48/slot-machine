# Game configuration constants for betting limits
MAX_LINES = 3    # Maximum number of lines a player can bet on
MAX_BET = 500    # Maximum bet amount per line
MIN_BET = 10     # Minimum bet amount per line


def deposit():
    """
    Get initial deposit amount from player with input validation.
    Keeps asking until a valid positive integer is entered.
    
    Returns:
        int: Valid deposit amount entered by player
    """
    # Keep asking for input until valid amount is provided
    while True:
        # Prompt player for deposit amount
        amount = input("What would you like to deposit? $")
        
        # Check if input contains only digits
        if amount.isdigit():
            # Convert string to integer
            amount = int(amount)
            
            # Check if amount is positive
            if amount > 0:
                # Valid amount entered, exit the loop
                break
            else:
                # Amount is zero or negative, show error message
                print("Amount must be greater than 0.")
        else:
            # Input contains non-digit characters, show error message
            print("Please enter a number. \n")

    # Return the valid deposit amount
    return amount


def number_of_lines():
    """
    Get number of lines player wants to bet on with input validation.
    Keeps asking until a valid number between 1 and MAX_LINES is entered.
    
    Returns:
        int: Valid number of lines (1-3) entered by player
    """
    # Keep asking for input until valid number of lines is provided
    while True:
        # Prompt player for number of lines to bet on
        lines = input(
            "Enter the number of lines to bet on (1-" +
            str(MAX_LINES) + ")? \n"
        )
        
        # Check if input contains only digits
        if lines.isdigit():
            # Convert string to integer
            lines = int(lines)
            
            # Check if lines is within valid range
            if 1 <= lines <= MAX_LINES:
                # Valid number of lines entered, exit the loop
                break
            else:
                # Lines is outside valid range, show error message
                print(f"Please enter a number between 1 and {MAX_LINES}.\n")
        else:
            # Input contains non-digit characters, show error message
            print("Please enter a number. \n")

    # Return the valid number of lines
    return lines


def get_bet():
    """
    Get bet amount per line from player with input validation.
    Keeps asking until a valid amount between MIN_BET and MAX_BET is entered.
    
    Returns:
        int: Valid bet amount per line entered by player
    """
    # Keep asking for input until valid bet amount is provided
    while True:
        # Prompt player for bet amount per line
        amount = input("What would you like to bet on each line?\n $")
        
        # Check if input contains only digits
        if amount.isdigit():
            # Convert string to integer
            amount = int(amount)
            
            # Check if amount is within valid betting range
            if MIN_BET <= amount <= MAX_BET:
                # Valid bet amount entered, exit the loop
                break
            else:
                # Amount is outside valid range, show error message with f-string
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.\n")
        else:
            # Input contains non-digit characters, show error message
            print("Please enter a number. \n")

    # Return the valid bet amount per line
    return amount
