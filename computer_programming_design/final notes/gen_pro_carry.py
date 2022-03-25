import carry
import random
min_,max_=1000,9999
def gen_additional_problem():
    for i in range(10):
        op1=random.randint(min_,max_)
        op2=random.randint(min_,max_)
        carry1=carry.estimate_carry(op1,op2)
        print('Problem %d: '%(i+1),op1,'+',op2,'=? ',carry1)

gen_additional_problem()
