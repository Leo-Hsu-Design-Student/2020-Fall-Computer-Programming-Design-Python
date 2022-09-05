fobj=open('123.txt')
line=fobj.readlines()
print(line)
lines=fobj.read()#這邊讀不到了，因為fobj已經被改動了
print(lines)
count=0
for i in fobj:
    count+=1
    print('Line',count,':',repr(i))

