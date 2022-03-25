def rank(dic,key1):
    scores=[]
    for i,j in dic.items():
        scores.append(j)
    compete=sorted(scores,reverse=True)
    ranks={}
    for i in range(len(compete)):
        if i == 0:
            ranks[compete[i]]=1
        else:
            if compete[i]==compete[i-1]:
                ranks[compete[i]]=ranks[compete[i-1]]
            else:
                ranks[compete[i]]=i+1
    #for i,j in ranks.items():
        #print(i,j)
    for key,value in dic.items():
        if key1==key:
            the_very_rank=ranks[dic[key]]
    return the_very_rank

"""def competition_rank(dictionary, name):
    rank = 0
    prevalue = -1
    count = 0

    for value in sorted(dictionary.values(), reverse=True):
        if value != prevalue:
            rank = rank + 1 + count
            count = 0
        else:
            count += 1

        if value == dictionary[name]:
            break

        prevalue = value

    return rank"""
if __name__=="__main__":
    print(rank({"George": 96,"Emily": 95,"Susan": 93,"Jane": 89,"Brett": 82}, "Jane"))
    print(rank({"Kate": 92,"Carol": 92,"Jess": 87,"Bruce": 87,"Scott": 84}, "Bruce"))
    