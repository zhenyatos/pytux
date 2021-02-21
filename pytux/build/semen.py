from ply import yacc
from pytux.build.lexa import tokens, Lexa
from pytux.build.varya import Varya, VarType
from os import path

parsed_file_dir = ''


# Program
def p_program(p):
    '''program : program sentence
                | sentence'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]


# Include sentence
def p_include_string(p):
    'sentence : INCLUDE STRING NEWLINE'
    with open(path.join(parsed_file_dir, p[2]), "r") as include_file:
        p[0] = include_file.read() + p[3]


# Variable initialization or assignment sentence
def p_assign_string_variable(p):
    'sentence : VARNAME EQUALS STRING NEWLINE'
    Varya.init_or_assign(p[1], p[3], VarType.STRING)
    p[0] = ''


# Print variable sentence
def p_print(p):
    'sentence : PRINT VARNAME NEWLINE'
    p[0] = Varya.get_value(p[2]) + '\n'


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


start = 'program'

# Building Semena
Semen = yacc.yacc(debug=False)


def parse(file):
    global parsed_file_dir
    parsed_file_dir = path.dirname(path.abspath(file.name))
    data = file.read()
    return Semen.parse(data)