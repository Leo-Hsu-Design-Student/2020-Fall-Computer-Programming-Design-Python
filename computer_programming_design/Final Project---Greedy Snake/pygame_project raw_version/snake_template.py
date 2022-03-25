"""
Snake Game
Made with PyGame
"""

import pygame, sys, time, random


# Initialize pygame and check for errors encountered
check_errors = pygame.init()

if check_errors[1] > 0:
    print('Had {} errors when initialising game, exiting...'.format(check_errors[1]))
    sys.exit(-1)


# your comment here
"""上述預防錯誤的方法，check_errors[1]>0這是在pygame無法成功執行的狀況下，pygame.init是一個tuple，
[0]代表有幾個成功被初始化的模組，[1]代表有幾個失敗的，可以print(check_errors)查看。
在上課時聽到老師說tuple不能被修改，推想這個計算成功與失敗的初始化模組應該是算完才丟到tuple裡的。
sys.exit(-1)是終止程式並且回傳-1。

以下在設定畫面的大小以及title，我認為變數定義的很清楚，比起上次我用x,y命名還好。
"""
frame_size_x = 720
frame_size_y = 640
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption('Snake')


# Game variables
# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

snake_head = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_x = random.randrange(1, (frame_size_x//10)) * 10
food_y = random.randrange(1, (frame_size_y//10)) * 10
food_pos = [food_x, food_y]
food_spawn = True

change_to = direction = 'RIGHT'

score = 0
over = 0


def game_over():
    """
    your comment here
    定義遊戲終止時的字幕，並且定義字型、大小，透過render這個function標明字串、顏色
    並將兩個字串放在方格內，定義midtop屬性的位置，並且把背景填滿黑色，最後則是將兩個字串的方塊繪製在背景上
    並且運用函數將分數呈現出來
    """
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

    show_score(0, red, 'times', 100)
    # Refresh game screen
    pygame.display.flip()
    time.sleep(1)

    return 1 


def end():
    """
    your comment here
    按下視窗的x可以離開遊戲，若是按下ESC也可以離開遊戲。
    終止的方式是sys.exit()
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    

def show_score(choice, color, font, size):
    """
    your comment here
    呈現分數的函數，輸入分數、顏色、字體、大小，可以得到文字的方塊，
    定義midtop屬性（位置）並且覆蓋在背景上
    """
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)


# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:

            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'

            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))


    # your comment here
    """第一次寫作業時，我直接在pygame.K_UP寫移動的狀況，但這樣會有問題是每壓一次只會動一格，而不是改變方向
    後來就寫成direction，但助教這邊又多一個change_to，這樣多寫一個可以防止方向往上時直接掉頭走
    """
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    
    # your comment here
    """方向移動只改變頭的值，我在猜想後續應該有寫說頭跟身體的關係"""
    if direction == 'UP':
        snake_head[1] -= 10
    if direction == 'DOWN':
        snake_head[1] += 10
    if direction == 'LEFT':
        snake_head[0] -= 10
    if direction == 'RIGHT':
        snake_head[0] += 10


    # your comment here
    """果然這邊有講身體跟頭的關係，insert(0,list())是說在index0的地方插入頭的值，如果撞到食物，則得一分，且改變食物產生的狀態，
    下面應該會提到，若是沒碰到食物，就pop()最後一個數值，身體就開始前進了"""
    snake_body.insert(0, list(snake_head))
    if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()


    # Spawning food on the screen
    """如果food_spawn是False則執行if的內容，隨機產生一個食物位置，並且改成True"""
    if not food_spawn:
        food_x = random.randrange(1, (frame_size_x//10)) * 10
        food_y = random.randrange(1, (frame_size_y//10)) * 10
        food_pos = [food_x, food_y]
    food_spawn = True


    # Display
    game_window.fill(black)

    # Draw Snake
    for pos in snake_body:
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))


    # your comment here
    """If snake_head were out of the bounds, then it terminates itself.
    if敘述中的 or第二項，是說若是蛇的右邊與下面超出介面一點點也是終止（因為位址只能呈現左邊、上面）
     """
    if snake_head[0] < 0 or snake_head[0] > frame_size_x-10:
        over = game_over()
        end()
    if snake_head[1] < 0 or snake_head[1] > frame_size_y-10:
        over = game_over()
        end()
    # your comment here
    """若蛇的頭碰到身體，則遊戲也結束，若是有兩條蛇一起就要寫兩個for loop"""
    for block in snake_body[1:]:
        if snake_head[0] == block[0] and snake_head[1] == block[1]:
            over = game_over()
            end()


    if not over:
        show_score(1, white, 'consolas', 10)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        pygame.time.Clock().tick(10)
