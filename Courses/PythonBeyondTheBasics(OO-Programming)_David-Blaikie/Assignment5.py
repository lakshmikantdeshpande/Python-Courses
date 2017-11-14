import os


class ConfigKeyError(Exception):
	def __init__(self, this, key):
		self.key = key
		self.keys = this.keys()
	
	def __str__(self):
		return 'key {0} not found. Available keys: {1}'.format(self.key, ', '.join(self.keys))


class ConfigPickleDict(dict):
	config_dir = '~/Desktop/'

	def __init(self, picklename):
		self._filename = os.path.join(ConfigPickleDict.config_dir, picklename + '.pickle')
		if not os.path.isfile(self._filename):
			with open(self._filename, 'w') as handle:
				pickle.dump({}, handle)
		with open(self._filename) as handle:
			pkl = pickle.load(handle)
			self.update(pkl)
	
	def __getitem__(self, key):
		if not key in self:
			raise ConfigKeyError(self, key)
		return dict.__getitem__(self, key)
	
	def __setitem__(self, key):
		dict.__setitem__(self, key, value)
		with open(self._filename, 'w') as handle:
			pickle.dump(self, handle)
			

cc = ConfigPickleDict('dictionary.txt')
cc['hello'] = 'xyz'
print(cc['hello'])
