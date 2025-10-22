# Import user input functions from text module
from text import deposit, number_of_lines, get_bet, MAX_LINES, MAX_BET, MIN_BET

# Import colorama for colored terminal output
from colorama import Fore, Style, init
init(autoreset=True, convert=True)  # Initialize colorama with Windows compatibility and auto-reset

# Import Counter for counting symbol occurrences in winning lines
from collections import Counter
# Import choice for random symbol selection (though not used in main.py)
from random import choice

# Import game logic functions and constants from game_logic module
from game_logic import (
    get_slot_machine_spin,      # Function to generate random slot machine spin
    check_winnings,             # Function to calculate winnings based on symbol matches
    symbol_count,               # Dictionary containing count of each symbol in the pool
    symbol_values,              # Dictionary containing point values for each symbol
    reels,                      # Number of reels (columns) in the slot machine
    rows,                       # Number of rows in the slot machine
    PARTIAL_MATCH_MULTIPLIER,   # Multiplier for partial wins (2 matching symbols)
    BONUS_PER_LINE_MULTIPLIER,  # Multiplier for bonus per line (currently unused)
)

# Import display functions from display module
from display import (
    spin_animation,             # Function to display spinning animation
    print_slot_machine,         # Function to display slot machine with color highlighting
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
    
    # Check if player has enough balance for minimum bet on chosen number of lines
    min_required_balance = MIN_BET * lines
    if balance < min_required_balance:
        # Player doesn't have enough balance for minimum bet on chosen lines
        print(f"\n{Fore.RED}Insufficient balance for {lines} line{'s' if lines > 1 else ''}!")
        print(f"You need at least ${min_required_balance} to bet on {lines} line{'s' if lines > 1 else ''}.")
        print(f"Your current balance is ${balance}.{Fore.RESET}")
        
        # Ask player what they want to do
        while True:
            print(f"\nWhat would you like to do?")
            print(f"1. Reduce number of lines (minimum: 1 line)")
            print(f"2. Add more money to your balance")
            print(f"3. Cancel this spin")
            
            choice = input("Enter your choice (1/2/3): ").strip()
            
            if choice == "1":
                # Option 1: Reduce number of lines
                if lines > 1:
                    # Calculate maximum lines player can afford
                    max_affordable_lines = balance // MIN_BET
                    if max_affordable_lines > 0:
                        print(f"\nYou can afford up to {max_affordable_lines} line{'s' if max_affordable_lines > 1 else ''} with your current balance.")
                        while True:
                            try:
                                new_lines = int(input(f"Enter number of lines (1-{max_affordable_lines}): "))
                                if 1 <= new_lines <= max_affordable_lines:
                                    lines = new_lines
                                    print(f"{Fore.GREEN}Changed to {lines} line{'s' if lines > 1 else ''}.{Fore.RESET}")
                                    break
                                else:
                                    print(f"{Fore.RED}Please enter a number between 1 and {max_affordable_lines}.{Fore.RESET}")
                            except ValueError:
                                print(f"{Fore.RED}Please enter a valid number.{Fore.RESET}")
                    else:
                        print(f"{Fore.RED}You don't have enough balance for even 1 line. Please add more money.{Fore.RESET}")
                        choice = "2"  # Force to add money option
                        continue
                else:
                    print(f"{Fore.RED}You're already at the minimum of 1 line. Please add more money.{Fore.RESET}")
                    choice = "2"  # Force to add money option
                    continue
                break
                
            elif choice == "2":
                # Option 2: Add more money
                additional_deposit = deposit()
                balance += additional_deposit
                print(f"{Fore.GREEN}Added ${additional_deposit} to your balance.")
                print(f"New balance: ${balance}{Fore.RESET}")
                break
                
            elif choice == "3":
                # Option 3: Cancel this spin
                print(f"{Fore.YELLOW}Spin cancelled. Returning to main menu.{Fore.RESET}")
                return 0  # Return 0 winnings/losses for cancelled spin
                
            else:
                # Invalid choice
                print(f"{Fore.RED}Please enter 1, 2, or 3.{Fore.RESET}")
    
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
        f"You are betting ${bet} on {lines} {'line' if lines == 1 else 'lines'}. \nTotal bet is ${total_bet}"
    )
    
    # Show spinning animation before revealing the result
    spin_animation(symbol_count, reels, rows, duration=1.5)
    
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
        
        # Check if player has sufficient balance to make minimum bet
        if balance < MIN_BET:
            # Player doesn't have enough money for minimum bet
            print(f"\n{Fore.RED}Insufficient balance! You need at least ${MIN_BET} to play.")
            print(f"Your current balance is ${balance}.{Fore.RESET}")
            
            # Ask if player wants to add more money
            while True:
                add_money = input(f"\nWould you like to add more money? (y/n): ").lower().strip()
                
                if add_money == "y" or add_money == "yes":
                    # Get additional deposit from player
                    additional_deposit = deposit()
                    balance += additional_deposit
                    print(f"{Fore.GREEN}Added ${additional_deposit} to your balance.")
                    print(f"New balance: ${balance}{Fore.RESET}")
                    break
                elif add_money == "n" or add_money == "no":
                    # Player chooses not to add money, exit the game
                    print(f"{Fore.YELLOW}Thanks for playing! You left with ${balance}.{Fore.RESET}")
                    return
                else:
                    # Invalid input, ask again
                    print(f"{Fore.RED}Please enter 'y' for yes or 'n' for no.{Fore.RESET}")
        
        # Get player input for next action
        answer = input("Press enter to play (q to quit).")
        
        # Check if player wants to quit
        if answer == "q":
            # Exit the game loop
            break
        
        # Execute one spin and update balance with the result
        spin_result = spin(balance)
        balance += spin_result
    
    # Display final balance when player exits
    print(f"You left with ${balance}")


# Entry point - only run main() when this file is executed directly
if __name__ == "__main__":
    main()
