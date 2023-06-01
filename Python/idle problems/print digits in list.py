n=eval(input("Enter a number: "))
digit=0
while n!=0:
    d=n%10
    n//=10
    digit+=n
print((digit))
    
