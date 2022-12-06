def remove_duplicate_chars(phrase):
    result = ""
    for char in phrase:
        if char not in result:
            result += char
    return result


if __name__ == "__main__":
    print(remove_duplicate_chars("12stars23"))
    print(remove_duplicate_chars("mickky"))
