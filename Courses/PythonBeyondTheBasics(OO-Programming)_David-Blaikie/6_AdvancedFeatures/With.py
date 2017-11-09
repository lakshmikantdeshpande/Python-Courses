"""
    with automatically frees the unused resources
    eg.
        with open('file.txt') as file:
            file.write('hello')

"""


class MyClass(object):
    def __enter__(self):
        print('We have entered with')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('We\'re leaving with')

    def sayhi(self):
        print('Hi, instance {}'.format(id(self)))


with MyClass() as cc:
    cc.sayhi()
