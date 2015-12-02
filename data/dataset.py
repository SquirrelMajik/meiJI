# coding=utf-8
from __future__ import absolute_import

from table import table
import inflection


class dataset(table):
    def __init__(self, labels, *data):
        if not labels and not data:
            raise DataSetError()
        if not labels: 
            labels = [inflection.ordinalize(i) for i in range(len(data[0]))]
        super().__init__(labels, *data)
        

class DataSetError(Exception):
    def __init__(self):
        message = "Empty dataset is not available"
        super().__init__(message)
        

if __name__ == "__main__":
    labels = ['aasfweg', 'adgahb', 'cahaeh']
    data = [
        [1,4,3],
        [2,3,4],
        [3,4,5],
    ]
    t = dataset(labels, *data)
    print(t)
    t = dataset(labels)
    print(t)
    t = dataset(None, *data)
    print(t)
    t = dataset(None)
