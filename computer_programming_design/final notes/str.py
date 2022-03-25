print('hi'.islower())
name='Leo'
print(name.center(10,'='))
print('you are trash'.upper())#可用來把user輸入的答案全部變小寫or大寫，用於比較

s=' spacious '
print(s.strip())
web='www.example.com'
print(web.strip('w.com'))

fruit='banana'
print(fruit.find('na'))#計算位置
print(fruit.count('a'))#計算有幾個
print('it' in 'fruit')

line='#qweqqeqwedsf lol'
print(line.startswith('#'))
print(line.endswith('lol'))

names=['Leo','Tom','Eason']
print('..'.join(names))
lines=' John and Mary Helen      Tom'
names=lines.split()
print(names)
lines1='Leo, Elaine, Yolk, '
names1=lines1.split(', ')
print(names1)

na='Leo has a virtuosity of dribbling.'
print(na.replace('Leo','Leo Hsu'))

str_extract=list()
a="It is a good idea to practice more."
b="John / Mary / Tom / Peter / Helen"
c="A 90 B 80 C 70 D 60 F"
d="apple , banana , cherry ; monkey turtle"
for line in (a,b,c,d):
    #line=line.strip()
    tokens=line.split()
    str_extract.extend(tokens[0:])
print(str_extract)