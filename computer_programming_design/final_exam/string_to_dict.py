def str_to_dict(list):
    d={}
    for i in range(len(list)):
        position=list[i].find("=")
        d[list[i][0:position]]=list[i][(position+1):len(list[i])]
    return d
    #find "="
    #assign到dictionary
if __name__=="__main__":
    print(str_to_dict(["1=one","2=two","3=three","4=four"]))
    print(str_to_dict(["dog=bark", "cat=meow", "cow=moo"]))
    print(str_to_dict(["bob=human", "lola=dog", "mittens=cat", "todd=frog"]))
