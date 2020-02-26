# A simple integer-guessing game in Python

import sys
from random import randint

# Takes two integer arguments after filename in command
sys.argv

start = int(sys.argv[1])
end = int(sys.argv[2])
count = 0

while True:
    count += 1
    random_int = randint(start, end)

    try:
        guess = int(input(f"Guess a number from {str(start)} and {str(end)}: "))

        # checks if number is within range
        if start <= guess <= end:

            # checks if number is guessed correctly
            if guess == random_int:
                print(f"Congratulations! You've guessed the number after {count} attempts")
                break

            else:
                print(f"Sorry, the random number was {random_int}. Try again")

        else:
            print("Guess a number in range")
    
    except ValueError:
        print("Only numbers allowed")
