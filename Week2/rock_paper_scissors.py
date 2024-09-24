import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['sten', 'sax', 'påse']

    def get_computer_choice(self):
        return random.choice(self.choices)

    def get_player_choice(self):
        choice = input("Välj sten, sax eller påse: ").lower()
        while choice not in self.choices:
            choice = input("Ogiltigt val. Välj sten, sax eller påse: ").lower()
        return choice

    def determine_winner(self, player, computer):
        if player == computer:
            return "Oavgjort"
        elif (player == 'sten' and computer == 'sax') or \
             (player == 'sax' and computer == 'påse') or \
             (player == 'påse' and computer == 'sten'):
            return "Spelaren vinner"
        else:
            return "Datorn vinner"

    def play_game(self):
        while True:
            computer_choice = self.get_computer_choice()
            player_choice = self.get_player_choice()
            print(f"Datorn valde: {computer_choice}")
            print(f"Spelaren valde: {player_choice}")
            result = self.determine_winner(player_choice, computer_choice)
            print(result)
            if result != "Oavgjort":
                break

