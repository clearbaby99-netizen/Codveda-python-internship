"""
Codveda Internship — Level 1, Task 2: Number Guessing Game
Author: Clemence
Description: Randomly generates a number between 1–100. The user
             guesses it with feedback per attempt. Exits on a correct
             guess or after MAX_ATTEMPTS tries.
"""

import random

def guessing_game():
    print("--- Number Guessing Game ---")
    print("I have chosen a number between 1 and 100.")
    
    # Generate the random number
    secret_number = random.randint(1, 100)
    attempts = 7  # Maximum number of attempts allowed
    
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}/{attempts}. Enter your guess: "))
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {attempt} attempts!")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
            
    else:
        # This executes only if the loop finishes without a 'break'
        print(f"Game Over! You've run out of attempts. The number was {secret_number}.")

# Run the game
guessing_game()
