
from tkinter import * 
from tkinter import ttk 

import os 

def buildlabels_list(master, l, object):
    #breakpoint()
    object.label_objects = [
        Label(
            master, 
            text = name, 
            background = '#e0dcdc', 
            font = ('Bahnschrif', 10)
        ) for name in l 
    ]

    object.order_context = {}
    for name in [label['text'] for label in object.label_objects]:
        object.order_context[name] = 0 

    for label in object.label_objects:
        label.bind('<Button-1>', object.sortrequest)
        label.pack(side=LEFT, fill=X, expand=True)


class BaseClass(ttk.Frame):
    
    def __init__(self, root, notebook, **kw):
        
        super().__init__(**kw)
        
        self.root = root 
        self.notebook = notebook    

        self.image = PhotoImage(file = os.path.join('icons', 'warehouse.png'))

        self.setmodel()

        # LEFT SECTION : 
        self.left = Frame(
            self,
            borderwidth = 1, 
            highlightcolor = 'black',
            relief=RAISED, 
            background='white', 
        )

        self.left_header = Frame(
            self.left, 
            borderwidth = 1, 
            highlightcolor='black',
            relief=RAISED, 
        )

        self.left_header_label = Label(
            self.left_header,
            text='Filters',
            font = ('Bahnscrif', 10, 'italic'),
            background='#e0dcdc'
        )

        self.left.pack(side=LEFT, fill=Y, padx=[0, 20])
        self.left_header.pack(side=TOP, fill=X)
        self.left_header_label.pack(ipadx=50)

        self.right = Frame(
            self, 
            borderwidth = 1, 
            highlightcolor = 'black', 
            relief = RAISED, 
            background = 'white'
        )

        self.right_header = Frame(
            self.right, 
            borderwidth = 1, 
            highlightcolor = 'black', 
            relief = RAISED,
            background = '#e0dcdc'
        )


        self.right_content = Frame(
            self.right,  
            background = 'white',
            borderwidth = 1, 
            relief = RAISED, 
            highlightcolor = 'black'
        )
        
        self.buttons = Frame(
            self.right, 
            background = 'white', 
            relief = RAISED, 
        )

        self.listbox = Listbox(self.right_content, listvariable=self.listboxmodel, border=0)
        self.listbox['font'] = ('Bahnschrif', 10)
        
        self.scroll = Scrollbar(self.right_content, orient=VERTICAL, command=self.listbox.yview)
        self.listbox['yscrollcommand'] = self.scroll.set
        
        self.right.pack(side=RIGHT, fill=BOTH, expand=True)
        
        self.right_header.pack(side=TOP, fill=X)
        
        self.right_content.pack(side=TOP, fill=BOTH, expand=True)
        
        self.buttons.pack(side=BOTTOM, fill=X)

        self.setheader()
        self.setbuttons()

        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)
        self.scroll.pack(side=RIGHT, fill=BOTH)
    

    def setbuttons(self):
        for i in range(5):
            Button(
                self.buttons, 
                background = 'white', 
                borderwidth = 0, 
                image = self.image,
            ).pack(side=LEFT, padx=20, pady=10)


    def sortrequest(self, event):
        label = event.widget
        if 'bold' in label['font']:
            key = label['text']
            if self.order_context[key]:
                self.sortby(key,ascending=False)
                self.order_context[key] = 0
            else:
                self.sortby(key)
                self.order_context[key] = 1 
        else:
            for l in self.label_objects:
                l['font'] = ('Bahnschrif', 10)
                label['font'] = ('Bahnschrif', 10, 'bold')
            self.sortrequest(event)

    def sortby(self, key, ascending=True):
        print(f'sorting by {key} in', 'asc' if ascending else 'desc')
    

class Partners(BaseClass):
    
    def setmodel(self):
        self.listboxvalues = [f'Partner [{i}]' for i in range(200)]
        self.listboxmodel = StringVar(value=self.listboxvalues)

    def setheader(self):
        buildlabels_list(
            self.right_header, 
            ['Code', 'Partner', 'Country', 'Contact', 'Fiscal Nº', 'Phone', 'Email'],
            self 
        )


class Agents(BaseClass):
    
    def setmodel(self):
        self.listboxvalues = [f'Agent {i}' for i in range(200)]
        self.listboxmodel = StringVar(value=self.listboxvalues)


    def setheader(self):

        buildlabels_list(
            self.right_header, 
            ['Code', 'Agent', 'Country', 'Phone'], 
            self 
        )


class Proformas(BaseClass):
    
    def setmodel(self):
        self.listboxvalues = [f'Proforma {i}' for i in range(200)]
        self.listboxmodel = StringVar(value=self.listboxvalues)

    def setheader(self):
        buildlabels_list(
            self.right_header, 
            ['Serie&num', 'Agent', 'xx', 'yy', 'zz'],
            self
        )
    

class Invoices(BaseClass):
    
    def setmodel(self):
        self.listboxvalues = [f'Invoice {i}' for i in range(200)]
        self.listboxmodel = StringVar(value=self.listboxvalues)

    def setheader(self):
        buildlabels_list(
            self.right_header, 
            ['Serie&num', 'Agent', 'xx', 'yy', 'zz'],
            self
        )


class Warehouse(BaseClass):

    def setmodel(self):
        self.listboxvalues = [f'Order {i}' for i in range(200)]
        self.listboxmodel = StringVar(value=self.listboxvalues)

    def setheader(self):
        buildlabels_list(
            self.right_header, 
            ['Serie&num', 'Agent', 'xx', 'yy', 'zz'],
            self
        )


class Rmas(BaseClass):
    
    def setmodel(self):
        self.listboxvalues = [f'Rma {i}' for i in range(200)]
        self.listboxmodel = StringVar(value=self.listboxvalues)

    def setheader(self):
        buildlabels_list(
            self.right_header, 
            ['Serie&num', 'Agent', 'xx', 'yy', 'zz'],
            self
        )


class Tools(BaseClass):
    
    def setmodel(self):
        self.listboxvalues = [f'Rma {i}' for i in range(200)]
        self.listboxmodel = StringVar(value=self.listboxvalues)

    def setheader(self):
        buildlabels_list(
            self.right_header, 
            ['Serie&num', 'Agent', 'xx', 'yy', 'zz'],
            self
        )