import requests

#practice with free api --> public Api

#get user 
# url = "https://api.freeapi.app/api/v1/public/randomusers"
# querystring = {"page":"1","limit":"10"}
# headers = {"accept": "application/json"}
# response = requests.get(url, headers=headers, params=querystring)
# print(response.json())


#get user by id
# url = "https://api.freeapi.app/api/v1/public/randomusers?userId=13"
# headers = {"accept": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.json())


#get random user
# url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
# headers = {"accept": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.json())


#get product 
# url = "https://api.freeapi.app/api/v1/public/randomproducts"
# headers = {"accept": "application/json"}
# querystring = {"page":"1", "limit":"10", "inc":"category,price,thumbnail,images,title,id", "query":"mens-watches"}
# response = requests.get(url, headers=headers, params=querystring)
# print(response.json())


#get product by id
# url = "https://api.freeapi.app/api/v1/public/randomproducts?productId=30"
# headers = {"accept": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.json())


#get a random product 
# url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
# headers = {"accept": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.json())


#get channel details
# url = "https://api.freeapi.app/api/v1/public/youtube/channel"
# headers =  {"accept": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.json())


#get youtube videos
# url = "https://api.freeapi.app/api/v1/public/youtube/videos"
# headers =  {"accept": "application/json"}
# querystring = {"page":"1", "limit":"10", "query":"javascript", "sortBy":"keep one: mostLiked | mostViewed | latest | oldest"}
# response = requests.get(url, params=querystring, headers=headers)
# print(response.json())


#get video by id 
# url = "https://api.freeapi.app/api/v1/public/youtube/videos/EQwmQLU1S6I"
# headers =  {"accept": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.json())


#get video comments
# url = "https://api.freeapi.app/api/v1/public/youtube/comments/cv-6bAeYsOY"
# headers =  {"accept": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.json())


#get related video 
# url = "https://api.freeapi.app/api/v1/public/youtube/related/eLyISYdoVac"
# headers =  {"accept": "application/json"}
# querystring = {"page":"1", "limit":"5"}
# response = requests.get(url, params=querystring, headers=headers)
# print(response.json())


#get playlists
# url = "https://api.freeapi.app/api/v1/public/youtube/playlists"
# headers =  {"accept": "application/json"}
# querystring = {"page":"1", "limit":"5"}
# response = requests.get(url, params=querystring, headers=headers)
# print(response.json())


# Get playlist details and items
# url = "https://api.freeapi.app/api/v1/public/youtube/playlists/PLRAV69dS1uWSx4erHGq8hW_GE-Eaj60r-"
# headers =  {"accept": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.json())



#kitchen sink 

#get request
# url = "https://api.freeapi.app/api/v1/kitchen-sink/http-methods/get"
# headers = {"accept": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.json())


#post request
# url = "https://api.freeapi.app/api/v1/kitchen-sink/http-methods/post"
# headers = {"accept": "application/json"}
# response = requests.post(url, headers=headers)
# print(response.json())


#send jpeg format
# url = "https://api.freeapi.app/api/v1/kitchen-sink/image/jpeg"
# response = requests.get(url)
# print(response.json())


#set cookie
# url = "https://api.freeapi.app/api/v1/kitchen-sink/cookies/set"
# payload = { "foo": "bar" }
# headers = {
#     "accept": "application/json",
#     # "content-type": "application/json"                    it's okay with that if i don't use content type
# }
# response = requests.post(url, json=payload, headers=headers)
# print(response.json())


#github login 
# url = "https://api.freeapi.app/api/v1/users/github"
# response = requests.get(url)
# print(response.json())

