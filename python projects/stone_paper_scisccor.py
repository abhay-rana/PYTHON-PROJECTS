import random
print("today we play stone paper scissor with the computer")
while True:
    x=int(input("enter \n1-->stone\n2--->paper\n3-->scissor\n"))
    if x==1:
        print("user input--->stone")
        x="stone"
    elif x==2:
        print("user input --->paper")
        x="paper"
    elif x==3:
        print("user input--->scissor")
        x="scissor"
    y=random.choice(("stone","paper","scissor"))
    print("computer output--->",y)
    if x=="scissor" and y=="stone":
        print("computer wins")
    elif x=="stone" and y=="paper":
        print("computer wins")
    elif x=="paper" and y=="scissor":
        print("computer wins")
    elif x=="scissor" and y=="paper":
        print("user wins")
    elif x=="stone" and y=="scissor":
        print("user wins")
    elif x=="paper" and y=="stone":
        print("user wins")
    elif x=="scissor" and y=="paper":
        print("user wins")
    else:
        print("draw")



