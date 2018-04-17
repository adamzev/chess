import chess
import chess.svg

import random

board = chess.Board()
print(board.legal_moves)
#print(board.push_san("e4"))
#print(board.push_san("e5"))
#board.push_san("Qh5")


def display_legal_moves(board):
    for n, move in enumerate(board.legal_moves):
        print(board.san(move), end=' | ')
        if (n + 1) % 5 == 0:
            print()
    print()

def make_a_move(board):
    print(board)
    print("Legal moves")
    display_legal_moves(board)

    move = input("Make a move: ")
    try:
        move_uci = board.parse_san(move)
        if move_uci in board.legal_moves:
            board.push_san(move)
            ai_move = random.choice(list(board.legal_moves))
            board.push(ai_move)
        else:
            raise ValueError("invalid move")
    except ValueError:
        print("Not a legal move")

board = chess.Board()
while True:
    make_a_move(board)