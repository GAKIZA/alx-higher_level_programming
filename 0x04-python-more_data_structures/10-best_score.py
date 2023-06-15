#!/usr/bin/python3

def best_score(a_dictionary):
    values_list = []
    keys_list = []
    biggest_value = 0
    if a_dictionary is None:
        return None
    else:
        for keys, values in a_dictionary.items():
            values_list.append(values)
            keys_list.append(keys)

        for i in range(len(values_list) - 1):
            if values_list[i] > biggest_value:
                biggest_value = i

        return (keys_list[i])
