# Uppgift6.py

# Ta emot en sträng som input från användaren
input_string = input("Ange en sträng: ")

# Ta bort alla mellanslag, tabbar och radbrytningar från strängen
cleaned_string = input_string.replace(" ", "").replace("\t", "").replace("\n", "")

# Ta bort alla tecken på ojämna indexvärden från den rensade strängen
result_string = cleaned_string[::2]

# Skriv ut den resulterande strängen
print("Den resulterande strängen är:", result_string)
