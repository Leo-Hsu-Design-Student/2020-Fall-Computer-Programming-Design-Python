import random
op1=random.randint(1,10)
op2=random.randint(1,10)
operator=random.choice(['+','-'])
print(op1,operator,op2,'=?',end='\n')
if operator=='+':
    solution=op1+op2
else:
    solution=op1-op2

answer=int(input())
if answer==int(solution):
    print(answer,"Well done!")
else:
    print("No good...Answer should be",solution)
