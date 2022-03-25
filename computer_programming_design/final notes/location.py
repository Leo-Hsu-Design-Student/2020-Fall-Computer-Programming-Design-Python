def calculate_location(origin,moves):
    origin=([origin[0]],[origin[1],origin[2]])#將輸入進來的tuple內容變成mutable的list
    direction,position=origin#設變數為tuple內容，不用寫兩次中括號
    for i in range(len(moves)):#看輸入的訊息有多少內容就跑幾次
        #定義四個起始方向在遇到前後左右轉的時候，會產生什麼變化
        if direction[0]=='E':
            if moves[i][0]=='F':
                position[0]+=moves[i][1]
                direction[0]='E'
            elif moves[i][0]=='B':
                position[0]-=moves[i][1]
                direction[0]='W'
            elif moves[i][0]=='R':
                position[1]+=moves[i][1]
                direction[0]='S'
            elif moves[i][0]=='L':
                position[1]-=moves[i][1]
                direction[0]='N'
        elif direction[0]=='W':
            if moves[i][0]=='F':
                position[0]-=moves[i][1]
                direction[0]='W'
            elif moves[i][0]=='B':
                position[0]+=moves[i][1]
                direction[0]='E'
            elif moves[i][0]=='R':
                position[1]-=moves[i][1]
                direction[0]='N'
            elif moves[i][0]=='L':
                position[1]+=moves[i][1]
                direction[0]='S'
        elif direction[0]=='N':
            if moves[i][0]=='F':
                position[1]-=moves[i][1]
                direction[0]='N'
            elif moves[i][0]=='B':
                position[1]+=moves[i][1]
                direction[0]='S'
            elif moves[i][0]=='R':
                position[0]+=moves[i][1]
                direction[0]='E'
            elif moves[i][0]=='L':
                position[0]-=moves[i][1]
                direction[0]='W'
        elif direction[0]=='S':
            if moves[i][0]=='F':
                position[1]+=moves[i][1]
                direction[0]='S'
            elif moves[i][0]=='B':
                position[1]-=moves[i][1]
                direction[0]='N'
            elif moves[i][0]=='R':
                position[0]-=moves[i][1]
                direction[0]='W'
            elif moves[i][0]=='L':
                position[0]+=moves[i][1]
                direction[0]='E'
    #用另一個tuple存取上述資料，為了將中括號去掉（變成非list形式）
    origin_final=(direction[0],position[0],position[1])
    return origin_final
if __name__=="__main__":#如果user開啟這份檔案才會執行，我ABCDE五種test cases
    origin=('E',2,3)
    moves=[('F',5),('R',3),('L',3),('L',4),('F',3),('L',4)]
    print(calculate_location(origin,moves))
    origin=('W',110,47)
    moves=[('F',5),('R',3),('L',3),('L',4),('F',3),('L',4)]
    print(calculate_location(origin,moves))
    origin=('N',-3,-19)
    moves=[('B',10),('L',111),('F',7),('L',0),('F',-3),('B',-11)]
    print(calculate_location(origin,moves))
    origin=('S',0,-100)
    moves=[('B',10),('L',111),('F',7),('L',0),('F',-3),('B',-11)]
    print(calculate_location(origin,moves))
    origin=('N',23.5,121.5)
    moves=[('R',10),('L',0),('F',-10),('B',5),('R',0),('L',-5)]
    print(calculate_location(origin,moves))
