a=input("Enter the file name: ")
b=open(a,"r")
data=b.read()
char=input("Enter a character: ")
char_cout=0
for i in data:
    if i==char:
        char_cout+=1
print("The character {} is appeared {} times in the file".format(char,char_cout))
