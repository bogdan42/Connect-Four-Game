
from board.BOARD import *

class ui:

    def gameCommand(self):
        command = input('column >')
        command = command.split(' ')
        return  command

    def gameMenu(self):
        print('You will place pieces on columns.')
        print('The command to place a piece is')
        print('column > <column letter>')
        print('Let the game begin')

    def gamePlay(self,board_game):
        self.gameMenu()
        print('This is the board:')
        print(board_game)
        while True:
            try:
                command = self.gameCommand()
                if len(command) != 1:
                    raise ValueError('Invalid Command')
                if board_game.validatePlacement(command[0].lower()) == 0:
                    raise ValueError('Invalid placement')
                xhum,yhum = board_game.makeMove(command[0].lower(),"H")
                if board_game.isWon(xhum,yhum,'H') == 1:
                    print('You win!')
                    print(board_game)
                    return 0
                else:
                    print(board_game)
                x,y = board_game.computerStrategy()
                if board_game.isWon(x,y,'C') == 1:
                    print('Computer Wins')
                    print(board_game)
                    return 0
                else:
                    print(board_game)
            except ValueError as error:
                print(error)

    def mainMenu(self):
        print('play')
        print('x')


    def getMainCommand(self):
        command = input('Type command\n >>>')
        command = command.split(' ')
        return  command

    def mainExe(self):
        while True:
            try:
                self.mainMenu()
                command = self.getMainCommand()
                if len(command) != 1:
                    raise ValueError('Invalid Command')
                else:
                    if command[0].lower() == 'play':
                        self.gamePlay(Board())
                    elif command[0].lower() == 'x':
                        return 0
                    else:
                        raise  ValueError('Invalid Command')
            except ValueError as error:
                print(error)