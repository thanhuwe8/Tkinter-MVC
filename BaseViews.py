import tkinter as tk
from tkinter import ttk

from abc import abstractmethod
from typing import List



class View(tk.Frame):
    @abstractmethod
    def create_view():
        raise NotImplementedError

class LabelEntry(tk.Frame):
    def __init__(self, master, var, label, input_args=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        input_args = input_args or {}
        
        self.variable = var
        self.label = ttk.Label(self, text=label).grid(row=0,column=0,sticky=(tk.W+tk.E))
        self.input = ttk.Entry(self, **input_args).grid(row=1,column=0,sticky=(tk.W+tk.E))
        self.columnconfigure(0,weight=1)


class LabelRadioButton(tk.Frame):
    def __int__(self, master, var, label, input_args=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        input_args = input_args or {}
        self.variable = var
        for v in input_args.pop('values',[]):
            button = ttk.Radiobutton(self, text=v, value=v, variable=self.variable,**input_args).pack(side=tk.TOP, ipadx=10, ipady=2, expand=True, fill='x')
        self.columnconfigure(0,weight=1)

class BaseView(View):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.labels = {}
        self.entries = {}
        self.buttons = {}
        self.comboboxes = {}
        self.dropdown = {}
        self.labelframe = {}
        self.treematrix = {}
        self.variables = {}
        self.labelvariables = {}
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0,weight=1)
        self.grid(row=0,column=0,sticky=tk.W+tk.E+tk.N+tk.S)

    # text can be changed with this label
    def CreateLabel(self,frame,objectname,label_text,row,column):
        #? set up frame
        name = objectname
        self.labelframe[name] = tk.LabelFrame(frame,font=('Helvetica 10 bold'))
        self.labelframe[name].grid(row=row,column=column,padx=3,pady=3,sticky=tk.W+tk.E)
        self.labelframe[name].grid(row=row, column=column, sticky=tk.N + tk.S + tk.W + tk.E, padx=3, pady=3)
        self.labelframe[name].columnconfigure(0,weight=1)
        self.labelframe[name].rowconfigure(0,weight=1)
        
        self.labelvariables[name] = tk.StringVar()
        self.labelvariables[name].set(label_text)
        
        self.labels[name] = ttk.Label(self.labelframe[name],textvariable=self.labelvariables[name])
        self.labels[name].grid(row=0,column=0,sticky=tk.W+tk.E)
        self.labels[name].columnconfigure(0,weight=1)
        self.labels[name].rowconfigure(0,weight=1)
    
    # 
    def CreateButton(self,frame,objectname,text,row,column):
        name = objectname
        self.buttons[name] = tk.Button(frame,height=1,width=25)
        self.buttons[name]['text'] = text
        self.buttons[name].grid(row=row,column=column,padx=3,pady=3,sticky=tk.W+tk.E+tk.N)
    
    
    def CreateEntry(self,frame,objectname):
        name = objectname