import tkinter as tk

class CheckList():

    genre_status_dict = dict()
    genre_list = []


    def __init__(self, genre_dict):
        self.window = tk.Tk()
        frame = tk.LabelFrame(self.window).pack()
        self.greeting = tk.Label(frame, text="I'm looking for a show within these genre(s):")
        self.greeting.pack()

        for key in genre_dict: # poulate the options for checkbox 
            var1 = tk.IntVar() # think of as a state that will change depending if checkbox clicked or not
            genre = genre_dict[key]
            c1 = tk.Checkbutton(frame, text=genre, variable=var1, onvalue=1, offvalue=0).pack(anchor='w')
            self.genre_status_dict[genre] = var1 #to check if checkboxes have been checked off 

        self.clearBtn = tk.Button(frame, text="Clear All", command=self.clearAll).pack()
        self.SelectAllBtn = tk.Button(frame, text="Select All", command=self.selectAll).pack()
        self.submitBtn = tk.Button(frame, text="Submit", command=self.submit).pack()

        self.window.mainloop() 

        
    def clearAll(self):
        if bool(self.genre_status_dict):
            pass
            print("list is empty")
        for item in self.genre_status_dict: 
            self.genre_status_dict[item].set(0)
        
        self.genre_list.clear()
        

    def selectAll(self):
        for item in self.genre_status_dict: 
            self.genre_status_dict[item].set(1)


    def submit(self): 
        for item in self.genre_status_dict: 
            if (self.genre_status_dict[item].get() == 1) & (item not in self.genre_list):
                self.genre_list.append(item)
        
        print(self.genre_list)
