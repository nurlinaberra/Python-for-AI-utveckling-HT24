def find_longest_word(words_list):
    if not words_list:
        return "Listan är tom"

    longest_word = max(words_list, key=len)  # Hitta det längsta ordet i listan
    longest_word_length = len(longest_word)  # Hitta längden på det längsta ordet

    return longest_word, longest_word_length

# Testa funktionen med en lista av ord
words_list = ["apple", "banana", "cherry", "datesssss"]
result = find_longest_word(words_list)
print(result)
