import os


class ConfigDictionary(dict):
    def __init__(self, filename):
        self._filename = filename
        if os.path.isfile(self._filename):
            with open(self._filename) as handle:
                for line in handle:
                    line = line.rstrip()
                    key, value = line.split('=', 1)
                    dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as file:
            for key, val in self.items():
                file.write('{}={}\n'.format(key, val))


cc = ConfigDictionary('dictionary.txt')
cc['hello'] = 'xyz'
print(cc['hello'])
