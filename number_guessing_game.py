import random

def get_difficulty():
    print("Select difficulty level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == '1':
            return 1, 50
        elif choice == '2':
            return 1, 100
        elif choice == '3':
            return 1, 200
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        low, high = get_difficulty()
        print(f"I'm thinking of a number between {low} and {high}.")
        number_to_guess = random.randint(low, high)
        guess_count = 0
        
        while True:
            try:
                guess = int(input(f"Enter your guess ({low}-{high}): "))
                guess_count += 1
                if guess < low or guess > high:
                    print(f"Please enter a number between {low} and {high}.")
                    continue
                if guess < number_to_guess:
                    print("Too low. Try again.")
                elif guess > number_to_guess:
                    print("Too high. Try again.")
                else:
                    print(f"Congratulations! You guessed the number {number_to_guess} in {guess_count} attempts.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        play_again = input("Would you like to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    number_guessing_game() 