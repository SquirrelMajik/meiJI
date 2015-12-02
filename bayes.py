# coding=utf-8
from __future__ import absolute_import

from data import data
import re


def split_words(string):
    pattern = re.compile(r"\w+")
    return re.findall(pattern, string)
    

def words_set(string_list):
    return set([split_words(string) for string in string_list])

                                                                                                                                                   
    

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
    
    