a=input("Enter a string: ")
reverse_string=" "
for i in range(len(a)-1,-1,-1):
    reverse_string+=a[i]
print(reverse_string)
