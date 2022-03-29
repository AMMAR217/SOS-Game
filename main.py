# "__SOS"
valid_entires = ["S","O"]
board = [

    ["__","__","__","__"]
    ,["__","__","__","__"]
    ,["__","__","__","__"]
    ,["__","__","__","__"]
]
def check_horizon():
     for row in board :
         x ="".join(i for i in row)
         if "SOS" in x :
             return True
def check_vertical():
    temp =[]
    for col in range (4):
        for row in range (4):
            temp.append(board[row][col])
        x ="".join(i for i in temp) 
        if "SOS" in x :
            return True  
        else :
            temp =[]     
def check_diagonally():
    try :
        if board[0][0] +board[1][1]+board[2][2] == "SOS":
             return True
        if board[3][3] +board[2][2]+board[1][1] == "SOS":
            return True        
        if board[0][3] +board[1][2]+board[2][1] == "SOS":
            return True        
        
        if board[3][0] +board[2][1]+board[1][2] == "SOS":
            return True        
    except BaseException:
        
        pass

def check_draw():
    for row in board:
        for col in row :
            if col == "__":
                 return False
    return True 



# def check_horizontally():
#     i = 0 
#     sum = ""
#     for row in board  :
#         while i <=3 :
#             for col in row  :
                
#                 sum += str(col)
#                 i +=1
#             if sum == "SOS" :
#                 return True
#             else : i = 0
    
# check_horizontally()

def coordinates():
    while True :
        row = int(input("Enter the row : "))
        col = int(input("Enter the col : "))
        row -=1
        col -=1
        if row in range (0,5) and col in range (0,5) and board[row][col] == "__" :
            break 
        print("make sure you enterd available coordinates")
    return row,col
def game_board():
    for row in board :
        print("  ".join(row))
game_board()
def main ():
    while True :
        def player1_turn():
            print("player1 : ")
            row,col =coordinates()
            while True :
                x= input("Enter either O or S :")
                if x.title() in valid_entires :
                    break
                print("make sure you enterd S or O")
            board[row][col] = x.upper()
            pass 
        player1_turn()
        
        game_board()
        if check_horizon() == True or check_vertical == True or check_diagonally() == True:
             print("player 1 wins")
             break 
        if check_draw()== True :
            print("The GAME DRAW")
            break
        def player2_turn():
            print("player2 : ")
            row,col =coordinates()
            while True :
                x= input("Enter either O or S :")
                if x.title() in valid_entires :
                    break 
                print("make sure you enterd S or O")
            board[row][col] = x.upper()
            pass 
        player2_turn()
        game_board()

        if check_horizon() == True or check_vertical == True  or check_diagonally()== True:
             print("player 2 wins")
             break 
        if check_draw()== True :
            print("The GAME DRAW")
            break

main()