def find_same_subsequent_chars(phrase):
    result = []
    for i in range(len(phrase) - 1):
        if phrase[i] == phrase[i + 1]:
            result.append(phrase[i])
    return result


if __name__ == "__main__":
    str1 = "Hello"
    str2 = "Yahhoo"
    print(find_same_subsequent_chars(str1))
    print(find_same_subsequent_chars(str2))
