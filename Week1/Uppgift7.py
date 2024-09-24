# Uppgift7.py

# Ta emot en komma-separerad sekvens av ord som input från användaren
input_sequence = input("Ange en komma-separerad sekvens av ord: ")

# Dela upp sekvensen i ord och skapa en lista av unika ord i alfabetisk ordning
unique_words = sorted(set([word.strip() for word in input_sequence.split(",")]))

# Skriv ut de unika orden i alfabetisk ordning
print("Unika ord i alfabetisk ordning:", ", ".join(unique_words))
