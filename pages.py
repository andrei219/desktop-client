from tkinter import *
from tkinter import ttk 


import objects

class Partners(ttk.Frame):
    
    def __init__(self, **kw):
    
        super().__init__(**kw)   
        
        self.leftsection = ttk.Frame(self, relief=SUNKEN)

        self.leftsection_header = ttk.Frame(self.leftsection)
        
        self.leftsection_header_label = ttk.Label(self.leftsection_header, text='Filters')
        self.leftsection_header_label.configure(background='red')

        self.leftsection_content = ttk.Frame(self.leftsection)

        self.leftsection_content_label = ttk.Label(
            self.leftsection_content, text='No filters available in this section'
        )

        self.leftsection.grid(row=0, column=0)
        self.leftsection_header.grid(row=0, column=0)
        self.leftsection_content.grid(row=1, column=0)

        self.leftsection_header_label.pack()
        self.leftsection_content_label.pack()

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

