"""
前置區
"""

from pygame import mixer


# Initialize pygame and check for errors encountered
import pygame, sys, time, random
check_errors = pygame.init()
if check_errors[1] > 0:
    print('Had {} errors when initialising game, exiting...'.format(check_errors[1]))
    sys.exit(-1)
#display background music#
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)
    
# 製造寬(x)1480，高(y)780單位的視窗。
frame_size_x = 1480
frame_size_y = 780
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption('Snake')#視窗標題為snake
screen = pygame.display.set_mode((1480,780))

#遊戲開始前
#導入封面圖
background_before_game = pygame.image.load("background_before_the_game.jpg")
background_before_game=pygame.transform.scale(background_before_game,(1480,780))
background_before_game.convert()
#導入封面文字
STHeitiUI = pygame.font.Font("STHeitiUI.ttf", 48)#字形
showingText = STHeitiUI.render("按一下開始遊戲", True, (255, 255, 255))#文字內容
showingText_pos=((screen.get_width()- showingText.get_width()) // 2, (screen.get_height() - showingText.get_height()) // 2)#文字位置
#將封面圖與文字更新出來
screen.blit(background_before_game,(0,0))
screen.blit(showingText, showingText_pos)
pygame.display.update()
#封面程式
beforeGame = True
while beforeGame:
    for event in pygame.event.get():
        #按視窗右上的X或鍵盤上的ESC可關閉程式
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #按滑鼠或鍵盤上的任一件可脫離迴圈，進入下一張圖
        elif event.type == pygame.MOUSEBUTTONDOWN:
            beforeGame = False

#導入規則圖
background_rule = pygame.image.load("rule.jpg")
background_rule = pygame.transform.scale(background_rule,(1480,780))
background_rule.convert()
#將規則圖更新出來
screen.blit(background_rule,(0,0))
pygame.display.update()
#規則圖程式
showRule = True
while showRule:
    for event in pygame.event.get():
        #按視窗右上的X或鍵盤上的ESC可關閉程式
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #按滑鼠或鍵盤上的任一件可脫離迴圈，進入遊戲
        elif event.type == pygame.MOUSEBUTTONDOWN:
            showRule = False
 
#圖片導入
#背景圖片導入，共兩項
new_background = pygame.image.load("new_background.jpg")
new_background =pygame.transform.scale(new_background ,(1120,780))
new_background.convert()
background_end = pygame.image.load("background_end.jpg")
background_end=pygame.transform.scale(background_end,(1120,780))
background_end.convert()
#道具圖片導入，共八項
opposite_direction_pic=pygame.image.load("opposite_direction.png")
opposite_direction_pic=pygame.transform.scale(opposite_direction_pic,(20,20))
opposite_direction_pic.convert()
speed_up_pic=pygame.image.load("speed_up.png")
speed_up_pic=pygame.transform.scale(speed_up_pic,(20,20))
speed_up_pic.convert()
score_up_pic=pygame.image.load("score_up.png")
score_up_pic=pygame.transform.scale(score_up_pic,(20,20))
score_up_pic.convert()
fixed_direction_pic=pygame.image.load("fixed_direction.png")
fixed_direction_pic=pygame.transform.scale(fixed_direction_pic,(20,20))
fixed_direction_pic.convert()
food_green_pic=pygame.image.load("food_green.png")
food_green_pic=pygame.transform.scale(food_green_pic,(20,20))
food_green_pic.convert()
food_orange_pic=pygame.image.load("food_orange.png")
food_orange_pic=pygame.transform.scale(food_orange_pic,(20,20))
food_orange_pic.convert()
food_red_pic=pygame.image.load("food_red.png")
food_red_pic=pygame.transform.scale(food_red_pic,(20,20))
food_red_pic.convert()
food_yellow_pic=pygame.image.load("food_yellow.png")
food_yellow_pic=pygame.transform.scale(food_yellow_pic,(20,20))
food_yellow_pic.convert()
#預設顏色(不一定會全用到)
red = pygame.Color(255, 0, 0)      
blue = pygame.Color(0, 0, 255)     
black = pygame.Color(0, 0, 0)      
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)    
yellow=pygame.Color(255, 255, 0)  
purple=pygame.Color(218,112,214)   
pink=pygame.Color(255, 0, 255)     
orange=pygame.Color(255, 153, 18)

