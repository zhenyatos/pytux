from ply import yacc
from pytux.build.lexa import tokens
from os import path

parsed_file_dir = ''


# Simple statement
def p_include_string(p):
    'sentence : INCLUDE STRING'
    with open(path.join(parsed_file_dir, p[2]), "r") as include_file:
        p[0] = include_file.read()


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Building Semky
Semka = yacc.yacc()


def parse(file):
    global parsed_file_dir
    parsed_file_dir = path.dirname(path.abspath(file.name))
    lines = file.readlines()
    res = ''
    for line in lines:
        temp = Semka.parse(line)
        if temp is not None:
            res += temp
            if line != lines[-1]:
                res += '\n\n'
    return res