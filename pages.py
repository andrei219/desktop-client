from tkinter import *
from tkinter import ttk 


import objects

class Partners(ttk.Frame):
    
    def __init__(self, root, **kw):
    
        super().__init__(**kw)   
        
        self.leftsection = Frame(
            master=self, 
            relief=RIDGE,
            width=root.winfo_height() - 20, 
            background='green',
        )

        self.right_section = Frame(
            master=self, 
            width= root.winfo_width() - 20, 
            relief = RIDGE, 
            background='red'
        )
        
        self.leftsection.pack(side=LEFT, fill=Y, expand=True)
        self.right_section.pack(side=LEFT, fill=Y, expand=True)

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

