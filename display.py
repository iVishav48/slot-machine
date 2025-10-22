import time  # For implementing delays in animation
import random  # For random emoji selection during animation
import os  # For screen clearing functionality

from colorama import Fore, Style, init  # For colored terminal output
init(autoreset=True, convert=True)  # Initialize Colorama with Windows compatibility


def clear_screen():
    """
    Clear the console screen for animation purposes.
    Works on both Windows and Unix-like systems.
    """
    # Clear screen command for Windows
    os.system('cls' if os.name == 'nt' else 'clear')


def spin_animation(symbols, reels, rows, duration=1.5):
    """
    Display a spinning animation for the slot machine.
    
    Args:
        symbols (dict): Dictionary mapping symbols to their counts
        reels (int): Number of reels (columns) in the slot machine
        rows (int): Number of rows in the slot machine
        duration (float): Duration of animation in seconds
    """
    # Create a list of all available symbols for animation
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)
    
    # Calculate number of animation frames based on duration
    frames_per_second = 10  # 10 frames per second for smooth animation
    total_frames = int(duration * frames_per_second)
    
    print(f"{Fore.CYAN}🎰 SPINNING... 🎰{Fore.RESET}")
    print()
    
    # Animation loop
    for frame in range(total_frames):
        # Clear the screen for each frame
        clear_screen()
        
        # Print spinning header
        print(f"{Fore.CYAN}🎰 SPINNING... 🎰{Fore.RESET}")
        print()
        
        # Generate random symbols for this frame
        animation_columns = []
        for _ in range(reels):
            column = []
            for _ in range(rows):
                # Select random symbol for animation
                symbol = random.choice(all_symbols)
                column.append(symbol)
            animation_columns.append(column)
        
        # Display the spinning symbols
        for row in range(rows):
            for i, column in enumerate(animation_columns):
                symbol = column[row]
                end_char = " | " if i != len(animation_columns) - 1 else ""
                # Use different colors for spinning effect
                color = random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])
                print(color + symbol + Style.RESET_ALL, end=end_char)
            print()
        
        # Add some spinning text effect
        spinner_chars = ["|", "/", "-", "\\"]
        spinner = spinner_chars[frame % len(spinner_chars)]
        print(f"\n{Fore.YELLOW}{spinner} Spinning... {spinner}{Fore.RESET}")
        
        # Delay between frames (faster at the end for dramatic effect)
        if frame < total_frames * 0.7:
            time.sleep(0.1)  # Normal speed
        else:
            time.sleep(0.15)  # Slower near the end for suspense
    
    # Final clear before showing result
    clear_screen()


def print_slot_machine(columns, full_wins=None, partial_wins=None):
    """
    Display the slot machine with color highlighting for winning lines.
    
    Args:
        columns (list): List of columns representing the slot machine spin
        full_wins (list, optional): List of line numbers with full wins
        partial_wins (list, optional): List of line numbers with partial wins
    """
    # Set default empty lists if no win information provided
    if full_wins is None:
        full_wins = []
    if partial_wins is None:
        partial_wins = []

    # Display each row of the slot machine
    for row in range(len(columns[0])):
        # Display each column in this row
        for i, column in enumerate(columns):
            # Get the symbol at this position
            symbol = column[row]
            
            # Determine separator character (pipe for all except last column)
            end_char = " | " if i != len(columns) - 1 else ""
            
            # Set default color (no highlighting)
            color = Fore.RESET

            # Apply color highlighting based on win type
            if (row + 1) in full_wins:
                # Green and bright for full wins (3 matching symbols)
                color = Fore.GREEN + Style.BRIGHT
            elif (row + 1) in partial_wins:
                # Yellow and bright for partial wins (2 matching symbols)
                color = Fore.YELLOW + Style.BRIGHT

            # Print the symbol with appropriate color and separator
            print(color + symbol + Style.RESET_ALL, end=end_char)
        
        # Move to next line after completing a row
        print()
