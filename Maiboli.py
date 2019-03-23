#Based on https://www.geeksforgeeks.org/python-simple-calculator-using-tkinter/
#calculator app template.
#Research more on https://stackoverflow.com/questions/2090464/python-window-activation
from tkinter import *
from tkinter import scrolledtext
import dix
from io import StringIO  # Python3
import sys

class maiboli:
    def getandreplace(self):
        
        self.expression = self.txt.get(1.0,END) ### Grabbing text from the scroll Text
        self.execute(self.expression)
    def execute(self,inputtext):
        eng = open('op.py','w')
        print(inputtext)
        iparr = inputtext.split('\n')
        iparr.remove(iparr[len(iparr)-1]) #TO remove that last \n of the array
        print(iparr)
        
        for y in iparr:     #Getting sentence
            self.convertor = True
            self.stack = ''
            for x in dix.en:    #Getting conversion word
                count = dix.en.index(x) 
                for letter in y:    #One letter from 
                    if letter == '"' or letter == '"':
                        inv_comma = letter
                        self.convertor != self.convertor
                        self.stack = self.stack + letter
                        if self.stack == dix.mar[count]:
                            y = self.stack.replace(dix.mar[count],dix.en[count])
                            self.stack = ''
                            y = y+'\n'
                            eng.write(y)
                        else:
                            eng.write(y)
                    else:
                        if self.convertor == True:
                            eng.write(y)
                    
                        

                # if self.susp == True:    
                #     y = y.replace(dix.mar[count],dix.en[count])
            # y = y+'\n'
            # eng.write(y)
        eng.close()
        eng = open('op.py','r')
        self.arr = eng.readlines()
        print(self.arr)
        eng.close()
        self.displayoutput()

    def displayoutput(self):
        #######
        self.txt.delete(1.0,END)
        self.eng_file = open('op.py','r')
        
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
        except SyntaxError.IndentationError:
            print('इनपुट दरम्यान जागा तपासा')
        except Exception:
            print("undefined exception occured")
            #End of stuff       
            sys.stdout = old_stdout
        
        # Then, get the stdout like a string and process it!
        
        result_string = result.getvalue()
        self.txt.insert(1.0,result_string)
        print(result_string)
            

        self.eng_file.close()
    def action(self,argi):
        """pressed button's value is inserted into the end of the text area"""
        print(argi)
        self.txt.insert(END,argi)
    def clearall(self): 
        """when clear button is pressed,clears the text input area"""
        x=0

    def __init__(self,master): 
        """Constructor method"""
        master.title('Maiboli - Marathi Programming Interface')
        master.geometry() 
        self.txt = Entry(master)
        self.txt.focus_set() #Sets focus on the input text area 
        self.txt = scrolledtext.ScrolledText(root,width=140,height=40)
        self.txt.grid(column=0,row=0)
        Button(master,text="चालवा",width=11,height=3,fg="blue", #This is the Execute button
            bg="orange",command=lambda:self.getandreplace()).grid( 
                row=0, column=4,columnspan=2)
         
root = Tk() 
  
obj=maiboli(root) 
root.mainloop() 
