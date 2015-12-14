# coding=utf-8
from __future__ import absolute_import

from __future__ import division


def P(dataset, under=None, **arg):
    def _p(dataset, **arg):
        count = 0
        # key, value = arg.items()[0]
        for data in dataset:
            for key, value in arg.items():
                if dataset[data, key] == value:
                    break
            else:
                count += 1
        return count / len(dataset)
        
    def _p_under(dataset, under, **arg):
        key, value = under.items()[0]
        dataset = dataset.shake({key: value})
        return _p(dataset, **arg)
        
    if under:
        if len(under) != 1:
            raise Exception("Error under args")
        return _p_under(dataset, under, **arg)
    else:
        return _p(dataset, **arg)
    

def under(**arg):
    return arg