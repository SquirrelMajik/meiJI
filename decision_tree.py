# coding=utf-8
from __future__ import absolute_import

from __future__ import division

from collections import Counter
from math import log
from data import DataSet
import json

    
# def create_dataset(dataset, labels=[]):
#     return [Data(labels, *data) for data in dataset]
    

def calculate_shannon_entropy(dataset):
    countor = Counter([data.category for data in dataset])
    shannon_entropy = 0
    for _, count in countor.items():
        prob = count/len(dataset)
        shannon_entropy -= prob * log(prob, 2)
    return shannon_entropy
    
    
# def _get_labels(dataset):
#     return [label for label in dataset[0].data]
    
    
def _feature(dataset):
    base_entropy = calculate_shannon_entropy(dataset)
    for label in dataset.labels:
        unique_values = set([data[label] for data in dataset])
        entropy = 0
        for value in unique_values:
            temp_set = dataset.saltshaker(label, value)
            prob = len(temp_set) / len(dataset)
            entropy -= prob * calculate_shannon_entropy(temp_set)
        gain = base_entropy - entropy
        yield label, gain
        
    
def gains(dataset):
    feature_result = [(label, gain) for label, gain in _feature(dataset)]
    feature_result.sort(lambda x,y : -1 if x[1] > y[1] else 1)
    return feature_result
    
    
def gain_best(dataset):
    return gains(dataset)[0][0]
    

def tree(dataset):
    counter = Counter([data.category for data in dataset])
    if len(counter) == 1 or len(dataset[0]) == 1:
        return counter.most_common()[0][0]
    best_label = gain_best(dataset)
    decision_tree = {best_label: {}}
    
    unique_values = set([data[best_label] for data in dataset])
    for value in unique_values:
        decision_tree[best_label][value] = tree(
            dataset.saltshaker(best_label, value))
    return decision_tree
    
    
if __name__ == "__main__":
    labels = ['room', 'size', 'poeple']
    dataset = [
        [1, 100, 3, 'good'],
        [2, 50, 2, 'good'],
        [4, 120, 3, 'good'],
        [4, 50, 3, 'bad'],
        [2, 30, 2, 'bad']
    ]
    dataset = DataSet(dataset, labels)
    d_tree = tree(dataset)
    print json.dumps(d_tree, indent=1)