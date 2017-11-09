class SumList(object):
    def __init__(self, this_list):
        self.mylist = this_list

    # we're changing the operator functionality for this class
    # We are broadcasting the sum operation
    def __add__(self, other):
        return SumList([x + y for x, y in zip(self.mylist, other.mylist)])

    def __repr__(self):
        return str(self.mylist)


list1 = SumList([1, 2, 8])
list2 = SumList([9, 8, 2])

list3 = list1 + list2
print(list3)
