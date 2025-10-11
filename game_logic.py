import random
from collections import Counter  

# Game configuration constants
reels = 3
rows = 3

# Win multipliers as constants (avoiding magic numbers)
PARTIAL_MATCH_MULTIPLIER = 0.3  # 30% of full value for partial wins
BONUS_PER_LINE_MULTIPLIER = 0.3  # 30% bonus per extra winning line

# dictionary of symbols and their values
symbol_count = {"🍒": 8, "🍋": 8, "🍊": 8, "🍇": 8, "7️⃣": 5, "⭐": 3}  # symbol and their count

symbol_values = {"🍒": 8, "🍋": 8, "🍊": 8, "🍇": 8, "7️⃣": 15, "⭐": 50}  # symbol and their values


"""logic for slot machine spin"""


def get_slot_machine_spin(symbols, reels, row):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(
                symbol
            )  # creates a list of all symbols based on their count

    columns = []  # defined columns as an empty list to store the symbols for each reel
    for _ in range(rows):  # iterates over the number of reels to create each column
        column = []
        current_symbols = all_symbols.copy()  # makes a copy to avoid modifying the original list
        for _ in range(reels):
            value = random.choice(
                current_symbols
            )  # randomly selects a symbol from the current symbols
            current_symbols.remove(
                value
            )  # removes the selected symbol to avoid duplicates in the same column
            # adds the selected symbol to the current column
            column.append(value)

        columns.append(column)

    return columns  # returns the list of columns, each containing the symbols for that reel


"""transposing the slot machine columns to rows for easier display(vertical to horizontal)
printing the slot machine"""


def print_slot_machine(columns):
    for row in range(
        len(columns[0])
    ):  # iterates over each row index based on the number of rows in the first column
        for i, column in enumerate(
            columns
        ):  # iterates over each column and its index using enumerate
            if (
                i != len(columns) - 1
            ):  # checks if the current column is not the last one
                print(
                    column[row], end=" | "
                )  # prints the symbol at the current row of the column followed by a separator " | ", by default end is a newline, but here it's set to " | "
            else:
                print(
                    column[row], end=""
                )  # prints the symbol at the current row of the last column without a separator
        print()  # moves to the next line after printing all columns for the current row


"""checking winnings"""


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    partial_winnings = 0

    for line in range(lines):  # iterates over each line the user has bet on
        symbols_in_line = [column[line] for column in columns]  # get all symbols in the line

        # Check for horizontal matches only (across reels)
        if symbols_in_line[0] == symbols_in_line[1] == symbols_in_line[2]:  # All 3 symbols match horizontally
            symbol = symbols_in_line[0]
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
        elif symbols_in_line[0] == symbols_in_line[1] or symbols_in_line[1] == symbols_in_line[2] or symbols_in_line[0] == symbols_in_line[2]:  # 2 symbols match horizontally
            # Find which symbol appears twice
            symbol_counts = Counter(symbols_in_line)
            for symbol, count in symbol_counts.items():
                if count >= 2:
                    partial_winnings += values[symbol] * bet * PARTIAL_MATCH_MULTIPLIER  # Use constant for partial wins
                    winning_lines.append(line + 1)  # Add the line to winning lines for partial wins too
                    break

    # Bonus multiplier for multiple winning lines
    if len(winning_lines) > 1:
        bonus_multiplier = 1 + (len(winning_lines) - 1) * BONUS_PER_LINE_MULTIPLIER  # Use constant for bonus
        winnings *= bonus_multiplier

    total_winnings = winnings + partial_winnings
    return total_winnings, winning_lines  # returns total winnings and list of winning lines
