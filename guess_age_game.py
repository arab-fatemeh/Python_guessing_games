import random

my_age = 26

print("Guess my age! (a number between 1 and 99)")
answer = int(input("Your guess: "))
tries = 1

while answer != my_age:
    if answer > my_age:
        print("noch noch noch... I am younger!")
    else:
        print("NA NA NA... I am older!")
    answer = int(input("Try again: "))
    tries += 1

print(f"wooow!!! you won in {tries} tries, You rock")



 