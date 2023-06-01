a=open("arun.txt","r")
b=open("a.txt","a")
data=a.read()
c=data
print("Data in file 1: ",data)
print("Data copied to file 2: ",c)
a.close()
b.close()
