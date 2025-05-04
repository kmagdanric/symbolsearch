from typing import List

ALLOWED_TOKENS = list("+-*/()0123456789")


class Tokenizer:
    def tokenize(self, expression: str) -> List[str]:
        tokens = []
        expression = expression.replace(" ", "")
        for token in list(expression):
            if token in ALLOWED_TOKENS:
                tokens.append(token)
            else:
                raise ValueError(f"Invalid token: {token}")
        return tokens
