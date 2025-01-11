"""
@author:         M. David Ferka
@detail:         

@created:     
@modified:
@version:     

@change:

@license: Copyright (c) 2021 mdf

@todo:


"""
from tkinter import *
from tkinter import ttk
from gui_local import info_tab
from utils import demo
import sys


class MainGui:
    def __init__(self):
        self.window = Tk()
        self.window.title(f"Fronius Modbus demo - by Ferka M. Dávid")
        self.window.geometry('900x500')

        # add tab control
        self.tab_control = ttk.Notebook(self.window)

        self.info_tab = info_tab.InfoTab(self.tab_control)
        self.tab_control.add(self.info_tab.info_tab, text='demo')

        self.tab_control.pack(expand=1, fill='both')

    def start_gui(self):
        self.window.mainloop()





