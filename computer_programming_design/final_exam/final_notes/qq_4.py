import random
tot=0

while True:
    try:
        num=int(input("Number of problems: "))#輸入問題的數量
        if (num>0):  
            for i in range(num): 
                op1, op2 = random.randint(10, 100), random.randint(10, 100)##隨機取數
                operator = random.choice(['+', '-'])#隨機決定正負號

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
                            correction-=1#看是否正確
                    break
                if wrong==True:
                    print('\tSorry, should be',solution)#錯誤並告訴答案
                correction/=3
                tot+=correction#將每題分數的比率加起來
            print("Final score:",(100/num)*tot)#計算分數
            break
        else:
            print('You Enter The Wrong Number!')#非正整數就告訴使用者錯誤
            continue
    except:
        print('You must enter an integer!')#如果亂輸入非整數就告訴使用者錯誤
        continue