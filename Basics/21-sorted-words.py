def sort_words(phrase):
    words = phrase.split()
    words.sort()
    for word in words:
        print(word)


sort_words('python is easy')
