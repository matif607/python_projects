from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
  def __init__(self) -> None: # why board is not there along with self?
    self.board = [" " for _ in range(9)]
  
  def print_board(self):
    for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
      print("| " + " | ".join(row) + " |") # what join(row) is doing

  def available_moves(self):
    return [i for i, spot in enumerate(self.board) if spot == " "]

  def empty_squares(self):
    return " " in self.board
  
  def num_empty_squares(self):
    return self.board.count(" ")
  

  def make_move(self, square, letter):
    if self.board[square] == " ":
      self.board[square] = letter
      return True
    return False

  def winner(self, square, letter):
    # row of the square you just played
    row_ind = square // 3
    row = self.board[row_ind * 3 : (row_ind + 1) * 3]
    if all(spot == letter for spot in row):
      return True
    
    # col of that square
    col_ind = square % 3
    column = [self.board[col_ind + i * 3] for i in range(3)]
    if all(spot == letter for spot in column):
      return True
    
    # diagonals only possible from even squares
    if square % 2 == 0:
      diagonal1 = [self.board[i] for i in [0, 4, 8]]
      if all(spot == letter for spot in diagonal1):
        return True
      
      diagonal2 = [self.board[i] for i in [2, 4, 6]]
      if all(spot == letter for spot in diagonal2):
        return True
    return False


if __name__ == "__main__":
  game = TicTacToe()
  # bot = RandomComputerPlayer("O")
  # human = HumanPlayer("X")
  # move = bot.get_move(game)
  # print(move)
  game.make_move(0, "X")
  game.make_move(3, "X")
  game.make_move(6, "X")
  # human_move = human.get_move(game)
  # game.make_move(human_move, human.letter)
  game.print_board()
  print(game.winner(0, "X"))
