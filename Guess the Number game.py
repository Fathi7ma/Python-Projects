import random
lower_bound = 1
upper_bound = 1000
max_attempts = 10
secret_number=random.randint(lower_bound,upper_bound)
def get_guess():
    while True:
        try:
            guess=int(input(f"Guess the number between {lower_bound} and {upper_bound}:"))
            if lower_bound<=guess<=upper_bound:
                return guess
            else:
                print("Invalid number.Enter a number between lower bound and upper bound")
        except ValueError:
            print("Invalid number,Please enter a valid number")
for attempt in range(max_attempts):
    user_guess=get_guess()
    if user_guess==secret_number:
        print(f"Congratulations!You guessed the secret number{secret_number}")
    elif user_guess<secret_number:
        print("Too low! Guess a higher number")
    elif user_guess>secret_number:
        print("Too high! Guess a lower number")
    else:
        print(f"Out of attempt. The secret number is{secret_number}.Better luck next time")
        