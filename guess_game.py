import random
answer = random.randint(1,99)

guess = input('guess a number betweem 0 and 100 and tell me what is your guess?')
guess = int (guess)
while guess != answer:
    if guess>answer:
        print ('mine is smaller')
    else:
        print('mine is larger')
    guess = input('what is your guess?')
    guess = int(guess)

print('woooow!!!you did it!you rock!')

