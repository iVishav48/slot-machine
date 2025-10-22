def print_slot_machine(columns, full_wins=None, partial_wins=None):
    if full_wins is None:
        full_wins = []
    if partial_wins is None:
        partial_wins = []

    for row in range(len(columns[0])):
        row_color = Fore.RESET
        if (row + 1) in full_wins:
            row_color = Fore.GREEN + Style.BRIGHT  # full win row
        elif (row + 1) in partial_wins:
            row_color = Fore.YELLOW + Style.BRIGHT  # partial win row

        for i, column in enumerate(columns):
            end_char = " | " if i != len(columns) - 1 else ""
            print(row_color + column[row] + Style.RESET_ALL, end=end_char)
        print()
