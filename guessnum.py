import random
p=random.randint(1,30)
print(p)
s=int(input("Guess the number from 1 to 30: "))

'''print("You have 5 chances to guess number")
i=0
for i in range(0,5):
    s=int(input("Guess the number from 1 to 30: "))
    if s==p:
        print("That's correct")
    elif s>p:
         print("your guess is hot")
    else:
        print("your guess is cold")'''
while (s!=p):
    print("you guessed it wrong try again")
print("l")
    

    

