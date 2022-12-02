import string


def capital_letters_counter(phrase):
    temp = 0
    capital_letters = string.ascii_uppercase
    for letter in phrase:
        if letter in capital_letters:
            temp += 1
    return temp


print(capital_letters_counter('The Sun emits UV light'))
