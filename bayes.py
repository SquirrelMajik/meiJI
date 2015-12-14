# coding=utf-8
from __future__ import absolute_import

import re
from data import DataSet
from collections import Counter



def split_words(string):
    pattern = re.compile(r"\w+")
    return re.findall(pattern, string)
    

def words_set(string_list):
    return set([split_words(string) for string in string_list])

                                                                    
def count_words(str_list):
    return Counter(str_list)
    
    
def count_words_in_unit_set(str_list, union_set):
    union = dict().fromkeys(unit_set, 0)
    union.update(Counter(str_list))
    return union
    

def P():



if __name__ == "__main__":
    labels = ['sentence']
    dataset = [
        ["I am a good man.", 'good'],
        ["You are such a bitch!", 'bad'],
        ["What the fuck!", 'bad'],
        ["I will go skating.", 'good'],
        ["Fuck you, bitch!", 'bad']
    ]
    dataset = DataSet(dataset, labels)
    print words_set(dataset)
    
    