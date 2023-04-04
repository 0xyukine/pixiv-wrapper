class Bookmark:
	def __init__(self, json):
		self.id = None
		self.title = None
		self.tags = None
		self.userId = None
		self.userName = None
		self.pageCount = None
		self.create = None

		self.__dict__.update({k:v for k,v in json.items() if k in self.__dict__.keys() and v})

	def print(self):
		for k,v in self.__dict__.items():
			print(f"{k}:{v}")