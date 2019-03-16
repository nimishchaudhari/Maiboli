#Based on https://www.geeksforgeeks.org/python-simple-calculator-using-tkinter/
#calculator app template.

from tkinter import *
import dix

class maiboli:
    def getandreplace(self): 
        """replace x with * and ÷ with /"""
        self.expression = self.e.get()
        self.execute(self.expression)
        #self.newtext=self.expression.replace('/','/') 
        #self.newtext=self.newtext.replace('x','*') 

    def execute(self,inputtext):
        eng = open('op.py','w')
        #inputtext = self.inputtext
        arr = inputtext
        i = len(arr)
        for y in arr:
            for x in dix.en:
                count = dix.en.index(x)
                y = y.replace(dix.mar[count],dix.en[count])
            eng.write(y)
        eng.close()
        eng = open('op.py','r')
        arr = inputtext.readlines()
    def action(self,argi): 
        """pressed button's value is inserted into the end of the text area"""
        self.e.insert(END,argi)
    def clearall(self): 
        """when clear button is pressed,clears the text input area"""
        self.e.delete(0,END)

    def __init__(self,master): 
        """Constructor method"""
        master.title('Maiboli - Marathi Programming Interface')
        master.geometry() 
        self.e = Entry(master) 
        self.e.grid(row=0,column=0,columnspan=6,pady=3) 
        self.e.focus_set() #Sets focus on the input text area 
        Button(master,text="Execute",width=11,height=3,fg="blue", #This is the Execute button
            bg="orange",command=lambda:self.getandreplace()).grid( 
                row=4, column=4,columnspan=2) 
root = Tk() 
  
obj=maiboli(root) 
root.mainloop() 
