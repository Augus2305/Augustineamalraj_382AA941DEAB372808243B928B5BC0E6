class Player:
  def play(self):
    print("Player is playing cricket")
class Batsman(Player):
  def play(self):
    print("Batsman is batting")
class Bowler(Player):
  def play(self):
    print("Bowler is bowling")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()