
import argparse, os

argparser = argparse.ArgumentParser(description='C- to MIPS32 compiler.')

argparser.add_argument('source', metavar='source', type=str, help="Source C- file.")
argparser.add_argument('-o', metavar='output', type=str, help="Destination asm file.")
argparser.add_argument('--AST', help="Mostrar AST graficamente. (Requires graphviz)", dest="ast", action='store_true')
argparser.add_argument('--ST', help="Printar tabela de símbolos.", dest="sts", action='store_true')

args = argparser.parse_args()

if not os.path.isfile(args.source):
    print("Error: origem deve ser um arquivo válido!")
    exit()

source = args.source
output = args.o

if output is None:
    name = os.path.splitext(os.path.basename(args.source))[0]
    output = os.path.join(os.path.dirname(args.source), name + ".asm")
else:
    if os.path.splitext(output)[1].lower() != '.asm':
        print("Output deve ter uma extensão ASM")
        exit()
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

with open(source, 'r') as f:
    source_code = f.read() + '$'

from callparser import globales, parser
from semantico import semantica
from codegen import codeGen

globales(source_code, 0, len(source_code))

AST = parser(False, args.ast)
semantica(AST, args.sts)
codeGen(AST, output)