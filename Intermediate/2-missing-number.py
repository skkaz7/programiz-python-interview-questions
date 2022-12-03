numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10]


def find_the_missing_number(num_list):
    for num in num_list:
        if num + 1 != num_list[num]:
            return num + 1


print(find_the_missing_number(numbers))
