import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
        if difficulty == "easy":
            max_attempts = 10
        elif difficulty == "medium":
            max_attempts = 7
        elif difficulty == "hard":
            max_attempts = 5
        else:
            print("Invalid choice. Please select easy, medium, or hard.")
            continue

        secret_number = random.randint(1, 100)
        attempts = 0
        
        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess (between 1 and 100): "))
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
                
                attempts += 1
                
                if guess < secret_number:
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print(f"Game Over! The correct number was {secret_number}.")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    number_guessing_game()
