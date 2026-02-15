import random
print("Welcome to hand cricket game!")
toss=input("First let's do a toss ,choose odd or even:")
play=int(input("Choose a number from 1 to 10: "))
sys=random.randint(1,10)
result_sys="ball"# System set to ball by default , changes if player wins toss
result_play=""
print(f"System chooses {sys} ")
if (sys+play)%2==0:
    if toss.lower()=="even":
        print("You win")
        result_play=input("Choose between bat and ball: ")
        
    else:
        print("You lost")
        print("System chooses ball")
        
else:
    if toss.lower()=="odd":
        print("You win")
        result_play=input("Choose between bat and ball: ")
        
    else:
        print("You lost")
        print("System chooses ball")
run=0
for i in range(1,6):
    play=int(input("Choose a number from 1  to 10 :"))
    sys=random.randint(1,10)
    if play==sys:
        print("Game ended")
        print(f"The final runs are{run}")
        break
    else:
        print(f"System chooses{sys}")
        if result_play!="" and result_play=="bat":
            run+=play
        else:
            run+=sys
print(run)
while True:
    try:
        play = int(input("Choose a number from 1 to 10: "))
        if 1 <= play <= 10:
            break
        else:
            print("Enter number between 1 and 10.")
    except:
        print("Invalid input.")


