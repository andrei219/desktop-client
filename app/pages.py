
from tkinter import ttk 

def partners(root):
    content = ttk.Frame(root)
    ttk.Label(content, text='partners').grid(row=1)
    return content 

def agents(root):
    content = ttk.Frame(root)
    ttk.Label(content, text='Agents').grid(row=1)
    return content 


def proformas(root):
    content = ttk.Frame(root)
    ttk.Label(content, text='Proformas').grid(row=1)
    return content

def invoices(root):
    content = ttk.Frame(root)
    ttk.Label(content, text='Invoices').grid(row=1)
    return content


def warehouse(root):
    content = ttk.Frame(root)
    ttk.Label(content, text='Warehouse').grid(row=1, column=4)
    return content

def rma(root):
    content = ttk.Frame(root)
    ttk.Label(content, text='RMA').grid(row=1)
    return content

def tools(root):
    content = ttk.Frame(root)
    ttk.Label(content, text='RMA').grid(row=1)
    return content



