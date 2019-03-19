#Based on https://www.geeksforgeeks.org/python-simple-calculator-using-tkinter/
#calculator app template.

from tkinter import *
from tkinter import scrolledtext
import dix
from io import StringIO  # Python3
import sys


class maiboli:
    def getandreplace(self):
        
        self.expression = self.txt.get(1.0,END) ### Grabbing text from the scroll Text
        self.execute(self.expression)
        #self.newtext=self.expression.replace('/','/') 
        #self.newtext=self.newtext.replace('x','*') 

    def execute(self,inputtext):
        eng = open('op.py','wb')
        #inputtext = self.inputtext
        #inputtext = str(inputtext)
        #print(inputtext)
        iparr = inputtext.split('\n')
        #print(len(arr))
        print(iparr)
        #i = len(arr)
        for y in iparr:
            for x in dix.en:
                #print('reached line 27')
                count = dix.en.index(x) 
                y = y.replace(dix.mar[count],dix.en[count])
                #print('reached line 30')
            y = y+'\n'
            y=y.encode('utf-8')
            eng.write(y)
        print('line 32')
        eng.close()
        print('closed eng')
        eng = open('op.py','r')
        print('reached line 36 opened read')
        self.arr = eng.readlines()
        print(self.arr)
        #eng = open('op.py','r')        
        eng.close()
        self.displayoutput()

    def displayoutput(self):
        #######
        self.txt.delete(1.0,END)
        self.eng_file = open('op.py','rb')
        
        old_stdout = sys.stdout
        result = StringIO() 
        sys.stdout = result
        self.eng_file.seek(0)
        #Do stuff here
        try:
            exec(self.eng_file.read())
        except SyntaxError:
            print('अवैध्य इनपुट, कृपया कोड तपासून पहा')
            """अवैध्य इनपुट, कृपया ओळ क्रमांक <member 'lineno' of 'SyntaxError' objects>तपासून पहा"""
            
        except NameError:
            print('NameError')
        # except SyntaxError.IndentationError:
            # print('इनपुट दरम्यान जागा तपासा')
        except Exception:
            print("undefined exception occured")
            #End of stuff
        sys.stdout = old_stdout
        
        # Then, get the stdout like a string and process it!
        
        result_string = result.getvalue()
        self.txt.insert(1.0,result_string)
        print(result_string)
            

        #print(result_string+'This is the result string')
        self.eng_file.close()
    def action(self,argi):
        """pressed button's value is inserted into the end of the text area"""
        print(argi)
        self.txt.insert(END,argi)
    def clearall(self): 
        """when clear button is pressed,clears the text input area"""
        #self.e.delete(0,END)
        x=0

    def __init__(self,master): 
        """Constructor method"""
        master.title('Maiboli - Marathi Programming Interface')
        master.geometry() 
        self.txt = Entry(master)
        #self.e.grid(row=0,column=0) 
        #self.e.focus_set() #Sets focus on the input text area 
        self.txt = scrolledtext.ScrolledText(root,width=40,height=10)
        self.txt.grid(column=0,row=0)
        #self.optxt = scrolledtext.ScrolledText(root,width=40,height=10)
        #self.optxt.grid(column=0,row=0)
        Button(master,text="Execute",width=11,height=3,fg="blue", #This is the Execute button
            bg="orange",command=lambda:self.getandreplace()).grid( 
                row=4, column=4,columnspan=2)
                # .grid( 
                #     row=4, column=4,columnspan=2) 
        Button(master,text="छापा",width=11,height=3,fg="blue", #This is the Execute button
            bg="orange",command=lambda:self.action('छापा')).grid( 
                row=0, column=4,columnspan=2)
        
root = Tk() 
  
obj=maiboli(root) 
root.mainloop() 
