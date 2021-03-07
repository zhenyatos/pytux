from ply import lex

# Reserved words
reserved = {
    'print': 'PRINT',
    'include': 'INCLUDE',
    'quiz': 'QUIZ',
    'end': 'END'
}

# List of token names
tokens = (
    'EQUALS',
    'VARNAME',
    'NEWLINE',
    'STRING',
    'MARKER',
    'RENPY',
) + tuple(d for d in reserved.values())

# Simple regular expression rules
t_EQUALS = r'='
t_MARKER = r'[+-]'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:         # Check for reserved words
        t.type = reserved[t.value]
        if t.type == 'QUIZ':
            t.value = t.lexer.lineno
    else:
        t.type = 'VARNAME'
    return t


# String regular expression, removes quotes
def t_STRING(t):
    r'\'(.+?)\''
    t.value = str(t.value).replace("'", '')
    return t


# Ren'Py tag regular expression, removes tag
def t_RENPY(t):
    r'\<renpy\s[^\<\>]*\>'
    insides = str(t.value)
    insides = (insides[7:])[:-1]
    t.value = insides
    return t


# Tracking line numbers
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.value = '\n'
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
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Building Lexy
Lexa = lex.lex()
