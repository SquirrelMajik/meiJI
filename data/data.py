# coding=utf-8
from __future__ import absolute_import

import copy

CATEGORY = 'category'


class Data:
    def __init__(self, **arg):
        if CATEGORY not in arg:
            raise Exception("data must have category")
        self.category = arg.pop(CATEGORY)
        self.data = arg
        
    def __str__(self):
        data_str = [value for _, value in self.data]
        data_str.append(self.category)
        data_str = '\t'.join(data_str)
        return data_str
        
    def __len__(self):
        return len(self.data)
        
    def __getitem__(self, key):
        return self.data.get(key)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]
        
    def get_labels(self):
        return set([label for label, _ in self.data])
            
            
class DataSet:
    def __init__(self, dataset=[], labels=[]):
        if not isinstance(dataset, list):
            raise Exception("dataset must be list")
        if not isinstance(dataset, list):
            raise Exception("labels must be list")
        if dataset:
            if not labels:
                labels = range(len(dataset[0]))
            if len(dataset[0]) == len(labels):
                self._category_label = labels[-1]
                labels = labels[:-1]
            elif len(dataset[0]) == len(labels) + 1:
                self._category_label = ''
            else:
                raise Exception("labels don't suit dataset")
        self.dataset = [_create_data(labels, data) for data in dataset]
        self.labels = set(labels)
        
    def __iter__(self):
        return iter(self.dataset)
        
    def __str__(self):
        label_str = '\t'.join(self.labels + [self._category_label])
        dataset_str = '\n'.join([data.__str__() for data in dataset])
        dataset_str = label_str + dataset_str
        return dataset_str
    
    def __len__(self):
        return len(self.dataset)
        
    def append(self, data):
        if not data.get_labels() == self.labels:
            raise Exception("append incorrect data into dataset")
        self.dataset.append(data)
        return self
        
    def saltshaker(self, label, value ,split=True):
        dataset = DataSet()
        temp_dataset = [copy.deepcopy(data) for data in self.dataset \
            if data[label] == value]
        labels = set(self.labels)
        if split:
            for data in temp_dataset:
                del data[label]
            labels -= set([label])
        dataset.dataset = temp_dataset
        dataset.labels = labels
        return dataset
        
        
def _create_data(labels, data):
    category = data[-1]
    data = data[:-1]
    common_data = {label:d for label, d in zip(labels, data)}
    common_data[CATEGORY] = category
    return Data(**common_data)
    