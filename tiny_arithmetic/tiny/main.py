from tiny.evaluator import evaluate
from tiny.parser import parse
from tiny.tokenizer import Tokenizer
from tiny.visualize import ast_to_dot, print_ast

examples = [
    # "1 + 2 * 3",
    "(2 + 3) * 4 / 5",
    "((2 + 3) * 4 / 5) + (4 / 2)",
    "()",
]


def run():
    for input in examples:
        tokens = Tokenizer().tokenize(input)
        print(tokens)
        ast = parse(input)
        print("AST:")
        print_ast(ast)
        dot = ast_to_dot(ast)
        dot.render("ast", format="png", view=True)
        print(f"Result: {evaluate(ast)}")
