import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

class mainclass( Frame ):
    #iptxt = 'test'
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("मायबोली")
        # self.textbox = scrolledtext.ScrolledText(self,width=40,height=10)
        # self.textbox.grid(column=0,row=0)
        # self.textbox2 = scrolledtext.ScrolledText(self,width=40,height=10)
        # self.textbox2.grid(column=0,row=0)
        test = Text(self)
        test.pack()
        
        def retrieve_input():
            input = self.test.get("1.0",END)    
            print(input)
        
        self.button1 = Button( self, text = "चालवा", width = 25,
                               command = retrieve_input)
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
           
    def chalva(self):
        print(mainclass.retrieve_input.input)
    
def main(): 
    mainclass().mainloop()
if __name__ == '__main__':
    main()
