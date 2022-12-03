numbers = [1, 7, 8, 7, 7, 7]


def find_majority_element(num_list):
    for number in num_list:
        count = num_list.count(number)
        if count > len(num_list) // 2:
            return number


print(find_majority_element(numbers))
