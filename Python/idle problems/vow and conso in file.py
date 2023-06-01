a=input("Enter the file name: ")
b=open(a,"r")
data=b.read()
v_cout=0
c_cout=0
vowels = ['a','e','i','o','u','A','E','i','O','U']
for char in data:
    if char in vowels:
        v_cout+=1
        
    elif char!=" ":
        c_cout+=1
print("The no.of vowels in file are: ",v_cout)
print("The no.of consonants in file are: ",c_cout)
b.close()
        
