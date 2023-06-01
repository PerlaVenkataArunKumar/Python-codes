a=eval(input("Enter a number: "))
sum=0
b=a
power=len(str(a))
while b!=0:
    digit=b%10
    sum+=digit**power
    b//=10
if a==sum:
    print(a,"is an Armstrong number")
else:
    print(a,"is not an Armstrong number")
