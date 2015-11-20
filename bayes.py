
from data import DataSet
import re


def split_words(string):
    pattern = re.compile(r"(?!:[a-zA-Z]+)|([0-9]+(\.[0-9]+)?)")
    return re.findall(pattern, string)
    


if __name__ == "__main__":
    # labels = ['string']
    # dataset = [
    #     [1, 100, 3, 'good'],
    #     [2, 50, 2, 'good'],
    #     [4, 120, 3, 'good'],
    #     [4, 50, 3, 'bad'],
    #     [2, 30, 2, 'bad']
    # ]
    # dataset = DataSet(dataset, labels)
    # d_tree = tree(dataset)
    print split_words("qwe 234 asg qwer 234 sadf 324gfas fawe3 wefetqwt")
    