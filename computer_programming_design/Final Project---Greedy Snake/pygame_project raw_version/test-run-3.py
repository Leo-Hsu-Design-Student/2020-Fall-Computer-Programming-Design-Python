"""
前置區
"""
# Initialize pygame and check for errors encountered
import pygame, sys, time, random
check_errors = pygame.init()
if check_errors[1] > 0:
    print('Had {} errors when initialising game, exiting...'.format(check_errors[1]))
    sys.exit(-1)

# 製造寬(x)720，高(y)640單位的視窗。視窗標題為snake
frame_size_x = 720
frame_size_y = 640
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption('Snake')

#預設顏色
red = pygame.Color(255, 0, 0)      #for snake a
blue = pygame.Color(0, 0, 255)     #for snake b
black = pygame.Color(0, 0, 0)      #for screen
white = pygame.Color(255, 255, 255)#for food
green = pygame.Color(0, 255, 0)    #score_up
yellow=pygame.Color(255, 255, 0)   #speed_up
purple=pygame.Color(139,0,255)     #upposite_direction
pink=pygame.Color(255, 0, 255)     #fixed_direction

#a,b兩條蛇初始位置與長度
snake_head_a=[540,320]
snake_body_a=[[540,320],[540,320+10],[540,320+10*2]]
snake_head_b=[160,320]
snake_body_b=[[160,320],[160,320+10],[160,320+10*2]]

