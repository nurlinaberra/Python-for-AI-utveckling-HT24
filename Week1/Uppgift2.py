# Uppgift2.py

# Ta emot en sträng som input från användaren
input_string = input("Ange en sträng: ")

# Skapa en tom dictionary för att lagra teckenfrekvensen
char_frequency = {}

# Iterera genom varje tecken i strängen
for char in input_string:
    # Om tecknet redan finns i dictionaryn, öka dess räkning
    if char in char_frequency:
        char_frequency[char] += 1
    # Annars, lägg till tecknet i dictionaryn med räkningen 1
    else:
        char_frequency[char] = 1

# Skriv ut teckenfrekvensen
print("Teckenfrekvensen är:", char_frequency)
