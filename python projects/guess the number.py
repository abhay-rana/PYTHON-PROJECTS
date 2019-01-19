# let suppose the number is 18

#the guess number is greater or lesser than the actual number is tell to the user everytime
#number of guesses by user is 5 (limited)
#print number of guesses left
#number of guesses he took to win
#print game over

N=18 #the actual number
print("you have the total number of chance is 5")
guess=5
while guess>0:
        n = int(input("enter a number \n"))
        if n==N:
            print("you win")
            print("guess=",guess)
            break
        elif n<N:
            print("enter the larger number")
            guess-=1
            print("no.of remaining guess =",guess)
        elif n>N:
            print("enter the smaller number")
            guess-=1
            print("number of remaing guess=",guess)
else:
        print("youn lost \n try again")
