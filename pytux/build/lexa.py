from ply import lex

# List of token names
tokens = (
    'INCLUDE',
    'STRING'
)

# Simple regular expression rules
t_INCLUDE = r'include'


# Action regular expression rule
def t_STRING(t):
    r'\'(.+?)\''
    t.value = str(t.value).replace("'", '')
    return t


# Tracking line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters
t_ignore = ' \t'


# Comments are also ignored
def t_COMMENT(t):
    r'\#.*'
    pass


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Building Lexy
Lexa = lex.lex()