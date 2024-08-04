'''
converts parser mnemonics into binary instructions
'''
import compdictionary
class Code:
    def __init__(self, parser):
        self.parser = parser
 #gives dest bits   
    def dest(self):
        mnem = self.parser.dest()
        dest=''
        if mnem == '':
            return '000'
        if 'A' in mnem:
            dest += ('1')
        else:
            dest += ('0')
        
        if 'D' in mnem:
            dest += ('1')
        else:
            dest += ('0')
        
        if 'M' in mnem:
            dest += ('1')
        else:
            dest += ('0')
        return dest
#comp bits    
    def comp(self):
        mnem = self.parser.comp()
        binary = ''
        if 'M' in mnem:
            binary+='1'
            aorm='M'
        else:
            binary+='0'
            aorm='A'
        comp_bits = compdictionary.comp_dict(aorm, mnem)
        binary += comp_bits
        return binary
 #jump bits   
    def jump(self):
        mnem = self.parser.jump()
        return compdictionary.jump_dict(mnem)

        
       

            

            
        
    
            
            
        
        
    
        
        
        
        
        

