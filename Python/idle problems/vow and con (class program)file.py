a=input("Enter the file name: ")
b=open(a,"r")
data=b.read().replace(" ","").lower()
v_cout=0
c_cout=0
l=['a','e','i','o','u']
for ch in data:
    if ch in l:
        v_cout+=1
    else:
        c_cout+=1
print("The no.of vowels in the file are: ",v_cout)
print("The no.of consonants in the file are: ",c_cout)
b.close()
