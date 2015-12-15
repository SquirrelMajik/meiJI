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
    def _p_c(dataset, condition):
        count = 0
        for data in dataset:
            if dataset[data, condition[0]] == condition[1]
                count += 1
        return count / len(dataset)
        
    def _p_c_u(dataset, condition, under):
        dataset = dataset.shake({under[0]: under[1]})
        return _p_c(dataset, condition[0], condition[1])
        
    def _p_cs(dataset, conditions):
        return mul([_p_c(dataset, condition) for condition in conditions])
        
    def _p_cs_u(dataset, conditions, under):
        return mul([_p_c_u(dataset, condition, under) \
            for condition in conditions])
            
    def _p_c_us(dataset, condition, unders):
        return _p_cs_u(dataset, unders, condition) * _p_c(dataset, condition) \
            / mul(_p_c(under) for under in unders)
            
    def _p_cs_us(dataset, conditions, unders):
        if not unders:
            return _p_cs(conditions)
        return mul(_p_c_us(dataset, condition, unders) \
            for condition in conditions)
            
    reg = r'(?:(\w+=\w+)(?:\*(?:\w+=\w+))*))' + \
          r'(?:\|((?:\w+=\w+)(?:\*(?:\w+=\w+))*))'
    match = re.match(reg, string)
    assert match
    conditions, unders = match.groups()
    return _p_cs_us(dataset, conditions, unders)
    # if not unders:
    #     return _p(dataset, condition)
    # unders = unders.split('*')
    # if len(under) == 1:
    #     under = unders[0]
    #     return _p_under(dataset, condition, under)
    # else:
    #     p_under = 1
    #     p = 1
    #     for under in unders:
    #         p_under *= _p_under(dataset, condition, under)
    #         p *= _p(dataset, under)
    #     return _p(dataset, condition) * p_under / p
        
    # if '|' in string:
    #     under, condition = string.split('|')
    #     under = under.split('=')
    #     condition = condition.split('=')
    #     return _p_under(dataset, under[0],
    #         under[1], condition[0], condition[1])
    # else:
    #     condition = string.split('=')
    #     return _p(dataset, condition[0], condition[1])
        
        
def mul(l):
    reduce(lambda x,y: x*y, l, 1)