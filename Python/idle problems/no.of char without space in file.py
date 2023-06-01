a=input("Enter the file name: ")
b=open(a,"r")
data=b.read()
char_cout=0
for char in data:
    if char!=" ":
        char_cout+=1
print("The number of characters in the file are: ",char_cout)
