def fibonacci(n):
    first,second=0,1
    for i in range(n):
        if i<1:
            result=i
        else:
            result=first+second
            first=second
            second=result
        print(result)
a=eval(input("Enter a number: "))
fibonacci(a)

