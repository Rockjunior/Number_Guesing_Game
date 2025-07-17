import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class NumberGuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.difficulty_settings = {
            'Easy': (1, 50),
            'Medium': (1, 100),
            'Hard': (1, 200)
        }
        self.setup_difficulty_selection()

    def setup_difficulty_selection(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Select Difficulty Level:", font=("Arial", 14)).pack(pady=10)
        for level in self.difficulty_settings:
            tk.Button(self.root, text=level, width=15, font=("Arial", 12),
                      command=lambda l=level: self.start_game(l)).pack(pady=5)

    def start_game(self, difficulty):
        self.low, self.high = self.difficulty_settings[difficulty]
        self.number_to_guess = random.randint(self.low, self.high)
        self.guess_count = 0
        self.difficulty = difficulty
        self.setup_game_ui()

    def setup_game_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text=f"I'm thinking of a number between {self.low} and {self.high}.", font=("Arial", 12)).pack(pady=10)
        self.guess_entry = tk.Entry(self.root, font=("Arial", 12))
        self.guess_entry.pack(pady=5)
        self.guess_entry.bind('<Return>', lambda event: self.check_guess())
        tk.Button(self.root, text="Submit Guess", command=self.check_guess, font=("Arial", 12)).pack(pady=5)
        self.hint_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.hint_label.pack(pady=5)
        self.guess_count_label = tk.Label(self.root, text="Guesses: 0", font=("Arial", 12))
        self.guess_count_label.pack(pady=5)
        tk.Button(self.root, text="Change Difficulty", command=self.setup_difficulty_selection, font=("Arial", 10)).pack(pady=10)

    def check_guess(self):
        guess = self.guess_entry.get()
        try:
            guess = int(guess)
            if guess < self.low or guess > self.high:
                self.hint_label.config(text=f"Enter a number between {self.low} and {self.high}.")
                return
        except ValueError:
            self.hint_label.config(text="Invalid input. Enter a valid integer.")
            return
        self.guess_count += 1
        self.guess_count_label.config(text=f"Guesses: {self.guess_count}")
        if guess < self.number_to_guess:
            self.hint_label.config(text="Too low. Try again.")
        elif guess > self.number_to_guess:
            self.hint_label.config(text="Too high. Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number {self.number_to_guess} in {self.guess_count} attempts.")
            self.ask_replay()

    def ask_replay(self):
        if messagebox.askyesno("Play Again?", "Would you like to play again?"):
            self.setup_difficulty_selection()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGameGUI(root)
    root.mainloop() 