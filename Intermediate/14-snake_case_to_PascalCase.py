def snake_case_to_PascalCase(string):
    new_string = ''
    i = 0
    while i < len(string):
        if i == 0:
            new_string += string[i].upper()
        elif string[i] == '_':
            new_string += string[i + 1].upper()
            i += 1
        else:
            new_string += string[i]
        i += 1
    return new_string


if __name__ == "__main__":
    sentence = "custom_date_builder"
    print(snake_case_to_PascalCase(sentence))
