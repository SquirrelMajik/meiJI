
from data import DataSet


if __name__ == "__main__":
    labels = ['string']
    dataset = [
        [1, 100, 3, 'good'],
        [2, 50, 2, 'good'],
        [4, 120, 3, 'good'],
        [4, 50, 3, 'bad'],
        [2, 30, 2, 'bad']
    ]
    dataset = DataSet(dataset, labels)
    d_tree = tree(dataset)
    