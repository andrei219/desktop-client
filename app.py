
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
        
    def basic_setup(self):
        
        self.root.title("Euromedia Investment Group, S.L")        
            
        self.root.configure(background='white')

        width = self.root.winfo_screenwidth() 
        height = self.root.winfo_screenheight() 
        self.root.geometry(f"{width}x{height}")

        self.root.protocol('WM_DELETE_WINDOW', self.exit_handler)

    def init_notebook(self):
        # Embed if's based on what user is logging 
        
        self.partners_icon = PhotoImage(file=r'.\icons\partners.png')
        self.agents_icon = PhotoImage(file=r'.\icons\agents.png')        
        self.proformas_icon = PhotoImage(file=r'.\icons\proformas.png')
        self.invoices_icon = PhotoImage(file=r'.\icons\invoices.png')
        self.warehouse_icon = PhotoImage(file=r'.\icons\warehouse.png')
        self.rmas_icon = PhotoImage(file=r'.\icons\rmas.png')
        self.tools_icon = PhotoImage(file=r'.\icons\tools.png')
        
        self.notebook = ttk.Notebook(self.root, )

        self.partners_frame = pages.Partners()
        self.agents_frame = pages.Agents()
        self.proformas_frame = pages.Proformas()
        self.invoices_frame = pages.Invoices()
        self.warehouse_frame = pages.Warehouse()
        self.rmas_frame = pages.Rmas()
        self.tools_frame = pages.Tools()

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

        self.notebook.pack(expand='y', fill='both', padx='15', pady='15')


    def exit_handler(self):
        if messagebox.askokcancel('Quit', 'Do you want to close ?'):
            # TODO clean up tasks 
            self.exit_cleanup()
            self.root.destroy()

    def exit_cleanup(self):
        pass 

    def mainloop(self):
        self.root.mainloop()

if __name__ ==  '__main__':

    Application().mainloop()  

    