
from parser import *
import pprint

import plylex as lex
import plyyacc as yacc

programa = None
posicion = None
progLong = None

def globales(prog, pos, long):
    global programa
    global posicion
    global progLong
    programa = prog
    posicion = pos
    progLong = long

def parser(imprime=True, graphic_tree=False):
    # Função principal do parser

    # cria o lexer
    lexer = lex.lex()
    # cria o parser
    parser = yacc.yacc(debug=False)
    # faz o parser com o programa dado e utiliza o lexer criado
    # inclui função que consome o parser
    AST = parser.parse(
        tracking=True,
        input=programa,
        lexer=lexer
    )

    # imprime a árvore
    if imprime:
        print("\nResulting AST:")
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(AST)
    
    # imprime o grafico da árvore
    if graphic_tree:
        try:
            import lolviz
            g = lolviz.treeviz(AST)
            g.view()
        except ModuleNotFoundError:
            print("lolviz not found! - More info at: https://github.com/parrt/lolviz")
        except Exception:
            print((
                "Gráfico não pode ser gerado!\n"
                "Confirme que o Source.gv e Source.gv.pdf não estão em uso."
            ))
    
    if AST is not None: AST.source = programa
    return AST
