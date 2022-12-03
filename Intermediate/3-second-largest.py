numbers = [4, 5, 6, 2, 51, 23]


def second_largest_1(num_list):
    num_list.pop(num_list.index(max(num_list)))
    return max(num_list)


print(second_largest_1(numbers))

numbers2 = [4, 5, 6, 2, 51, 23]


def second_largest_2(num_list):
    return sorted(num_list, reverse=True)[1]


print(second_largest_2(numbers2))

numbers3 = [51, 51, 13, 6, 5, 2]


def second_largest_3(num_list):
    num_list = list(set(num_list))
    num_list.remove(max(num_list))
    return max(num_list)


print(second_largest_3(numbers3))
