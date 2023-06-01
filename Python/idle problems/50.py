d1={'a':10,'b':20,'c':30}
d2={'a':30,'b':20,'d':40}
for i in d1:
    if i in d2:
        d1[i]=d1[i]+d2[i]
for i in d2:
    if i not in d1:
        d1[i]=d2[i]
print(d1)
