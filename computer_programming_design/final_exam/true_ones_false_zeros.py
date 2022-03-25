def integer_boolean(a):
    boolean_store=[]
    for i in range(len(a)):
        if a[i]=="1":
            boolean_store.append(True)
        elif a[i]=="0":
            boolean_store.append(False)
    return boolean_store
if __name__=="__main__":
    print(integer_boolean("100101"))
    print(integer_boolean("10"))
    print(integer_boolean("001"))