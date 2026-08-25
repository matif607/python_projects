class Player:
  def __init__(self, letter) -> None:
    self.letter = letter

  def get_move(self, game):
    pass


class RandomComputerPlayer(Player):
  def __init__(self, letter) -> None:
    super().__init__(letter)
  
  def get_move(self, game):
    return super().get_move(game)

class HumanPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)
  
  def get_move(self, game):
    pass