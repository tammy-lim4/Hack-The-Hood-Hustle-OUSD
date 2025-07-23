# Guessing Game Tammy, Alvert, Liz, Anthony
import random

def generate_random_number():
    '''Generates a random number between 1 through 100'''
    random_number = random.randint(1,100)
    return random_number

def get_user_guess():
    '''Asks for the users input, checks if it is a valid number (1-100)'''
    while True:
        user_input = input("Please enter a number between 1-100: ")
        try:
            if 1 <= int(user_input) <= 100:
                return user_input
        except:
            print("This is not a valid number!")

def play_guessing_game():
    '''Logs the # of attempts, checks if the user's input is the correct answer'''
    secret_number = generate_random_number()
    Attempts = 0
    while True:
        guess = int(get_user_guess())
        if guess > secret_number:
            print('Your guess is too high!')
            Attempts += 1
            print(f'Attempts {Attempts}')
        elif guess < secret_number:
            print('Your guess is too low!')
            Attempts += 1
            print(f'Attempts {Attempts}')
        else:
            print(f'You win! You guessed the number in {Attempts} attempts!')
            break

def game_loop():
    '''Starts the game loop, allows the user to continue or exit after winning'''
    while True:
        play_guessing_game()

        play_again = input('Would you like to play again? yes/no: ').lower()
        if play_again == 'no':
            print('Quitting now')
            break

if __name__ == "__main__": 
    game_loop()