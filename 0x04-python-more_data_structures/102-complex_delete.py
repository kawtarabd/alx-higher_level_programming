#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary.keys())
    for val_list in key_list:
        if value == a_dictionary.get(val_list):
            del a_dictionary[val_list]
    return a_dictionary
