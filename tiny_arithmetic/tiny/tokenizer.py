import re
from typing import List, NamedTuple


# A simple Token type with a type name and its string value
class Token(NamedTuple):
    type: str
    value: str


class Tokenizer:
    # Regex rules for token types:
    # including number, operators, parentheses, and whitespace
    TOKEN_SPEC = [
        ("NUMBER", r"\d+"),
        ("PLUS", r"\+"),
        ("MINUS", r"-"),
        ("STAR", r"\*"),
        ("SLASH", r"/"),
        ("LPAREN", r"\("),
        ("RPAREN", r"\)"),
        ("WS", r"\s+"),
    ]

    def __init__(self):
        # Compile a single regex with named capture groups for each token type
        parts = (f"(?P<{name}>{pattern})" for name, pattern in self.TOKEN_SPEC)
        self.token_regex = re.compile("|".join(parts))

    def tokenize(self, expression: str) -> List[Token]:
        tokens: List[Token] = []
        for mo in self.token_regex.finditer(expression):
            kind = mo.lastgroup
            if kind == "WS":
                continue  # skip whitespace
            tokens.append(Token(kind, mo.group()))
        return tokens
