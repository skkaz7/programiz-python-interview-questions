def dict_value_increment(my_dict):
    for key in my_dict:
        my_dict[key] += 1
    return my_dict


print(dict_value_increment({'Cody': 50, 'Jack': 57, 'Seth': 59, 'Roman': 67}))
