class MyNumber(object):
    def __init__(self, value):
        print('calling __init__')
        try:
            self.val = int(value)
        except ValueError:
            print('Oops! You didn\'t pass an integer. Setting val to 0')
            value = 0
        self.val = value

    def increment(self):
        self.val += 1


dd = MyNumber(5)
dd.increment()
dd.increment()
print(dd.val)
dd = MyNumber('hello')
print(dd.val)
