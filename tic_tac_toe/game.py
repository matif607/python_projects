from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
  def __init__(self) -> None: # why board is not there along with self?
    self.board = [" " for _ in range(9)]
  
  def print_board(self):
    for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
      print("| " + " | ".join(row) + " |") # what join(row) is doing

if __name__ == "__main__":
  # x = RandomComputerPlayer("X")
  # o = HumanPlayer("O")
  # print(x.letter)
  # print(o.letter)
  game = TicTacToe()
  game.board[0] = "X"
  game.board[4] = "O"
  game.print_board()