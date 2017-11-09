class OldClass():
    pass


class NewClass(object):
    pass


oc = OldClass()
nc = NewClass()

print(type(oc))
print(type(nc))

print(oc.__class__)
