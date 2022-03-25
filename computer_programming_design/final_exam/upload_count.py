def upload_count(a,b):
    times=0
    for i in range(len(a)):
        if b in a[i]:
            times+=1
    return times
"""def upload_count(list_date, month):
    count = 0
    for date in list_date:
        if date.split()[0] == month:
            count += 1

    return count"""
if __name__=="__main__":
    print(upload_count(["Sept 22","Sept 21","Oct 15"],"Sept"))
    print(upload_count(["Sept 22","Sept 21","Oct 15"],"Oct"))
