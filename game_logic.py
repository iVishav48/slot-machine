# Import random module for generating random symbol selections
import random
# Import Counter for counting occurrences of symbols in each line
from collections import Counter  
# Import colorama for colored terminal output
from colorama import Fore, Style, init
# Initialize colorama with Windows compatibility and auto-reset
init(autoreset=True, convert=True)


# Game configuration constants
reels = 3  # Number of reels (columns) in the slot machine
rows = 3   # Number of rows in the slot machine
PARTIAL_MATCH_MULTIPLIER = 0.1  # Multiplier for partial wins (2 matching symbols)
BONUS_PER_LINE_MULTIPLIER = 0.3  # Multiplier for bonus per line (currently unused)

# Dictionary defining how many of each symbol are available in the symbol pool
# Higher counts = more common symbols, lower counts = rarer symbols
symbol_count = {"🍒": 10, "🍋": 10, "🍊": 10, "🍇": 10, "🍓": 10, "🍑": 10, "7️⃣": 5, "⭐": 3}

# Dictionary defining point values for each symbol when winning
# Higher values = more valuable symbols (rarer symbols are worth more)
symbol_values = {"🍒": 8, "🍋": 8, "🍊": 8, "🍇": 8, "🍓": 8, "🍑": 8, "7️⃣": 15, "⭐": 50}


def get_slot_machine_spin(symbols, reels, rows):
    """
    Generate a random slot machine spin without replacement.
    Each reel gets unique symbols (no duplicates within a column).
    
    Args:
        symbols (dict): Dictionary mapping symbols to their counts
        reels (int): Number of reels (columns) in the slot machine
        rows (int): Number of rows in the slot machine
        
    Returns:
        list: List of columns, where each column is a list of symbols
    """
    # Create a list containing all available symbols based on their counts
    all_symbols = []
    # Iterate through each symbol and its count
    for symbol, count in symbols.items():
        # Add the symbol to the list 'count' number of times
        all_symbols.extend([symbol] * count)

    # Initialize list to store all columns (reels)
    columns = []
    
    # Generate each reel (column) one by one
    for _ in range(reels):
        # Create a new column for this reel
        column = []
        # Create a copy of all symbols for this reel (to avoid duplicates within a column)
        current_symbols = all_symbols.copy()
        
        # Fill this column with the required number of rows
        for _ in range(rows):
            # Randomly select a symbol from available symbols
            value = random.choice(current_symbols)
            # Remove the selected symbol to prevent duplicates in this column
            current_symbols.remove(value)
            # Add the selected symbol to this column
            column.append(value)
        
        # Add the completed column to the list of columns
        columns.append(column)
    
    # Return the complete slot machine spin
    return columns


def check_winnings(columns, bet):
    """
    Calculate winnings based on symbol matches in each line.
    
    Args:
        columns (list): List of columns representing the slot machine spin
        bet (int): Bet amount per line
        
    Returns:
        tuple: (total_winnings, full_win_lines, partial_win_lines)
            - total_winnings: Total amount won
            - full_win_lines: List of line numbers with 3 matching symbols
            - partial_win_lines: List of line numbers with 2 matching symbols
    """
    # Initialize variables to track different types of winnings
    winnings = 0          # Winnings from full matches (3 symbols)
    partial_winnings = 0  # Winnings from partial matches (2 symbols)
    full_win_lines = []   # Lines with full wins
    partial_win_lines = [] # Lines with partial wins

    # Get the number of lines (rows) to check
    num_lines = len(columns[0])
    
    # Check each line for winning combinations
    for line in range(num_lines):
        # Extract symbols from this line (one symbol from each column)
        symbols_in_line = [column[line] for column in columns]
        
        # Count occurrences of each symbol in this line
        counts = Counter(symbols_in_line)

        # Check for full win (3 matching symbols)
        if 3 in counts.values():
            # Find which symbol has 3 occurrences
            symbol = max(counts, key=counts.get)
            # Calculate winnings: symbol_value × bet_amount
            winnings += symbol_values[symbol] * bet
            # Record this line as a full win (convert to 1-based indexing)
            full_win_lines.append(line + 1)
        
        # Check for partial win (2 matching symbols) - only if no full win
        elif 2 in counts.values():
            # Find which symbol has 2 occurrences
            symbol = max(counts, key=counts.get)
            # Calculate partial winnings: symbol_value × bet_amount × partial_multiplier
            partial_winnings += symbol_values[symbol] * bet * PARTIAL_MATCH_MULTIPLIER
            # Record this line as a partial win (convert to 1-based indexing)
            partial_win_lines.append(line + 1)

    # Calculate total winnings from both full and partial wins
    total_winnings = winnings + partial_winnings
    
    # Return all win information
    return total_winnings, full_win_lines, partial_win_lines



