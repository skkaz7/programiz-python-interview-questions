def check_if_anagram(str1, str2):
    return True if sorted(str1.strip()) == sorted(str2.strip()) else False


if __name__ == "__main__":
    word1 = "listen"
    word2 = "silent"
    print(check_if_anagram(word1, word2))
