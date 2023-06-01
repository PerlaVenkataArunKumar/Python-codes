x=eval(input("Enter a number: "))
y=eval(input("Enter a number: "))
if x>y:
    small=y
else:
    small=x
for i in range(1,small+1):
    if x%i==0 and y%i==0:
        hcf=i
print("hcf of",x,"and",y,"is: ",hcf)
