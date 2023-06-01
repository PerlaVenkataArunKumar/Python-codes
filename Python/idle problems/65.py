class Student:
    def __init__(self,id,name,mid1_marks,mid2_marks,quiz_marks):
        self.id=id
        self.name=name
        self.mid1_marks=mid1_marks
        self.mid2_marks=mid2_marks
        self.quiz_marks=quiz_marks
    def info(self):
        print("ID:",self.id)
        print("name:",self.name)
        print("mid1_marks:", self.mid1_marks)
        print("mid2_marks:", self.mid2_marks)
        print("quiz_marks:", self.quiz_marks)
    def total(self):
        total=self.mid1_marks+self.mid2_marks+self.quiz_marks
        print("TOTAL:",total)
        if(total>=80):
            print("A GRADE")
        elif(total<80 and total>=60):
            print("B GRADE")
        elif(total>=50 and total<60):
            print("C GRADE")
x=Student(11012,"ARUN",10,10,30)
x.info()
x.total()
