#Define the base class player

class palyer:
  def play(self):
    print("The Player Is Playing Cricet")

#Define the derived class Batsman

class Batsman:
  def play(self):
    print("The Batsman Is Batting")

#Define the derived class Bowler

class Bowler:
  def play(self):
    print("The Bowler Is Bowling")

#create objects of batsman and bowler classes

batsman=Batsman()
bowler=Bowler()

#call the play() method for each object

batsman.play()
bowler.play()