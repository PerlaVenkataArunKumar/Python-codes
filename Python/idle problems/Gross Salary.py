Basic_Salary=eval(input("Enter the salary"))

if Basic_Salary<=10000:
    HRA = (Basic_Salary * 20)/100
    DA = (Basic_Salary * 80)/100
    Gross_Salary = Basic_Salary+HRA+DA
    print(Gross_Salary)
elif Basic_Salary>10000 and Basic_Salary<=20000:
    HRA = (Basic_Salary * 25)/100
    DA = (Basic_Salary * 90)/100
    Gross_Salary = Basic_Salary+HRA+DA
    print(Gross_Salary)
else:
    HRA = (Basic_Salary * 30)/100
    DA = (Basic_Salary * 95)/100
    Gross_Salary = Basic_Salary+HRA+DA
    print(Gross_Salary)
