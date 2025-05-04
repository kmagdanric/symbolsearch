# tiny/evaluator.py

from typing import Union

from tiny.model.nodes import (
    DivideTerm,
    Expr,
    FactorTerm,
    MultiplyTerm,
    Negation,
    Number,
    ParenExpr,
)

# Union of all AST node types we know how to evaluate
ASTNode = Union[
    Number,
    Negation,
    ParenExpr,
    FactorTerm,
    MultiplyTerm,
    DivideTerm,
    Expr,
]


def evaluate(node: ASTNode) -> float:
    """
    Recursively evaluate the AST node and return its numeric value.
    """
    # Base literal
    if isinstance(node, Number):
        return node.value

    # Unary negation
    if isinstance(node, Negation):
        return -evaluate(node.operand)

    # Parenthesized expression or term
    if isinstance(node, ParenExpr):
        return evaluate(node.expression)

    # A Term that is just a single Factor
    if isinstance(node, FactorTerm):
        return evaluate(node.factor)

    # Multiplication
    if isinstance(node, MultiplyTerm):
        return evaluate(node.left) * evaluate(node.right)

    # Division
    if isinstance(node, DivideTerm):
        return evaluate(node.left) / evaluate(node.right)

    # Addition or subtraction
    if isinstance(node, Expr):
        left_val = evaluate(node.left)
        right_val = evaluate(node.right)
        if node.op == "+":
            return left_val + right_val
        else:  # node.op == "-"
            return left_val - right_val
