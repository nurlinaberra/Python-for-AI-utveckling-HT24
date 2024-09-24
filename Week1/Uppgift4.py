# Uppgift4.py

# Ta emot två strängar som input från användaren
str1 = input("Ange den första strängen: ")
str2 = input("Ange den andra strängen: ")

# Skapa en ny sträng genom att byta de två första tecknen i varje sträng
new_str = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]

# Skriv ut den nya strängen
print("Den nya strängen är:", new_str)
