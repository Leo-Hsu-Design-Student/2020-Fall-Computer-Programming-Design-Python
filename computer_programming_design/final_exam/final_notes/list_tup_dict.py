#大寫字母永遠比較小
lists = [[2,4],[],[1,2,3],[1]]
lists.sort(key=len) 
print(lists)

#hist=histogram([1,2,3],"ㄇ")
#print(hist)

#tuple:immutable，不像list可以改變值
T=()
T=1,1,2,3,'x'
print(T)
T=tuple('xyz')
print(T)
