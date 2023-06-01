def Tow_Of_Hanoi(n,source,dest,middle):
    if n<1:
        print("please enter positive number to move")
    elif n==1:
        print("Move disk {} from {} to {}".format(n,source,dest))
    else:
        Tow_Of_Hanoi(n-1,source,middle,dest)
        print("Move disk {} from {} to {}".format(n,source,dest))
        Tow_Of_Hanoi(n-1,middle,dest,source)
a=eval(input("Enter number of disks: "))
Tow_Of_Hanoi(a,"A","C","B")
