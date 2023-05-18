
from BaseViews import *

import tkinter as tk
from tkinter import *


from Template1 import *

# import ctypes
# ctypes.windll.shcore.GetProcessDpiAwareness(1)


class Application(ttk.Notebook):
    def __init__(self, master=None):
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(row=0,column=0,sticky=tk.E+tk.W+tk.N+tk.S)
    
    #? use functional programming as part of parameters
    def new_tab(self,view,name):
        # view = view(self)
        # controller.bind(view)
        self.add(view,text=name)


if __name__=="__main__":
    
    
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use('vista')
    
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.geometry("800x800")
    
    app = Application(master=root)
    myview = TemplateView1(app)
    myview.create_view()
    app.new_tab(view=myview, name="test")
    root.mainloop()