import os


class ConfigDictionary(dict):
    def __init__(self, filename):
        self._filename = filename
        if os.path.isfile(self._filename):
			try:
				open(self.filename, 'w').close()
			except IOError:
				raise IOError('invalid filename specified')

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

	def __getitem__(self, key):
		if not key in self:
			raise ConfigKeyError(self, key)
		return dict.__getitem__(self, key)


class ConfigKeyError(Error):
	def __init__(self, this, key):
		self.key = key
		self.keys = this.keys()
	
	def __str__(self):
		return 'key {0} not found. Available keys: {1}'.format(self.key, ', '.join(self.keys))


cc = ConfigDictionary('dictionary.txt')
cc['hello'] = 'xyz'
print(cc['hello'])
