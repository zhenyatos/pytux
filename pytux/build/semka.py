from ply import yacc
from pytux.build.lexa import tokens, Lexa
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


# Simple sentence
def p_include_string(p):
    'sentence : INCLUDE STRING NEWLINE'
    with open(path.join(parsed_file_dir, p[2]), "r") as include_file:
        p[0] = include_file.read() + p[3]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


start = 'program'

# Building Semky
Semka = yacc.yacc(debug=False)


def parse(file):
    global parsed_file_dir
    parsed_file_dir = path.dirname(path.abspath(file.name))
    data = file.read()
    return Semka.parse(data)
