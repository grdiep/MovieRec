import requests
import json
import tkinter as tk 
import CheckList as ck


# API call to TMHB -------------------------------

params = {"api_key": '78ad3cf3bc5f962e42fd7740e8cb33d0'}
r = requests.get("https://api.themoviedb.org/3/genre/movie/list", params=params)

data = r.json() # python dict
# print(data)

genre_dict = dict()

for genre in data['genres']: 
    id = genre['id']
    genre = genre['name']
    genre_dict[id] = genre
    

# TODO:Testing Checklist ------------------------------------
checkList = ck.CheckList(genre_dict)


