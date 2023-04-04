import requests

BASE_URL = "https://www.pixiv.net"

def get_user():
	pass

def get_bookmarks(session, user_id, offset, post_limit):
	return session.get(f"{BASE_URL}/ajax/user/{user_id}/illusts/bookmarks?tag=&offset={offset}&limit={post_limit}&rest=show&lang=en")

#/ajax/user/48523658/following?offset=24&limit=24&rest=show&tag=&acceptingRequests=0&lang=en&version=ee57a9ee72abc13ad00d807c0a7a5ecde735f71b
def get_following(session, user_id, params):
	return session.get(f"{BASE_URL}/ajax/user/{user_id}/following?{params}")

#https://www.pixiv.net/ajax/follow_latest/illust?p=1&mode=all&lang=en&version=0032d4bcb39dd63e18bebdca0ab7e80167604a5c
def get_following_latest(session, page):
	return session.get(f"{BASE_URL}/ajax/follow_latest/illust?p={page}")

#https://www.pixiv.net/ajax/user/4780277/illusts?ids[]=104831162&ids[]=104753590&ids[]=104701028&ids[]=104624617 #mini illust preview, basic info, thumbnail images
def get_illust_preview(session, user_id, illust_ids):
	return session.get(f"{BASE_URL}/ajax/user/{user_id}/illusts?{ids}")

#https://www.pixiv.net/ajax/illust/105021185 #full illust information
def get_illust(session, illust_id):
	return session.get(f"{BASE_URL}/ajax/illust/{illust_id}")

def get_illust_images(session, illust_id): #https://www.pixiv.net/ajax/illust/105021185/pages?lang=en&version=ee57a9ee72abc13ad00d807c0a7a5ecde735f71b #actual images
	return session.get(f"{BASE_URL}/ajax/illust/{illust_id}/pages")