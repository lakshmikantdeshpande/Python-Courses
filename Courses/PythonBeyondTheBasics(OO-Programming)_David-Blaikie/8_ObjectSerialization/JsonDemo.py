import json

with open('temp.json') as handle:
	conf = json.load(handle)

print("BEFORE: ", conf)
conf['newkey'] = 5757
print("AFTER: ", conf)

with open('temp.json', 'w') as handle:
	json.dump(conf, handle)

