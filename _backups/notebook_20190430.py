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
        f = open(self.notebook_file,'r')

        i = 0
        x_offset = 12*6
        y_offset = 12*2
        max_length = 80
        text = f.read()
        print(len(text))
        raw_lines = text.split('\n')
        lines = []
        for line in raw_lines:
            new_lines = len(line)//max_length+1

            for j in range(new_lines):
                start = j*max_length
                stop = (j+1)*max_length
                if stop > len(line):
                    stop = len(line)
                new_line = line[start:stop]
                if len(new_line) > 0:
                    lines.append(new_line)

        num_lines = len(lines)
        
        self.read_window = tk.Toplevel()
        self.read_window.title('Notebook')
        canvas = tk.Canvas(self.read_window,width=12*max_length,
                           height=12*50,
                           scrollregion=(0,0,12*80,y_offset*num_lines))
        canvas.pack(side=tk.LEFT,fill=tk.BOTH, expand=1)
        vbar=tk.Scrollbar(self.read_window,orient=tk.VERTICAL)
        vbar.pack(side=tk.RIGHT,fill=tk.BOTH)
        vbar.config(command=canvas.yview)
        for line in lines:
            canvas.create_text(0,y_offset*i,font="Courier 12",anchor='nw',text=str(i))
            canvas.create_text(x_offset,y_offset*i,font="Courier 12",anchor='nw',text=line)
            i+=1
        canvas.yview_moveto(1)
        f.close()
        

    def clear_notebook(self):
        self.text.delete('1.0','end')
      
root = tk.Tk()
gui = gui(root)
root.mainloop()


