a,b,c=input("Please Enter Three Integer split by a space:").split()
if a==b==c:
    print(a,b,c,"The equal numbers=3")
elif (a==b and b!=c) or (a!=b and b==c) or (a==c and b!=c):
    print(a,b,c,"The equal numbers=2")
else:
    print(a,b,c,"There are no equal numbers")


A,B,C,D=input("Please Enter Four Integer split by a space:").split()
if A==B==C==D:
    print(A,B,C,D,"The equal numbers=4")
elif A!=B!=C!=D:
    print(A,B,C,D,"There are no equal numbers")
elif (A==B==C!=D)or(A==B==D!=C)or(A!=B==C==D)or(A==B==D!=C):
    print(A,B,C,D,"The equal numbers=3")
else:
    print(A,B,C,D,"The equal numbers=2")
