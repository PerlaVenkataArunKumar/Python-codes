def lsearch(l1,key):
    for i in range(len(l1)):
        if key==l1[i]:
            print("Key element is found at index: ",i)
            break
    else:
        print("Element is not found")
l1=eval(input("Enter a list: "))
key=eval(input("Enter the key element: "))
lsearch(l1,key)
