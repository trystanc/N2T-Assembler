class SymbolTable:
    
    def __init__(self):
        self._table = {}

        for i in range(16):
            self._table['R'+str(i)] = i
        self._table['SP'] = 0
        self._table['LCL'] = 1
        self._table['ARG'] = 2
        self._table['THIS'] = 3
        self._table['THAT'] = 4
        self._table['SCREEN'] = 16384
        self._table['KBD'] = 24576
    
    def addEntry(self, symbol, address):
        self._table[symbol] = address
    def contains(symbol, self):
        if symbol in self._table:
            return True
        else:
            return False
    def GetAddress(symbol, self):
        return self._table[symbol]
    
        