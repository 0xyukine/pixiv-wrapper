#https://www.pixiv.net/ajax/user/{id}?full=1&lang=en
class FullUser:
	def __init__(self, json):
		self.userId = None 			#String Integer
		self.name = None 			#String
		self.image = None 			#String
		self.imageBig = None 		#String
		self.premium = None 		#Boolean
		self.isFollowed = None 		#Boolean
		self.isMyPixiv = None 		#Boolean
		self.isBlocking = None 		#Boolean
		self.background = None 		#String
		self.sketchLiveId = None 	#String
		self.partial = None 		#Integer
		self.acceptReqest = None 	#Boolean
		self.sketchLives = None 	#Array
		self.following = None 		#Boolean
		self.followedBack = None 	#Boolean
		self.comment = None 		#String
		self.commentHtml = None 	#String
		self.webpage = None 		#String
		self.social = None 			#JSON 	#dict[site] -> url
		self.region = None 			#JSON 	#name, region, prefecture, privacyLevel
		self.age = None 			#JSON 	#name, privacyLevel
		self.birthday = None 		#JSON 	#name, privacyLevel
		self.gender = None 			#JSON 	#name, privacyLevel
		self.job = None 			#JSON 	#name, privacyLevel
		self.workspace = None 		#String
		self.official = None 		#Boolean
		self.group = None 			#JSON	#array -> id, title, iconurl

		self.__dict__.update(json)

class User:
	def __init__(self, json):
		self.userId = None 			#String Integer
		self.name = None 			#String
		self.isFollowed = None 		#Boolean
		self.isMyPixiv = None 		#Boolean
		self.following = None 		#Boolean
		self.followedBack = None 	#Boolean
		self.comment = None 		#String
		self.commentHtml = None 	#String
		self.webpage = None 		#String
		self.social = None 			#JSON 	#dict[site] -> url

		self.__dict__.update({k:v for k,v in json.items() if v})

#https://www.pixiv.net/ajax/user/{artist_id}/works/latest?lang=en
class FullWorks:
	def __init__(self, json):
		self.illusts = None 		#JSON 	#dict[id]
		self.novels = None 			#Array

#https://www.pixiv.net/ajax/illust/{Post ID}
class FullIllustration:
	def __init__(self, json):
		self.illustId = None				#String Integer
		self.illustTitle = None				#String
		self.illustComment = None			#String
		self.id = None						#String Integer
		self.title = None					#String
		self.description = None				#String
		self.illustType = None				#Integer
		self.createDate = None				#String yyyy-mm-ddThh:mm:ssz (Zulu time, ISO 8601?) 
		self.uploadDate = None				#String yyyy-mm-ddThh:mm:ssz
		self.restrict = None				#Integer
		self.xRestrict = None				#Integer
		self.sl = None						#Integer
		self.urls = None 					#mini, thumb, small, regular, original
		self.tags = None 					#authorId, isLocked, {tags} -> tag,locked,deleteable,userId,userName, writable
		self.alt = None						#String
		self.storableTags = None			#JSON #Number:Hash
		self.userId = None					#String
		self.userName = None				#String
		self.userAccount = None				#String
		self.userIllusts = None				#JSON #IllustID
		self.likeData = None				#Boolean
		self.width = None					#Integer
		self.height = None					#Integer
		self.pageCount = None				#Integer
		self.bookmarkCount = None			#Integer
		self.likeCount = None				#Integer
		self.commentCount = None			#Integer
		self.responseCount = None			#Integer
		self.viewCount = None				#Integer
		self.bookStyle = None				#String
		self.isHowTo = None					#Boolean
		self.isOriginal = None				#Boolean
		self.imageResponseOutData = None	#Array
		self.imageResponseData = None		#Array
		self.imageResponseCount = None		#Integer
		self.pollData = None
		self.seriesNavData = None
		self.descriptionBoothId = None
		self.descriptionYoutubeId = None
		self.comicPromotion = None
		self.fanboxPromotion = None 		#add new class
		self.contestBanners = None			#Array
		self.isBookmarkable = None			#Boolean
		self.bookmarkData = None
		self.contestData = None
		self.zoneConfig = None #add new class
		self.extraData = None #add new class
		self.titleCaptionTranslation = None #workTitle, workCaption
		self.isUnlisted = None				#Boolean
		self.request = None
		self.commentOff = None				#Integer

#https://www.pixiv.net/ajax/illust/82954344/pages?lang=en #illust images
class Illustration:
	def __init__(self, json):
		self.urls = None	#JSON #thumb_mini,small,regular,original
		self.width = None	#Integer
		self.height = None	#Integer

		self.__dict__.update(json)

#https://www.pixiv.net/ajax/user/{id}/illusts/bookmarks?tag=&offset={offset}&limit={page_limit}&rest=show&lang=en
class FullBookmarks:
	def __init__(self, json):
		self.works 			= None #array of work dictionaries
		self.total 			= None #Integer
		self.zoneConfig 	= None #add new class
		self.extraData		= None #add new class
		self.bookmarkTags	= None #array

		self.__dict__.update(json)

class FullSingleWork:
	def __init__(self, json):
		self.id = None #String Integer
		self.title = None #String
		self.illustType = None #Integer
		self.xRestrict = None #Integer
		self.restrict = None #Integer
		self.sl = None #Integer
		self.url = None #String
		self.description = None #String
		self.tags = None #JSON #count:tag
		self.userId = None #String
		self.userName = None #String
		self.width = None #Integer
		self.height = None #Integer
		self.pageCount = None #Integer
		self.isBookmarkable = None #Boolean
		self.bookmarkData = None #JSON #id, private
		self.alt = None #String
		self.titleCaptionTranslation = None #JSON #workTitle, workCaption
		self.createDate = None #Date
		self.updateDate = None #Date
		self.isUnlisted = None #Boolean
		self.isMasked = None #Boolean
		self.profileImageUrl = None #String

class SingleWork:
	def __init__(self, json):
		self.id = None #String Integer
		self.title = None #String
		self.description = None #String
		self.tags = None #JSON #count:tag
		self.pageCount = None #Integer

class FanboxPromotion:
	def __init__(self, json):
		self.userName			= None #String
		self.userImageUrl		= None #String
		self.description		= None #String
		self.imageUrl			= None #String
		self.imageUrlMobile		= None #String
		self.hasAdultContent	= None #Boolean

class ZoneConfig:
	pass

class ExtraData: #meta
	def __init__(self, json):
		self.title 				= None #String
		self.description 		= None #String
		self.canonical 			= None #String
		self.ogp 				= None #JSON #description, image, title, type
		self.twitter 			= None #JSON #description, image, title, type
		self.alternateLanguages = None #JSON #ja, en
		self.descriptionHeader 	= None #String