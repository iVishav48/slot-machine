# Import user input functions from text module
from text import deposit, number_of_lines, get_bet, MAX_LINES, MAX_BET, MIN_BET

# Import colorama for colored terminal output
from colorama import Fore, Style, init
init(autoreset=True)  # Initialize colorama to automatically reset colors after each print

# Import Counter for counting symbol occurrences in winning lines
from collections import Counter
# Import choice for random symbol selection (though not used in main.py)
from random import choice

# Import game logic functions and constants from game_logic module
from game_logic import (
    get_slot_machine_spin,      # Function to generate random slot machine spin
    print_slot_machine,         # Function to display slot machine with color highlighting
    check_winnings,             # Function to calculate winnings based on symbol matches
    symbol_count,               # Dictionary containing count of each symbol in the pool
    symbol_values,              # Dictionary containing point values for each symbol
    reels,                      # Number of reels (columns) in the slot machine
    rows,                       # Number of rows in the slot machine
    PARTIAL_MATCH_MULTIPLIER,   # Multiplier for partial wins (2 matching symbols)
    BONUS_PER_LINE_MULTIPLIER,  # Multiplier for bonus per line (currently unused)
)


def spin(balance):
    """
    Execute one complete slot machine spin.
    
    Args:
        balance (int): Current player balance
        
    Returns:
        int: Net gain or loss from this spin (winnings - total_bet)
    """
    # Get number of lines player wants to bet on (1-3)
    lines = number_of_lines()
    
    # Keep asking for bet amount until player has sufficient balance
    while True:
        # Get bet amount per line from player
        bet = get_bet()
        
        # Calculate total bet amount (bet per line × number of lines)
        total_bet = bet * lines
        
        # Check if player has enough balance for this bet
        if total_bet > balance:
            # Display error message with current balance and maximum bet per line
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance} \nYou can bet up to: ${balance // lines} on each line. "
            )
        else:
            # Player has sufficient balance, exit the validation loop
            break
    
    # Recalculate total bet (redundant but ensures consistency)
    total_bet = bet * lines
    
    # Display betting information to player
    print(
        f"You are betting ${bet} on {lines} {'line' if lines == 1 else 'lines'}. Total bet is ${total_bet}"
    )
    
    # Generate random slot machine spin using symbol pool, reels, and rows
    slots = get_slot_machine_spin(symbol_count, reels, rows)
    
    # Calculate winnings and identify winning lines
    winnings, full_win_lines, partial_win_lines = check_winnings(slots, bet)
    
    # Display slot machine with color highlighting for winning lines
    print_slot_machine(slots, full_win_lines, partial_win_lines)
    
    # Display total winnings amount
    print(f"You won ${winnings}.")
    
    # Display detailed win information if there are any wins
    if full_win_lines or partial_win_lines:
        # Display full wins (3 matching symbols) if any exist
        if full_win_lines:
            print(f"Full wins on lines: {full_win_lines}")
        # Display partial wins (2 matching symbols) if any exist
        if partial_win_lines:
            print(f"Partial wins on lines: {partial_win_lines}")
    else:
        # No wins this round
        print("No wins this round.")
    
    # Return net result (winnings - total bet) to update player balance
    return winnings - total_bet


def main():
    """
    Main game loop that manages the overall slot machine game flow.
    Handles initial deposit, game rounds, and final balance display.
    """
    # Get initial deposit from player
    balance = deposit()
    print(f"You have deposited: ${balance}")
    
    # Main game loop - continues until player quits
    while True:
        # Display current balance to player
        print(f"Current balance is ${balance}")
        
        # Get player input for next action
        answer = input("Press enter to play (q to quit).")
        
        # Check if player wants to quit
        if answer == "q":
            # Exit the game loop
            break
        
        # Execute one spin and update balance with the result
        balance += spin(balance)
    
    # Display final balance when player exits
    print(f"You left with ${balance}")


# Entry point - only run main() when this file is executed directly
if __name__ == "__main__":
    main()
