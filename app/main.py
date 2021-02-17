
from tkinter import * 
from tkinter import ttk, messagebox
import Pmw

import requests



class Application:
        
    def __init__(self):
        self.root = Tk()
        self.basic_setup()
        self.init_notebook()
        
    def basic_setup(self):

        self.root.title("Euromedia Investment Group, S.L")
        self.style = ttk.Style(self.root)
        
        windowingsystem = self.root.tk.call('tk', 'windowingsystem')
        if windowingsystem == 'win32':
            self.style.theme_use('clam')
        elif windowingsystem == 'aqua':
            self.style.theme_use('aqua')
        else: 
            # TODO for linux systems 
            pass    

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        width = self.root.winfo_screenwidth() 
        height = self.root.winfo_screenheight() 
        self.root.geometry(f"{width}x{height}")
        self.root.configure(background='white')

        self.root.protocol('WM_DELETE_WINDOW', self.exit_handler)

    def init_notebook(self):
        
        # Embed if's based on what user is logging 
        import os 
        import pages
        

        notebook = ttk.Notebook(self.root, padding=(10, 10))
    
        partners = pages.partners(self.root)
        agents = pages.agents(self.root)
        proformas = pages.proformas(self.root)
        invoices = pages.invoices(self.root)
        warehouse = pages.warehouse(self.root)
        rma = pages.rma(self.root)
        tools = pages.tools(self.root)

        notebook.add(partners, text='Partners')
        notebook.add(agents, text='Agents')
        notebook.add(proformas, text='Proformas')
        notebook.add(invoices, text='Invoices')
        notebook.add(warehouse, text='Warehouse')
        notebook.add(rma, text='RMA')

        notebook.add(
            tools, 
            text='Tools',
            image=PhotoImage(file='tools.png')
        )
        
        #notebook.enable_traversal()
        notebook.pack()


    def exit_handler(self):
        if messagebox.askokcancel('Quit', 'Do you want to exit?'):
            # TODO clean up tasks 
            self.root.destroy()

    def mainloop(self):
        self.root.mainloop()

if __name__ ==  '__main__':

    # Application().mainloop()  
    root = Tk()
    dialog = Pmw.PromptDialog(root, title='Passowrd', label_text='Password:',
                entryfield_labelpos=N, entry_show='*', default_button=0, 
                buttons=('OK', 'Cancel'))
    
    result = dialog.active()
    print('You selected ', result)