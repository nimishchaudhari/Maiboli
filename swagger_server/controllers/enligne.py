# Callable functions 
import sys
import dix
import exp
from io import StringIO     #Python3 - console output reader

class enligne:
    def pullquotedstring(self,indexset,array,scam): #Define Funtion
        for i in range(indexset[0],indexset[1]+1):  
                scam.append(array[i])
                array[i] = ''       #Initializing
                #print(scam)
    def trim(self,arr):
        op_arr=[]
        for i in arr:
            i.strip()
            op_arr.append(i)
        return op_arr
    def execute(self,inputtext,dix1,dix2):        # Dix1: English Version, Dix2: Target language
        eng = open('test.py','w')         # Opening a blank file to save the input data into
        #print(inputtext)                # Printing the data input from the user in the console for reference
        iparr = inputtext.split('\n')   # Splitting the data code paragraph into lines - iparr (Lines of code in Marathi)
        tab_count=[]                #Counting no of \ts
        #iparr.pop()                     # Popping the last line since it's a blank spot 
        #print(iparr)                    # Printing the array of lines of code for reference.
        for y in iparr:                 # y is the line input 
            tc = 0
            tc_flag=False
            array = []                  # This one's to chop the sentence into letters 
            indexset = []               # This one's to keep the start and end index of the "quoted area"   
            for char in y:
                array.append(char)      # Adding as single single letter input to array
            flag = False                # Setting flags to help figure out if the index has quotes
            quotes = False              # Setting flags to help figure out if the index has quotes
            endindex = 1                # Just initializing for keeping the last index of the quoted character
            scam = []                   # Array to put those "quoted characters" in
            #tab_count.append(str(y).find('\t')) #Trying to note down no of tabs on each line
            #if(y.count('\t')>0):
            #    tc+=1
            #    tc_flag=True
            tc+=y.count('\t')
                                        #Then I'm gonna use it with the count variable line by line 
                                        #  and hope it works
            for i in array:             # Calling one letter at a time
                #print(i)
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
            #print(array)
            #print('indexset variable is ',indexset) # Printing the start and end index of the quoted area
            if quotes == True:                      #Only runs pullquotedstring when there's a quote mark selected.
                self.pullquotedstring(indexset,array,scam)  #Calling the pull quoted string function to pull out the quotes and make it ready to process.
            else:
                pass
            modified_array_of_string = []           # Initialized two variables, to keep the read quote modified sentence in both string and array format
            modified_string = ''
            for i in array:
                modified_array_of_string.append(i)       #This is the modified string array without quoted stuff
            for i in modified_array_of_string:
                modified_string = modified_string+i
            modified_string = modified_string + '\n'
            # print("Modified string 1")
            # print(modified_string)
            
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
            length_of_func=[]               #Gonna note here the length of a function in ENG dix, do +1/+2 
                                            #Guessing that i'll take me to the point after the bracket
            for count in range(0,len(dix1)): #Count is the array index of these dixs
                #count = dix1.index(x)
                #if(dix2[count])
                #
                # print(dix2[count].strip(),modified_string)
                if(dix2[count].strip() in modified_string):
                    length_of_func.append(dix1[count].strip())
                    modified_string = modified_string.replace(dix2[count].strip(),dix1[count].strip()) #Conversion module to convert marathi stuff into python code.                                                #print(count)
                                                                    #print(dix2[count],dix1[count])
                #modified_string = modified_string.replace(dix2[count],dix1[count]) #Conversion module to convert marathi stuff into python code.
            """ This code is to get the quoted stuff back inside the output before putting it in the interpreter"""
            modified_array_of_string = ['']
            if quotes == True:
                for i in modified_string:
                    modified_array_of_string.append(i)
                #count = indexset[0]
                #if(tc_flag):
                count = len(length_of_func[0])+1+tc#+tab_count
                #else:
                #    count = len(length_of_func[0])+1#+tab_count
                """
                #THIS COUNT PARAMETER IS A BITCH
                Count variable is storing the index of the place where the quotation marks started / ended.
                Problem here: Count changes with language, so possible soln
                is to take the length of English dix word, and add 1 to it, to maybe solve it
                

                ##Have to figure out what's the scene here, it lets me work with Greek, but not with Marathi now
                ##If i have it set to +1, it works in Marathi, then not in Greek. WTF?
                """
                if(modified_array_of_string[0]==''):
                    modified_array_of_string.pop(0)
                # if(modified_array_of_string[-1]=='\n'):
                #     modified_array_of_string.pop(len(modified_array_of_string)-1)
                #"modified array"+"grnegnibgn   "+str(modified_array_of_string))
                #modified_array_of_string.pop(0)
                for i in scam:
                    modified_array_of_string.insert(count,i)
                    #count+=1
                #print("modified array of string" +str(modified_array_of_string))
                ready_to_exec = ''
                for x in modified_array_of_string:
                    ready_to_exec = ready_to_exec+x
                #print(ready_to_exec)
                eng.write(ready_to_exec)
            else:
                #print(modified_string)
                eng.write(modified_string)
        eng.close()
        
        # Stops modifying the op.txt file and opens it as read only once the execution is done and the output it stored in op.py
        eng = open('test.py','r')
        self.arr = eng.readlines()      #Displays the content as output
        #print(self.arr)
        eng.close()
        #self.displayoutput()
        """ This module is to print output as per the user's problems. """
        return(self.displayoutput())

    def displayoutput(self):            
        self.eng_file = open('test.py','r')
        print(self.eng_file.read())
        self.eng_file.seek(0)
        old_stdout = sys.stdout
        result = StringIO() 
        sys.stdout = result
        self.eng_file.seek(0)
        #Do stuff here that goes in the result variable as string text
        try:
            exec(self.eng_file.read())

        # except SyntaxError:
        #     #print('अवैध्य इनपुट, कृपया कोड तपासून पहा')
        #     print(exp.exc_mar[0])
            
        #     """अवैध्य इनपुट, कृपया ओळ क्रमांक <member 'lineno' of 'SyntaxError' objects>तपासून पहा""" #This string can be put up as per your setup language for exception handling
            
        except NameError:
            print('NameError')
        # except SyntaxError.IndentationError:
        #     print('इनपुट दरम्यान जागा तपासा')
        # except Exception:
        #     #print("अवैध्य इनपुट")
        #     print(exp.exc_mar[1])
        #     #End of stuff that gets copied in that variable.
        sys.stdout = old_stdout
        
        result_string = result.getvalue()
        #print(result_string)
        self.eng_file.close()
        return result_string

        
