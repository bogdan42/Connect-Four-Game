from texttable import Texttable
from random import choice


class Board:

    def __init__(self):
        self._board = []
        for i in range(6):
            lst = []
            for j in range(7):
                lst.append(0)
            self._board.append(lst)


    def __str__(self):
        board = Texttable()

        for i in range(6):
            lst = []
            for j in range(7):
                if self._board[i][j] == 0:
                    lst.append(' ')
                if self._board[i][j] == 1:
                    lst.append('H')
                if self._board[i][j] == 2:
                    lst.append("C")
            board.add_row(lst)
        board.add_row(['a','b','c','d','e','f','g'])
        return  board.draw()

    def isColumn(self,column):
        '''
        Checks if column can describe a valid column
        on the board.
        Input: column(str)
        Output: 1 or 0
            - 1 if column can describe a valid column
            - 0 otherwise
        '''
        if column.lower() in 'abcdefg':
            return 1
        return 0

    def fromLetterToIndex(self,column):
        '''
        This function returns the index of the letter
        column from the a list. In case it is not in
        the list, the function will return -1
        '''
        list = ['a','b','c','d','e','f','g']
        for index in range(len(list)):
            if column.lower() == list[index]:
                return index
        return -1

    def isFree(self,column):
        '''
        This function checks if there is still possible
        to put at least one piece on the column.
        Input: column(int)
        Output: 1 if possible, 0 otherwise
        '''
        if self._board[0][column] == 0:
            return 1
        return 0

    def validatePlacement(self,column):
        '''
        This function validates a possible placement
        It checks if:
            o the column is valid
            o moves are still possible
            to make on that column
        '''

        if self.isColumn(column) == 0:
            return 0
        index = self.fromLetterToIndex(column)

        if self.isFree(index) == 0:
            return 0
        return 1

    def makeMove(self,column,symbol):
        '''
        This function will place a piece of type symb.
        on a given column. It returns the coordinates
        of the point where the movement has been made
        '''
        column = self.fromLetterToIndex(column)
        index = 5

        while index >= 0:
            if self._board[index][column] == 0:
                if symbol == 'C':
                    self._board[index][column] = 2
                    return index,column
                if symbol == 'H':
                    self._board[index][column] = 1
                    return index,column
            index -= 1

    def checkLine(self,x,y,symbol):
        '''
        This function checks if there is a strike of
        4 same symbols in a row on a line
        Function returns 1 if there is a strike of 4
        symbols in a row, 0 otherwise
        '''
        sum = 0
        for index in range(4):
            if y - index >= 0 and y - index + 4 <= 7:
               for j in range(y-index,y-index+4):
                   if symbol == 'C' and self._board[x][j] == 2:
                       sum += 1
                   if symbol == 'H' and self._board[x][j] == 1:
                        sum += 1
            if sum == 4:
                return 1
            else:
                sum = 0
        return 0

    def checkColumn(self,x,y,symbol):
        '''
        Checks if on a given column there is a strike of
        4 same symbols in a row.
        Function returns 1 if the condition is satisfied
        and 0 otherwise
        '''
        sum = 0
        for index in range(4):
            if x - index >= 0 and x - index + 4 <= 6:
                for i in range(x-index,x-index+4):
                   if symbol == 'C' and self._board[i][y] == 2:
                       sum += 1
                   if symbol == 'H' and self._board[i][y] == 1:
                        sum += 1
            if sum == 4:
                return 1
            else:
                sum = 0

        return 0

    def checkPrincDiagonal(self,x,y,symbol):
        '''
        Checks if there is a strike of 4 elements on the
        principal diagonal...
        If condition is satisfied the function returns 1
        and 0 otherwise
        '''
        sum = 0
        for index in range(4):
            if x - index >= 0 and x - index + 4 <= 6:
                if y - index  >= 0 and y - index + 4 <= 7:
                    i = x - index
                    j = y - index
                    while i < x - index + 4 and j < y - index + 4:
                        if symbol == 'C' and self._board[i][j] == 2:
                            sum += 1
                        if symbol == 'H' and self._board[i][j] == 1:
                            sum += 1
                        i += 1
                        j += 1
                if sum == 4:
                    return 1
                else:
                    sum = 0
        return 0


    def checkSecondDiagonal(self,x,y,symbol):
        '''
        Function that checks if ...
        Cond satisf. ==> 1 , 0 oth.
        '''
        sum  = 0
        for index in range(4):
            if x - index >= 0 and x - index + 4 <= 6:
                if y + index <= 6 and y + index - 3 >= 0:
                    i = x - index
                    j = y + index
                    while i < x - index + 4 and j >= y + index -4:
                        if symbol == 'C' and self._board[i][j] == 2:
                            sum += 1
                        if symbol == 'H' and self._board[i][j] == 1:
                            sum += 1
                        i += 1
                        j -= 1
                if sum == 4:
                    return 1
                else:
                    sum = 0


    def isWon(self,x,y,symbol):
        '''
        Function checks if the game is won
        Returns 1 if there is a strike of
        4 same symbols in a row on a line
        ,columnn or diagonal that contains
        the point x,y
        '''

        if self.checkLine(x,y,symbol) == 1:
            return 1
        elif self.checkColumn(x,y,symbol) == 1:
            return 1
        elif  self.checkPrincDiagonal(x,y,symbol) == 1:
            return 1
        elif self.checkSecondDiagonal(x,y,symbol) == 1:
            return 1
        elif self.checkSecondDiagonal(x,y,symbol) == 1:
            return 1
        return 0

    def randomMove(self):
        '''
        Make a random  move , random but VALID
        '''
        table = ['a','b','c','d','e','f','g']
        while True:
            move = choice(table)
            if self.validatePlacement(move) == 1:
                x,y = self.makeMove(move,'C')
                return x,y


    def blockOnLine(self,x,y,symbol,value):
        '''
        This function returns the first empty
        square from a line of 4 that has 3 same
        symbols
        '''
        sum = 0
        for index in range(4):
            if y - index >= 0 and y - index + 4 <= 7:
               for j in range(y-index,y-index+4):
                   if self._board[x][j] == 1 and symbol == 'H':
                        sum += 1
                   if self._board[x][j] == 2 and symbol == 'C':
                        sum += 1

            if sum == value:
                for j in range(y-index,y-index+4):
                    if self._board[x][j] == 0:
                        return x,j
            else:
                sum = 0
        return -1,-1

    def blockColumn(self,x,y,symbol,value):
        '''
        This function blocks a possible
        winning move for the human player.
        '''
        sum = 0
        for index in range(4):
            if x - index >= 0 and x - index + 4 <= 6:
                for i in range(x-index,x-index+4):
                   if self._board[i][y] == 1 and symbol == 'H':
                        sum += 1
                   if self._board[i][y] == 2 and symbol == 'C':
                        sum += 1
            if sum == value:
                for i in range(x-index,x-index+4):
                    if self._board[i][y] == 0:
                        return i,y
            else:
                sum = 0

        return -1,sum

    def blockPrincDiag(self,x,y,value,symbol):
        '''
        Function that checks if the computer
        can
        '''
        sum = 0
        for index in range(4):
            if x - index >= 0 and x - index + 4 <= 6:
                if y - index  >= 0 and y - index + 4 <= 7:
                    i = x - index
                    j = y - index
                    while i < x - index + 4 and j < y - index + 4:
                        if symbol == 'C' and self._board[i][j] == 2:
                            sum += 1
                        if symbol == 'H' and self._board[i][j] == 1:
                            sum += 1
                        i += 1
                        j += 1
                if sum == value:
                    i = x - index
                    j = y - index
                    while i < x - index + 4 and j < y - index + 4:
                        if self._board[i][j] == 0:
                            return i,j
                        i += 1
                        j += 1
                else:
                    sum = 0
        return -1,-1

    def blockSecDiag(self,x,y,symbol,value):
        sum  = 0
        for index in range(4):
            if x - index >= 0 and x - index + 4 <= 6:
                if y + index <= 6 and y + index - 3 >= 0:
                    i = x - index
                    j = y + index
                    while i < x - index + 4 and j >= y + index -4:
                        if symbol == 'C' and self._board[i][j] == 2:
                            sum += 1
                        if symbol == 'H' and self._board[i][j] == 1:
                            sum += 1
                        i += 1
                        j -= 1
                if sum == value:
                    i = x - index
                    j = y + index
                    while i < x - index + 4 and j >= y + index -4:
                        if self._board[i][j] == 0:
                            return i,j
                        i += 1
                        j -= 1
                else:
                    sum = 0
        return -1,-1

    def computerStrategy(self):
        '''
        This function will make the decission on
        how the computer should move.
        It firstly blocks all the moves of the
        human player which might lead to a win
        for the human player.
        If there is no such move, the computer
        tries to make a line of 4 by its pieces.
        '''
        table = ['a','b','c','d','e','f','g']
        for i in  range(6):
            for j in range(7):
                x,y = self.blockOnLine(i,j,'H',3)
                if x!= -1:
                    x,y = self.makeMove(table[y],'C')
                    return x,y
                x,y = self.blockColumn(i,j,'H',3)
                if x!=-1:
                    x,y = self.makeMove(table[y],'C')
                    return x,y
                x,y = self.blockPrincDiag(i,j,3,'H')
                if x!=-1:
                    x,y = self.makeMove(table[y],'C')
                    print('HAI CA INTRU PE IF')
                    return x,y
                x,y = self.blockSecDiag(i,j,'H',3)
                if x!=-1:
                    x,y = self.makeMove(table[y],'C')
                    return x,y

        for i in range(6):
            for j in range(7):
                x,y = self.blockOnLine(i,j,'C',3)
                if x!= -1:
                    x,y = self.makeMove(table[y],'C')
                    return x,y
                x,y = self.blockColumn(i,j,'C',3)
                if x!=-1:
                    x,y = self.makeMove(table[y],'C')
                    return x,y
                x,y = self.blockPrincDiag(i,j,3,'C')
                if x!=-1:
                    x,y = self.makeMove(table[y],'C')
                    print('HAI CA INTRU PE IF')
                    return x,y
                x,y = self.blockSecDiag(i,j,'C',3)
                if x!=-1:
                    x,y = self.makeMove(table[y],'C')
                    return x,y

        for i in range(6):
            for j in range(7):
                x,y = self.blockOnLine(i,j,'C',2)
                if x!= -1:
                    x,y = self.makeMove(table[y],'C')
                    return x,y
                x,y = self.blockColumn(i,j,'C',2)
                if x!=-1:
                    x,y = self.makeMove(table[y],'C')
                    return x,y
                x,y = self.blockPrincDiag(i,j,3,'C')
                if x!=-1:
                    x,y = self.makeMove(table[y],'C')
                    print('HAI CA INTRU PE IF')
                    return x,y
                x,y = self.blockSecDiag(i,j,'C',2)
                if x!=-1:
                    x,y = self.makeMove(table[y],'C')
                    return x,y
        return self.randomMove()

