import random

low = 1
high = 99

print("keep a number between 1 to 100 in your mind so I will try to guess it! Tell me if my guess is correct or not.")

while True:
    guess = (low + high) // 2  # Guess the middle number
    print(f"Is the number {guess}?")  

    response = input("Enter 'c' if correct, 'h' if too high, or 'l' if too low: ").lower()

    if response == 'c':
        print(f"Hooooora! I guessed it right. The number is {guess}! ")
        break
    elif response == 'h':
        high = guess - 1  # Narrow down the range (guess a smaller number)
    elif response == 'l':
        low = guess + 1  # Narrow down the range (guess a larger number)
    else:
        print("Please enter only 'c' for correct, 'h' for too high, or 'l' for too low.")

    

