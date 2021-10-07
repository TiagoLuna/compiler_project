import numpy
from tabulate import tabulate
import sys
from lexer import *

lexer = lex.lex()

with open(sys.argv[1], 'r') as f:
    lexer.input(f.read())
    tok_array = [[tok.type, tok.value, tok.lexpos, tok.lineno] for tok in lexer]

    '''for tok in lexer:
        tok_array.append([tok.type, tok.value, tok.lexpos, tok.lineno])
    '''

    print(tabulate(tok_array, headers=['Tipo','Valor','Posição','Linha']),'\n')