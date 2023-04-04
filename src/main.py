import methods.getmethods
import structs.illustration
import structs.bookmark
import requests
import json
import os

class PixivWrapper:
	def __init__(self, user_id="111111", session_cookie=""):
		if session_cookie == "":
			print("No session cookie provided. Personal and contentious content will be unavailable until one is provided.")

		self.user_id = user_id
		self.session = requests.Session()
		self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0', 'referer': "https://www.pixiv.net/", 'Cookie':session_cookie})

	def get_session_cookie():
		pass

	def get_user():
		pass

	def get_bookmarks():
		pass

	def get_following():
		pass

	def get_illust_preview():
		if type(illust_ids) == list:
			ids = f"&ids[]={illust_ids[0]}"
			for x in illust_ids[1:]:
				ids = ids + f"&ids[]={x}"
		else:
			ids = f"&ids[]={illust_ids}"

	def get_illust_basic():
		pass

	def get_illust_images():
		pass

	def get_illust():
		pass

"""
x = structs.illustration.IllustBasic(methods.getmethods.get_illust(s, 105021185).json()["body"])
x.print()

for k,v in x.tags.items():
	print(k,v.romaji)

images = []
w = methods.getmethods.get_illust_images(s, 105021185).json()
print(w)
for x in methods.getmethods.get_illust_images(s, 105021185).json()["body"]:
	images.append(structs.illustration.Images(x))

print(images[0].original)
x = methods.getmethods.get_bookmarks(s, 48523658, 0, 1).json()
x = structs.bookmark.Bookmark(x["body"]["works"][0]).id
print()

bookmarks = {}
errors = []

offset = 0
while True:
	print(offset)
	x = methods.getmethods.get_bookmarks(s, 48523658, offset, 100).json()
	if x["error"] == "true":
		break
	else:
		for bm in x["body"]["works"]:
			bm = structs.bookmark.Bookmark(bm)
			images = []
			for image in methods.getmethods.get_illust_images(s, bm.id).json()["body"]:
				images.append(structs.illustration.Images(image).original)
			bookmarks[bm.id] = {"id":bm.id, "title":bm.title, "tags":bm.tags, "userId":bm.userId, "user":bm.userName, "images":images}

	if offset + 100 > x["body"]["total"]:
		break
	else:
		offset += 100

with open("bms.json", "w") as file:
	json.dump(bookmarks, file, indent=4)
"""