math=eval(input("enter the marks secured by the canditate in math:"))
science=eval(input("enter the marks secured by the canditate in science:"))
english=eval(input("enter the marks secured by the canditate in english:"))
history=eval(input("enter the marks secured by the canditate in history:"))
economics=eval(input("enter the marks secured by the canditate in economics:"))
hindi=eval(input("enter the marks secured by the canditate in hindi:"))
result=(math+science+english+history+economics+hindi)/6
print("The percentage secured by a canditate is:",result)
if result>90:
    print("Grade A")
elif result>=80 and result<90:
    print("Grade B")
elif result>=70 and result<80:
    print("Grade C")
elif result>=60 and result<70:
    print("Grade D")
elif result>=50 and result<60:
    print("Grade E")
elif result<50:
    print("Grade F")