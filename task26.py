def extract_uppercase_letters(strings):
    return [char for string in strings for char in string if char.isupper()]

strings = ["Song", "world", "Car", "Gamming"]
uppercase_letters = extract_uppercase_letters(strings)
print(uppercase_letters)