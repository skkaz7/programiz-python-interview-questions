def move_zeros_to_end(num_list):
    for i in range(len(num_list)):
        if num_list[i] == 0:
            num_list.pop(i)
            num_list.append(0)
    return num_list


if __name__ == "__main__":
    lst = [1, 0, 2, 0, 4, 0, 6, 5]
    print(move_zeros_to_end(lst))
