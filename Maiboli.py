
#Based on a tkinter module, application will take input text in devanagari code
#and convert it into English Python code and run it in the compiler. Once the compilation is complete,
#the output is displayed in the same text input box.


"""
Workflow

Take input from the user by the TKinter window
->
Put it through the maiboli functions 
->
getandreplace function grabs text from the TK and pushes it to execute()
-> 
execute function:
1. saves the text to a file 
2. pullquotedstring function will pull out the content inside the ""quote marks (e.g. Print("THIS CONTENT")).
3. converts the remaining file to english devanagari
4. re-adds the pulledquotedstring
5. puts it in python compiler
6. Copies that console output to a variable and displays it using displayoutput()
 
"""

"""Importing libraries required for the program"""


from tkinter import *               #TK
from tkinter import scrolledtext    #TK
import dix                  #Dictionary file where all the translations are input
import exp                  #Exception handling Dictionry, to get exceptions
from io import StringIO     #Python3 - console output reader
import sys                  #Sys
# Defining class for adding functions of both the program and tkinter to work
class maiboli:
    def pullquotedstring(self,indexset,array,scam): #Define Funtion
        for i in range(indexset[0],indexset[1]+1):  
                scam.append(array[i])
                array[i] = ''       #Initializing
                print(scam)
    def getandreplace(self):
        
        self.expression = self.txt.get(1.0,END) ### Grabbing text from the scroll Text
        self.execute(self.expression)

    def execute(self,inputtext):        # Beginning the Execution
        eng = open('op.py','w')         # Opening a blank file to save the input data into
        print(inputtext)                # Printing the data input from the user in the console for reference
        iparr = inputtext.split('\n')   # Splitting the data code paragraph into lines - iparr (Lines of code in Marathi)
        iparr.pop()                     # Popping the last line since it's a blank spot 
        print(iparr)                    # Printing the array of lines of code for reference.
        for y in iparr:                 # y is the line input 
            array = []                  # This one's to chop the sentence into letters 
            indexset = []               # This one's to keep the start and end index of the "quoted area"   
            for char in y:
                array.append(char)      # Adding as single single letter input to array
            flag = False                # Setting flags to help figure out if the index has quotes
            quotes = False              # Setting flags to help figure out if the index has quotes
            endindex = 1                # Just initializing for keeping the last index of the quoted character
            scam = []                   # Array to put those "quoted characters" in
            for i in array:             # Calling one letter at a time
                print(i)
                """
                Code working:
                The loops divide the sentence into words and then into characters. 
                When one character is spotted to be a double quote, the flag for 'quotes' is set to True, and the
                array index is noted. The loop proceeds and notes the index of the closing 'quotes'. 
                """
                if i == "'" and flag == False:
                    self.startindex = array.index(i,0)
                    indexset.append(int(self.startindex))
                    flag = True
                    quotes = True
                elif i == "'" and flag == True:
                    endindex = array.index(i,self.startindex+1)
                    indexset.append(int(endindex))
                    flag = False
            print(array)
            print('indexset variable is ',indexset) # Printing the start and end index of the quoted area
            if quotes == True:                      #Only runs pullquotedstring when there's a quote mark selected.
                self.pullquotedstring(indexset,array,scam)  #Calling the pull quoted string function to pull out the quotes and make it ready to process.
            else:
                pass
            modified_array_of_string = []           # Initialized two variables, to keep the readded quote modified sentence in both string and array format
            modified_string = ''
            for i in array:
                modified_array_of_string.append(i)       #This is the modified string array without quoted stuff
            for i in modified_array_of_string:
                modified_string = modified_string+i
            modified_string = modified_string + '\n'
            
            #The Content stays without the quoted stuff, before running the conversion module.
            """
            Problem: sometimes marathi dictionary has less number of words and english dictionary has more number of words
            This makes our previous setup compromise. To avoid that, I've written two cases.
            1. when Marathi word length < English word length -> 
            add ' ' spaces to fill the  difference of lengths between the two.
            2. When English word lengths < Marathi word length - Yet to think what to do

            Solution:
            Screw this, I'm hardcoding in the dix.py file with required spacings.
            """
            for x in dix.en:
                count = dix.en.index(x) 
                modified_string = modified_string.replace(dix.mar[count].strip(),dix.en[count]) #Conversion module to convert marathi stuff into python code.


            """ This code is to get the quoted stuff back inside the output before putting it in the interpreter"""
            modified_array_of_string = ['']
            if quotes == True:
                for i in modified_string:
                    modified_array_of_string.append(i)
                count = indexset[0]+1
                modified_array_of_string.pop(0)
                for i in scam:
                    modified_array_of_string.insert(count,i)
                    count+=1
                print(modified_array_of_string)
                ready_to_exec = ''
                for x in modified_array_of_string:
                    ready_to_exec = ready_to_exec+x
                print(ready_to_exec)
                eng.write(ready_to_exec)
            else:
                print(modified_string)
                eng.write(modified_string)
        
        eng.close()
        
        # Stops modifying the op.txt file and opens it as read only once the execution is done and the output it stored in op.py
        eng = open('op.py','r')
        
        self.arr = eng.readlines()      #Displays the content as output
        print(self.arr)
        eng.close()
        self.displayoutput()
    """ This module is to print output as per the user's problems. """
    def displayoutput(self):            
        self.txt.delete(1.0,END)
        self.eng_file = open('op.py','r')
        
        old_stdout = sys.stdout
        result = StringIO() 
        sys.stdout = result
        self.eng_file.seek(0)
        #Do stuff here that goes in the result variable as string text
        try:
            exec(self.eng_file.read())
        except SyntaxError:
            #print('अवैध्य इनपुट, कृपया कोड तपासून पहा')
            print(exp.exc_mar[0])
            """अवैध्य इनपुट, कृपया ओळ क्रमांक <member 'lineno' of 'SyntaxError' objects>तपासून पहा""" #This string can be put up as per your setup language for exception handling
            
        except NameError:
            print('NameError')
        # except SyntaxError.IndentationError:
        #     print('इनपुट दरम्यान जागा तपासा')
        except Exception:
            #print("अवैध्य इनपुट")
            print(exp.exc_mar[1])
            #End of stuff that gets copied in that variable.
            sys.stdout = old_stdout
        
        result_string = result.getvalue()
        self.txt.insert(1.0,result_string)
        print(result_string)
            

        self.eng_file.close()
    
    #These are TKinter window functions
    def action(self,argi):
        """pressed button's value is inserted into the end of the text area"""
        print(argi)
        self.txt.insert(END,argi)
    def clearall(self): 
        """when clear button is pressed,clears the text input area"""
        #x=0

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