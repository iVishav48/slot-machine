import random
from collections import Counter  
from colorama import Fore, Style, init
init(autoreset=True)


# Game configuration constants
reels = 3
rows = 3
PARTIAL_MATCH_MULTIPLIER = 0.3
BONUS_PER_LINE_MULTIPLIER = 0.3

symbol_count = {"🍒": 8, "🍋": 8, "🍊": 8, "🍇": 8, "7️⃣": 5, "⭐": 3}
symbol_values = {"🍒": 8, "🍋": 8, "🍊": 8, "🍇": 8, "7️⃣": 15, "⭐": 50}


def get_slot_machine_spin(symbols, reels, rows):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(reels):
        column = []
        current_symbols = all_symbols.copy()
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def check_winnings(columns, bet):
    winnings = 0
    partial_winnings = 0
    full_win_lines = []
    partial_win_lines = []

    num_lines = len(columns[0])
    for line in range(num_lines):
        symbols_in_line = [column[line] for column in columns]
        counts = Counter(symbols_in_line)

        if 3 in counts.values():
            symbol = max(counts, key=counts.get)
            winnings += symbol_values[symbol] * bet
            full_win_lines.append(line + 1)
        elif 2 in counts.values():
            symbol = max(counts, key=counts.get)
            partial_winnings += symbol_values[symbol] * bet * PARTIAL_MATCH_MULTIPLIER
            partial_win_lines.append(line + 1)

    total_winnings = winnings + partial_winnings
    return total_winnings, full_win_lines, partial_win_lines


def print_slot_machine(columns, full_wins=None, partial_wins=None):
    if full_wins is None:
        full_wins = []
    if partial_wins is None:
        partial_wins = []

    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            symbol = column[row]
            end_char = " | " if i != len(columns) - 1 else ""
            color = Fore.RESET

            # Highlight based on line type
            if (row + 1) in full_wins:
                color = Fore.GREEN + Style.BRIGHT  # full win
            elif (row + 1) in partial_wins:
                color = Fore.YELLOW + Style.BRIGHT  # partial win

            print(color + symbol + Style.RESET_ALL, end=end_char)
        print()