obj = enligne() 
# ignore print(obj.execute("tẹjade('tẹjade Τύπωσε छापा')",dix.en_final,dix.yrb_final))

print(obj.execute("Τύπωσε('Τύπωσε Τύπωσε छापा')",dix.en_final,dix.gr_final))
x="तोपर्यंत बा मध्ये रांग(0,4): \n\tतोपर्यंत बा मध्ये रांग(0,4): \n\t\tछापा('iugerhuihgireviugerhuihgire')\n\t\tछापा('iugerhuihgireviugerhuihgire')"
#print(x)
print(obj.execute(x,dix.en_final,dix.mar_final))
# print(obj.execute("छापें('छापें fuyazguyfaz')",dix.en_final,dix.hin_final))
# print(obj.execute("tẹjade('uighzuihiez  tẹjade ')",dix.en_final,dix.yrb_final))
# print(obj.execute("طباعة('طباعة igueruygue')",dix.en_final,dix.arb_final))
# y="तोपर्यंत बा मध्ये रांग(0,4):\n\tछापा('iugerhuihgireviugerhuihgire')\n\tछापा('iugerhuihgireviugerhuihgire')"
# print(obj.execute(y,dix.en_final,dix.mar_final))
#print(obj.execute("imprime('imprime  tẹjade ')",dix.en_final,dix.sp_final))




