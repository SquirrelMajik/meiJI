# coding=utf-8
from __future__ import absolute_import

def table_format(labels, data):
    lengths = []
    label_str = []
    for label in labels:
        length = len(label) + 2
        lengths.append(length)
        label_str.append(string_format(label, length))
    
    label_str = ''.join(label_str)
    data_str = '\n'.join([''.join([string_format(v, lengths[i]) \
        for i,v in enumerate(d)]) for d in data])
    return '\n'.join([label_str, '-'*len(label_str), data_str])
    
    
def string_format(string, length):
    return ('{0: ^' + str(length) + '}').format(string)
    

# def find_the_longest_string(string_list):
#     the_longest = ''
#     for string in string_list:
#         the_longest = string if len(string) > len(the_longest) else the_longest
#     return the_longest, len(the_longest)



    