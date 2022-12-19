def display_board(board):
    print("\t{0} | {1} | {2}".format(board[0], board[1], board[2]))
    print("\t_ | _ | _")
    print("\t{0} | {1} | {2}".format(board[3], board[4], board[5]))
    print("\t_ | _ | _")
    print("\t{0} | {1} | {2}".format(board[6], board[7], board[8]))

class Player(object):
    def __init__(self,take='X'):
        self.take=take
    def legal_moves(self, board):
        """Returns the list of available positions"""
        moves = []
        for i in range(9):
            if board[i] in list("012345678"):
                moves.append(i)
        return moves

class HumanPlayer(Player):
    def getPlayerMove(self, board):
        move = 9
        while move not in self.legal_moves(board):
            move = int(input("Player please select the drop position (0-8):"))
        return move

class ComputerPlayer(Player):
    def __init__(self, take, game):
        super().__init__(take)
        self.game = game
    def getPlayerMove(self, board):
        computerLetter = self.take
        playerLetter = 'X' if self.take == 'O' else 'X'
        boardcopy = board.copy()

        for move in self.legal_moves(boardcopy):
            boardcopy[move] = computerLetter
            if self.game.isWinner(boardcopy):
                return move
            boardcopy[move] = str(move)
    
        for move in self.legal_moves(boardcopy):
            boardcopy[move] = playerLetter
            if self.game.isWinner(boardcopy):
                return move
            boardcopy[move] = str(move)
    
        for move in (4,0,2,6,8,1,3,5,7):
            if move in self.legal_moves(board):
                return move


class Game(object):
    def __init__(self):
        self.board = list("012345678")
    
    def mk_player (self,p, take='X'): # p in [0,1]
        if p == 0:
            return HumanPlayer(take)
        else:
            return ComputerPlayer(take, self)
    
    def switch_player(self, player1, player2):
        if self.current_player is None:
            return player1
        else:
            return [player1, player2][self.current_player == player1]
            

    def isWinner(self, board):
        WIN = {(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)}
        for r in WIN:
            if board[r[0]] == board[r[1]] == board[r[2]]:
                return True
        return False

    def isDraw(self, board):
        for i in list("012345678"):
            if i in board:
                return False
        return True

    

def tic_tac_toe():
    game_mode = input("Please choose your game mode (pvp or pve):")
    game = Game()
    if game_mode == 'pvp':
        playerLetter = input("Player1 please choose'X'and'O', X goes first" )
        if playerLetter in ("X"):
            turn = "player1"
            player1Letter = "X"
            player2Letter ="O"
            player1 = HumanPlayer(take="X")
            player2 = HumanPlayer(take="O")
        else:
            turn = "player2"
            player2Letter = "X"
            player1Letter = "O"
            player1 = HumanPlayer(take="O")
            player2 = HumanPlayer(take="X")
    elif game_mode == 'pve':
        playerLetter = input("Player please choose'X'and'O', X goes first" )
        if playerLetter in ("X"):
            turn = "player1"
            player1Letter = "X"
            player2Letter ="O"
            player1 = HumanPlayer(take="X")
            player2 = ComputerPlayer(game=game, take="O")
        else:
            turn = "player2"
            player2Letter = "X"
            player1Letter = "O"
            player1 = HumanPlayer(take="O")
            player2 = ComputerPlayer(game=game, take="X")
    else:
        return None
    
    print("{}goes first".format(turn))
    while True:
        display_board(game.board)
        if turn == 'player1':
            move = player1.getPlayerMove(game.board)
            game.board[move] = player1Letter
            if game.isWinner(game.board):
                display_board(game.board)
                print("Player1 Win")
                break
            else:
                turn = "player2"
        else:
            move = player2.getPlayerMove(game.board)
            game.board[move] = player2Letter
            if game.isWinner(game.board):
                display_board(game.board)
                print("Player2 Win")
                break
            else:
                turn = "player1"

        if game.isDraw(game.board):
            display_board(game.board)
            print('Draw')
            break

if __name__ == '__main__':
    tic_tac_toe()