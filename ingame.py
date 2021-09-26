import numpy as np
import pygame
def create_board():
    board=np.zeros((6,7))
    return board

def horizontal(board,p):
    for i in range(6):
        check=0
        for j in range(7):
            if(board[i][j]==p):
                check+=1
                if check==4:
                    return True
            else:
                check=0
    return False

def vertical(board,p):
    for i in range(7):
        check=0
        for j in range(6):
            if(board[j][i]==p):
                check+=1
                if check==4:
                    return True
            else:
                check=0
    return False

def daigonal_right(board,p):
    for j in range(6):
        check=0
        same=j
        for x in range(5,-1,-1):
            j=same
            for i in range(x,-1,-1):
                if j>6:
                    continue
                if(board[i][j]==p):
                    check+=1
                    if check==4:
                            return True
                    else:
                        check=0
                    j+=1
    return False

def daigonal_left(board,p):
    for j in range(6,-1,-1):
        check=0
        same=j
        for x in range(5,-1,-1):
            j=same
            for i in range(x,-1,-1):
                if j<0:
                    continue
                if(board[i][j]==p):
                        check+=1
                        if check==4:
                            return True
                else:
                    check=0
                j-=1
    return False

def win(board,p):
    
    if horizontal(board,p):
        return True
    if vertical(board,p):
        return True
    if daigonal_right(board,p):
        return True
    if daigonal_left(board,p):
        return True

    return False

def game(board):
    for i in range(7):
        for j in range(7):
            if i == 0:
                continue
            pygame.draw.rect(surface, blue, pygame.Rect(j*square,i*(square) , square, square))
            pygame.draw.circle(surface, black, (j*square+50,i*(square)+50),45)
    


##############################################################################
blue = (0,0,255)
black = (0,0,0)
red = (255,0,0)
yellow= (255,255,0)
color=''
pygame.init()
surface = pygame.display.set_mode((700,700))
square=100
  

continue_game = True

board = create_board()

print(board)
game(board)
pygame.display.update()

#############################################################################
turn=1
player_1_turn= True
player_2_turn= False
while continue_game:
    
   
    for event in pygame.event.get():
      
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            turn+=1
            if turn%2==1:
                player_2_turn= True
                
            else:
                player_1_turn= True
            line=5
            while player_1_turn:
                pos=event.pos[0]/100
                column=int(pos)
                if(line < 0):
                    print("player1 that line is full: ")
                    line = 5
            
                elif (board[line][column]!= 0):
                    line -= 1
                else:
                    board[line][column] = 1
                    pygame.draw.circle(surface, red, (column*square+50,((line+1)*square)+50),45)
                    pygame.display.update()
                    line=5
                    player_1_turn= False

                if (win(board,1)):
                    print("Player 1 Won the game")
                    print(board)
                    continue_game = False
                    break

            line=5
            while player_2_turn:
                pos=event.pos[0]/100
                column=int(pos)
                if(line < 0):
                    print("player1 that line is full: ")
                    line = 5
            
                elif (board[line][column]!= 0):
                    line -= 1
                else:
                    board[line][column] = 2
                    pygame.draw.circle(surface, yellow, (column*square+50,((line+1)*square)+50),45)
                    pygame.display.update()
                    line=5
                    player_2_turn= False

                if (win(board,2)):
                    print("Player 2 Won the game")
                    print(board)
                    continue_game = False
                    break



                
          
