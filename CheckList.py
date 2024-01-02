import tkinter as tk

class CheckList():

    list1 = dict()
    list2 = []

    def __init__(self, genre_dict):
        self.window = tk.Tk()
        self.greeting = tk.Label(text="I'm looking for a show within these genre(s):")
        self.greeting.pack()

        for key in genre_dict: # poulate the options for checkbox 
            var1 = tk.IntVar() # think of as a state that will change depending if checkbox clicked or not
            genre = genre_dict[key]
            c1 = tk.Checkbutton(self.window, text=genre, variable=var1, onvalue=1, offvalue=0).pack(anchor='w')
            self.list1[genre] = var1 #to check if checkboxes have been checked off 

        self.clearBtn = tk.Button(text="Clear All", command=self.clearAll).pack()
        self.SelectAllBtn = tk.Button(text="Select All", command=self.selectAll).pack()
        self.submitBtn = tk.Button(text="Submit", command=self.submit).pack()

        self.window.mainloop() 

        
    def clearAll(self):
        if bool(self.list1):
            pass
            print("list is empty")
        for item in self.list1: 
            self.list1[item].set(0)
        
        self.list2.clear()
        

    def selectAll(self):
        for item in self.list1: 
            self.list1[item].set(1)

    def submit(self): 
        for item in self.list1: 
            if (self.list1[item].get() == 1) & (item not in self.list2):
                self.list2.append(item)
        
        print(self.list2)

