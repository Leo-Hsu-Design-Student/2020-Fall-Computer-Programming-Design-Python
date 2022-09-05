def estimate_carry(a,b):
    count=0
    while a>0 and b>0:
        digit_a=a%10
        digit_b=b%10
        a=a//10
        b=b//10
        if digit_a+digit_b>9:
            count+=1
    return count

if __name__ == '__main__':#只能在這份程式碼執行，不能從import執行，improt的話name會等於檔名，不等於main
    #這是測試碼的部分，在import不一定要測試，但在主程式碼可以測試
    test_cases = [
    [0,0,0], # a, b, estimated
    [0,10,0],[10,0,0],
    [123,321,0],[123,32,0],[32,123,0],
    [789,141,2],[789,14,1],[78,141,1]
    ]

    for case in test_cases:
        estimated = estimate_carry(case[0],case[1])
        print('%d + %d => ~ %d carries.'
            % (case[0],case[1],estimated))
        if estimated != case[2]:
            print('\tError: %d expected.' % case[2])