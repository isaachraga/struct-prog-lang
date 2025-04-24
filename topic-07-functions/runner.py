import tokenizer
import parser
import evaluator
import sys

def run(text):
    tokens = tokenizer.tokenize(text)
    ast = parser.parse(tokens)
    return evaluator.evaluate(ast)

def repl():
    env = {}
    lastValue = None
    print("Welcome to your sopl REPL!\n")
    print("Available commands:\n")
    print("info --------------- additional information\n")
    print("dir ---------------- print environment\n")
    print("^ ------------------ result of last expression\n")
    print("exit/quit ---------- terminate session\n")
    while True:
        try:
            line = input(">>>> ")
            if line.strip() in {"exit", "quit"}:
                print("Closing sopl...")
                break
            if line.strip() in {"info"}:
                print("Uses the synax of the language created in the Structures of Programming Languages class\n")
                continue;
            if line.strip() in {"dir"}:
                print(env)
                continue;
            if line.strip() in {"^"}:
                print(lastValue)
                line = ""
                continue;
            if '^' in line.strip() :
                line = str(line).replace("^", str(lastValue))
                print(line)
            lastValue, env = run(line)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1],"r") as f:
            source = f.read()
        run(source)
    else:
        repl()


