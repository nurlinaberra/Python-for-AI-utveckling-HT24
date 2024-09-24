import random

def guessing_game():
    target_number = random.randint(1, 100)
    
    while True:
        user_guess = int(input("Gissa på ett nummer mellan 1 och 100: "))
        #print(f"Det slumpmässiga numret är: {target_number}")
        
        if user_guess == target_number:
            print("Grattis! Du har gissat rätt.")
            break
        elif user_guess < target_number:
            print("Det rätta svaret är högre. Försök igen.")
        else:
            print("Det rätta svaret är lägre. Försök igen.")

# Starta gissningsspelet
print("Välkommen till gissningsspelet!")
print("Jag tänker på ett nummer mellan 1 och 100. Kan du gissa vilket?")

guessing_game()

