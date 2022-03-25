def min_removals(str1,str2):
    remove=0
    for i in range(len(str1)):
        if str1[i] not in str2:
            str1.replace(str1[i],"")
            remove+=1
    for i in range(len(str2)):
        if str2[i] not in str1:
            str2.replace(str2[i],"")
            remove+=1
    return remove

"""def str_to_dict(list_str):
    dict_str = dict()
    for string in list_str:
        key, value = string.split("=")
        dict_str[key] = value

    return dict_str


# check if the function work right
print(str_to_dict(["1=one", "2=two", "3=three", "4=four"]))
print(str_to_dict(["dog=bark", "cat=meow", "cow=moo"]))
print(str_to_dict(["bob=human", "lola=dog", "mittens=cat", "todd=frog"]))"""

if __name__=="__main__":
    print(min_removals("abcde","cab"))
    print(min_removals("deafk","kfeap"))
    print(min_removals("acb","ghi"))


