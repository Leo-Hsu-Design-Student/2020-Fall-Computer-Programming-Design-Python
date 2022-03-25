import random
tot=0
num=int(input("Number of problems: "))
if (num>0):  
    for i in range(num): 
        op1, op2 = random.randint(10, 100), random.randint(10, 100)
        operator = random.choice(['+', '-'])
        if (operator == '-'):
            if(op1<op2):
                op1, op2 = op2, op1
            solution = op1 - op2
        else:
            solution = op1 + op2
        correction=3
        wrong=True
        while(wrong):
            for i in range(3):
                print(op1, operator, op2, '= ? ', end='')
                if (int(input()) == solution):
                    print('\tGood job!')
                    wrong=False
                    break
                else:
                    correction-=1
            break
        if wrong==True:
            print('\tSorry, should be',solution)
        correction/=3
        tot+=correction
    print("Final score:",(100/num)*tot)
else:
    print('You Enter The Wrong Number!')