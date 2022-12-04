def can_make_string(letters_list, phrase):
    for letter in phrase:
        if letter not in letters_list and letter not in str(letters_list).upper():
            return False
    return True


if __name__ == "__main__":
    lst = ['a', 'l', 'p', 'c', 'e', 'd']
    string = 'apPle'
    print(can_make_string(lst, string))
