from structs import FullUser, User, FullWorks, FullIllustration, Illustration, FullBookmarks, FullSingleWork, SingleWork, FanboxPromotion, ZoneConfig, ExtraData
import requests
import json

def GetUser(session, userID):
	r = session.get("https://www.pixiv.net/ajax/user/{}?full=1&lang=en".format(userID))
	if r.json()["error"] == True:
		raise Exception("{}: {}".format(r.status_code, r["message"]))
	else:
		return User(r.json()["body"])

def GetFullUser(session, userID):
	r = session.get("https://www.pixiv.net/ajax/user/{}?full=1&lang=en".format(userID))
	if r.json()["error"] == True:
		raise Exception("{}: {}".format(r.status_code, r["message"]))
	else:
		return FullUser(r.json()["body"])

def GetWorks(session, artistID):
	r = session.get("https://www.pixiv.net/ajax/user/{}/works/latest?lang=en".format(artistID))
	if r.json()["error"] == True:
		raise Exception("{}: {}".format(r.status_code, r["message"]))
	else:
		return 

def GetBookmarks(session, userID, offset=0, pageLimit=48):
	r = session.get("https://www.pixiv.net/ajax/user/{}/illusts/bookmarks?tag=&offset={}&limit={}&rest=show&lang=en".format(userID, offset, pageLimit))
	if json.loads(r.text)["error"] == True:
		raise Exception("{}: {}".format(r.status_code, r.json()["message"]))
	else:
		return FullBookmarks(r.json()["body"])

def GetIllustration(session, illustID):
	r = session.get("https://www.pixiv.net/ajax/illust/{}".format(illustID))
	if r.json()["error"] == True:
		raise Exception("{}: {}".format(r.status_code, r["message"]))
	else:
		return 

def GetImages(session, illustID):
	r = session.get("https://www.pixiv.net/ajax/illust/{}/pages?lang=en".format(illustID))
	if r.json()["error"] == True:
		raise Exception("{}: {}".format(r.status_code, r["message"]))
	else:
		images = []
		for image in r.json()["body"]:
			images.append(Illustration(image))
		return images