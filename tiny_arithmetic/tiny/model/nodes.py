from __future__ import annotations

from typing import Literal, Union

from pydantic import BaseModel


class ASTNode(BaseModel):
    pass


# factor level: leaf or grouping
class Number(ASTNode):
    value: int


class ParenExpr(ASTNode):
    expression: Union[Expr, Term]


class Negation(ASTNode):
    operand: Factor


# expression level: additive
class Expr(ASTNode):
    # left associative
    left: Union[Term, Expr]
    op: Literal["+", "-"]
    right: Term


# term level: multiplicative
class Term(ASTNode):
    pass


class FactorTerm(Term):
    factor: Factor


class MultiplyTerm(Term):
    left: Term
    op: Literal["*"]
    right: Factor


class DivideTerm(Term):
    left: Term
    op: Literal["/"]
    right: Factor


# define Factor now that classes exist
Factor = Union[Number, Negation, ParenExpr]


# Enable recursive references
ASTNode.update_forward_refs()
Number.update_forward_refs()
Negation.update_forward_refs()
ParenExpr.update_forward_refs()
Term.update_forward_refs()
Expr.update_forward_refs()
