## QUIZ GAME!
# Ask the user many questions, and give how many questions she/he got correct and give the percentage.

#Welcome the user.
print("Welcome to my Statistics Quiz Game!")

# Ask the user whether they want to play a game.
playing=input("Would you like to play a Statistics quiz game? ")
if playing.lower() == "yes":
    print("Okay! Let's start! ")
else:  
    print("Goodbye")
    quit()

#Creating quiz questions and scores
score=0
number_of_questions=0

answer=input("What does ANOVA stand for? ")
number_of_questions+=1
if answer.lower()== "analysis of variance" :
    print("Correct!")
    score=score+1
else:
    print("Wrong! ")

answer=input("What does CI stand for? ")
number_of_questions+=1
if answer.lower()== "confidence interval" :
    print("Correct!")
    score+=1
else:
    print("Wrong! ")
    
answer=input("What does MSE stand for? ")
number_of_questions+=1
if answer.lower()== "mean square error" :
    print("Correct!")
    score+=1
else:
    print("Wrong! ")

answer=input("What does SS stand for? ")
number_of_questions+=1
if answer.lower()== "sum of squares" :
    print("Correct!")
    score+=1
else:
    print("Wrong! ")

# Tell how many questions the user got correct.
print(f"You got {score} question(s) correct!")

# Tell how much % the user got correct.
print(f"You got {(score/number_of_questions)*100} percent correct!")


