import requests
import json
from tkinter import *
from tkinter import messagebox as mb



params = {"api_key": '78ad3cf3bc5f962e42fd7740e8cb33d0'}
r = requests.get("https://api.themoviedb.org/3/genre/movie/list", params=params)

data = r.json() # python dict
# print(data)

genre_dict = dict()

for item in data['genres']: 
    id = item['id']
    genre = item['name']
    genre_dict[id] = genre
    
# print(genre_dict)




