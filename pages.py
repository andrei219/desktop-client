
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


class HeaderHandler:
    pass 

class ButtonsHandler:
    pass 

class SwitchHandler:
    
    def setswitch(self, master):
        # default behaviour : do nothing 
        Label(
            master, 
            text = 'Switch', 
            background = 'white', 
            font = ('Bahnschrif', 10)
        ).pack(pady=10)

        ttk.Separator(master, orient=HORIZONTAL).pack(fill=X)

class FiltersHandler:
    
    def setfilters(self, master):
        Label(
            master, 
            text = 'No filters available \n in this section ', 
            background = 'white', 
            font = ('Bahnschrif', 10)
        ).pack(pady=40)

class DynamicWidgetsHandler(HeaderHandler, ButtonsHandler, SwitchHandler, FiltersHandler):
    pass 

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

        
        self.listbox = Listbox(
            self.right_content, 
            listvariable=self.listboxmodel,
            border=0,
            font=('Bahnschrif', 13),
            activestyle='none'
        )
        
        for i in range(1, 200, 2):
            self.listbox.itemconfigure(i, background='#f0f0f0')
        
        self.scroll = Scrollbar(self.right_content, orient=VERTICAL, command=self.listbox.yview)
        self.listbox['yscrollcommand'] = self.scroll.set
        
        self.right.pack(side=RIGHT, fill=BOTH, expand=True)
        
        self.right_header.pack(side=TOP, fill=X)
        
        self.right_content.pack(side=TOP, fill=BOTH, expand=True)
        
        self.buttons.pack(side=BOTTOM, fill=X)

        # The responsability of this is implementation is in the subclasses.
        # In turn, these methods are definded in the concrete handlers, sintetized in the bulk
        # dynamic handler. If one section needs specific handlers, they have to write them. 
        self.setheader()
        self.setbuttons()
        self.setswitch(self.left)
        self.setfilters(self.left)

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
    

class Partners(BaseClass, DynamicWidgetsHandler ):
    
    def setmodel(self):
        self.listboxvalues = [f'\n   Partner {i}' for i in range(200)]
        self.listboxmodel = StringVar(value=self.listboxvalues)

    def setheader(self):
        buildlabels_list(
            self.right_header, 
            ['Code', 'Partner', 'Country', 'Contact', 'Fiscal Nº', 'Phone', 'Email'],
            self 
        )


class Agents(BaseClass, DynamicWidgetsHandler):
    
    def setmodel(self):
        self.listboxvalues = [f'Agent {i}' for i in range(200)]
        self.listboxmodel = StringVar(value=self.listboxvalues)

    
    def setswitch(self, master):
        pass 
    

    def setheader(self):

        buildlabels_list(
            self.right_header, 
            ['Code', 'Agent', 'Country', 'Phone'], 
            self 
        )


class Proformas(BaseClass, DynamicWidgetsHandler):
    
    def setmodel(self):
        self.listboxvalues = [f'Proforma {i}' for i in range(200)]
        self.listboxmodel = StringVar(value=self.listboxvalues)

    def setheader(self):
        buildlabels_list(
            self.right_header, 
            ['Serie&num', 'Agent', 'xx', 'yy', 'zz'],
            self
        )
    

class Invoices(BaseClass, DynamicWidgetsHandler):
    
    def setmodel(self):
        self.listboxvalues = [f'  Invoice {i}' for i in range(200)]
        self.listboxmodel = StringVar(value=self.listboxvalues)

    def setheader(self):
        buildlabels_list(
            self.right_header, 
            ['Serie&num', 'Agent', 'xx', 'yy', 'zz'],
            self
        )


class Warehouse(BaseClass, DynamicWidgetsHandler):

    def setmodel(self):
        self.listboxvalues = [f'  Order {i}' for i in range(200)]
        self.listboxmodel = StringVar(value=self.listboxvalues)

    def setheader(self):
        buildlabels_list(
            self.right_header, 
            ['Serie&num', 'Agent', 'xx', 'yy', 'zz'],
            self
        )


class Rmas(BaseClass, DynamicWidgetsHandler):
    
    def setmodel(self):
        self.listboxvalues = [f'  Rma {i}' for i in range(200)]
        self.listboxmodel = StringVar(value=self.listboxvalues)

    def setheader(self):
        buildlabels_list(
            self.right_header, 
            ['Serie&num', 'Agent', 'xx', 'yy', 'zz'],
            self
        )


# This class will be completely separated from the rest
class Tools(BaseClass, DynamicWidgetsHandler):
    
    def setmodel(self):
        self.listboxvalues = [f'Rma {i}' for i in range(200)]
        self.listboxmodel = StringVar(value=self.listboxvalues)

    def setheader(self):
        buildlabels_list(
            self.right_header, 
            ['Serie&num', 'Agent', 'xx', 'yy', 'zz'],
            self
        )