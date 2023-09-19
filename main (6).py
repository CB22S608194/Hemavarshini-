''' implement a cricket player '''





#Define the base class Player
class Player:
   def play(self):
      print("The player is playing cricket.")

#Define thr derived class Batsman
class Batsman(Player):
   def play(self):
        print("The bowler is bowling.")

#Define the derived class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

#Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#Call the play() method for each object
batsman.play()
bowler.play()