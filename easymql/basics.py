from pyparsing import Suppress


LPAREN, RPAREN, LBRACE, RBRACE, LBRACK, RBRACK, COLON, SEMICOLON, COMMA = map(
    Suppress, tuple('(){}[]:;,')
)
