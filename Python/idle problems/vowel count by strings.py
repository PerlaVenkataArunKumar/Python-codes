s=input("Enter any string: ")
s1=s.lower()


count=0
for i in s1:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count+=1

print(count)
