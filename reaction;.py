import tkinter as tk  # tkinter for GUI
import random  # generating random delays and colors for the game
import time  # measuring reaction time for each click and calculate average later


def start_game():
    """
    Initializes the game by resetting round count and reaction times.
    Starts the first flash sequence.
    """
    global current_round, reaction_times # variables defined outside of a function (at the script level) are considered global variables.
    current_round = 0  # round count to 0
    reaction_times = []  # List for reaction times
    next_flash()  # Start


def next_flash():
    """
    Schedules the next color flash after a random delay.
    Ends the game if all rounds are completed.
    """
    global current_round
    if current_round >= rounds:  # Check if all rounds are completed
        end_game()
        return
    current_round += 1  # next round
    delay = random.uniform(0.5, 2)  # random delay between 0.5 - 2 seconds
    root.after(int(delay * 1000), flash)  # Wait for the delay, then call flash(); root.after is a tkinter method that delays the execution of a function by a specified number of milliseconds.


def flash():
    """
    Changes the canvas background to a random color and records the start time.
    """
    global current_color, start_time
    current_color = random.choice(list(colors.keys()))  #random color key ('r', 'g', etc.)
    canvas.configure(bg=colors[current_color])  # Change canvas background to the chosen color
    start_time = time.time()  # Record the start time for reaction


def check_reaction(event):
    """
    Checks if the user's keypress matches the current color.
    If correct, records reaction time, resets the background, and proceeds to the next round.

    Parameters:
    event (tkinter.Event): The keypress event captured by tkinter.
    """
    if event.char == current_color:  # Check if the pressed key matches the current color ; event.char is tkinter event object (event) that captures the character associated with a keypress.
        reaction_time = time.time() - start_time  # Calc reaction time
        reaction_times.append(reaction_time)  # Add reaction time to the list
        canvas.configure(bg='white')  # Reset background color
        next_flash()  # next round


def end_game():
    """
    Calculates and displays the average reaction time at the end of the game.
    Unbinds keypress events to stop further input.
    """
    avg_time = sum(reaction_times) / len(reaction_times) if reaction_times else 0  # Calculate average
    canvas.create_text(200, 200, text=f"Avg Reaction Time: {avg_time:.3f} sec", font=("Arial", 16))  # Show result with specific font & size
    root.unbind("<KeyPress>")  # Stop detecting keypresses once game is done ; from tkinter


def get_rounds():
    """
    Asks the user to input the number of rounds and ensures valid integer input.
    Returns:
    int: The number of rounds entered by the user.
    """
    while True:
        try:
            return int(input("Enter the number of rounds (Recommended: 10-30): "))  # number of rounds as integer
        except ValueError:  # handle the error
            print("Try typing an integer number.")  # Ask for correction


# Display instructions for the game
print(
    "Welcome to the Reaction Time Game!\nA color will appear on the screen, and you must press the corresponding key ('r' for red, 'g' for green, etc.) as quickly as possible.\nLet's see how fast your reactions are!")

rounds = get_rounds()  # Get number of rounds from player

# Set up the main game window
root = tk.Tk()
root.title("Reaction Time Game")
canvas = tk.Canvas(root, width=400, height=400)  # Create a canvas where colors will be displayed
canvas.pack()

# Define the colors and their corresponding keys
colors = {'r': 'red', 'g': 'green', 'b': 'blue', 'y': 'yellow', 'o': 'orange'}

# Initialize game variables
current_color = None  # Stores the current color key
start_time = None  # Stores the time when the color appears
reaction_times = []  # List for reaction times
current_round = 0  # Tracks current round

root.bind("<KeyPress>", check_reaction)  # Check keypress events
start_game()  # Start game
root.mainloop()  # Keep GUI window open