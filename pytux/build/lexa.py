from ply import lex

# Reserved words
reserved = {
    'print': 'PRINT',
    'include': 'INCLUDE'
}

# List of token names
tokens = (
    'EQUALS',
    'VARNAME',
    'NEWLINE',
    'STRING',
) + tuple(d for d in reserved.values())

# Simple regular expression rules
t_EQUALS = r'='


def t_ID(t):
    r'[a-zA-Z$][a-zA-Z_0-9]*'
    if t.value in reserved:         # Check for reserved words
        t.type = reserved[t.value]
    else:
        t.type = 'VARNAME'
    return t


# Action regular expression rule
def t_STRING(t):
    r'\'(.+?)\''
    t.value = str(t.value).replace("'", '')
    return t


# Tracking line numbers
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.value = '\n' * (len(t.value) + 1)
    return t


# A string containing ignored characters
t_ignore = ' \t'


# Comments are also ignored
def t_COMMENT(t):
    r'\#.*\n+'
    t.lexer.lineno += 1
    pass


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Building Lexy
Lexa = lex.lex()
