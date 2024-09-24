import random

class RockPaperScissors:
    def __init__(self):
        # Initialiserar valen för spelet
        self.choices = ['sten', 'sax', 'påse']

    def get_computer_choice(self):
        # Slumpar datorns val från listan av val
        return random.choice(self.choices)

    def get_player_choice(self):
        # Tar spelarens val och säkerställer att det är giltigt
        choice = input("Välj sten, sax eller påse: ").lower()
        while choice not in self.choices:
            # Om spelaren inte har valt något av de tre valen så frågas spelaren igen
            choice = input("Ogiltigt val. Välj sten, sax eller påse: ").lower()
        return choice

    def determine_winner(self, player, computer):
        # Bestämmer vinnaren baserat på reglerna
       
        if player == computer:
             # Om spelaren och datorn har samma val så är det oavgjort
            return "Oavgjort"
        # Om spelaren har valt sten och datorn har valt sax så vinner spelaren  
        elif (player == 'sten' and computer == 'sax') or \
             (player == 'sax' and computer == 'påse') or \
             (player == 'påse' and computer == 'sten'):
            return "Spelaren vinner"
        
        else:
            return "Datorn vinner"

    def play_game(self):
        # Kör spelet tills spelaren vinner eller förlorar
        while True:
            computer_choice = self.get_computer_choice()
            player_choice = self.get_player_choice()
            print(f"Datorn valde: {computer_choice}")
            print(f"Spelaren valde: {player_choice}")
            result = self.determine_winner(player_choice, computer_choice)
            print(result)
            if result != "Oavgjort":
                break