#! /usr/bin/python
import os
import time
import json
import tkinter as tk
import tkinter.scrolledtext
from tkinter import ttk
from tkinter import messagebox, filedialog

class gui(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.master = master
        self.notebook_file = './notebook.txt'
        self.notebook_json = './notebook.json'
        self.saved = False
        self.initialize_program_files()
        self.initialize_menu()
        self.initialize_notebook()
        self.read_notebook()

    def initialize_program_files(self):
        notebook_exists = os.path.exists(self.notebook_file)
        if notebook_exists:
            pass
        else:
            print('Missing files...')
            print('Initializing required system files...')
            try:
                f = open('./notebook.txt','w')
                f.close()
            except:
                print('Failed to create ./notebook.txt')
            
    def initialize_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        file_menu = tk.Menu(menu)
        file_menu.add_command(label="Save Notebook",command=self.write_notebook)
        file_menu.add_command(label="Clear Notebook",command=self.clear_notebook)
        file_menu.add_command(label="Read Notebook",command=self.read_notebook)
        menu.add_cascade(label="File",menu = file_menu)
        
    def initialize_notebook(self):
        self.text = tkinter.scrolledtext.ScrolledText()
        self.text.pack(fill=tk.BOTH, expand=1)

    def write_notebook(self):
        date = time.asctime()
        text = self.text.get('1.0','end')
        entry = date+'\n'+text+'\n'
        print(entry)
        f = open(self.notebook_file,'a')
        f.write(entry)
        self.saved = True
        f.close()

    def read_notebook(self):
        pass

    def clear_notebook(self):
        self.text.delete('1.0','end')
      
root = tk.Tk()
gui = gui(root)
root.mainloop()


