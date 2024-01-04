import requests
import json
import tkinter as tk 
import CheckList as ck

voting_avg = 9
# API call to get genres from TMHB -------------------------------

params = {"api_key": '78ad3cf3bc5f962e42fd7740e8cb33d0'}
r = requests.get("https://api.themoviedb.org/3/genre/movie/list", params=params)

data = r.json() # python dict
# print(data)

genre_dict = dict()

for genre in data['genres']: 
    id = genre['id']
    genre = genre['name']
    genre_dict[id] = genre

# print(genre_dict)    

# converting genre name to its ID --------------------------------------

def genreID_conversion(genre_list):
    # take the list 2 which contains our genre of interest 
    # and compare it to our genre_dict 
    # convert genre name >> genre_ID 
    genreID_list = []
    for genre in genre_list:
        for genre_ID in genre_dict:
            if genre_dict[genre_ID] == genre:
                genreID_list.append(genre_ID)
                break

    return genreID_list


# calling Checklist class ------------------------------------

checkList = ck.CheckList(genre_dict)
genreID_list = genreID_conversion(checkList.genre_list)
print(genreID_list)


#TODO: API call to discover API  -----------------------------------

params = {"api_key": '78ad3cf3bc5f962e42fd7740e8cb33d0', 
          "sort_by": 'vote_average.asc',
          "vote_average.gte": voting_avg,
          "with_genres": genreID_list}

r = requests.get("https://api.themoviedb.org/3/discover/movie", params=params)
data = r.json()

for item in data['results']:
    movieTitle = item['original_title']
    # print(movieTitle) 

    overview = item['overview']
    # print(overview)

    file_path = item['poster_path']
    # print(file_path)

# full image URL: https://image.tmdb.org/t/p/w500/ + filepath!! 

# ---------------------------------------







