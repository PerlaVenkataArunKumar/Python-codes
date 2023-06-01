def power(n,p):
    if p==0:
        return 1
    else:
        return n*power(n,p-1)

a=eval(input("Enter a number: "))
b=eval(input("Enter a number: "))
c=power(a,b)
print(c)
