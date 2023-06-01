def cout_digits(n):
    if n>0:
        d=n//10
        count=1+cout_digits(d)
    else:
        return 0
    return count
a=eval(input("Enter a number: "))
b=cout_digits(a)
print("The number of digits in",a,"are",b)
