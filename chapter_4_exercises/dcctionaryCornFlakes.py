
num = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
numb = {0: 10, 1: 20}


dictionary_list = dict(sorted(num.items()))
print(dictionary_list)


# def sort_dict_by_value_reverse(test_dict):
#     sorted_list = sorted(test_dict.items(), key=itemgetter(1), reverse=True)
#     return OrderedDict(sorted_list)

def add_key_to_a_dictionary(dictionary: dict, key, value):
    dictionary.update({key: value})
    return dictionary
print(add_key_to_a_dictionary())


