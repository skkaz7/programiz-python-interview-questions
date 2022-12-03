import string

alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def vowels_consonants_counter(phrase):
    vowels_count = 0
    consonants_count = 0
    for letter in phrase:
        if letter in vowels:
            vowels_count += 1
        elif letter in alphabet:
            consonants_count += 1
    return f"Vowels: {vowels_count}, consonants: {consonants_count}"


print(vowels_consonants_counter('juice'))
print(vowels_consonants_counter('Computer'))
