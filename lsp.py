# Liskov Segregation Principle
"""
Seja q(x) um atributo comprovavel sobre objetos x do tipo T.
Então q(y) deve ser comprovavel para objetos y do tipo S, se S for um subconjunto de T
"""

class User:

    def __init__(self, color, board):
        create_pieces()
        self.color = color
        self.board = board

    def move(self, piece: Piece, position: int):
        piece.move(position)
        chessmate_check()


board = chessBoard()
white_user = User('white', board)
black_user = User('black', board)

pieces = white_user.pieces
horse = helper.get_horse(white_user, 1)
white_user.move(horse)
