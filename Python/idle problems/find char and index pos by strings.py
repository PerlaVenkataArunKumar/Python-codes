s=str(input("Enter your string: "))
c=str(input("Enter your character: "))
index=-1
for i in range(0,len(s)):
    if s[i]==c:
        index=i
        break
print(index)