#蛇的初始狀態
#a,b兩條蛇初始位置與長度
snake_head_b=[460,400]
snake_body_b=[[460,400],[460,400+20],[460,400+20*2]]
snake_head_a=[1020,400]
snake_body_a=[[1020,400],[1020,400+20],[1020,400+20*2]]
#初始方向
change_to_a = direction_a = 'UP'
change_to_b = direction_b = 'UP'
#初始分數
score_a=0
score_b=0
#起始速度
move_times_a=1
move_times_b=1

#附加在蛇身上的狀態，初始情況皆為False。
#snake_a
a_speed_up=False             
a_upposite_direction=False
a_score_up=False
a_fixed_direction=False
a_cool_down=False            
#snake_b
b_speed_up=False             
b_upposite_direction=False
b_score_up=False
b_fixed_direction=False
b_cool_down=False            
#狀態的時間控制器(秒為單位)，初始狀態皆為0
#a蛇
upposite_direction_control_a=0  
speed_up_control_a=0
score_up_control_a=0
fixed_direction_control_a=0
cool_down_control_a=0           
#b蛇
upposite_direction_control_b=0  
speed_up_control_b=0
score_up_control_b=0
fixed_direction_control_b=0
cool_down_control_b=0

#combo相關設置
#累積的combo的類型
combo_status_a="none"
combo_status_b="none"
#累積的combo數
combo_a=0
combo_b=0
#連吃三個食物後獲得的獎勵(沒獎勵時為0)
bonus_a=0
bonus_b=0
#判斷狀態列是否需顯示combo(0時不顯示，1、2、3、4時顯示相應的文字)
a_combo_trigger=0       
b_combo_trigger=0

#時間設置
time_count=0   #用於紀錄時間經過多久
limit=180       #控制遊戲結束的變數
over =False    #True時遊戲結束

##計時器區，只在第一個event做註解解釋。其餘可依此類推
#架設a蛇和b蛇狀態的計時器，功用是每隔一秒將狀態的時間控制器減1，以控制持續時間
tool_trigger_a=pygame.USEREVENT + 1       #tool_trigger_a為event的名字
pygame.time.set_timer(tool_trigger_a,1000)#架設tool_trigger_a這個event的計時器，1000代表tool_trigger_a每經過1秒發生一次
tool_trigger_b=pygame.USEREVENT + 2
pygame.time.set_timer(tool_trigger_b,1000)
#架設狀態欄顯示combo時的計時器
combo_trigger_a=pygame.USEREVENT+3
pygame.time.set_timer(combo_trigger_a,0)#0代表此計時器的初始狀態為不發生，產生combo時會設為3000(3秒)，及讓combo在狀態列顯示3秒
combo_trigger_b=pygame.USEREVENT+4
pygame.time.set_timer(combo_trigger_b,0)
#架設時間限制的計時器，每隔1秒ime_count+1，達到limit就OVER
time_limit=pygame.USEREVENT + 5
pygame.time.set_timer(time_limit,1000)

#stuff_list用於儲存所有食物和道具
stuff_list=[]
#儲存食物的list
food_list=[]
food1=[]
food2=[]
food3=[]
food4=[]
#儲存道具的list
tool_list=[]
tool_upposite_direction=[]
tool_speed_up=[]
tool_score_up=[]
tool_fixed_direction=[]

