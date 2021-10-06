import numpy
from tabulate import tabulate
import sys
from lexer import *

lexer = lex.lex()

with open(sys.argv[1], 'r') as f:
    lexer.input(f.read())

    for tok in lexer:
        tok_array = numpy.array([tok.type, tok.value, tok.lexpos, tok.lineno])
        print(tabulate([tok_array], headers=['Tipo','Valor','Posição','Linha']),'\n')
        
    '''
    for i in tok_array
    print(tabulate([[tok.type,tok.value]]))
    '''