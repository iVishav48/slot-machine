import random 

reels = 3
rows = 3

#dictionary of symbols and their values
symbol_count = {
    "A": 1,
    "B": 1,
    "C": 1,
    "D": 1
} # symbol and their count

symbol_values = {
    "A": 5,
    "B": 5,
    "C": 5,
    "D": 5
} # symbol and their values




"""logic for slot machine spin"""
def get_slot_machine_spin(symbols, reels, row ):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol) # creates a list of all symbols based on their count


    columns = [ ]#defined columns as an empty list to store the symbols for each reel
    for _ in range (rows):# iterates over the number of reels to create each column
        column = [ ]
        current_symbols = all_symbols[:] # makes a copy(with slice operator [:]) of all_symbols to avoid modifying the original list, so that any change we make to current_symbols does not affect all_symbols
        for _ in range(reels):
            value = random.choice(current_symbols) # randomly selects a symbol from the current symbols
            current_symbols.remove(value) # removes the selected symbol to avoid duplicates in the same column
            column.append(value)#adds the selected symbol to the current column

        columns.append(column)

    return columns # returns the list of columns, each containing the symbols for that reel




"""transposing the slot machine columns to rows for easier display(vertical to horizontal)
printing the slot machine""" 
def print_slot_machine(columns):
    for row in range(len(columns[0])): # iterates over each row index based on the number of rows in the first column
        for i, column in enumerate(columns): # iterates over each column and its index using enumerate
            if i != len(columns) - 1: # checks if the current column is not the last one
                print(column[row], end=" | ") # prints the symbol at the current row of the column followed by a separator " | ", by default end is a newline, but here it's set to " | "
            else:
                print(column[row], end="") # prints the symbol at the current row of the last column without a separator
        print() # moves to the next line after printing all columns for the current row





"""checking winnings"""
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): # iterates over each line the user has bet on
        symbol = columns[0][line] # gets the symbol in the first column of the current line
        for column in columns: # iterates over each column to check if the symbols match
            symbol_to_check = column[line] # gets the symbol in the current column of the current line
            if symbol != symbol_to_check: # if any symbol does not match, break out of the loop
                break
        else: # this else corresponds to the for loop, it executes if the loop was not broken, meaning all symbols matched
            winnings += values[symbol] * bet # calculates winnings based on the symbol's value and the bet amount
            winning_lines.append(line + 1) # adds the winning line (1-indexed) to the list of winning lines

    return winnings, winning_lines # returns total winnings and list of winning lines



"""
if __name__ == "__main__":
    slots = get_slot_machine_spin(symbol_count, reels, rows)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, 3, 20, symbols_count)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines) #unpacks the winning_lines list to print each line number separately

"""