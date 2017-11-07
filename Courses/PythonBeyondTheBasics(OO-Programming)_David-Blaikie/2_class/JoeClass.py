class Joe(object):
    greeting = 'Hello Joe'

    def callme(self):
        print("Calling 'CallMe' method with instance : ")
        print(self)


this_joe = Joe()
print(this_joe.greeting)

this_joe.callme()
print(this_joe)
