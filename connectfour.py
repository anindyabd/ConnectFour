########################
##       Graphics     ##
########################

import turtle

def setup_screen(w,h):
    '''This sets up the turtle screen'''
    turtle.setup(width = w*100, height = h*100)
    turtle.setworldcoordinates(0,0,w,h)
    turtle.speed('fastest')

def draw_board():
    '''Draws the board for Connect Four'''
    turtle.hideturtle()
    for i in range(6):
        turtle.penup()
        turtle.goto(0,i)
        turtle.setheading(0)
        turtle.pendown()
        turtle.forward(7)
    for i in range(7):
        turtle.penup()
        turtle.goto(i,0)
        turtle.setheading(90)
        turtle.pendown()
        turtle.forward(6)
    turtle.penup()
    
def draw_circle(x,y):
    '''Draws a circle for player 'o'.'''
    turtle.hideturtle()
    turtle.pencolor('blue')
    turtle.goto(x-0.25, y-0.5)
    turtle.pendown()
    turtle.circle(0.25)
    turtle.penup()

def draw_xmark(x,y):
    '''Draws an x for player 'x'.'''
    turtle.hideturtle()
    turtle.pencolor('red')
    turtle.goto(x - 0.75, y - 0.75)
    turtle.pendown()
    turtle.setheading(45)
    turtle.forward(0.72)
    turtle.penup()
    turtle.goto(x - 0.25, y - 0.75)
    turtle.pendown()
    turtle.setheading(135)
    turtle.forward(0.72)
    turtle.setheading(90)
    turtle.penup()

def setup():
    '''This sets up the screen and draws the board for Connect Four'''
    setup_screen(7,6)
    draw_board()

##############
## Gameplay ##
##############

def yes_no():
    '''This function asks for confirmation from the user about quitting the game after the user types 'done' '''
    res = raw_input('Are you sure (Y/N)? ')
    if res.lower() not in ['y','n','yes','no']:
        print('You must choose Yes or No (Y/N)')
        return yes_no()
    
    return res.lower()

def take_input():
    '''This function asks the user which column to play in.'''

    try:
        col = raw_input('Enter the column where you want to play \
(or type "done" to close the game): ')
                    
        # Allow the player to end the game or not
        if col.lower() == 'done':
            res = yes_no()
            if res == 'y' or res == 'yes':
                col = 'done'
            if res == 'n' or res == 'no':
                return take_input()
                
        # The input must be between 1 and 7
        elif int(col) not in range(1,8):
            print('You must enter a number between 1 and 7')
            return take_input()
    
    except ValueError:
        print('You must enter a number between 1 and 7')
        return take_input()

    return col
    

def enter_move(player, col, recent_move, board):
    '''The function makes the move that the player wants to make on the turtle screen, and updates the game board.'''
    global win

    col = int(col)
    
    if max(column_rec[col]) >= 6:
        print('You must choose another column...')
        col = take_input()
        return enter_move(player, col, recent_move, board)

        
    column_rec[col] = column_rec.setdefault(col,[0]) + [max(column_rec[col])+1]
    
    board[(col, max(column_rec[col]))] = player

    if player == 'o': 
        draw_circle(col, max(column_rec[col]))
    if player == 'x':
        draw_xmark(col, max(column_rec[col]))

    recent_move = [col, max(column_rec[col])]
    win = find_winner(player, recent_move, board)


def compenter_move(player, col, recent_move, board):
    '''The function makes the move that the computer wants to make on the turtle screen, and updates the game board.'''

    global win

    column_rec[col] = column_rec.setdefault(col,[0]) + [max(column_rec[col])+1]


    board[(col, max(column_rec[col]))] = player

    if player == 'o': 
        draw_circle(col, max(column_rec[col]))
    if player == 'x':
        draw_xmark(col, max(column_rec[col]))

    recent_move = [col, max(column_rec[col])]
    win = find_winner(player, recent_move, board)


