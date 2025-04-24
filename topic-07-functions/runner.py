import tokenizer
import parser
import evaluator
import sys

def run(text):
    tokens = tokenizer.tokenize(text)
    ast = parser.parse(tokens)
    evaluator.evaluate(ast)

def repl():
    print("Welcome to your sopl REPL!")

    while True:
        try:
            line = input(">>>> ")
            if line.strip() in {"exit", "quit"}:
                print("Goodbye!")
                break
            run(line)
        except Exception as e:
            print("❌ Error:", e)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1],"r") as f:
            source = f.read()
        run(source)
    else:
        repl()


