from graphviz import Digraph

from tiny.model.nodes import (
    DivideTerm,
    Expr,
    FactorTerm,
    MultiplyTerm,
    Negation,
    Number,
    ParenExpr,
)


def print_ast(node, indent=0):
    prefix = "  " * indent

    # 1) Bare‐factor term
    if isinstance(node, FactorTerm):
        print(f"{prefix}FactorTerm")
        print_ast(node.factor, indent + 1)
        return

    # 2) Multiplicative terms
    if isinstance(node, MultiplyTerm):
        print(f"{prefix}MultiplyTerm(*)")
        print_ast(node.left, indent + 1)
        print_ast(node.right, indent + 1)
        return
    if isinstance(node, DivideTerm):
        print(f"{prefix}DivideTerm(/)")
        print_ast(node.left, indent + 1)
        print_ast(node.right, indent + 1)
        return

    # 3) Additive expressions
    if isinstance(node, Expr):
        print(f"{prefix}Expr({node.op})")
        print_ast(node.left, indent + 1)
        print_ast(node.right, indent + 1)
        return

    # 4) Factors
    if isinstance(node, Number):
        print(f"{prefix}Number({node.value})")
    elif isinstance(node, Negation):
        print(f"{prefix}Negation")
        print_ast(node.operand, indent + 1)
    elif isinstance(node, ParenExpr):
        print(f"{prefix}ParenExpr")
        print_ast(node.expression, indent + 1)
    else:
        print(f"{prefix}<unknown node {node!r}>")


def ast_to_dot(node):
    dot = Digraph()

    def visit(n):
        uid = str(id(n))
        label = type(n).__name__
        if isinstance(n, Number):
            label += f"({n.value})"
        dot.node(uid, label)
        for child in getattr(n, "__dict__", {}).values():
            if isinstance(
                child,
                (
                    Number,
                    Negation,
                    ParenExpr,
                    FactorTerm,
                    MultiplyTerm,
                    DivideTerm,
                    Expr,
                ),
            ):
                cid = visit(child)
                dot.edge(uid, cid)
        return uid

    visit(node)
    return dot
