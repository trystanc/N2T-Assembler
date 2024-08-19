from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable
import sys
#initialise parts of assembler and I/O files

if len(sys.argv) > 1:
    file_name = sys.argv[1]
    if not os.path.isfile(file_name):
        raise FileNotFoundError(f"The file '{file_name}' does not exist.")
else:
    raise ValueError("No file name provided as a command-line argument.")
file = open(file_name, 'r')
hack = open(file_name[:-3]+'hack', 'w')
parser = Parser(file_name)
code =  Code(parser)
parser.advance()
symboltable = SymbolTable()
#first pass
while parser.hasMoreCommands():
    if parser.commandType() == 'L_Command':
        symboltable.addEntry(parser.symbol(), parser.line_counter() + 1)
    parser.advance()
file.close() 

#second pass       
file_name_2nd = 'Add.asm'
file_2nd = open(file_name, 'r')
parser = Parser(file_name_2nd)
code =  Code(parser)
parser.advance()
#main loop
variable_counter = 16
while parser.hasMoreCommands():
    


    if parser.commandType() == 'A_Command':
        instruction = '0'      
        if parser.symbol()[0].isdigit():
            number = int(parser.symbol())
        else:
            if symboltable.contains( parser.symbol() ):
                number = symboltable.getAddress( parser.symbol() )
            else:
                symboltable.addEntry(parser.symbol(), variable_counter)
                variable_counter += 1
        instruction += '{0:015b}'.format(number)
        hack.write(instruction + '\n')
   
    elif parser.commandType() == 'C_Command':    
        instruction = '111'
        instruction += code.dest()
        instruction += code.comp()
        instruction += code.jump()
        hack.write(instruction + '\n')
    parser.advance()
        
hack.close()        
print(parser.line_counter())
        
        
    
    
