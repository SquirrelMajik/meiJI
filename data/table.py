# coding=utf-8
from __future__ import absolute_import

from utils import table_format

class table:
    def __init__(self, labels, *data):
        self.labels = table._shake_labels_(labels)
        self.data = table._shake_data_(labels ,data)
        
    def __len__(self):
        return len(self.data)
        
    def __getitem__(self, tup):
        if isinstance(tup, tuple):
            num, label = tup
            return self.get(num, label)
        else:
            num = tup
            return self.data[num]

    # def __setitem__(self, key, value):
    #     self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]
        
    def __str__(self):
        return table_format(self.labels, self.data)
        
    @staticmethod
    def _shake_labels_(labels):
        if not isinstance(labels, list):
            raise LabelsTypeError()
        for label in labels:
            if not isinstance(label, str):
                raise LabelTypeError()
        return labels
    
    @staticmethod
    def _shake_one_data_(labels, data, num=None):
        if not isinstance(data, list):
            raise DataTypeError()
        if len(labels) != len(data):
            raise DataValueError(num)
        return data
        
    @staticmethod
    def _shake_data_(labels, data):
        return [table._shake_one_data_(labels, d, i) \
            for i,d in enumerate(data)]
         
    def append(self, data):
        data = table._shake_one_data_(self.labels, data)
        self.data.append(data)
        return self
        
    def extends(self, *data):
        data = table._shake_data(self.lables, data)
        self.data.extends(data)
        return self
        
    def get(self, data, label):
        if not isinstance(label, int):
            label = self.labels.index(label)
        if isinstance(data, list) and not label:
            return data
        return self.data[data][label]
        
    def slice(*labels, **except):
        pass
        

class LabelsTypeError(Exception):
    def __init__(self):
        message = "Labels must be a list"
        super().__init__(message)
         

class LabelTypeError(Exception):
    def __init__(self):
        message = "Label must be a string"
        super().__init__(message)
        

class DataTypeError(Exception):
    def __init__(self):
        message = "Data must be a list"
        super().__init__(message)
         
         
class DataValueError(Exception):
    def __init__(self, num=None):
        message = "Data is incorrect"
        if num is not None:
            message += " at {}".format(num)
        super().__init__(message)

        
if __name__ == "__main__":
    labels = ['aasfweg', 'adgahb', 'cahaeh']
    data = [
        [1,2,3],
        [2,3,4],
        [3,4,5],
    ]
    t = table(labels, *data)
    print(t[1])