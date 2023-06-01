
# Online IDE - Code Editor, Compiler, Interpreter

x1=eval(input("Enter a number for x1:"))
y1=eval(input("Enter a number for y1:"))
x2=eval(input("Enter a number for x2:"))
y2=eval(input("Enter a number for y2:"))

distance=(((x2-x1)**2+(y2-y1)**2)**0.5)
if x1==x2 and y1==y2:
    print("The distance between the 2 coordinate points",(x1,y1),"and",(x2,y2),"is Zero(0)")

else:
    print("The distance between the 2 coordinate points",(x1,y1),"and",(x2,y2),"is",distance)
