class MyError(Exception):
    def __init__(self, *args):
        print('calling init')
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('Calling str')
        if self.message:
            return "Here's MyError exception with message: {0}".format(self.message)
        else:
            return "Here's a MyError exception"


raise MyError()
# raise MyError('Houston, we have a problem')
