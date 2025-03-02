import random

print("Welcome to the game! \n You got 5 attemps to guess the number between 50 to 100, Lets start the game!")

number_to_guess = random.randrange(50, 100)

chances: int = 5

guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Guess a number: "))
    
    if my_guess == number_to_guess:
        print(f"The number is (number_to_guess) and you found it right! in the (guess_counter) attempt")
        break
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"Sorry, you've run out of chances. The correct number was (number_to_guess)")
        
    elif my_guess < number_to_guess:
            print("Your guess is too low, try again!")

    elif my_guess > number_to_guess:
            print("Your guess is too high, try again!")