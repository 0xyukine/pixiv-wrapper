class IllustBasic:
	def __init__(self, json):
		self.illustId = None
		self.illustTitle = None
		self.illustComment = None
		self.uploadDate = None
		self.bookmarkCount = None
		self.likeCount = None
		self.userId = None
		self.userName = None

		self.__dict__.update({k:v for k,v in json.items() if k in self.__dict__.keys() and v})

		self.tags = {}

		print(json["tags"])
		for tag in json["tags"]["tags"]:
			self.tags[tag["tag"]] = Tags(tag)

	def print(self):
		for k,v in self.__dict__.items():
			print(f"{k}:{v}")

class Tags:
	def __init__(self, json):
		self.tag = None
		self.locked = None
		self.deletable = None
		self.userId = None
		self.userName = None
		self.romaji = None
		self.translation = None

		self.__dict__.update({k:v for k,v in json.items() if k in self.__dict__.keys() and v})

class Images:
	def __init__(self, json):
		self.original = json["urls"]["original"]
		self.width = None
		self.height = None

		self.__dict__.update({k:v for k,v in json.items() if k in self.__dict__.keys() and v})