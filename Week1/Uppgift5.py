# Uppgift5.py

# Ta emot en sträng som input från användaren
input_string = input("Ange en sträng: ")

# Kontrollera om strängen är kortare än 3 tecken
if len(input_string) < 3:
    new_string = input_string  # Behåll strängen oförändrad om den är kortare än 3 tecken
else:
    new_string = input_string + "ing"  # Lägg till "ing" om strängen är 3 tecken eller längre

# Skriv ut den modifierade strängen
print("Den modifierade strängen är:", new_string)
