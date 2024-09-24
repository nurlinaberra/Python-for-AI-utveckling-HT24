def generate_multiplication_table():
    # Generera en enkel multiplikationstabell för talen 1-10
    for i in range(1, 11):
        for j in range(1, 11):
            result = i * j
            print(f"{i} * {j} = {result:2}", end="\t")  # Använd f-string för snygg formatering
        print()  # Ny rad för varje nytt tal i yttre loopen

# Anropa funktionen för att generera multiplikationstabellen
generate_multiplication_table()
