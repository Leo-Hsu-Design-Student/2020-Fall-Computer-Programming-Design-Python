import pygame as pg
pg.init()#初始化
screenX, screenY=640,480#螢幕長寬
screen=pg.display.set_mode((screenX,screenY))
title="moving block"
pg.display.set_caption(title)#螢幕標題
background=pg.Surface(screen.get_size())#背景大小
background=background.convert()
background.fill((255,255,0))#背景顏色

box=pg.Surface((80,60))#建立方塊的繪圖層
box.fill((0,255,255))

x, y, dx, dy = 280, 210, 0, 0 #定義初始位置與初始動量
direction='stay'
#關閉程式的程式碼
run=True
clock=pg.time.Clock()#建立時間物件
clock.tick(60)#一秒更新幾次
"""時間物件記得設在While loop外面，不用每次都設定一次，另外若是要讓他跑超快，就直接不要設定clock，等於無限更新"""

while run:#保持視窗開啟
    for event in pg.event.get():
        if event.type==pg.QUIT:#設定關閉鍵
            run=False
        if event.type == pg.KEYDOWN:#按下上下左右鍵
            if event.key == pg.K_LEFT:
                direction='left'
            elif event.key == pg.K_RIGHT:
                direction='right'                    
            elif event.key == pg.K_UP:
                direction='up'
            elif event.key == pg.K_DOWN:
                direction='down'
    #計算動量
    if direction=='left':
        if x>0:
            dx,dy=-10,0
        else:
            dx,dy=0,0
    elif direction=='right':
        if x<560:
            dx,dy=10,0
        else:
            dx,dy=0,0
    elif direction=='up':
        if y>0:
            dx,dy=0,-10
        else:
            dx,dy=0,0
    elif direction=='down':
        if y<420:
            dx,dy=0,10
        else:
            dx,dy=0,0
    x += dx #更新位置
    y += dy #更新位置
    screen.blit(background,(0,0))#更新背景
    screen.blit(box,(x,y))#更新方塊
    pg.display.update()#後面可以加上一些值，更新部分畫面，pg.display.flip()是更新全部畫面
pg.quit()#關閉視窗