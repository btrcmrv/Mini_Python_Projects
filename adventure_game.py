name=input("What is your name? ")
print("Welcome", name, "to this adventure! The game starts...")

question1=input('''You come to a dirty road.
It has come to an end and you can go either to the left or to the right. 
Which way would you like to go? ''').lower()

if question1=="left":
   q2=input('''You come to a river, you can walk around it or swim accross?
            Type walk or swim: ''')
   if q2=="swim":
       print("You swam acrross and were eaten by an alligator.")
   elif q2=="walk":
       print("You walked for many kms, ran out of water and you lost the game.")
   else:
       print('Not a valid option. You lose.')
elif question1=="right":
    q3=input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    if q3=="back":
        print("You go back and lose.")
    elif q3=="cross":
        q4= input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        if q4=="yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif q4=="no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')         
    else: 
        print('Not a valid option. You lose.')   
else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)