def find_winner(player, recent_move, board):
    '''The function looks at the game board and the most recent move made. If it finds four pieces in a row for the same player, it declares that player as the winner.'''

    c = recent_move[0]
    r = recent_move[1]

    for i in range(0,-4,-1):
        count = 0
        for j in range(4):
            if board.get((c, r+i+j)) == player: # Win by column
                count += 1
        if count == 4:
            print('We have a winner!', player, 'wins!')
            return True

    for i in range(0,-4,-1):
        count = 0
        for j in range(4):
            if board.get((c+i+j, r)) == player: # Win by row
                count += 1
        if count == 4:
            print('We have a winner!', player, 'wins!')
            return True

    for i in range(0,-4,-1):
        count = 0
        for j in range(4):
            if board.get((c+i+j, r+i+j)) == player: # Win by diagonal up
                count += 1
        if count == 4:
            print('We have a winner!', player, 'wins!')
            return True

    for i in range(0,-4,-1):
        count = 0
        for j in range(4):
            if board.get((c+i+j, r-i-j)) == player: # Win by diagonal down
                count += 1
        if count == 4:
            print('We have a winner!', player, 'wins!')
            return True

    return False

###############
###Simulation##
###############

import random

def firstmodenter_move(player, simrecent_move, simboard, simmove):
    '''The function takes one more argument than modenter_move, simmove, and simulates that move. This is done to keep track of the first move made.'''
    global simwin
    col = simmove

    while max(simcolumn_rec[col]) > 6:
        break

    simcolumn_rec[col] = simcolumn_rec.setdefault(col, [0]) + [max(simcolumn_rec[col])+1] # updates each column by going to the column and finding the max amount of pieces in it and then added a new value that is the max added to one

    simboard[(col, max(simcolumn_rec[col]))] = player


    simrecent_move = [col, max(simcolumn_rec[col])]
    simwin = simfind_winner(player, simrecent_move, simboard)

def modenter_move(player, simrecent_move, simboard):
    '''This function simulates entering moves on the board'''
    global simwin
    
    col = random.randint(1, 7)


    while max(simcolumn_rec[col]) >= 6:
        col = random.randint(1, 7)

    simcolumn_rec[col] = simcolumn_rec.setdefault(col, [0]) + [max(simcolumn_rec[col])+1] # updates each column by going to the column and finding the max amount of pieces in it and then added a new value that is the max added to one

    simboard[(col, max(simcolumn_rec[col]))] = player

    simrecent_move = [col, max(simcolumn_rec[col])]
    simwin = simfind_winner(player, simrecent_move, simboard)

def simfind_winner(player, recent_move, board):
    '''This function finds a winner from the simulations.'''

    c = recent_move[0]
    r = recent_move[1]

    for i in range(0,-4,-1):
        count = 0
        for j in range(4):
            if board.get((c, r+i+j)) == player: # Win by column
                count += 1
        if count == 4:
            return True

    for i in range(0,-4,-1):
        count = 0
        for j in range(4):
            if board.get((c+i+j, r)) == player: # Win by row
                count += 1
        if count == 4:
            return True

    for i in range(0,-4,-1):
        count = 0
        for j in range(4):
            if board.get((c+i+j, r+i+j)) == player: # Win by diagonal up
                count += 1
        if count == 4:
            return True

    for i in range(0,-4,-1):
        count = 0
        for j in range(4):
            if board.get((c+i+j, r-i-j)) == player: # Win by diagonal down
                count += 1
        if count == 4:
            return True

    return False

def bestmove(d, availmoves):
    '''The function takes a dictionary and a list of available moves as arguments. The dictionary, from the simuation function, has columns as keys, and lists of wins, ties and losses as values. This function finds the column that has the best ratio of wins over losses, and returns that column.'''
    best = 0
    winsovertotal = []
    wlist = list()                                          #list of wins
    tlist = list()                                          #list of ties
    llist = list()                                          #list of losses
    for k in range(1,len(d) + 1):                           #creates the list of wins, ties, and losses from dictionary
        wlist.append(d[k][0])
        tlist.append(d[k][1])
        llist.append(d[k][2])
    try:
        for i in range(0, len(d)):
            winsovertotal.append(float(wlist[i])/(wlist[i] + tlist[i] + llist[i]))
        if winsovertotal.count(max(winsovertotal)) > 1:
            clist = list()
            for i in range(len(winsovertotal)):
                if winsovertotal[i] == max(winsovertotal):
                    clist.append(i)
            return random.choice(clist) + 1
        return winsovertotal.index(max(winsovertotal)) + 1
    except ZeroDivisionError:
        return random.choice(availmoves)
                    
