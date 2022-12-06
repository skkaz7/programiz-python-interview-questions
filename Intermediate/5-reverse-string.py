def reverse_string(phrase):
    return ' '.join(phrase.split()[::-1])


if __name__ == "__main__":
    sentence = "this is blue"
    sentence2 = "welcome to hollywood"
    print(reverse_string(sentence))
    print(reverse_string(sentence2))
