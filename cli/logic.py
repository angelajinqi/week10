class Board:

    board = None

    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]


    def get_winner(self):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        if self.board[0][0] == self.board[0][1]== self.board [0][2]:
            return self.board[0][0]
        if self.board[1][0] == self.board[1][1]== self.board [1][2]:
            return self.board[1][0]
        if self.board[2][0] == self.board[2][1]== self.board [2][2]:
            return self.board[2][0]
        if self.board[0][0] == self.board[1][0]== self.board [2][0]:
            return self.board[0][0]
        if self.board[0][1] == self.board[1][1]== self.board [2][1]:
            return self.board[0][1]
        if self.board[0][2] == self.board[1][2]== self.board [2][2]:
            return self.board[0][2]
        if self.board[0][2]== self.board[1][1]== self.board [2][0]:
            return self.board[0][2]
        if self.board[0][0]== self.board[1][1]== self.board [2][2]:
            return self.board[0][0]
        return None

    def other_player(player):
        """Given the character for a player, returns the other player."""
        if player == '1':
            return '0'
        if player == '0':
            return '1'
    # class Game:
    #     def __init__(self,player1, player2):
    #         self.player1 =player1 
    #         self.player2 = player2
    # class Human:
    #     def get_move(board):
    #         raise NotImplementedError
