from text import deposit, number_of_lines, get_bet, MAX_LINES, MAX_BET, MIN_BET
from game_logic import (
    get_slot_machine_spin,
    print_slot_machine,
    check_winnings,
    symbol_count,
    symbol_values,
    reels,
    rows,
)


"""    """


def spin(balance):
    lines = number_of_lines()  # step2 calling number_of_lines function
    while True:
        bet = get_bet()

        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance} \nYou can bet up to: ${balance // lines} on each line. "
            )
        else:
            break

    total_bet = bet * lines

    print(
        f"You are betting ${bet} on {lines} {'line' if lines == 1 else 'lines'}. Total bet is ${total_bet}"
    )
    # tells you your total bet and how many lines you are betting on, used f string for singular and plural lines

    slots = get_slot_machine_spin(symbol_count, reels, rows)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    print(
        f"You won on lines:", *winning_lines
    )  # unpacks (unpack operator) the winning_lines list to print each line number separately
    return winnings - total_bet  # returns the net gain or loss from the spin


def main():
    balance = deposit()  # step1 calling deposit function
    print(f"You have deposited: ${balance}")
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(
            balance
        )  # updates the balance after each spin by adding the result of the spin function

    print(f"You left with ${balance}")


if (
    __name__ == "__main__"
):  # this is used to run the main function only when the file is run directly, not when it is imported
    main()
