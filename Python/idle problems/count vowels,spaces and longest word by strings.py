def cout_vowels(a):
    v_cout=0
    s_cout=0
    for i in range(0,len(a)):
        if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U':
            v_cout+=1
        if a[i]==" ":
            s_cout+=1
    print("The no.of vowels are: ",v_cout)
    print("The no.of spaces are: ",s_cout)
a=str(input("Enter a string: "))
cout_vowels(a)
b=a.split()
m=0
for i in range(0,len(b)):
    if len(b[i])>m:
        ans=b[i]
        m=len(b[i])
print(ans)
