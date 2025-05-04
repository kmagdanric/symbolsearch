from __future__ import annotations

from typing import List, Optional

from tiny.model.nodes import (
    DivideTerm,
    Expr,
    Factor,
    FactorTerm,
    MultiplyTerm,
    Negation,
    Number,
    ParenExpr,
    Term,
)
from tiny.tokenizer import Token, Tokenizer


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0

    def peek(self) -> Optional[Token]:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected_type: Optional[str] = None) -> Token:
        token = self.peek()
        if token is None:
            raise SyntaxError(
                f"Unexpected end of input, expected {expected_type}"
            )
        if expected_type and token.type != expected_type:
            raise SyntaxError(
                f"Expected token type {expected_type}, got {token.type}"
            )
        self.pos += 1
        return token

    def parse_factor(self) -> Factor:
        tok = self.peek()
        if tok is None:
            raise SyntaxError("Unexpected end of input in factor")
        if tok.type == "NUMBER":
            self.consume("NUMBER")
            return Number(value=int(tok.value))
        if tok.type == "MINUS":
            self.consume("MINUS")
            operand = self.parse_factor()
            return Negation(operand=operand)
        if tok.type == "LPAREN":
            self.consume("LPAREN")
            # ←–– if the very next token is RPAREN, it's an empty ()
            if self.peek() and self.peek().type == "RPAREN":
                raise SyntaxError("Empty parentheses are not allowed")
            expr = self.parse_expression()
            self.consume("RPAREN")
            return ParenExpr(expression=expr)
        raise SyntaxError(f"Unexpected token in factor: {tok}")

    def parse_term(self) -> Term:
        # 1) Parse the base Factor
        first = self.parse_factor()
        node: Term = FactorTerm(factor=first)

        # 2) Then loop on * or /
        while True:
            tok = self.peek()
            if tok and tok.type in ("STAR", "SLASH"):
                op = tok.value
                self.consume(tok.type)
                right = self.parse_factor()
                if op == "*":
                    node = MultiplyTerm(left=node, op=op, right=right)
                else:
                    node = DivideTerm(left=node, op=op, right=right)
            else:
                break

        return node

    def parse_expression(self) -> Expr:
        node: Term = self.parse_term()
        while True:
            tok = self.peek()
            if tok and tok.type in ("PLUS", "MINUS"):
                op = tok.value
                self.consume(tok.type)
                right = self.parse_term()
                node = Expr(left=node, op=op, right=right)  # type: ignore
            else:
                break
        return node  # type: ignore


def parse(text: str) -> Expr:
    """
    Tokenize the input `text` and parse it into an `Expr` AST node.
    Raises SyntaxError on invalid syntax or leftover tokens.
    """
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)
    parser = Parser(tokens)
    expr = parser.parse_expression()
    if parser.peek() is not None:
        raise SyntaxError(f"Unexpected token at end: {parser.peek()}")
    return expr
