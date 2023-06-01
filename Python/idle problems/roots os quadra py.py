a=eval(input("Enter a: "))
b=eval(input("Enter b: "))
c=eval(input("Enter c: "))

d= b**2 - 4*a*c
m = d**0.5
if d>0:
    print("The roots are real and distnict")
    print("root 1",(-b+m)/(2*a))
    print("root 2",(-b-m)/(2*a))
elif d==0:
    print("The roots are: ",-b/2*a)
    print("The roots are real and equal")
else:
    print("The roots are imaginary")
    
