from ply import yacc
import ply.lex as lex
import sys
from lexer import *
from parser import Parser

lexer = lex.lex()

parser = yacc.yacc(module=Parser)

with open(sys.argv[1], 'r') as f:
    t = parser.parse(f.read())
    print(t)

'''while True:
    try:
        with open(sys.argv[1], 'r') as f:
            s = input(f.read())
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)'''