#交給負責人修改
food_x = random.randrange(1, (frame_size_x//10)) * 10
food_y = random.randrange(1, (frame_size_y//10)) * 10
food_pos = [food_x, food_y]
food_spawn = True

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
a_speed_up=False
a_upposite_direction=False
a_score_up=False
a_fixed_direction=False
b_speed_up=False
b_upposite_direction=False
b_score_up=False
b_fixed_direction=False
a_cool_down=False
b_cool_down=False

#狀態的計時器(秒為單位)，初始狀態皆為0
upposite_direction_control_a=0
speed_up_control_a=0
score_up_control_a=0
fixed_direction_control_a=0
upposite_direction_control_b=0
speed_up_control_b=0
score_up_control_b=0
fixed_direction_control_b=0

#控制遊戲結束
over =False

#架設狀態的計時器
tool_trigger_a=pygame.USEREVENT + 1
pygame.time.set_timer(tool_trigger_a,1000)

tool_trigger_b=pygame.USEREVENT + 2
pygame.time.set_timer(tool_trigger_b,1000)

#時間限制的計時器
time_limit=pygame.USEREVENT + 3
pygame.time.set_timer(time_limit,1000)
time_count=0

#cool dowm的計時器
cool_down_a=pygame.USEREVENT + 4
pygame.time.set_timer(cool_down_a,0)

cool_down_b=pygame.USEREVENT + 5
pygame.time.set_timer(cool_down_b,0)

#儲存道具的list

tool_upposite_direction=[]
tool_speed_up=[]
tool_score_up=[]
tool_fixed_direction=[]

"""
def 區
"""

#產生道具
def tool_spawn():
    #道具座標
    tool_x = random.randrange(1, (frame_size_x//10)) * 10
    tool_y = random.randrange(1, (frame_size_y//10)) * 10
    tool_pos = [tool_x, tool_y]
    #道具種類
    tool_code=random.randrange(1, 5)
    if tool_code==1:
        tool_upposite_direction.append(tool_pos)
    if tool_code==2:
        tool_speed_up.append(tool_pos)
    if tool_code==3:
        tool_score_up.append(tool_pos)
    if tool_code==4:
        tool_fixed_direction.append(tool_pos)

#分數判斷
def score(snake):
    if snake=="a":
        if a_score_up:
            return 2
        else:
            return 1
        
    if snake=="b":
        if b_score_up:
            return 2
        else:
            return 1
        
#撞到東西後的懲罰
def snake_halfed(snake):
    if snake=="a":
        if len(snake_body_a)==1:
            objective=1
        else:
            objective=len(snake_body_a)//2
            a_cool_down==True
        while len(snake_body_a)>objective:
            snake_body_a.pop()

    if snake=="b":
        if len(snake_body_b)==1:
            objective=1
        else:
            objective=len(snake_body_b)//2
        while len(snake_body_b)>objective:
            snake_body_b.pop()
            
#處理snake_head跑到不被接受的地方時所作的反應
def snake_return(snake):
    if snake=="a":
        if direction_a=='UP':
            snake_head_a[1] += 10 
        if direction_a== 'DOWN':
            snake_head_a[1] -= 10
        if direction_a== 'LEFT':
            snake_head_a[0] += 10
        if direction_a== 'RIGHT':
            snake_head_a[0] -= 10
    if snake=="b":
        if direction_b=='UP':
            snake_head_b[1] += 10 
        if direction_b== 'DOWN':
            snake_head_b[1] -= 10
        if direction_b== 'LEFT':
            snake_head_b[0] += 10
        if direction_b== 'RIGHT':
            snake_head_b[0] -= 10

#交給負責人修改
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    my_font2 = pygame.font.SysFont('times new roman', 36)
    game_over_surface = my_font.render('GG', True, red)
    game_over_surface2 = my_font2.render('< Press ESC To Exit >', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect2 = game_over_surface2.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_over_rect2.midtop = (frame_size_x/2, frame_size_y/3+30)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    game_window.blit(game_over_surface2, game_over_rect2)

    show_score(red, 'times', 100)
    # Refresh game screen
    pygame.display.flip()
    time.sleep(1)

    return 1

def end():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
#交給負責人修改
def show_score(color, font, size):
    score_a_font= pygame.font.SysFont(font, size)
    score_b_font= pygame.font.SysFont(font, size)
    time_font=pygame.font.SysFont(font, size)
    score_a_surface = score_a_font.render('Score_red:' + str(score_a), True, color)
    score_b_surface = score_b_font.render('Score_blue:' + str(score_b), True, color)
    time_surface = time_font.render(str(time_count), True, color)
    score_a_rect = score_a_surface.get_rect()
    score_a_rect.midtop = (frame_size_x/10*1.5,15)
    score_b_rect = score_b_surface.get_rect()
    score_b_rect.midtop = (frame_size_x/10*8, 15)
    time_rect = time_surface.get_rect()
    time_rect.midtop = (frame_size_x/10*5, 15)
    game_window.blit(score_a_surface, score_a_rect)
    game_window.blit(score_b_surface, score_b_rect)
    game_window.blit(time_surface, time_rect)

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
        #時間限制(time_count==180(秒
        elif event.type == time_limit:
            time_count+=1
            if time_count==180:
                over=True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

# 決定chang_to的方向
# 道具a_upposite_direction的功用在這裡。
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

            
                
#前面設置的計時器。時間到了狀態就變為False，即該項狀態變為沒有。
                
        elif event.type ==tool_trigger_a:             
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
            
        elif event.type ==tool_trigger_b:             
            if upposite_direction_control_b>0:
                upposite_direction_control_b-=1
            else:
                b_upposite_direction=False
            if speed_up_control_b>0:
                speed_up_control_b-=1
            else:
                b_speed_up=False
            if score_up_control_b>0:
                score_up_control_b-=1
            else:
                b_score_up=False
            if fixed_direction_control_b>0:
                fixed_direction_control_b-=1
            else:
                b_fixed_direction=False

#cool_down的計時器。時間(5秒)到了，狀態就變為False，意即蛇撞到時就會受到分數和長度減半的懲罰

        elif event.type ==cool_down_a:
            a_cool_down=False
            pygame.time.set_timer(cool_down_a,0)
    
        elif event.type ==cool_down_b:
            b_cool_down=False
            pygame.time.set_timer(cool_down_b,0)
        

#決定 direcion
#避免snake突然往相反方向前進，但一單位(len(snake_body_a)==不受此限，因為不合理
#道具fixed dirction的功用在這裡，基本上就是讓change_to跟著direction走。
            
    #snake_a
    if a_fixed_direction:
        change_to_a=direction_a
    
    elif len(snake_body_a)==1:
        if change_to_a== 'UP':
            direction_a= 'UP'
        if change_to_a== 'DOWN': 
            direction_a= 'DOWN'
        if change_to_a== 'LEFT':
            direction_a= 'LEFT'
        if change_to_a== 'RIGHT': 
            direction_a= 'RIGHT'
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

#道具speed_up。move_time_time_a指的是snake a moving logic得施行次數。也就是說如果處於speed_up 狀態下的話，等於是在相同時間(1/10秒)裡作了兩次的位移,即兩倍速
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
        
# snake a moving logic，只對snake_a寫註解，因為snake_b格式也一樣
    #snake_a
    #產生一個新的snake_head_a
    for i in range(move_time_a):
        if direction_a=='UP':
            snake_head_a[1] -= 10 
        if direction_a== 'DOWN':
            snake_head_a[1] += 10
        if direction_a== 'LEFT':
            snake_head_a[0] -= 10
        if direction_a== 'RIGHT':
            snake_head_a[0] += 10
        
        #doom代表snake_head處在一個不能被規則接受的座標，包括邊界外，snake_body_a自己以外的任一座標，和snake_body_b的任一座標
        doom_a=False
        if snake_head_a[0] < 0 or snake_head_a[0] > frame_size_x-10 or snake_head_a[1] < 0 or snake_head_a[1] > frame_size_y-10 or snake_head_a in snake_body_a[1:] or snake_head_a in snake_body_b:
            doom_a=True
    
        #doom的應對方式
        if doom_a:
            if a_cool_down:
                snake_return("a")
            elif not a_cool_down:
                score_a=score_a//2
                snake_halfed("a")
                snake_return("a")
                a_cool_down=True
                pygame.time.set_timer(cool_down_a,5000)

        #正常的移動方式
        elif not doom_a: 
            snake_body_a.insert(0, list(snake_head_a))
            if snake_head_a[0] == food_pos[0] and snake_head_a[1] == food_pos[1]:
                score_a+=score("a")
                food_spawn = False
            elif len(snake_body_a)>1:
                snake_body_a.pop()
            else:
                snake_body_a=[snake_head_a]
    
    #碰到道具的時候，註解只寫第一項，因為格式都一樣
        if snake_head_a in tool_upposite_direction:
            upposite_direction_control_b+=5                 
            tool_upposite_direction.remove(snake_head_a)    
            b_upposite_direction=True                       
        if snake_head_a in tool_speed_up:
            speed_up_control_a+=10
            tool_speed_up.remove(snake_head_a)
            a_speed_up=True
        if snake_head_a in tool_score_up:
            score_up_control_a+=30
            tool_score_up.remove(snake_head_a)
            a_score_up=True
        if snake_head_a in tool_fixed_direction:
            fixed_direction_control_b+=2
            tool_fixed_direction.remove(snake_head_a)
            b_fixed_direction=True

        # snake b
    for i in range(move_time_b):
        if direction_b=='UP':
            snake_head_b[1] -= 10 
        if direction_b== 'DOWN':
            snake_head_b[1] += 10
        if direction_b== 'LEFT':
            snake_head_b[0] -= 10
        if direction_b== 'RIGHT':
            snake_head_b[0] += 10
        doom_b=False
        if snake_head_b[0] < 0 or snake_head_b[0] > frame_size_x-10 or snake_head_b[1] < 0 or snake_head_b[1] > frame_size_y-10 or snake_head_b in snake_body_b[1:] or snake_head_b in snake_body_a:
            doom_b=True
        if doom_b:
            if b_cool_down:
                snake_return("b")
            elif not b_cool_down:
                score_b=score_b//2
                snake_halfed("b")
                snake_return("b")
                b_cool_down=True
                pygame.time.set_timer(cool_down_b,5000)
        elif not doom_b: 
            snake_body_b.insert(0, list(snake_head_b))
            if snake_head_b[0] == food_pos[0] and snake_head_b[1] == food_pos[1]:
                score_b+=score("b")
                food_spawn = False
            elif len(snake_body_b)>1:
                snake_body_b.pop()
            else:
                snake_body_b=[snake_head_b]
        if snake_head_b in tool_upposite_direction:
            upposite_direction_control_a+=5
            tool_upposite_direction.remove(snake_head_b)
            a_upposite_direction=True
        if snake_head_b in tool_speed_up:
            speed_up_control_b+=10
            tool_speed_up.remove(snake_head_b)
            b_speed_up=True
        if snake_head_b in tool_score_up:
            score_up_control_b+=30
            tool_score_up.remove(snake_head_b)
            b_score_up=True
        if snake_head_b in tool_fixed_direction:
            fixed_direction_control_a+=2
            tool_fixed_direction.remove(snake_head_b)
            a_fixed_direction=True
        
# Spawning food and tool on the screen
    #負責人修改
    if not food_spawn:
        food_x = random.randrange(1, (frame_size_x//10)) * 10
        food_y = random.randrange(1, (frame_size_y//10)) * 10
        food_pos = [food_x, food_y]
    food_spawn = True

    #道具再生,場上永遠有兩個道具
    while len(tool_upposite_direction)+len(tool_speed_up)+len(tool_score_up)+len(tool_fixed_direction)<2:
        tool_spawn()

    
# Display
    game_window.fill(black)

    # Draw Snake
    #負責人修改
    for pos in snake_body_a:
        pygame.draw.rect(game_window, red, pygame.Rect(pos[0], pos[1], 10, 10))
        
    for pos in snake_body_b:
        pygame.draw.rect(game_window,blue, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    #負責人修改
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Draw tool
    #先以方塊顏色區分，負責人修改
    for tool in tool_upposite_direction:
        pygame.draw.rect(game_window, purple, pygame.Rect(tool[0], tool[1], 10, 10))
    for tool in tool_speed_up:
        pygame.draw.rect(game_window, yellow, pygame.Rect(tool[0], tool[1], 10, 10))
    for tool in tool_score_up:
        pygame.draw.rect(game_window, green, pygame.Rect(tool[0], tool[1], 10, 10))
    for tool in tool_fixed_direction:
        pygame.draw.rect(game_window, pink, pygame.Rect(tool[0], tool[1], 10, 10))


    
    #負責人修改
    if over:
        over = game_over()
        end()
    
    if not over:
        show_score( white, 'consolas', 25)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        pygame.time.Clock().tick(10)
