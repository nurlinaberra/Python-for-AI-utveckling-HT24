print("Test main hello world new code:")
from rock_paper_scissors import RockPaperScissors

if __name__ == "__main__":
     # Skapar en instans av RockPaperScissors och kör spelet
    game = RockPaperScissors()
    game.play_game()