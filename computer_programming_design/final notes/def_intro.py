def Fibnocil(i):
    a,b=0,1
    while a<10:
        print(a)
        a,b=b,a+b
limit=int(input("Please Enter It:"))
Fibnocil(limit)
#如果只有寫return，或是都沒有寫，其實還是有回傳值叫做None

q,r=divmod(5,2)#可以得到商數、餘數（q＝商,r＝餘）
print(q,r)

a = int(input('enter a: '))
b = int(input('enter b: '))
while a != b:
 if a > b:
    a -= b
 else:
    b -= a
print('gcd = %d' % a)