"""
def 區
"""
#產生食物
def food_spawn(code):
        #產生座標
        food_x= random.randrange(18, ((frame_size_x-180)//20)) * 20
        food_y= random.randrange(1, ((frame_size_y-180)//20)) * 20
        food_pos= [food_x, food_y]
        #將此座標放入code所對應的食物種類，同時將此座標放入stuff_list。
        if code==1 and (food_pos not in snake_body_a) and (food_pos not in snake_body_b) and (food_pos not in food_list) and (food_pos not in tool_list):
            food1.append(food_pos)
            stuff_list.append(food_pos)
        if code==2 and (food_pos not in snake_body_a) and (food_pos not in snake_body_b) and (food_pos not in food_list) and (food_pos not in tool_list):
            food2.append(food_pos)
            stuff_list.append(food_pos)
        if code==3 and (food_pos not in snake_body_a) and (food_pos not in snake_body_b) and (food_pos not in food_list) and (food_pos not in tool_list):
            food3.append(food_pos)
            stuff_list.append(food_pos)
        if code==4 and (food_pos not in snake_body_a) and (food_pos not in snake_body_b) and (food_pos not in food_list) and (food_pos not in tool_list):
            food4.append(food_pos)
            stuff_list.append(food_pos)
#產生道具
def tool_spawn():
    #產生座標
    tool_x = random.randrange(18, ((frame_size_x-180)//20)) * 20
    tool_y = random.randrange(18, ((frame_size_y-180)//20)) * 20
    tool_pos = [tool_x, tool_y]
    #隨機產生1到4的數字，將座標放入數字所對應的道具種類，同時將此座標放入stuff_list。
    tool_code=random.randrange(1, 5)
    if tool_code==1 and (tool_pos not in snake_body_a) and (tool_pos not in snake_body_b) and (tool_pos not in food_list) and (tool_pos not in tool_list):
        stuff_list.append(tool_pos)
        tool_upposite_direction.append(tool_pos)
    if tool_code==2 and (tool_pos not in snake_body_a) and (tool_pos not in snake_body_b) and (tool_pos not in food_list) and (tool_pos not in tool_list):
        stuff_list.append(tool_pos)
        tool_speed_up.append(tool_pos)
    if tool_code==3 and (tool_pos not in snake_body_a) and (tool_pos not in snake_body_b) and (tool_pos not in food_list) and (tool_pos not in tool_list):
        stuff_list.append(tool_pos)
        tool_score_up.append(tool_pos)
    if tool_code==4 and (tool_pos not in snake_body_a) and (tool_pos not in snake_body_b) and (tool_pos not in food_list) and (tool_pos not in tool_list):
        stuff_list.append(tool_pos)
        tool_fixed_direction.append(tool_pos)

#每次吃到食物都會觸發，用於判定combo狀態，並return 三樣東西：新的combo的狀態、獎勵分數和新的combo數。
def combo(snake,food_eaten,status,combo):
    #4個paramete:(哪條蛇，碰到甚麼食物、碰到時的combo狀態為何、碰到時combo數為多少)
    #snake a
    if snake=="a":
        if status=="none" or status==food_eaten:
            combo+=1
            if combo==3:
                if status=="food1":
                    return "none",1,0   
                elif status=="food2":
                    return "none",2,0
                elif status=="food3":
                    return "none",3,0
                elif status=="food4":
                    return "none",4,0
            elif combo<3:
                return food_eaten,0,combo
        else:
            return food_eaten,0,1
    #snake b
    if snake=="b":
        if status=="none" or status==food_eaten:
            combo+=1
            if combo==3:
                if status=="food1":
                    return "none",1,0
                elif status=="food2":
                    return "none",2,0
                elif status=="food3":
                    return "none",3,0
                elif status=="food4":
                    return "none",4,0
            elif combo<3:
                return food_eaten,0,combo
        else:
            return food_eaten,0,1
#通常的分數判斷，return應該獲得分數
def score(snake):
    #snake a
    if snake=="a":
        if a_score_up:
            return 2
        else:
            return 1
    #snake b
    if snake=="b":
        if b_score_up:
            return 2
        else:
            return 1

#撞到東西後的懲罰
def snake_halfed(snake):
    #snake_a
    if snake=="a":
        if len(snake_body_a)==1:            #身長為1時，不能再減半
            objective=1          
        else:
            objective=len(snake_body_a)//2  #身長減半
            effect_food=pygame.mixer.Sound('crash.wav')
            effect_food.play(0)                           
        while len(snake_body_a)>objective:  #將蛇的長度縮短到objective的長度
            snake_body_a.pop()              
    #snake b
    if snake=="b":
        if len(snake_body_b)==1:
            objective=1
        else:
            objective=len(snake_body_b)//2
            effect_food=pygame.mixer.Sound('crash.wav')
            effect_food.play(0)
        while len(snake_body_b)>objective:
            snake_body_b.pop()
#處理snake_head跑到不被接受的地方時所作的反應，基本上就是將蛇頭回復到上次移動的位置
def snake_return(snake):
    #snake a
    if snake=="a":
        if direction_a=='UP':
            snake_head_a[1] += 20 
        if direction_a== 'DOWN':
            snake_head_a[1] -= 20
        if direction_a== 'LEFT':
            snake_head_a[0] += 20
        if direction_a== 'RIGHT':
            snake_head_a[0] -= 20
    #snake b
    if snake=="b":
        if direction_b=='UP':
            snake_head_b[1] += 20 
        if direction_b== 'DOWN':
            snake_head_b[1] -= 20
        if direction_b== 'LEFT':
            snake_head_b[0] += 20
        if direction_b== 'RIGHT':
            snake_head_b[0] -= 20
#顯示時間
def show_time(color, font, size):
    time_font=pygame.font.SysFont(font, size)
    time_surface = time_font.render(str(time_count), True, color)
    time_rect = time_surface.get_rect()
    time_rect.midtop = (frame_size_x/10*5, 15)
    game_window.blit(time_surface, time_rect)
##狀態列:顯示分數、狀態、combo。
def show_score(color, font, size):
    #snake a
    pygame.draw.rect(game_window ,red, [1300, 0, 180, 780], 2)
    score_a_font= pygame.font.SysFont(font, size)
    score_a_surface = score_a_font.render('Score_red:' + str(score_a), True, color)
    score_a_rect = score_a_surface.get_rect()
    score_a_rect = score_a_surface.get_rect()
    score_a_rect.midtop = (frame_size_x-90,15)
    game_window.blit(score_a_surface, score_a_rect)
    #snake b
    pygame.draw.rect(game_window ,blue, [0, 0, 180, 780], 2)
    score_b_font= pygame.font.SysFont(font, size)
    score_b_surface = score_b_font.render('Score_blue:' + str(score_b), True, color)
    score_b_rect = score_b_surface.get_rect()
    score_b_rect.midtop = (90, 15)
    game_window.blit(score_b_surface, score_b_rect)
def draw_combo(self,kind,font,size):
    if kind!=0:
        combo_Font=pygame.font.SysFont(font, size)
        if kind==1:
            combo=combo_Font.render("3 combos! +1", True ,orange)
        elif kind==2:
            combo=combo_Font.render("3 combos! +2", True ,green)
        elif kind==3:
            combo=combo_Font.render("3 combos! +3", True ,yellow)
        elif kind==4:
            combo=combo_Font.render("3 combos! +4", True ,red)
        combo_rect=combo.get_rect()
        if self=='a':
            combo_rect.midtop = (frame_size_x-90,200)
        elif self=='b':
            combo_rect.midtop = (90,200)
        game_window.blit(combo,combo_rect)
def show_status(font, size):
    #list_status內的東西各自代表或用於：[剩餘秒數、顯示名稱、顏色，狀態(判斷是否需要顯示於狀態列)]
    list_status_a=[[upposite_direction_control_a,"反方向:",purple,a_upposite_direction],[speed_up_control_a,"加速:",yellow,a_speed_up],[score_up_control_a,"加分:",green,a_score_up],[fixed_direction_control_a,"固定方向:",pink,a_fixed_direction],[cool_down_control_a,"無傷:",white,a_cool_down]]
    list_status_b=[[upposite_direction_control_b,"反方向:",purple,b_upposite_direction],[speed_up_control_b,"加速:",yellow,b_speed_up],[score_up_control_b,"加分:",green,b_score_up],[fixed_direction_control_b,"固定方向:",pink,b_fixed_direction],[cool_down_control_b,"無傷:",white,b_cool_down]]
    for status in list_status_a:
        if status[0]>=0 and status[3]==True:
            status_font_a=pygame.font.SysFont(font,size)
            status_surface_a=status_font_a.render(str(status[1])+ str(status[0]), True, status[2])
            status_rect_a= status_surface_a.get_rect()
            status_rect_a.midtop = (frame_size_x-90,(list_status_a.index(status)+2)*20)
            game_window.blit(status_surface_a,status_rect_a)
    for status in list_status_b:
        if status[0]>=0 and status[3]==True:
            status_font_b=pygame.font.SysFont(font,size)
            status_surface_b=status_font_b.render(str(status[1])+ str(status[0]), True, status[2])
            status_rect_b= status_surface_b.get_rect()
            status_rect_b.midtop = (90,(list_status_b.index(status)+2)*20)
            game_window.blit(status_surface_b,status_rect_b)

#顯示over時的文字與圖片
def game_over():
    #顯示遊戲結束了
    over_font = pygame.font.SysFont('times new roman', 90)
    over_surface = over_font.render("Time's up!", True,black)
    over_rect = over_surface.get_rect()
    over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    #判斷贏家並顯示對應文字
    winner_font = pygame.font.SysFont('times new roman', 36)
    if score_a>score_b:
        winner_surface= winner_font.render('Red wins!', True, red)
    elif score_a<score_b:
        winner_surface= winner_font.render('Blue wins!', True, blue)
    else:
        winner_surface= winner_font.render('Tied!', True, black)
    winner_rect= winner_surface.get_rect()
    winner_rect.midtop = (frame_size_x/2, frame_size_y/3+30)
    #更新螢幕
    game_window.blit(background_end,(180,0))
    game_window.blit(over_surface, over_rect)
    game_window.blit(winner_surface,winner_rect)
    show_score(white, 'consolas', 20)
    pygame.display.flip()
    time.sleep(1)
    return 1
#over後，控制離開程式的方式
def end():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

"""
運行區
"""
# Main logic
while True:
    for event in pygame.event.get():
        #關閉功能
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        #時間限制判斷
        elif event.type == time_limit:
            time_count+=1
            if time_count==limit:
                over=True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

        # 決定chang_to的方向
        # 道具a_upposite_direction的功用在這裡。
            #snake_a
            if a_upposite_direction:
                if event.key == pygame.K_UP:
                    change_to_a ='DOWN'
                if event.key == pygame.K_DOWN:
                    change_to_a= 'UP'
                if event.key == pygame.K_LEFT:
                    change_to_a= 'RIGHT'
                if event.key == pygame.K_RIGHT:
                    change_to_a= 'LEFT'
            else:
                if event.key == pygame.K_UP:
                    change_to_a= 'UP'
                if event.key == pygame.K_DOWN:
                    change_to_a= 'DOWN'
                if event.key== pygame.K_LEFT:
                    change_to_a= 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to_a= 'RIGHT'
            #snake_b
            if b_upposite_direction:
                if event.key == ord('w'):
                    change_to_b= 'DOWN'
                if event.key == ord('s'):
                    change_to_b= 'UP'
                if event.key == ord('a'):
                    change_to_b= 'RIGHT'
                if event.key == ord('d'):
                    change_to_b= 'LEFT'
            else:
                if event.key == ord('w'):
                    change_to_b = 'UP'
                if event.key == ord('s'):
                    change_to_b= 'DOWN'
                if event.key == ord('a'):
                    change_to_b= 'LEFT'
                if event.key == ord('d'):
                    change_to_b= 'RIGHT'    
        #前面設置的計時器。時間控制器每隔1秒減1，到零後，對應狀態就變為False，即該項狀態變為沒有。
        #snake a
        if event.type ==tool_trigger_a:
            if upposite_direction_control_a>0:
                upposite_direction_control_a-=1
            else:
                a_upposite_direction=False
            if speed_up_control_a>0:
                speed_up_control_a-=1
            else:
                a_speed_up=False
                
            if score_up_control_a>0:
                score_up_control_a-=1
            else:
                a_score_up=False
                
            if fixed_direction_control_a>0:
                fixed_direction_control_a-=1
            else:
                a_fixed_direction=False

            if cool_down_control_a>0:
                cool_down_control_a-=1
            else:
                a_cool_down=False
        #snake b
        if event.type ==tool_trigger_b:             
            if upposite_direction_control_b>0:
                upposite_direction_control_b-=1
            else:
                b_upposite_direction=False
            if speed_up_control_b>0:
                speed_up_control_b-=1
            else:
                b_speed_up=False
            if score_up_control_b>0:
                 b_score_up=False
            if fixed_direction_control_b>0:
                fixed_direction_control_b-=1
            else:
                b_fixed_direction=False
            if cool_down_control_b>0:
                cool_down_control_b-=1
            else:
                b_cool_down=False
        #觸發過combo_trigger_a三秒後，a_combo_trigger回歸0(即沒有)，同時不再計時
        if event.type == combo_trigger_a:
            a_combo_trigger=0
            pygame.time.set_timer(combo_trigger_a,0)
        if event.type == combo_trigger_b:
            b_combo_trigger=0
            pygame.time.set_timer(combo_trigger_b,0)


#決定 direcion
    #snake_a
    #道具fixed dirction的功用在這裡，基本上就是讓change_to跟著direction走。
    if a_fixed_direction:
        change_to_a=direction_a
    #長度只有1時，因為玩家看不出來移動方向，就不限制移動的方向
    elif len(snake_body_a)==1:
        if change_to_a== 'UP':
            direction_a= 'UP'
        if change_to_a== 'DOWN': 
            direction_a= 'DOWN'
        if change_to_a== 'LEFT':
            direction_a= 'LEFT'
        if change_to_a== 'RIGHT': 
            direction_a= 'RIGHT'
    #避免snake突然往相反方向前進。
    else:
        if change_to_a== 'UP' and direction_a!= 'DOWN':
            direction_a= 'UP'
        if change_to_a== 'DOWN' and direction_a!= 'UP':
            direction_a= 'DOWN'
        if change_to_a== 'LEFT' and direction_a!= 'RIGHT':
            direction_a= 'LEFT'
        if change_to_a== 'RIGHT' and direction_a!= 'LEFT':
            direction_a= 'RIGHT'
    #snake_b
    if b_fixed_direction:
        change_to_b=direction_b
    elif len(snake_body_b)==1:
        if change_to_b== 'UP':
            direction_b= 'UP'
        if change_to_b== 'DOWN':
            direction_b= 'DOWN'
        if change_to_b== 'LEFT':
            direction_b= 'LEFT'
        if change_to_b== 'RIGHT':
            direction_b= 'RIGHT'        
    else:
        if change_to_b== 'UP' and direction_b!= 'DOWN':
            direction_b= 'UP'
        if change_to_b== 'DOWN' and direction_b!= 'UP':
            direction_b= 'DOWN'
        if change_to_b== 'LEFT' and direction_b!= 'RIGHT':
            direction_b= 'LEFT'
        if change_to_b== 'RIGHT' and direction_b!= 'LEFT':
            direction_b= 'RIGHT'

#道具speed_up的功用在這裡。move_time_time指的是snake moving logic得施行次數。也就是說如果處於speed_up狀態下的話，等於是在相同時間(1/10秒)裡作了兩次的位移,即兩倍速
    #snake_a
    if a_speed_up:
        move_time_a=2
    else:
        move_time_a=1
    #snake_a
    if b_speed_up:
        move_time_b=2
    else:
        move_time_b=1
        
###snake moving logic
    #snake_a
    #產生一個新的snake_head_a
    for i in range(move_time_a):
        if direction_a=='UP':
            snake_head_a[1] -= 20 
        if direction_a== 'DOWN':
            snake_head_a[1] += 20
        if direction_a== 'LEFT':
            snake_head_a[0] -= 20
        if direction_a== 'RIGHT':
            snake_head_a[0] += 20
        #doom代表snake_head處在一個不能被規則接受的座標，包括邊界外，snake_body_a自己以外的任一座標，和snake_body_b的任一座標
        doom_a=False
        if snake_head_a[0] < 180 or snake_head_a[0] > frame_size_x-190 or snake_head_a[1] < 0 or snake_head_a[1] > frame_size_y-20 or snake_head_a in snake_body_a[1:] or snake_head_a in snake_body_b:
            doom_a=True
        #doom的應對方式
        if doom_a:
            if a_cool_down:
                snake_return("a")  #限制位移
            elif not a_cool_down:
                score_a=score_a//2      #分數減半
                snake_halfed("a")       #長度減半
                snake_return("a")       #限制位移
                cool_down_control_a+=5  #五秒的cool_down時間控制器
                a_cool_down=True        #a的無傷狀態開啟

        #正常的移動方式
        elif not doom_a: 
            snake_body_a.insert(0, list(snake_head_a))  #將位移後的蛇頭加入身體的第一位
            #有吃到食物的話，做以下的事情
            if snake_head_a in food1 or snake_head_a in food2 or snake_head_a in food3 or snake_head_a in food4:
                #只對food1做註解，因為格式都一樣
                if snake_head_a in food1:
                    effect_food=pygame.mixer.Sound('food.wav') #放音效
                    effect_food.play(0)                        
                    score_a+=score("a")                        #加通常分數
                    food1.remove(snake_head_a)                 #消除被吃掉的食物
                    stuff_list.remove(snake_head_a)            
                    combo_status_a,bonus_a,combo_a=combo("a","food1",combo_status_a,combo_a)#判斷新的combo狀態和combo數，同時判斷是否有額外分數
                elif snake_head_a in food2:
                    effect_food=pygame.mixer.Sound('food.wav')
                    effect_food.play(0)
                    score_a+=score("a")
                    food2.remove(snake_head_a)
                    stuff_list.remove(snake_head_a)
                    combo_status_a,bonus_a,combo_a=combo("a","food2",combo_status_a,combo_a)
                elif snake_head_a in food3:
                    effect_food=pygame.mixer.Sound('food.wav')
                    effect_food.play(0)
                    score_a+=score("a")
                    food3.remove(snake_head_a)
                    stuff_list.remove(snake_head_a)
                    combo_status_a,bonus_a,combo_a=combo("a","food3",combo_status_a,combo_a)
                elif snake_head_a in food4:
                    effect_food=pygame.mixer.Sound('food.wav')
                    effect_food.play(0)
                    score_a+=score("a")
                    food4.remove(snake_head_a)
                    stuff_list.remove(snake_head_a)
                    combo_status_a,bonus_a,combo_a=combo("a","food4",combo_status_a,combo_a)
                #如果有額外分數，說明有combo，因此要在狀態欄顯示combo
                if bonus_a>0:
                    a_combo_trigger=bonus_a                    #從額外分數，可知是何種combo，最後會以a_combo_trigger這個變數來顯示combo的樣式
                    pygame.time.set_timer(combo_trigger_a,3000)#設定combo_trigger_a的計時器為3秒，3秒後a_combo_trigger會變為0，也就是不顯示combo。,換句話說，只顯示3秒
                    score_a+=bonus_a                           #獲得額外分數
                    bonus_a=0                                  #額外分數歸零
                
            #沒吃到食物的話，做以下的事情以維持長度一致
            elif len(snake_body_a)>1:
                snake_body_a.pop()
            else:
                snake_body_a=[snake_head_a]
    
    #碰到道具的時候，註解只寫第一項，因為格式都一樣
        if snake_head_a in tool_upposite_direction:
            effect_food=pygame.mixer.Sound('tool.wav')    #放音效
            effect_food.play(0)             
            upposite_direction_control_b=5                #給b蛇加五秒的upposite_direction的時間控制器                   
            tool_upposite_direction.remove(snake_head_a)  #消除被吃掉的道具
            stuff_list.remove(snake_head_a)               #同上
            b_upposite_direction=True                     #b蛇的upposite_direction狀態啟動
        if snake_head_a in tool_speed_up:
            effect_food=pygame.mixer.Sound('tool.wav')
            effect_food.play(0)
            speed_up_control_b=10
            tool_speed_up.remove(snake_head_a)
            stuff_list.remove(snake_head_a)
            b_speed_up=True
        if snake_head_a in tool_score_up:
            effect_food=pygame.mixer.Sound('tool.wav')
            effect_food.play(0)
            score_up_control_a=30
            tool_score_up.remove(snake_head_a)
            stuff_list.remove(snake_head_a)
            a_score_up=True
        if snake_head_a in tool_fixed_direction:
            effect_food=pygame.mixer.Sound('tool.wav')
            effect_food.play(0)
            fixed_direction_control_b=2
            tool_fixed_direction.remove(snake_head_a)
            stuff_list.remove(snake_head_a)
            b_fixed_direction=True
    # snake b
    for i in range(move_time_b):
        if direction_b=='UP':
            snake_head_b[1] -= 20 
        if direction_b== 'DOWN':
            snake_head_b[1] += 20
        if direction_b== 'LEFT':
            snake_head_b[0] -= 20
        if direction_b== 'RIGHT':
            snake_head_b[0] += 20
        doom_b=False
        if snake_head_b[0] < 180 or snake_head_b[0] > frame_size_x-190 or snake_head_b[1] < 0 or snake_head_b[1] > frame_size_y-20 or snake_head_b in snake_body_b[1:] or snake_head_b in snake_body_a:
            doom_b=True
        if doom_b:
            if b_cool_down:
                snake_return("b")
            elif not b_cool_down:
                score_b=score_b//2
                snake_halfed("b")
                snake_return("b")
                cool_down_control_b+=5
                b_cool_down=True
        elif not doom_b: 
            snake_body_b.insert(0, list(snake_head_b))
            if snake_head_b in food1 or snake_head_b in food2 or snake_head_b in food3 or snake_head_b in food4:
                if snake_head_b in food1:
                    effect_food=pygame.mixer.Sound('food.wav')
                    effect_food.play(0)
                    score_b+=score("b")
                    food1.remove(snake_head_b)
                    stuff_list.remove(snake_head_b)
                    combo_status_b,bonus_b,combo_b=combo("b","food1",combo_status_b,combo_b)
                elif snake_head_b in food2:
                    effect_food=pygame.mixer.Sound('food.wav')
                    effect_food.play(0)
                    score_b+=score("b")
                    food2.remove(snake_head_b)
                    stuff_list.remove(snake_head_b)
                    combo_status_b,bonus_b,combo_b=combo("b","food2",combo_status_b,combo_b)
                elif snake_head_b in food3:
                    effect_food=pygame.mixer.Sound('food.wav')
                    effect_food.play(0)
                    score_b+=score("b")
                    food3.remove(snake_head_b)
                    stuff_list.remove(snake_head_b)
                    combo_status_b,bonus_b,combo_b=combo("b","food3",combo_status_b,combo_b)
                elif snake_head_b in food4:
                    effect_food=pygame.mixer.Sound('food.wav')
                    effect_food.play(0)
                    score_b+=score("b")
                    food4.remove(snake_head_b)
                    stuff_list.remove(snake_head_b)
                    combo_status_b,bonus_b,combo_b=combo("b","food4",combo_status_b,combo_b)
                if bonus_b>0:
                    b_combo_trigger=bonus_b
                    pygame.time.set_timer(combo_trigger_b,3000)
                    score_b+=bonus_b
                    bonus_b=0
            elif len(snake_body_b)>1:
                snake_body_b.pop()
            else:
                snake_body_b=[snake_head_b]
        if snake_head_b in tool_upposite_direction:
            effect_food=pygame.mixer.Sound('tool.wav')
            effect_food.play(0)
            upposite_direction_control_a=5
            tool_upposite_direction.remove(snake_head_b)
            stuff_list.remove(snake_head_b)
            a_upposite_direction=True
        if snake_head_b in tool_speed_up:
            effect_food=pygame.mixer.Sound('tool.wav')
            effect_food.play(0)
            speed_up_control_a=10
            tool_speed_up.remove(snake_head_b)
            stuff_list.remove(snake_head_b)
            a_speed_up=True
        if snake_head_b in tool_score_up:
            effect_food=pygame.mixer.Sound('tool.wav')
            effect_food.play(0)
            score_up_control_b=30
            tool_score_up.remove(snake_head_b)
            stuff_list.remove(snake_head_b)
            b_score_up=True
        if snake_head_b in tool_fixed_direction:
            effect_food=pygame.mixer.Sound('tool.wav')
            effect_food.play(0)
            fixed_direction_control_a=2
            tool_fixed_direction.remove(snake_head_b)
            stuff_list.remove(snake_head_b)
            a_fixed_direction=True
# Spawning food and tool on the screen
    #食物再生，每個食物場上一定有一
    if len(food1)<1:
        food_spawn(1)
    if len(food2)<1:
        food_spawn(2)
    if len(food3)<1:
        food_spawn(3)
    if len(food4)<1:
        food_spawn(4)
    #道具再生,場上永遠有兩個道具
    while len(tool_upposite_direction)+len(tool_speed_up)+len(tool_score_up)+len(tool_fixed_direction)<2:
        tool_spawn()

    
# Display
    game_window.fill(black)
    game_window.blit(new_background,(180,0))
    # Draw Snake
    for pos in snake_body_a:
        pygame.draw.rect(game_window, red, pygame.Rect(pos[0], pos[1], 20, 20))
        
    for pos in snake_body_b:
        pygame.draw.rect(game_window,blue, pygame.Rect(pos[0], pos[1], 20, 20))
    # Draw food
    for food in food1:
        game_window.blit(food_orange_pic,food)
    for food in food2:
        game_window.blit(food_green_pic,food)
    for food in food3:
        game_window.blit(food_yellow_pic,food)
    for food in food4:
        game_window.blit(food_red_pic,food)
    # Draw tool
    for tool in tool_upposite_direction:
        game_window.blit(opposite_direction_pic,tool)
    for tool in tool_speed_up:
        game_window.blit(speed_up_pic,tool)
    for tool in tool_score_up:
        game_window.blit(score_up_pic,tool)
    for tool in tool_fixed_direction:
        game_window.blit(fixed_direction_pic,tool)
    #game over
    if over:
        game_over()
        end()
    if not over:
        #狀態欄和時間顯示
        show_score(white, 'consolas', 20)
        show_time( white, 'consolas', 25)
        show_status('microsoftjhengheimicrosoftjhengheiui', 20)
        if a_combo_trigger:
            draw_combo("a",a_combo_trigger,'bebasneue',30)
        if b_combo_trigger:
            draw_combo("b",b_combo_trigger,'bebasneue',30)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        pygame.time.Clock().tick(10)
