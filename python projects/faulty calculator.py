# #there is a faulty calculator which gives the
# # wrong results of some specific calculations
# #wrong calculations for --> 45*3=555, 56+9=77, 56/6=4
# # do this only by if and else methods
a=int(input("enter a numbers"))
b=int(input("enter a number"))
opt=input("enter a operator")
if  opt=="*" and a==45 and b==3 :
    print(555)
elif opt=="+" and a==56 and b==9 :
    print(77)
elif opt=="/" and a==56 and b==6 :
    print(4)
elif opt=="*":
    print(a*b)
elif opt=="+":
    print(a+b)
elif opt=="/":
    print(a/b)
