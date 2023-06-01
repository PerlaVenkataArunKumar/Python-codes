def odd_sum(n):
    sum=0
    for i in range(2,n):
        if i%2 !=0:
            sum+=i
    return sum
a=eval(input("Enter a number: "))
r=odd_sum(a)
print(r)

