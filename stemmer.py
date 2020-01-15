# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.scrolledtext as tkst
from stemmer import Stemmer

#################################################
#
#       Class for create simple GUI app 
#             using tkinter module
#
#################################################

class StemmerGUI(tk.Frame):

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('450x550')
        tk.Frame.__init__(self, self.root)
        self.stemmer = Stemmer()
        self.master = self.root
        self.results =  None
        self.init_window()
        

    def init_window(self):
        self.master.title('Stemmer')

        tk.Label(self.master,
                 text = 'Podaj wyraz w języku polskim:',
                 font=("Helvetica", 12),
                 anchor=tk.CENTER
                 ).place(x=220, y=15, anchor="center")
        self.word_entry = tk.Entry(self.master)
        self.word_entry.place(x=220, y=45, anchor="center")
        
        self.print_results = tkst.ScrolledText(self.master, font=("Helvetica", 12), width=40, height=18, wrap=tk.WORD)
        self.print_results.place(x=30, y=100)
        self.print_results.insert(tk.END, '')

        self.btn = tk.Button(self.master,
                  text = "Start",
        )
        
        self.btn.config(command=lambda: [self.print_results.delete(1.0, tk.END), self.print_results.insert(tk.END, self.stemmer.stemming(self.word_entry.get()))])
        
        self.btn.place(x=220, y=80, anchor="center")
        
        
        quitButton = tk.Button(self.master, text='Quit', command=self.close_window)
        quitButton.place(x=350, y=500)

    def close_window(self):
        self.master.destroy()


app = StemmerGUI()
app.root.mainloop()
