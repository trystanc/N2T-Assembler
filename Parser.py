'''
Takes assembly file and returns nmenonics of each line amongst other things
'''
class Parser:
    
    def __init__(self, file_name):        
        
        #removes any white space or comments from line that is to be read o
        file_handle = open(file_name, 'r')
        

        self._current_line= 'placeholder'
        self._prev_line = 'placeholder again'
        self._fh = file_handle
        self._line_counter = 0 #counts current line program is on
        self._hasMoreCommands  = True

        
        
    #access attribute functions   
    def file_length(self):
        return self._fl
    def current_line(self):
        return self._current_line
    def line_counter(self):
        return self._line_counter
    def fh(self):
        return self._fh
    def prev_line(self):
        return self._prev_line
    
        
    #returns true if there are any more lines to be read
    def hasMoreCommands(self):
        return self._hasMoreCommands
    
    #loads new instruction
    def advance(self):
        try:
            #reads next line
            temp = self.fh().readline()
    
 #if there are no more lines to read then updates has more commands to false
            if temp == '':
                self._hasMoreCommands = False
            temp_2 = ''
          
            i=0
            # removes any comments from current line
            while (temp[i] != '/') and i < (len(temp)-1) :
                temp_2 += temp[i]
                i+=1
                
            #remove white space from current line
            temp_2=temp_2.replace(' ', '')   

        
        #if after removing all of this the line is empty - i.e. a line of white
        #space or comment - move on to the next line in .asm file...
            if temp_2 == '':
                self.advance()
       #...or just update the current line being assembled         
            else:
                self._current_line = temp_2
                self._line_counter+=1
        except:
            pass


    
    def commandType(self):
        
        if self.current_line()[0] == '@':
            return 'A_Command'
        
        elif self.current_line()[0] == '(':
            return 'L_Command'        
        else:
            return 'C_Command'
             
    def symbol(self): #not to be used when current line is a C-Command
       symbol=''
       for char in self.current_line()[1:]:
           if char != ')':
            symbol += char
       return symbol
       
    def comp(self):

        if ';' in self.current_line():
            return self.current_line()[0]
        else:
            i=1
            while self.current_line()[i] != '=':
                i+=1
            return self.current_line()[i+1:]
            
    def jump(self):
        if ';' not in self.current_line():
            return ''
        else:
            i=1
            while self.current_line()[i] != ';':
                i+=1  
            return self.current_line()[i+1:]
        
        
    
    def dest(self):
        dest=''
        cur_lin = self.current_line()
        for char in cur_lin:
            if char not in [';', '=']:
                dest += char
            else:
                break
        return dest

            

            
                
     
         
        

        
        
        
    
    
        
        

        
        
        
        
        
        
        
        
    