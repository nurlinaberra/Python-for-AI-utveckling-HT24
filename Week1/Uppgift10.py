def create_new_string(input_string):
    # Kontrollera om strängen har minst 2 tecken
    if len(input_string) >= 2:
        last_two_chars = input_string[-2:]  # Hämta de två sista tecknen i strängen
        new_string = last_two_chars * 4  # Skapa en ny sträng med 4 kopior av de två sista tecknen
        return new_string
    else:
        return "Strängen måste ha minst 2 tecken"

# Testa funktionen med en given sträng
input_string = "Python"
result = create_new_string(input_string)
print(result)
