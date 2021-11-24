import lexer

class Parser():
    tokens = lexer.tokens

    precendence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
    )

    def p_program(p):
        'program : declaration_list'
        print('program: ',[x for x in p])
        p[0] = p[1]

    def p_declaration_list(p):
        '''declaration_list : declaration_list declaration
                            | declaration'''
        print('declaration_list: ',[x for x in p])
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_declaration(p):
        '''declaration : var_declaration 
                       | fun_declaration'''
        print('declaration: ',[x for x in p])
        p[0] = p[1]

    def p_var_declaration(p):
        '''var_declaration : type_specifier ID 
                           | type_specifier ID LBRACKET NUM RBRACKET'''
        print('var_declaration: ',[x for x in p])
        if len(p) == 3:
            p[0] = ('ASSIGN', ('ID', p[1]))
        else:
            p[0] = ('ASSIGN', ('ID', p[1]), ('NUM', p[4]))

    def p_type_specifier(p):
        '''type_specifier : INT 
                          | VOID'''
        print('type_specifier: ',[x for x in p])
        p[0] = p[1]

    def p_fun_declaration(p):
        'fun_declaration : type_specifier ID LPAREN params RPAREN compound_stmt'
        print('fun_declaration: ',[x for x in p])
        p[0] = ('ASSIGN', ('ID', p[1]), p[4], p[6])

    def p_params(p):
        '''params : param_list 
                  | VOID'''
        print('params: ',[x for x in p])
        p[0] = [p[1]]

    def p_param_list(p):
        '''param_list : param_list COLON param 
                      | param'''
        print('param_list: ',[x for x in p])
        if len(p) == 4:
            p[0] = p[1] + p[3]
        else:
            p[0] = p[1]

    def p_param(p):
        '''param : type_specifier ID 
                 | type_specifier ID LBRACKET RBRACKET'''
        print('param: ',[x for x in p])
        p[0] = ('ASSIGN', ('ID', p[1]))
        
    def p_compound_stmt(p):
        'compound_stmt : LKEY local_declarations statement_list RKEY'
        print('compound_stmt: ',[x for x in p])
        p[0] = (p[2], p[3])

    def p_local_declarations(p):
        '''local_declarations : local_declarations var_declaration
                              | empty'''
        print('local_declarations: ',[x for x in p])
        if len(p) == 3:
            p[0] = (p[1], p[2])
        else:
            pass

    def p_statement_list(p):
        '''statement_list : statement_list statement
                          | empty'''
        print('statement_list: ',[x for x in p])
        if len(p) == 3:
            p[0] = (p[1], p[2])
        else:
            pass

    def p_statement(p):
        '''statement : expression_stmt
                     | compound_stmt
                     | selection_stmt
                     | iteration_stmt
                     | return_stmt'''
        print('statement: ',[x for x in p])
        p[0] = p[1]
                    
    def p_expression_stmt(p):
        '''expression_stmt : expression SEMICOLON
                           | SEMICOLON'''
        print('expression_stmt: ',[x for x in p])
        if len(p) == 3:
            p[0] = p[1]
        else:
            pass

    def p_selection_stmt(p):
        '''selection_stmt : IF LPAREN expression RPAREN statement 
                          | IF LPAREN expression RPAREN statement ELSE statement'''
        print('selection_stmt: ',[x for x in p])
        if len(p) == 6:
            p[0] = ('IF', p[3], p[5])
        else:
            p[0] = ('IF', p[3], p[5], p[7])

    def p_iteration_stmt(p):
        'iteration_stmt : WHILE LPAREN expression RPAREN statement'
        print('iteration_stmt: ',[x for x in p])
        p[0] = ('WHILE', p[3], p[5])

    def p_return_stmt(p):
        '''return_stmt : RETURN SEMICOLON
                       | RETURN expression SEMICOLON'''
        print('return_stmt: ',[x for x in p])
        if len(p) == 3:
            p[0] = ('RETURN',)
        else:
            p[0] = ('RETURN', p[2])

    def p_expression(p):
        '''expression : var EQUAL expression 
                      | simple_expression'''
        print('expression: ',[x for x in p])
        if len(p) > 2:
            p[0] = ('ASSIGN', (p[1], p[3]))
        else:
            p[0] = [p[1]]

    def p_var(p):
        '''var : ID 
               | ID LBRACKET expression RBRACKET'''
        print('var: ',[x for x in p])
        if len(p) == 2:
            p[0] = ('ID', p[1])
        else:
            p[0] = (('ID', p[1]), [p[3]])

    def p_simple_expression(p):
        '''simple_expression : additive_expression relop additive_expression
                             | additive_expression'''
        print('simple_expression: ',[x for x in p])
        if len(p) == 4:
            p[0] = (p[1], ('RELOP', p[2]), p[4])
        else:
            p[0] = [p[1]]

    def p_relop(p):
        '''relop : LESSOREQUAL
                 | LESS
                 | GREAT
                 | GREATOREQUAL
                 | DOUBLEEQUAL
                 | NOTEQUAL'''
        print('relop: ',[x for x in p])
        p[0] = ('RELOP', p[1])

    def p_additive_expression(p):
        '''additive_expression : additive_expression addop term 
                               | term'''
        print('additive_expression: ',[x for x in p])
        if len(p) == 4:
            p[0] = (p[1], p[2], p[3])
        else:
            p[0] = p[1]

    def p_addop(p):
        '''addop : PLUS
                 | MINUS'''
        print('addop: ',[x for x in p])
        p[0] = p[1]
                 
    def p_term(p):
        '''term : term mulop factor 
                | factor'''
        print('term: ',[x for x in p])
        if len(p) == 4:
            p[0] = (p[1], p[2], p[3])
        else:
            p[0] = p[1]

    def p_mulop(p):
        '''mulop : MULT
                 | DIV'''
        print('mulop: ',[x for x in p])
        p[0] = p[1]

    def p_factor(p):
        '''factor : LPAREN expression RPAREN
                  | var 
                  | call 
                  | NUM'''
        print('factor: ',[x for x in p])
        if len(p) == 4:
            p[0] = p[2]
        elif p == 'NUM':
            p[0] = ('ASSIGN', ('NUM', p[1]))
        else:
            p[0] = p[1]

    def p_call(p):
        'call : ID LPAREN args RPAREN'
        print('call: ',[x for x in p])
        p[0] = (('ID', p[1]), p[3])

    def p_args(p):
        '''args : arg_list 
                | empty'''
        print('args: ',[x for x in p])
        if p == '':
            pass
        else:
            p[0] = [p[1]]

    def p_args_list(p):
        '''arg_list : arg_list COLON expression 
                    | expression'''
        print('args_list: ',[x for x in p])
        if len(p) == 4:
            p[0] = p[1] + [p[3]]
        else:
            p[0] = p[1]

    def p_error(p):
        if not p:
            print("SYNTAX ERROR AT EOF")

    def p_empty(p):
        'empty :'
        pass

start='program | declaration_list'