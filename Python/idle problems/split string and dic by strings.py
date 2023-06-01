a=str(input("Enter a string: "))
b=a.split()
print(b)
d={}
for i in range(0,len(b)):
    d[b[i]]=len(b[i])
print(d)
