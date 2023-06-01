def fact_num(n):
    if n==1:
        return n
    elif n==0:
        return 1
    else:
        return n*fact_num(n-1)

a=eval(input("Enter a number: "))
b=fact_num(a)
print("Factorial of",a,"is ",b)
