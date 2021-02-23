from tkinter import *
from tkinter import ttk 


import objects

class Partners(ttk.Frame):
    
    def __init__(self, root, **kw):
    
        super().__init__(**kw)   
        
        width = int(root.winfo_screenwidth() * 0.7 )

        self.leftsection = Frame(
            master=self, 
            relief=RIDGE,
            width= int(width * 0.10),
            #background='green',
        )

        self.right_section = Frame(
            master=self, 
            width = int(width * 0.90),
            relief = RIDGE, 
            #background='white'
        )
        

        self.leftsection.pack(side=LEFT, fill=BOTH, padx=[1,10], pady=1,  expand=True)
        self.right_section.pack(side=LEFT, fill=BOTH,padx=[10,1], pady=1,  expand=True)

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

