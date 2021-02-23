from tkinter import *
from tkinter import ttk 


import objects

class Partners(ttk.Frame):
    
    def __init__(self, root, **kw):
    
        super().__init__(**kw)   
        
        self.leftsection = Frame(
            master=self, 
            relief=SUNKEN,
            background='red', 
            width=100
        )
        
        print(root.winfo_screenheight(), root.winfo_screenwidth())
        
        self.rightsection = Frame(
            self,
            relief=SUNKEN, 
            background='green',
        )

        self.leftsection.pack(side=LEFT, fill=BOTH, padx=[0, 10])
        self.rightsection.pack(side=RIGHT,fill=BOTH, padx=[10, 0])


class Agents(ttk.Frame):
    
    def __init__(self, **kw):

        super().__init__(**kw)

class Proformas(ttk.Frame):

    def __init__(self, **kw):

        super().__init__(**kw)


class Invoices(ttk.Frame):

    def __init__(self, **kw):
        
        super().__init__(**kw)

class Warehouse(ttk.Frame):
    
    def __init__(self, **kw):

        super().__init__(**kw)


class Rmas(ttk.Frame):

    def __init__(self, **kw):

        super().__init__(**kw)
    
class Tools(ttk.Frame):

    def __init__(self, **kw):

        super().__init__(**kw)

