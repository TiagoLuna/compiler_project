reserved = {
    'else' : 'ELSE',
    'if' : 'IF',
    'int' : 'INT',
    'return' : 'RETURN',
    'void' : 'VOID',
    'while' : 'WHILE'
}

tokens = [
    'ID',
    'NUM',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'LESS',
    'LESSOREQUAL',
    'GREAT',
    'GREATOREQUAL',
    'DOUBLEEQUAL',
    'NOTEQUAL',
    'EQUAL',
    'SEMICOLON',
    'COLON',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LKEY',
    'RKEY',
    'COMENT'
] + list(reserved.values())

def t_COMENT(t):
    r'(/\*){1}([^{/*}] | \*[^/] | /[^\*])*(\*/){1}'
    pass

def t_ID(t):
    r'[a-zA-Z]+'
    t.type = reserved.get(t.value,'ID')
    return t

def t_NUM(t):
    r'[0-9]+'
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_MINUS(t):
    r'\-'
    return t

def t_MULT(t):
    r'\*'
    return t

def t_DIV(t):
    r'\/'
    return t

def t_LESS(t):
    r'\<'
    return t

def t_LESSOREQUAL(t):
    r'\<\='
    return t

def t_GREAT(t):
    r'\>'
    return t

def t_GREATOREQUAL(t):
    r'\>\='
    return t

def t_DOUBLEEQUAL(t):
    r'\=\='
    return t

def t_NOTEQUAL(t):
    r'\!\='
    return t

def t_EQUAL(t):
    r'\='
    return t

def t_SEMICOLON(t):
    r'\;'
    return t

def t_COLON(t):
    r'\,'
    return t

def t_LPAREN(t):
    r'\('
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_LBRACKET(t):
    r'\['
    return t

def t_RBRACKET(t):
    r'\]'
    return t

def t_LKEY(t):
    r'\{'
    return t

def t_RKEY(t):
    r'\}'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("ERROR: Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
    t.lexer.skip(1)

t_ignore  = ' \t'