def copycat(mastercopy):
    '''The function makes copies of any variable.'''
    copydict = {}
    copylist = []
    copystring = ''
    copyint = 0
    if type(mastercopy) == dict:
        for k in mastercopy:
            copydict[k] = mastercopy[k]
        return copydict
    elif type(mastercopy) == list:
        for i in mastercopy:
            copylist.append(i)
        return copylist
    elif type(mastercopy) == str:
        for ch in mastercopy:
            copystring += ch
        return copystring
    elif type(mastercopy) == int:
        for i in range(mastercopy):
            copyint += 1
        return copyint
    elif type(mastercopy) == 'bool':
        if mastercopy == True:
            return True
        else:
            return False

    

def simulation(player, board, n):                                               
    '''The function takes current board and an integer n as arguments along with player. Each simulation proceeds by making random choices, out of the list of available columns, for each player until one player wins. A dictionary is made, containing columns as keys, and a list of wins, ties and losses for each column as values. Then the bestmove function is invoked to find out which column has best chance of winning,'''
    global simcolumn_rec
    global simwin
    moves = {1:[0,0,0], 2:[0,0,0], 3:[0,0,0], 4:[0,0,0],5:[0,0,0], 6:[0,0,0], 7:[0,0,0]}          #a dictionary where the keys are columns and the values are lists of length three with integers denoting wins, ties, and losses
    availmoves = list()                       #a list of available columns
    for col in range(1, 8):                 #run a check for columns 1 to 6
      
        if max(column_rec[col]) < 6:       #if the column is a key and the max value in the list paired with that key is less than 7, we can play in it.
            availmoves.append(col)
    for i in range(n):                          #performs n number of simulations
        simwin = copycat(win)
        simboard = copycat(board)
        simcolumn_rec = copycat(column_rec)
        simrecent_move = copycat(recent_move)
        simmove = random.choice(availmoves)         #choose our first move randomly from the list of available columns
        firstmodenter_move(player, simrecent_move, simboard, simmove)  #this is done to get the first move's column when computer player is o
        turn = 2
        while not simwin and len(simboard.keys()) != 42:             #runs the game until all spaces are filled or victory occurs
            if turn % 2 == 1:
                modenter_move('o', simrecent_move, simboard)
                turn += 1
            else:
                modenter_move('x', simrecent_move, simboard)
                turn += 1
        if simwin == True and turn % 2 == 0 and player == 'o':              #victory occured and we need to check if it was on computer's turn and what player computer is. The turn is reverse because the while loop will change turns before checking for victory. 
            moves[simmove][0] += 1
        elif simwin == True and turn % 2 == 1 and player == 'x':
            moves[simmove][0] += 1
        elif simwin == False and len(simboard.keys()) == 42:                   #conditions for a tie are no victories occurring and all spaces being filled up
            moves[simmove][1] += 1
        else:                                                              #conditions for a loss is when victories do not occur on our turn 
            moves[simmove][2] += 1
    return bestmove(moves, availmoves)                  #calls bestmove to analyze the dictionary of moves for the most winning column to choose

##################
##   Strategies   ##
##################


def block(player, board):
    '''The function simulates moves for the opponent, and checks whether the opponent wins by making a move in a certain column. If opponent does win by playing in a column, that column is returned, and the computer makes a move there, thus blocking the opponent.'''   
    newdict=copycat(column_rec)
    
    availcol = list()
    for col in range(1, 8):
        if max(newdict[col]) <= 6:     
            availcol.append(col)
    for col in availcol:
        newboard=copycat(board)
        newrecentmove=copycat(recent_move)
        newdict[col] = newdict.setdefault(col,[0]) + [max(newdict[col])+1]
        newboard[(col, max(newdict[col]))] = player
        newrecentmove=[col,max(newdict[col])]
        diffsimwin= simfind_winner(player, newrecentmove, newboard)
        if diffsimwin==True:
            return col
        newdict=copycat(column_rec)  
    return False

