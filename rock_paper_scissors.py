import random

#create the scores for the user and computer
user_score=0
computer_score=0

#create a list of options 
options=["rock","paper","scissors"]

#ask the user what to pick
while True:
    user_pick= input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    if user_pick=="q":
        break
    if user_pick not in options:
        continue
      
    ## Assign the rock paper and scissors to random pick so #rock:0, paper:1, scissors:2
    random_number= random.randint(0,2)
    computer_pick=options[random_number]
    print(f'Computer picked {computer_pick}.')
    
    if user_pick=="rock" and computer_pick=="scissors":
        print("You won! ")
        user_score+=1
    elif user_pick=="scissors" and computer_pick=="paper":
        print("You won!")
        user_score+=1
    elif user_pick=="paper" and computer_pick=="rock":
        print("You won!")
        user_score+=1
    elif user_pick==computer_pick:
        print("Withdraw! ")
        user_score
    else:
        print("Computer won!")
        computer_score+=1
    
print(f"You won {user_score} time(s).")
print(f"Computer won {computer_score} time(s).")
    
