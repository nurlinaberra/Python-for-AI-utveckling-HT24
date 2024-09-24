def is_palindrome(word):
    word = word.lower()  # Konvertera ordet till gemener för att vara oberoende av versaler
    reversed_word = word[::-1]  # Skapa en omvänd version av ordet
    
    return word == reversed_word

# Testa om ett ord är ett palindrom
word = "radar"
if is_palindrome(word):
    print(f"{word} är ett palindrom.")
else:
    print(f"{word} är inte ett palindrom.")
