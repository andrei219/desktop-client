from tkinter import *
from tkinter import ttk 

from copy import deepcopy

import objects

class Partners(ttk.Frame):
    
    def __init__(self, **kw):
    
        super().__init__(**kw)   
        
        self.bold_active = False

        # LEFT SECTION : 
        self.left_section = Frame(
            self,
            borderwidth = 1, 
            highlightcolor = 'black',
            relief=RAISED, 
            background='white', 
        )

        self.left_section_header = Frame(
            self.left_section, 
            borderwidth = 1, 
            highlightcolor='black',
            relief=RAISED, 
        )

        self.left_section_header_label = Label(
            self.left_section_header,
            text='Filters',
            font = ('Bahnscrif', 10, 'italic'),
            background='#e0dcdc'
        )

        self.left_section_message = Label(
            self.left_section, 
            text = 'No filters available\nin this section', 
            background='white',
            font = ('Bahnschrif', 10)
        )

        self.left_section_header_label.bind('<Button-1>', self.make_bold)

        self.left_section.pack(side=LEFT, fill=Y, padx=[0, 20])
        self.left_section_header.pack(side=TOP, fill=X)
        self.left_section_header_label.pack(ipadx=50)
        self.left_section_message.pack(pady=30)

        # Right section: 
        self.right_section = Frame(
            self,
            borderwidth = 1, 
            highlightcolor = 'black', 
            relief = RAISED, 
            background = 'white'
        )

        self.right_section_header = Frame(
            self.right_section, 
            borderwidth = 1, 
            highlightcolor = 'black', 
            relief = RAISED, 
            background = '#e0dcdc'
        )

        
        self.header_labels = [
            
            Label(
                self.right_section_header, 
                text = 'Code', 
                font = ('Bahnscrif', 10),
                background = '#e0dcdc'
            ),
            Label (
                self.right_section_header, 
                text = 'Partner', 
                font = ('Bahnscrif', 10), 
                background = '#e0dcdc'
            ), 
            Label (
                self.right_section_header, 
                text = 'Country', 
                font = ('Bahnschrif', 10), 
                background = '#e0dcdc'
            ), 
            Label(
                self.right_section_header, 
                text = 'Contact', 
                font = ('Bahnschrif', 10), 
                background = '#e0dcdc', 
            ),
            Label(
                self.right_section_header, 
                text = 'Fiscal Nº', 
                font = ('Bahnschrif', 10), 
                background = '#e0dcdc'
            ),
            Label(
                self.right_section_header, 
                text = 'Phone Nº', 
                font = ('Bahnschrif', 10), 
                background = '#e0dcdc'
            ), 

            Label(
                self.right_section_header, 
                text = 'E-Mail', 
                font = ('Bahnschrif', 10), 
                background = '#e0dcdc'
            )
        ]
        
        self.right_section.pack(side= LEFT, fill=BOTH, expand=True)
        self.right_section_header.pack(side=TOP, fill=X )
        
        for label in self.header_labels:
            label.bind('<Button-1>', self.make_bold)
            label.pack(side=LEFT,fill=X, expand=True)
    

    def make_bold(self, event):
        widget = event.widget
        if 'Filters' == widget['text']:
            if 'bold' in widget['font']:
                widget['font'] = ('Bahnschrif', 10, 'italic')
            else:
                widget['font'] = ('Bahnschrif', 10, 'italic bold')
        else:
            if 'bold'  not in ''.join([ label['font'] for label in self.header_labels]):
                widget['font'] = ('Bahnschrif', 10, 'bold')
                for label in self.header_labels:
                    if 'bold' in label['font']:
                        self.order_partners_by(key=label['text'])
            else:
                if 'bold' in widget['font']:
                    widget['font'] = ('Bahnschrif', 10)
                    self.order_partners_by(key=None)

    def order_partners_by(self, key=None):
        """Key == None means no order, otherwhise, map the key with a property of the partner object and order it"""
        
        
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

