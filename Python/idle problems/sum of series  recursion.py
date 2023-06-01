def sum_series(n):
    if n==1:
        return 1
    else:
        return n**5+sum_series(n-1)
a=eval(input("Enter a number: "))
if a>=1:
    print("Sum of Series is: ",sum_series(a))
else:
    print("Please enter a positive number")
    
