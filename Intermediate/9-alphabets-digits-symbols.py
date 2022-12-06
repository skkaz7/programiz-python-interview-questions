def alphabets_digits_symbols_counter(phrase):
    alphabets = 0
    digits = 0
    symbols = 0
    for char in phrase:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1
    return f"Alphabets: {alphabets}, digits: {digits}, symbols: {symbols}"


if __name__ == "__main__":
    str1 = "Hello123."
    print(alphabets_digits_symbols_counter(str1))
