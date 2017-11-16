import timeit

print('By Index: ', timeit.timeit(stmt="mydict['c']", setup="mydict={'b':5,'c':'s'}", number=100000))

print('By Get: ', timeit.timeit(stmt="mydict.get('c')", setup="mydict={'b':5, 'c':'s'}", number=100000))

