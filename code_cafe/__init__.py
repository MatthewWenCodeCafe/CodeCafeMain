from .demo import board as demo_board, player as demo_player
from .p1 import board as p1_board, player as p1_player
from .p2 import board as p2_board, player as p2_player
from .p3 import board as p3_board, player as p3_player
from .p4 import board as p4_board, player as p4_player
from .p5 import board as p5_board, player as p5_player
from .p6 import board as p6_board, player as p6_player
from .p7 import board as p7_board, player as p7_player
from .p8 import board as p8_board, player as p8_player


def get_board(reference):
    types_boards = {
        "demo": lambda: demo_board.Board(),
        "p1": lambda: p1_board.Board(),
        "p2": lambda: p2_board.Board(),
        "p3": lambda: p3_board.Board(),
        "p4": lambda: p4_board.Board(),
        "p5": lambda: p5_board.Board(),
        "p6": lambda: p6_board.Board(),
        "p7": lambda: p7_board.Board(),
        "p8": lambda: p8_board.Board(),
    }
    return types_boards[reference]() if reference in types_boards else None
