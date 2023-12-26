import requests
import json
import tkinter as tk 


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
    

# create a new class for the tkinter(?) --------------------- 
    
window = tk.Tk()
greeting = tk.Label(text="I'm looking for a show within these genre(s):")
greeting.pack()

list1 = dict()

for key in genre_dict: # poulate the options for checkbox 
    var1 = tk.IntVar() # think of as a state that will change depending if checkbox clicked or not
    genre = genre_dict[key]
    c1 = tk.Checkbutton(window, text=genre, variable=var1, onvalue=1, offvalue=0).pack(anchor='w')
    list1[genre] = var1

def clearAll():
    if bool(list1):
        pass
        print("list is empty")
    for item in list1: 
        list1[item].set(0)

#clear button 
clearBtn = tk.Button(text="Clear", command=clearAll).pack()

def selectAll():
    for item in list1: 
        list1[item].set(1)
    
#select all button 
SelectAllBtn = tk.Button(text="Select All", command=selectAll).pack()

def submit(): 
    list2 = [] 
    for item in list1: 
        if list1[item].get() == 1:
            list2.append(item)

    print(list2)

#submit button
submitBtn = tk.Button(text="Submit", command=submit)
submitBtn.pack()

window.mainloop()

# ------------------------

