def perfect_num(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum
a=eval(input("Enter a number: "))
r=perfect_num(a)

if a==r:
    print(a," is a perfect number")
else:
    print(a," is not a perfect number")
