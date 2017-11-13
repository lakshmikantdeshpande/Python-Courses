import yaml

mydict = {'a' : 1, 'b' : 2}
mylist = [1, 2, 3, 4, 5]
mytuple = (1, 'b', 'c')

loaded_yaml = yaml.dump(mydict, default_flow_style=False)
print(loaded_yaml)

print(yaml.dump(mylist, default_flow_style=False))

print(yaml.dump(mytuple, default_flow_style=False))

