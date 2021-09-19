import numpy as np
def create_board():
    board=np.zeros((6,7))
    return board

def win(board,p):
    #horizantal
    for i in range(6):
        check=0
        #print("horizontal board[{}]".format(i))
        for j in range(7):
            if(board[i][j]==p):
                check+=1
                #print("in horizontal check board[{}][{}] and check is {}".format(i,j,check))
                if check==4:
                    return True
            else:
                check=0
                
    #vertical
    for i in range(7):
        check=0
        #print("vertical board[{}]".format(i))
        for j in range(6):
            if(board[j][i]==p):
                check+=1
                #print("in vertical check board[{}][{}] and check is {}".format(j,i,check))
                
                if check==4:
                    return True
            else:
                check=0
    return False
            
            
        
    

continue_game = True

board = create_board()

print(board)



while continue_game:
    line = 5
    p1 = int(input("player1 pick a line: "))
    player_1_turn= True
    while player_1_turn:
        if(line < 0):
            p1 = int(input("player1 that line is full: "))
            line = 5
            
        elif (board[line][p1]!= 0):
            line -= 1
        else:
            board[line][p1] = 1
            player_1_turn= False

        if (win(board,1)):
            print("Player 1 Won the game")
            continue_game = False
            break
    if continue_game != True:
        print(board)
        break
       
        

    print(board)
    p2 = int(input("player2 pick a line: "))
    player_2_turn = True
    while player_2_turn:
        if(line < 0):
            p2 = int(input("player2 that line is full: "))
            line = 5
            
        elif (board[line][p2]!= 0):
            line -= 1
        else:
            board[line][p2] = 2
            player_2_turn= False
        if (win(board,2)):
            print("Player 2 Won the game")
            continue_game = False
            break
            
        
    print(board)

    
   

    
