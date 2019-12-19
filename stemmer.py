import tkinter as tk
from stemmer import stemming

class Stemmer(tk.Frame):

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('450x550')
        tk.Frame.__init__(self, self.root)
        self.master = self.root
        self.init_window()

    def init_window(self):
        self.master.title('Stemmer')

        tk.Label(self.master,
                 text = 'Podaj wyraz w języku polskim:',
                 font=("Helvetica", 12),
                 anchor=tk.CENTER
                 ).place(x=220, y=10, anchor="center")
        self.word_entry = tk.Entry(self.master)
        self.word_entry.place(x=220, y=30, anchor="center")
        
        self.result = tk.Label(self.master,
                          text = '',
                          font=("Helvetica", 12),
                          borderwidth=4
                          )
        self.result.place(x=220, y=200, anchor="center")
        
        self.btn = tk.Button(self.master,
                  text = "Start",
        )

        self.btn.config(command=lambda: self.result.config(text=stemming(self.word_entry.get())))
        self.btn.place(x=220, y=60, anchor="center")
        quitButton = tk.Button(self.master, text='Quit', command=self.close_window)
        quitButton.place(x=350, y=500)


    def close_window(self):
        self.master.destroy()


app = Stemmer()
app.root.mainloop()

