'''
    1 : snake
    -1 : water
    0 : gun

'''

import random

computer = random.choice([-1, 1, 0])
youstr = input("Enter your choice : ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a Draw...")

else:
    if(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == 0 and you == 1):
        print("You lose!")
    elif(computer == 0 and you == -1):
        print("You win!")
    else:
        print("Something went wrong")