a=eval(input("Enter a list: "))
char=eval(input("Enter a character: "))
sum=0
for i in range(len(a)):
    if a[i]==char:
        print(i)
        sum+=1
print("The no.of times", char,"repeated in list is: ",sum)
