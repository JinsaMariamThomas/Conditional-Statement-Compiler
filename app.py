
from flask import Flask, render_template, request, jsonify
from pprint import pformat

from lexer import tokenize
from parser import parse_source
from semantic import SemanticAnalyzer

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Conditional Statement Compiler backend is running!"
    })


@app.route("/api/compile", methods=["POST"])
def compile_code():
    data = request.get_json(silent=True) or {}

    source_code = data.get("code", "")
    predefined_text = data.get("predefined_variables", "")

    predefined_variables = [
        name.strip()
        for name in predefined_text.split(",")
        if name.strip()
    ]

    result = {
        "tokens": "",
        "syntax": "",
        "ast": "",
        "semantic": "",
        "symbols": [],
        "errors": []
    }

    # Stage 1: Lexical Analysis
    try:
        tokens = tokenize(source_code)
        result["tokens"] = pformat(tokens)

    except Exception as error:
        result["errors"].append({
            "stage": "Lexical Analysis",
            "message": str(error)
        })
        return jsonify(result)

    # Stage 2: Syntax Analysis and AST Generation
    try:
        ast = parse_source(source_code)
        result["syntax"] = "Syntax analysis successful."
        result["ast"] = pformat(ast)

    except Exception as error:
        result["syntax"] = "Syntax analysis failed."
        result["errors"].append({
            "stage": "Syntax Analysis",
            "message": str(error)
        })
        return jsonify(result)

    # Stage 3: Semantic Analysis and Symbol Table
    try:
        analyzer = SemanticAnalyzer(
            predefined_variables=predefined_variables
        )

        semantic_result = analyzer.analyze(ast)

        # Collect the symbol table returned by the analyzer.
        result["symbols"] = semantic_result.get("symbols", [])

        if semantic_result.get("success"):
            result["semantic"] = "Semantic analysis successful."
        else:
            result["semantic"] = "Semantic analysis failed."

            for message in semantic_result.get("errors", []):
                result["errors"].append({
                    "stage": "Semantic Analysis",
                    "message": message
                })

    except Exception as error:
        result["semantic"] = "Semantic analysis failed."
        result["errors"].append({
            "stage": "Semantic Analysis",
            "message": str(error)
        })

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
