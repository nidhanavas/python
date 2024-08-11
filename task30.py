def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_consonants = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1

    return num_vowels, num_consonants


input_string = input("enter the string")
num_vowels, num_consonants = count_vowels_and_consonants(input_string)
print("Number of vowels:", num_vowels)
print("Number of consonants:", num_consonants)
