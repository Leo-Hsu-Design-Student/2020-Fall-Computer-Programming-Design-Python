age=int(input("PLease Enter Your Age"))
citizen=int(input("PLease Enter Your Citizenship"))

if age>=25 and age<30:
    A=True
    B=False
elif age>=30:
    A=True
    B=True
else:
    A=False
    B=False

if citizen>=7 and citizen<9:
    C=True
    D=False
elif citizen>=9:
    C=True
    D=True
else:
    C=False
    D=False

print(A and C, B and D)
