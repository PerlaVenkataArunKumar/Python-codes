a=input("Enter the file name: ")
b=open(a,"r")
data=b.read().replace(" ","")
d={}
for char in data:
    if char in d:
        d[char]+=1

    else:
        d[char]=1
print(d)
