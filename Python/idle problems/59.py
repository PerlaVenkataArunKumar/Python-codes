str1=input("Enter a string: ")
str2=str1.lower()
a1=["a","e","i","o","u"]
v_cout=0
s_cout=0
for i in str2:
    if i in a1:
        v_cout+=1
print("The no.of vowels in string are: ",v_cout)
a2=str1.split()
print("The no.of spaces in given string are: ",len(a2)-1)
g=""
for i in a2:
    if len(i)>=len(g):
        g=i
print("The longest word in string is: ",g)
