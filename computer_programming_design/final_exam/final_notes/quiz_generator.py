print('###Quiz Generator###')
que_num=int(input('number of problems:'))
min_op =int(input('minimun operand:'))
max_op =int(input('maxmun operand:'))
file_name=input('file name:')

import random
fout=open(file_name,'w')
for i in range(que_num):
    op1=random.randint(min_op,max_op)
    op2=random.randint(min_op,max_op)
    operator=random.choice(['+','-'])

    if operator=='-' and op1<op2:
        op1,op2=op2,op1
    fout.write('%d %s %d= ?\n'%(op1,operator,op2))
fout.close()