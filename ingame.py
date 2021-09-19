import numpy as np

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
            print("board[{}][{}] is occupied".format(line,p1))
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
    line = 5
    while player_2_turn:
        
        if(line < 0):
            p2 = int(input("player2 that line is full: "))
            line = 5
            
        elif (board[line][p2]!= 0):
            print("board[{}][{}] is occupied".format(line,p2))
            line -= 1
        else:
            board[line][p2] = 2
            print("board[{}][{}] is added with 2".format(line,p2))
            player_2_turn = False
        if (win(board,2)):
            print("Player 2 Won the game")
            continue_game = False
            break
            
        
    print(board)

    
   

    
