A=eval(input("Enter the angle 'A'of the triangle:"))
B=eval(input("Enter the angle 'B'of the triangle:"))
C=eval(input("Enter the angle 'C'of the triangle:"))

sum_ofangles=A+B+C 

if((sum_ofangles==180)and(A!=0 and B!=0 and C!=0)and(A<90 and B<90 and C<90)):
    print("The Triangle is VALID,since the sum of the angles is:",sum_ofangles)
    print("It is an Acute angled triangle")
elif((sum_ofangles==180)and(A!=0 and B!=0 and C!=0)and(A==90 or B==90 or C==90)):
    print("The Triangle is VALID,since the sum of the angles is:",sum_ofangles)
    print("It is a Right angled triangle")
elif((sum_ofangles==180)and(A!=0 and B!=0 and C!=0)and(A>90 or B>90 and C>90)):
    print("The Triangle is VALID,since the sum of the angles is:",sum_ofangles)
    print("It is an Obtuse angled triangle")
else:
    print("The Triangle is INVALID,since the sum_ofanglesis:",sum_ofangles)