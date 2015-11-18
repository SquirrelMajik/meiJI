from __future__ import division

from math import log


class Data:
    def __init__(self, labels, *arg):
        self.category = arg[-1]
        if not labels:
            labels = range(len(arg))
        self.data = {label: value for label,value in zip(labels, arg[:-1])}
        
    def __str__(self):
        category = "category:{}".format(self.category)
        data_str = ["{0}:{1}".format(label, value) \
            for label,value in self.data.items()]
        data_str.append(category)
        data_str = '\n'.join(data_str)
        return data_str
            

def create_dataset(dataset, labels=[]):
    return [Data(labels, *data) for data in dataset]
    

def calculate_shannon_entropy(dataset):
    lenth = len(dataset)
    labels = {}
    for data in dataset:
        if data.category not in labels:
            labels[data.category] = 0
        labels[data.category] += 1
    shannon_entropy = 0
    for _, count in labels.items():
        prob = count/lenth
        shannon_entropy -= prob * log(prob, 2)
    return shannon_entropy
    

def saltshaker(dataset, label, value):
    return [data for data in dataset if data.data[label] == value]


def _get_labels(dataset):
    return [label for label in dataset[0].data]
    
    
def _feature(dataset):
    base_entropy = calculate_shannon_entropy(dataset)
    for label in _get_labels(dataset):
        unique_values = set([data.data[label] for data in dataset])
        entropy = 0
        for value in unique_values:
            temp_set = saltshaker(dataset, label, value)
            prob = len(temp_set) / len(dataset)
            entropy -= prob * calculate_shannon_entropy(temp_set)
        gain = base_entropy - entropy
        yield label, gain
        
    
def gains(dataset):
    feature_result = [(label, gain) for label, gain in _feature(dataset)]
    feature_result.sort(lambda x,y : int(x[1]-y[1]))
    return feature_result
    
    
def gain_first(dataset):
    return gains(dataset)[0]
    
    
if __name__ == "__main__":
    labels = ['room', 'size', 'poeple']
    dataset = [
        [1, 100, 3, 'good'],
        [2, 50, 2, 'good'],
        [4, 120, 3, 'good'],
        [4, 50, 3, 'bad'],
        [2, 30, 2, 'bad']
    ]
    dataset = create_dataset(dataset, labels)
    feature = gain_first(dataset)
    print feature