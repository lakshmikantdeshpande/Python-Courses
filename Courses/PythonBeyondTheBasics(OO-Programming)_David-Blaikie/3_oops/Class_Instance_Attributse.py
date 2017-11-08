# Lookup = instance -> class


class YourClass(object):
    classy = 'Class Value'  # class variable


dd = YourClass()

print(dd.classy)  # prints class variable

dd.classy = 'Instance Value'
print(dd.classy)  # prints instance variable

del dd.classy
print(dd.classy)  # prints class variable
