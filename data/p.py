# coding=utf-8
from __future__ import absolute_import

from __future__ import division


# def P(dataset, under=None, **arg):
#     def _p(dataset, **arg):
#         count = 0
#         # key, value = arg.items()[0]
#         for data in dataset:
#             for key, value in arg.items():
#                 if dataset[data, key] == value:
#                     break
#             else:
#                 count += 1
#         return count / len(dataset)
#
#     def _p_under(dataset, under, **arg):
#         key, value = under.items()[0]
#         dataset = dataset.shake({key: value})
#         return _p(dataset, **arg)
#
#     if under:
#         if len(under) != 1:
#             raise Exception("Error under args")
#         return _p_under(dataset, under, **arg)
#     else:
#         return _p(dataset, **arg)
#
#
# def under(**arg):
#     return arg
    
    
def P(dataset, string):
    def _p(dataset, condition):
        count = 0
        for data in dataset:
            if dataset[data, condition[0]] == condition[1]
                count += 1
        return count / len(dataset)
        
    def _p_under(dataset, condition, under):
        dataset = dataset.shake({under[0]: under[1]})
        return _p(dataset, condition[0], condition[1])
        
    match = re.match(r'(?:(\w+=\w+))(?:\|((?:\w+=\w+)(?:\*(?:\w+=\w+))*))',
                     string)
    assert match
    condition, unders = match.groups()
    if not unders:
        return _p(dataset, condition)
    unders = unders.split('*')
    if len(under) == 1:
        under = unders[0]
        return _p_under(dataset, condition, under)
    else:
        p_under = 1
        p = 1
        for under in unders:
            p_under *= _p_under(dataset, condition, under)
            p *= _p(dataset, under)
        return _p(dataset, condition) * p_under / p
        
    # if '|' in string:
    #     under, condition = string.split('|')
    #     under = under.split('=')
    #     condition = condition.split('=')
    #     return _p_under(dataset, under[0],
    #         under[1], condition[0], condition[1])
    # else:
    #     condition = string.split('=')
    #     return _p(dataset, condition[0], condition[1])
        
        
        
P(dataset, under(a=1), b=2)
dataset.P("a=1|b=2")