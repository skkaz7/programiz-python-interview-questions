def break_list_into_chunks(num_list):
    chunks = []
    for i in range(0, len(num_list), 4):
        chunk = num_list[i:i + 4]
        chunks.append(chunk)

    for chunk in chunks:
        print(chunk)


if __name__ == "__main__":
    numbers = [2, 3, 6, 7, 3, 5, 7, 8, 9, 2, 20, 24, 16, 17, 23, 19]
    break_list_into_chunks(numbers)
