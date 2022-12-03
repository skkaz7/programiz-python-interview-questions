import string


def capital_letters_index(phrase):
    return [idx for idx, letter in enumerate(phrase) if letter in string.ascii_uppercase]


print(capital_letters_index('heLLo'))
