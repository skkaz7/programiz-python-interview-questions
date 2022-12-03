def middle_letter(sentence):
    return sentence[len(sentence) // 2] if len(sentence) % 2 != 0 else 'empty'


print(middle_letter('hello'))
print(middle_letter('nana'))
