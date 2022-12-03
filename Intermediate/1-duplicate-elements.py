my_list = [2, 'python', 5, 7, 'python', 'java', 5]


def find_duplicates(some_list):
    new_list = []
    for element in set(some_list):
        if some_list.count(element) > 1:
            new_list.append(element)
    return new_list


print(find_duplicates(my_list))
