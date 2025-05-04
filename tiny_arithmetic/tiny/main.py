from tiny.tokenizer import Tokenizer

examples = [
    "((2 + 3) * 4 / 5) + (4 / 2)",
]


def run():
    for input in examples:
        tokens = Tokenizer().tokenize(input)
        print(tokens)
