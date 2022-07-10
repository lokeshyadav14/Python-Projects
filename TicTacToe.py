#Tic Tac Toe, is a two player paper and pencil game

import random

class tic_tac_toe :
    def __init__(self) :
        self.board = [" " for _ in range(0, 9)]
        self.p_moves = 0
        print("<<< Enter no. to place your 'X' >>>")
        for i in range(1, 8, 3) :
            if i != 1 :
                print("  -----------------------")
            print("         |       |       ")
            print("     " + str(i) + "   |   " + str(i+1) + "   |   " + str(i+2) + " ")
            print("         |       |       ")

    #------------------ Methods ----------------------------------
    def play(self) :
        play_next_move = True
        while play_next_move :
            play_next_move = self.player_move()
            if play_next_move :    
                play_next_move = self.computer_move()
    

    #--------------player move----------------------------------
    def player_move(self) :
        print("\n.....Player move.....")
        while True:
            try :
                move = int(input("Enter 1-9 : "))
                if self.board[move-1] == ' ' :
                    self.board[move-1] = 'X'
                    self.display_board()
                    if self.is_winner('X') :
                        print("(^_^) Player X Wins the game!!!")
                        return False
                    else :
                        if self.is_board_full() :
                            print("- Game is tie!!!")
                            return False
                        else :
                            self.p_moves += 1
                            return True
                else :
                    print("Place is already accupied, please select another place.")
            except ValueError :
                print("Please enter valid number...")


    #------------- AI based moves of computer------------------
    def computer_move(self) :
        print("\n.....Computer move.....")
        move = -1
        position_O = self.is_winning('O')
        position_X = self.is_winning('X')
        #computer can win or not in this move(attacking)
        if position_O > -1 :
            move = position_O
        #player can win or not in next move(defending)
        elif position_X > -1 :
            move = position_X
        else :
            #if player moves captures two corners then take a side
            if self.p_moves == 2 and ((self.board[0] == 'X') + (self.board[2] == 'X') + (self.board[6] == 'X') + (self.board[8] == 'X')) == 2 :
                move = random.choice([1, 3, 5, 7])
            #first go for center then corners and then sides
            elif self.board[4] == ' ' :
                move = 4                
            else :
                valid_corners = []
                valid_sides = []

                for i in range(0, 9) :
                    if i == 4 :
                        continue
                    if i%2 == 0 :
                        if self.board[i] == ' ':
                            valid_corners.append(i)
                    else :
                        if self.board[i] == ' ' :
                            valid_sides.append(i)

                if len(valid_corners) > 0 :
                    move = random.choice(valid_corners)
                else :
                    move = random.choice(valid_sides)

        self.board[move] = 'O'
        self.display_board()
        if self.is_winner('O') :
            print("[-_-] Computer Wins the game!!!")
            return False
        else :
            if self.is_board_full() :
                print("- Game is tie!!!")
                return False
            else :
                return True


    #------------------Helping methods-------------------------
    def display_board(self) :
        for i in range(0, 7, 3) :
            if i != 0 :
                print("  -----------------------")
            print("         |       |       ")
            print("     " + self.board[i+0] + "   |   " + self.board[i+1] + "   |   " + self.board[i+2] + " ")
            print("         |       |       ")

    def is_winner(self, p) :
        # for row positions
        for i in range(0, 7, 3) :
            if (self.board[i+0]==p and self.board[i+1]==p and self.board[i+2]==p) :
                return True
        # for column position
        for i in range(0, 3, 1) :
            if (self.board[i+0]==p and self.board[i+3]==p and self.board[i+6]==p) :
                return True        
        # for diagonal position
        if (self.board[0]==p and self.board[4]==p and self.board[8]==p) or (self.board[2]==p and self.board[4]==p and self.board[6]==p) :
            return True
        return False    

    def is_board_full(self) :
        for i in self.board :
            if i == ' ' :
                return False
        return True 

    #it returns the index of vacant place if player is winning else returns -1
    def is_winning(self, player) :
        #for all three rows
        for i in range(0, 7, 3) :
            if ((self.board[i]==player) + (self.board[i+1]==player) + (self.board[i+2]==player)) == 2 :
                for j in range(0, 3) :
                    if self.board[i+j] == ' ':
                        return (i+j)
        #for all three columns
        for i in range(0, 3) :
            if ((self.board[i]==player) + (self.board[i+3]==player) + (self.board[i+6]==player)) == 2 :
                for j in range(0, 7, 3) :
                    if self.board[i+j] == ' ':
                        return (i+j)
        #for two diagonals
        if ((self.board[0]==player) + (self.board[4]==player) + (self.board[8]==player)) == 2 :
            for i in range(0, 9, 4) :
                if self.board[i] == ' ':
                    return i
        if ((self.board[2]==player) + (self.board[4]==player) + (self.board[6]==player)) == 2 :
            for i in range(2, 7, 2) :
                if self.board[i] == ' ':
                    return i
        #if the player is not winning
        return -1

#--------------------------Driver code-------------------------------------

print("Welcome to game ----- Tic Tac Toe -----")
while True :
    new_game = tic_tac_toe()
    new_game.play()
    if int(input("Enter 0 to exit or 1 to play again : ")) :
        continue
    break
        