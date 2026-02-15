p=input("Do you want to play? ")
score=0
if p.lower()!="yes":
    quit()
ques=["CPU Fullform","GPU Fullform","RAM Fullform"]
ans=["central processing unit","graphics processing unit","random access memory"]
for i in range(0,3):
   p= input (f"Whats the {ques[i]}? ")
   if p.lower()== ans[i]:
       score+=1
   else:
      print("The answer is ",ans[i])
   
print("Your final score is: ",score)