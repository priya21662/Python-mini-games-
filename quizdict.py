print("Welcome to the quiz game")
'''p=input("Do you want to play? ")
score=0
if p.lower()!="yes":
    quit()
ques=["CPU Fullform","GPU Fullform","RAM Fullform"]
ans=["central processing unit","graphics processing unit","random access memory"]
for i in range(0,3):
   p= input (f"Whats the {ques[i]}? ")
   if p.lower()== ans[i]:
       score+=1
   else: print(p)
   
print("Your final score is: ",score)'''
war=0

dict1={"cpu": "c process","gpu":"g process"}
for q,a in dict1.items():
    s=input(f"{q} full form is? ")
    if s.lower()==a:
        war+=1
print(war)


