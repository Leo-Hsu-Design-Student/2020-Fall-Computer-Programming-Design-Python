list_int = list(map(int, input().split()))
#list_int = [int(x) for x in input().split()]

max, min, total = list_int[0], list_int[0], 0

for i in list_int:
    total += i
    if i > max:
        max = i
    if i < min:
        min = i

average = total / len(list_int)

print('max = {}, min = {}, average = {}'.format(max, min, average))