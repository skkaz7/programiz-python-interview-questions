def last_word_length(phrase):
    last_word = phrase.split()[-1]
    return len(last_word[:-1]) if last_word[-1] == '.' else len(last_word)


if __name__ == "__main__":
    str1 = "I love Python Programming"
    str2 = "A red rose grew up out of ice."
    print(last_word_length(str1))
    print(last_word_length(str2))