def forecast(player, board, col):
    '''The function simulates two moves, one by itself an another by the opponent, for each available column. If, when computer plays in a column, and the opponent wins by playing in that column again, the column in returned, and the computer does not play in that column unless it has no other choice.'''
    precolumn = copycat(column_rec)
    availcol = list()
    safecol = list()
    for col in range(1, 8):                    
        if max(precolumn[col]) <= 5:       #if the column is a key and the max value in the list paired with that key is less than 5 or less, we can play in it. We say 5 since this predicts if two moves are made in one column
            availcol.append(col)
    for col in availcol:
        if player == 'o':
            preboard = copycat(board)
            premove = copycat(recent_move)
            precolumn[col] = precolumn.setdefault(col,[0]) + [max(precolumn[col])+1]
            preboard[(col, max(precolumn[col]))] = player
            precolumn[col] = precolumn.setdefault(col,[0]) + [max(precolumn[col])+1]
            preboard[(col, max(precolumn[col]))] = 'x'
            premove = [col, max(precolumn[col])]
            prewin = find_winner(player, premove, preboard)
            if prewin == False:
                safecol.append(col)
            
            precolumn = copycat(column_rec)

        else:
            preboard = copycat(board)
            premove = copycat(recent_move)
            precolumn[col] = precolumn.setdefault(col,[0]) + [max(precolumn[col])+1]
            preboard[(col, max(precolumn[col]))] = player
            precolumn[col] = precolumn.setdefault(col,[0]) + [max(precolumn[col])+1]
            preboard[(col, max(precolumn[col]))] = 'o'
            premove = [col, max(precolumn[col])]
            prewin = find_winner(player, premove, preboard)
            if prewin == False:
                safecol.append(col)
            precolumn = copycat(column_rec)

    if safecol == availcol:
        return False
    elif len(safecol) == 0:      #if there are no safe places to play, just make a move
        return False
    elif not col in safecol:
        return True
    return False

def fourinarow(player, board):
    '''The computer simulates moves in all available columns, to see whether playing in that column causes a win (i.e. four pieces in a row for the computer). If it does, that column is returned. Then computer plays in that column.'''
    offcolumn = copycat(column_rec)
    availcol =[]
    for col in range(1, 8):                    
        if max(offcolumn[col]) <= 6:       #if the column is a key and the max value in the list paired with that key is less than 7, we can play in it.
            availcol.append(col)
    for col in availcol:
        offboard = copycat(board)
        offmove = copycat(recent_move)
        offcolumn[col] = offcolumn.setdefault(col,[0]) + [max(offcolumn[col])+1]
        offboard[(col, max(offcolumn[col]))] = player
        offmove = [col, max(offcolumn[col])]
        offwin = simfind_winner(player, offmove, offboard)
        if offwin == True:
            return col
        offcolumn = copycat(column_rec)
    return False
    

###############
###   Run   ###
###############

column_rec = {1:[0], 2:[0], 3:[0], 4:[0], 5:[0], 6:[0], 7:[0]}
board = dict()
recent_move = [0,0]
win = False
    
def main():
    '''Runs the whole program. It first asks the user whether or not user wants to play first, and then proceeds with the game. If a winner is found, or if there is a tie (the board is filled), the game stops.'''
    try:
        human = raw_input('Do you want to play first (Y/N)? ')
        print('')
        if human.lower() == 'y' or human.lower() == 'yes':
            turn = 0
        elif human.lower() == 'n' or human.lower() == 'no':
            turn = 1
        else:
            print('You must say Yes or No (Y/N)')
            return main()
    except ValueError:
        print('You must choose Yes or No (Y/N)')
        return main()

    setup()

    actual_turn = 1
    while not win and turn!=42:
        if turn % 2 == 1:
            print("Turn %s: This is the computer's turn ('o') ." % (actual_turn))

            if fourinarow('o', board)!= False: 
                col = fourinarow('o', board)
            elif block('x',board):
                col=block('x',board)

            else:
                col = simulation('o', board, 150)   
                while forecast('o', board, col):
                    col = simulation('o', board, 150)
            print("Computer plays in column", col)
            if col == 'done':
                break
            compenter_move('o', col, recent_move, board)
            print('')
            turn += 1
            actual_turn += 1
        
        else:
            print("Turn %s: This is the human player's turn ('x')." % (actual_turn))
            col =take_input()
            if col == 'done':
                break
            enter_move('x', col, recent_move, board)
            print('')
            turn += 1
            actual_turn += 1
    if turn==42:
        print("Game tied!")

        #for computer vs computer, the below else statement should be used instead of the above one
        '''else:
            print "This is player 'x' turn."                                             
            if fourinarow('x', board)!= False: 
                col = fourinarow('x', board)
                print 'fourinarow'
                
            elif block('o',board):
                col=block('o',board)
                print 'block'

            else:
                col = simulation('x', board, 200)
                while forecast('o', board, col):
                    col = simulation('o', board, 800)
            print "Computer plays in column", col
            compenter_move('x', col, recent_move, board)
            print ''
            turn += 1
            actual_turn += 1'''
   
if __name__ == '__main__':
    main()
