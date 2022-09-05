list_int = input('Please input a list of integers:').split()

for index in range(len(list_int)):
    list_int[index] = int(list_int[index])

max, min, total = list_int[0], list_int[0], 0

for i in list_int:
    total += i
    if i > max:
        max = i
    if i < min:
        min = i

average = total / len(list_int)

print('max = {}, min = {}, average = {}'.format(max, min, average))