
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
        iparr.pop()
        print(iparr)
        for y in iparr:             #y is the line input
            array = []              # This one's to chop the sentence into letters 
            indexset = []           # This one's to keep the start and end index of the "quoted area"
            for char in y:
                array.append(char)  #Adding as object to array
            flag = False
            startindex = 0
            endindex = 1
            for i in array:         #Calling one object at a time
                print(i)
                if i == "'" and flag == False:
                    self.startindex = array.index(i,0)
                    indexset.append(int(self.startindex))
                    flag = True
                elif i == "'" and flag == True:
                    endindex = array.index(i,self.startindex+1)
                    indexset.append(int(endindex))
                    flag = False
            scam = []               #Array to put those "quoted characters"
            print(array)
            print('indexset variable is ',indexset) #printing the start and end indedx of the quoted area
            for i in range(indexset[0],indexset[1]+1):
                #print('scam this',array[i])
                scam.append(array[i])
                array[i] = ''
                #scam.append(array.pop(i))
                print(scam)
            modified_array_of_string = []
            modified_string = ''
            for i in array:
                modified_array_of_string.append(i)       #This is the modified string array without quotes
            for i in modified_array_of_string:
                modified_string = modified_string+i
            
            for x in dix.en:
                count = dix.en.index(x) 
                #y = y.replace(dix.mar[count],dix.en[count]) #Conversion module
                mar_len = len(dix.mar[count])
                eng_len = len(dix.en[count])
                
                modified_string = modified_string.replace(dix.mar[count],dix.en[count])
            #y = y+'\n'
            modified_array_of_string = ['']
            for i in modified_string:
                modified_array_of_string.append(i)
            count = indexset[0]
            for i in scam:
                modified_array_of_string.insert(count,i)
                count+=1
            print(modified_array_of_string)
            ready_to_exec = ''
            for x in modified_array_of_string:
                ready_to_exec = ''.join(x)
            eng.write(ready_to_exec)
        print('line 32')
        eng.close()
        print('closed eng')
        eng = open('op.py','r')
        print('reached line 36 opened read')
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