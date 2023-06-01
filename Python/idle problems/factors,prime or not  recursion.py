def factors_num(n):
    count=0
    print("The factors of",n,"are")
    for i in range(1,n+1):
        if n%i==0:
            print(i)
            count+=1
    if count==2:
        print("The number",n,"is prime")
    else:
        print("The number",n,"is not a prime")
a=eval(input("Enter a numbre: "))
factors_num(a)

