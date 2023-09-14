##GENERATE a random NUMBER from 0 up to 10
# AND track how many times it takes the user to guess this number

#import random module
import random

#create a random number from 0 up to 10
random_number=random.randrange(0,11)

#Tell the user to guess a number
guessed_number=int(input("Guess a number between 0-10: "))
if guessed_number<0 or guessed_number>10:
        print("Please guess a number larger than 0 or smaller than 10.")

# count of how many attempts the user will guess correctly
guesses=0

#create the game!
while guessed_number!=random_number:
    guesses+=1  
    guess=int(input("Guess a number: "))  
    if guess<0 or guess>10:
        print("Please guess a number larger than 0 or smaller than 10.")
    elif guess==random_number:
        print("Congrats, you got it!")
        break
    elif guess> random_number:
        print("Your guess is higher than the random number!")
    elif guess< random_number:
        print("Your guess is smaller than the random number!")
          
print(f"You found the number in {guesses+1} attemps.") 
