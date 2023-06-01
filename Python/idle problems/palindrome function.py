def palin(n):
    rev=0
    while n!=0:
        d=n%10
        rev=rev*10+d
        n//=10
    return rev

a=eval(input("Enter a number: "))
r=palin(a)


if a==r:
        print(a," is palindrome")
else:
        print(a," is not palindrome")

