import tkinter as tk
from stemmer import stemming

class Stemmer(tk.Frame):

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x400')
        tk.Frame.__init__(self, self.root)
        self.master = self.root
        self.init_window()

    def init_window(self):
        self.master.title('Stemmer')

        tk.Label(self.master,
                 text = 'Podaj wyraz w języku polskim:',
                 font=("Helvetica", 12)
                 ).grid(row=0, column=0, columnspan=2, sticky=tk.W)
        self.word_entry = tk.Entry(self.master)
        self.word_entry.grid(row=1, column=0, sticky=tk.W)
        
        self.result = tk.Label(self.master,
                          text = '',
                          font=("Helvetica", 12)
                          )
        self.result.grid(row=3, column=1, sticky=tk.E)
        
        self.btn = tk.Button(self.master,
                  text = "Start",
        )

        self.btn.config(command=lambda: self.result.config(text=stemming(self.word_entry.get())))
        self.btn.grid(row=2, column=0, sticky=tk.N)
        quitButton = tk.Button(self.master, text='Quit', command=self.close_window)
        quitButton.place(x=380, y=350)


    def close_window(self):
        self.master.destroy()


app = Stemmer()
app.root.mainloop()

