
from tkinter import * 
from tkinter import ttk, messagebox

import requests

import pages


class Application:
        
    def __init__(self):
        
        self.root = Tk()
        
        self.style = ttk.Style(self.root)

        self.style.theme_create(
            
            'appstyle', parent='alt', settings={
                
                'TNotebook':{
                    'configure':{
                        'tabmargins':[2, 5, 2, 0], 
                        'background':'white', 
                    
                    }
                }, 
                'TNotebook.Tab':{
                    'configure':{
                        'padding': [15, 3], 
                        'width': 10,
                        'background':'white', 
                        'highlightbackground':'black',
                        'focuscolor':'white', 
                        'font':('Bahnschrif', 11)
                    }, 
                    'map':{
                        'expand':[('selected', [3, 3, 3, 0])]
                    }
                }, 

                'TFrame':{
                    'configure': {
                        'padding':[20, 20], 
                        'background':'white', 
                        'width':100, 
                        'height':100
                    }
                }, 

                'TLabel': {
                    'configure':{
                        'padding':[10, 2], 
                        'bordercolor':'red',
                    }
                }
            }
        )

        self.style.theme_use('appstyle')

        self.basic_setup()
        self.init_notebook()
        self.init_statusbar()

    def dologin(self):
        pass 
        
    def basic_setup(self):
        
        self.root.title("Euromedia Investment Group, S.L.")        
            
        self.root.configure(background='white')

        width = int(self.root.winfo_screenwidth() * 0.7)
        height = int(self.root.winfo_screenheight() * 0.7)
        
        self.root.geometry(f"{width}x{height}")

        self.root.protocol('WM_DELETE_WINDOW', self.exit_handler)

    def init_notebook(self):
        # Embed if's based on what user is logging 
        import os
        self.partners_icon = PhotoImage(file=os.path.join('icons', 'partners.png'))
        self.agents_icon = PhotoImage(file=os.path.join('icons', 'agents.png'))      
        self.proformas_icon = PhotoImage(file=os.path.join('icons', 'proformas.png'))
        self.invoices_icon = PhotoImage(file=os.path.join('icons', 'invoices.png'))
        self.warehouse_icon = PhotoImage(file=os.path.join('icons','warehouse.png'))
        self.rmas_icon = PhotoImage(file=os.path.join('icons', 'rmas.png'))
        self.tools_icon = PhotoImage(file=os.path.join('icons', 'tools.png'))
        
        self.notebook = ttk.Notebook(self.root)
        

        self.partners_frame = pages.Partners(self.root, self.notebook)
        self.agents_frame = pages.Agents(self.root, self.notebook)
        self.proformas_frame = pages.Proformas(self.root, self.notebook)
        self.invoices_frame = pages.Invoices(self.root, self.notebook)
        self.warehouse_frame = pages.Warehouse(self.root, self.notebook)
        self.rmas_frame = pages.Rmas(self.root, self.notebook)
        self.tools_frame = pages.Tools(self.root, self.notebook)

        

        self.notebook.add(
            
            self.partners_frame, 
            text='Partners', 
            image=self.partners_icon,
            compound = LEFT, 
            padding=(20, 20)
        )

        self.notebook.add(
            self.agents_frame, 
            text='Agents',
            image=self.agents_icon,
            compound=LEFT, 
            padding=(20, 20)
        )

        self.notebook.add(
            self.proformas_frame, 
            text='Proformas', 
            image = self.proformas_icon, 
            compound = LEFT, 
            padding =(20,20)
        )
        
        self.notebook.add(
            self.invoices_frame, 
            text='Invoices', 
            image = self.invoices_icon, 
            compound= LEFT, 
            padding=(20, 20)
        )

        self.notebook.add(
            self.warehouse_frame, 
            text='Warehouse', 
            image = self.warehouse_icon, 
            compound=LEFT, 
            padding=(20, 20)
        )

        self.notebook.add(
            self.rmas_frame, 
            text='RMAs', 
            image = self.rmas_icon, 
            compound = LEFT, 
            padding = (20, 20)
        )

        self.notebook.add(
            self.tools_frame, 
            text='Tools', 
            image=self.tools_icon, 
            compound=LEFT,
            padding=(20, 20)
        )

        self.notebook.pack(side=TOP, expand=True, fill=BOTH, padx='15', pady='2')

    def init_statusbar(self):
        
        self.statusbar_frame  = Frame(self.root, background='#33D1FF')
        Label(self.statusbar_frame, text = 'STATUS BAR', background='#33D1FF').pack()
        self.statusbar_frame.pack(side=BOTTOM, fill=BOTH, pady=[10, 0])

    def exit_handler(self):
        if messagebox.askokcancel('Quit', 'Do you want to close?'):
            # TODO clean up tasks 
            self.cleanup()
            self.root.destroy()

    def cleanup(self):
        pass 

    def mainloop(self):
        self.root.mainloop()

if __name__ ==  '__main__':

    Application().mainloop()  

    