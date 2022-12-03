vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def remove_vowels(phrase):
    result = ''
    for letter in phrase:
        if letter not in vowels:
            result += letter
    return result


print(remove_vowels('icecream23'))
