
from pprint import pprint

from lexer import tokenize
from parser import parse_source
from semantic import SemanticAnalyzer


def run_compiler():
    print("=" * 50)
    print("   CONDITIONAL STATEMENT MINI COMPILER")
    print("=" * 50)
    print("Supports: if, if-else, nested if")
    print("Enter your code below.")
    print("Type END on a separate line when finished.\n")

    source_lines = []

    while True:
        try:
            line = input()
        except EOFError:
            break

        if line.strip() == "END":
            break

        source_lines.append(line)

    source_code = "\n".join(source_lines)

    if not source_code.strip():
        print("\nNo source code entered.")
        return

    # Stage 1: Lexical analysis
    print("\n--- 1. LEXICAL ANALYSIS ---")

    try:
        tokens = tokenize(source_code)

        for token in tokens:
            if token["type"] != "EOF":
                print(f"{token['type']:12} {token['value']}")

    except SyntaxError as error:
        print("Lexical error:", error)
        return

    # Stage 2: Syntax analysis and AST construction
    print("\n--- 2. SYNTAX ANALYSIS ---")

    try:
        ast = parse_source(source_code)
        print("Syntax is valid.")
        print("\n--- 3. ABSTRACT SYNTAX TREE (AST) ---")
        pprint(ast, sort_dicts=False)

    except SyntaxError as error:
        print("Syntax error:", error)
        return

    # Stage 3: Semantic analysis
    print("\n--- 4. SEMANTIC ANALYSIS ---")
    names = input(
        "Enter predefined variables, separated by commas "
        "(or press Enter for none): "
    )

    predefined_variables = [
        name.strip()
        for name in names.split(",")
        if name.strip()
    ]

    analyzer = SemanticAnalyzer(
        predefined_variables=predefined_variables
    )
    result = analyzer.analyze(ast)

    if result["success"]:
        print("Semantic analysis passed.")
    else:
        print("Semantic analysis failed.")
        for error in result["errors"]:
            print(" -", error)

    print("Symbol table:", result["symbols"])

    # Final result
    print("\n--- 5. COMPILER RESULT ---")

    if result["success"]:
        print("Compilation successful: no errors detected.")
    else:
        print("Compilation failed: semantic errors detected.")

    print("=" * 50)


if __name__ == "__main__":
    run_compiler()
