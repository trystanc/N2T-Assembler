def comp_dict(aorm, mnem):
   dictionary = {'0' : '101010',
                 '1' : '111111',
                 '-1': '111010',
                 'D' : '001100',
                 aorm: '100110',
                 '!D': '001101',    
             '!'+aorm: '110001',
                 '-D': '001111',
             '-'+aorm: '110011',
                'D+1': '011111', 
            aorm+'+1': '110111',
                'D-1': '001110',
            aorm+'-1': '110010',
            'D+'+aorm: '000010',
            'D-'+aorm: '010011',
            aorm+'-D': '000111',
            'D&'+aorm: '000000',
            'D|'+aorm: '010101',
        }
   return dictionary[mnem]

def jump_dict(mnem):
    jump_dict = {'' : '000',
               'JGT': '001',
               'JEQ': '010',
               'JGE': '011',
               'JLT': '100',
               'JNE': '101',
               'JLE': '110',
               'JMP': '111',  
    }
    return jump_dict[mnem]
