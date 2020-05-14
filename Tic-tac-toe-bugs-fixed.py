#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output
clear_output()


def start():
    #variables for spaces
    list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    board = []
    v = []
    d1 = [15,70,80]
    d2 = [17,90,35]
    horizontals =[[list1[0],list1[1],list1[2]],
             [ list1[3],list1[4],list1[5]],
             [ list1[6],list1[7],list1[8]]]
    w = 0
    moves = []
    set_moves = set(moves)

    #test_board == horizontals

    import pprint
    def display_board(board):
        clear_output()
        #changing verticals 
        vCT = (f'  {list1[0]}  |  {list1[1]}  |  {list1[2]}  ')
        #verticals2ndrow
        vCM = (f'  {list1[3]}  |  {list1[4]}  |  {list1[5]}  ')
        #vericals3rd row
        vCB = (f'  {list1[6]}  |  {list1[7]}  |  {list1[8]}  ')
        #horizontals 
        h1 = ('_________________')
        #verticals
        v1 = ('     |     |     ')
        board = [v1, vCT, v1, h1,v1, vCM, v1, h1, v1, vCB, v1]
        pprint.pprint(board)
    def player_input():  
        inputP1 = input('player 1 please type X').upper()
        inputP2 = input('player 2 please type O').upper()
    
        while inputP1 != 'X':
            inputP1 = input('player 1 please type X').upper()    
    
        while inputP2 != 'O':
            inputP2 = input('player 2 please type O').upper()
        play = [inputP1, inputP2]
        return play
    def win_check():
        y = 0
        v = []
        d1 = [15,70,80]
        d2 = [17,90,35]
        horizontals =[[list1[0],list1[1],list1[2]],
                     [ list1[3],list1[4],list1[5]],
                     [ list1[6],list1[7],list1[8]]]
        while y in range(y, len(horizontals)):
            #vertical
            v.append([item[y] for item in horizontals])
            #diagonal
            d1[y] = horizontals[y][y]
            d2[y] = horizontals[y][-y-1]
            #horizontal check
            if len(set(horizontals[y])) == 1:
                return True 
                print('hello')
                #vertical check
            elif len(set(v[y])) == 1:
                return True
                print('hello')
            #diagonal check
            elif (y>0<len(horizontals)) and (len(set(d1)) == 1 or len(set(d2)) == 1):
                return True 
                print('hello')
            y+=1 
        return False
    
    def Pos():
        while True:
            try:
                User_Turn = int(input('Please enter number between 0 and 8'))
                if (type(User_Turn)) == int: 
                    return User_Turn

            except TypeError:
                print('this will  not work ')
                continue

            except ValueError:
                print('this will  not work ')
                continue 


            else:
                print('you got your answer mate')
                break

    while win_check() == True:
        break
    while win_check() == False: 
        display_board(board)
        user = player_input()
        print(user)
        while w < (len(list1)+1):
            Posi = Pos()
            if (0 <= Posi <= 8):
                moves.append(Posi)
                set_moves = set(moves)
            elif Posi not in range(0,8):
                print('you are out of range MATE')
                continue
            if (w%2 ==0) and (len(moves) == len(set_moves)):
                list1[Posi] = user[0]
            elif (w%2 !=0) and (len(moves) == len(set_moves)):
                list1[Posi] = user[1]
            else:
                w -=1 
                moves.pop()
                print('please choose another move')
   
            
            win_check()
            display_board(board) 
            if (w == 8) and (win_check () != True):
                list1[0] = w
                list1[3] = w
                list1[6] = w
                print('This is a TIE')
                print(win_check(),'third')
                break 
            elif (w< len(list1)) and win_check () == True and (w%2 ==0):
                print('User X wins')
                break
            elif (w< len(list1)) and win_check () == True and (w%2 !=0):
                print('User O wins')
                break
            w +=1  


# In[ ]:


def replay ():
    while 1 > 0:
        ans = input('Would you like to play again ? Type Y for Yes and  any other button for No')
        if ans.upper() == 'Y':
            start()
        else:
            print ('Too bad you were really good!')
            break


# In[ ]:


def game ():
    start()
    replay()


# In[ ]:


game ()

