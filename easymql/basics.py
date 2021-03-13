from easymql.core import Suppress, Literal


(
    LPAREN,
    RPAREN,
    LBRACE,
    RBRACE,
    LBRACK,
    RBRACK,
    COLON,
    SEMICOLON,
    COMMA,
    PERIOD,
    HYPHEN,
) = map(Suppress, map(Literal, tuple('(){}[]:;,.-')))
