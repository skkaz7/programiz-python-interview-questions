def starts_with_consonant(str_list):
    return [word for word in str_list if word[0] not in 'aeiouAEIOU']


print(starts_with_consonant(['apple', 'banana', 'pineapple', 'mango', 'watermelon']))
