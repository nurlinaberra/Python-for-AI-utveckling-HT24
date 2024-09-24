def reverse_string_if_multiple_of_4(input_string):
    # Kontrollera om längden av strängen är en multipel av 4
    if len(input_string) % 4 == 0:
        return input_string[::-1]  # Vänd på strängen om längden är en multipel av 4
    else:
        return input_string  # Returnera strängen oförändrad om längden inte är en multipel av 4

# Testa funktionen med en given sträng
input_string = "abcdefeg"
result = reverse_string_if_multiple_of_4(input_string)
print(result)
