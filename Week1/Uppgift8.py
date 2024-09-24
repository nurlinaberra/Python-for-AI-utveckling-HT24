def convert_to_uppercase(input_string):
    # Kontrollera om strängen innehåller minst 4 tecken
    if len(input_string) >= 4:
        # Räkna antalet versaler bland de första 4 tecknen
        uppercase_count = sum(1 for char in input_string[:4] if char.isupper())
        
        # Om det finns minst 2 versaler, konvertera hela strängen till versaler
        if uppercase_count >= 2:
            return input_string.upper()
    
    return input_string  # Returnera strängen oförändrad om villkoret inte uppfylls

# Testa funktionen med en given sträng
input_string = "AcBbcDef"
result = convert_to_uppercase(input_string)
print(result)


