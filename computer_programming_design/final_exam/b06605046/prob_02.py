# Problem 2. Location Calculator - locate() (20 pts)

def locate(origin, moves):
    # write your answer here
    # complete the function
    final_location=()#bulid a tuple
    x_pos=origin[0]
    y_pos=origin[1]
    for i in range(len(moves)):#seek the direction
        if moves[i]=='E' or moves[i]=='e':
            x_pos+=1
        elif moves[i]=='W' or moves[i]=='w':
            x_pos-=1
        elif moves[i]=='S' or moves[i]=='s':
            y_pos-=1
        elif moves[i]=='N' or moves[i]=='n':
            y_pos+=1
    final_location=(x_pos,y_pos)#store in the tuple
    return final_location

if __name__ == '__main__':
    origin = (1, -2)
    moves = 'eEEssWwWwwwnnnnneeenee'

    print(locate(origin, moves))
