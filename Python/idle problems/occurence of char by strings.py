s=str(input("Enter your string: "))
c=str(input("Enter your character: "))
count=0
for i in range(0,len(s)):
    if s[i]==c:
        count=count+1
print(count) 
