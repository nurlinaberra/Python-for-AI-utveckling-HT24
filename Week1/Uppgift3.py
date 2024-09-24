# Uppgift3.py

# Ta emot en sträng som input från användaren
input_string = input("Ange en sträng: ")

# Kontrollera att strängen är tillräckligt lång
if len(input_string) < 2:
    print("Strängen är för kort.")
else:
    # Extrahera de två första och de två sista tecknen
    first_two = input_string[:2]
    last_two = input_string[-2:]
    
    # Skriv ut de två första och de två sista tecknen
    print(f"{first_two} {last_two}")
