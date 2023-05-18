import sys
import os
import re
import time


from BaseViews import *




class TemplateView1(BaseView):
    def __init__(self, master=None):
        super().__init__(master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=1)
    
    def create_view(self):
        my_frame = tk.LabelFrame(master=self, text='Template 1')
        my_frame.grid(row=0,column=0,sticky=tk.W+tk.E+tk.N,padx=3,pady=3)
    
        self.CreateLabel(my_frame,name='StatusBar',label_text='Status Bar is showing',row=0,column=0)
        self.Create
        self.CreateButton(my_frame,name='ClickMe',text='ClickMePlease',row=1,column=0)