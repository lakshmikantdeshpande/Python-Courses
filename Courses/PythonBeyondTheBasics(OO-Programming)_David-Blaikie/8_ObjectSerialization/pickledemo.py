import pickle

mylist = ['1', '2', '3', 'a']

with open('filename.txt', 'wb') as handle:
	pickle.dump(mylist, handle)

with open('filename.txt', 'rb') as handle:
	unpickled = pickle.load(handle)

print(unpickled)
