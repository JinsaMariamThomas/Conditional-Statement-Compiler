
class SemanticAnalyzer:
    def __init__(self, predefined_variables=None):
        # Variables supplied as program inputs
        self.symbol_table = {
            name: "defined"
            for name in (predefined_variables or [])
        }
        self.errors = []

    def check_expression(self, node, symbols):
        """Check whether every variable in an expression is defined."""
        node_type = node["type"]

        if node_type == "Identifier":
            name = node["name"]

            if name not in symbols:
                self.errors.append(
                    f"Variable '{name}' used before definition"
                )
            return

        if node_type == "BinaryExpression":
            self.check_expression(node["left"], symbols)
            self.check_expression(node["right"], symbols)
            return

        if node_type == "UnaryExpression":
            self.check_expression(node["operand"], symbols)

    def check_statements(self, statements, symbols):
        """Check assignments, blocks and conditional statements."""
        for statement in statements:
            statement_type = statement["type"]

            if statement_type == "Assignment":
                self.check_expression(statement["value"], symbols)

                # Define the variable after checking its value.
                symbols.add(statement["name"])
                self.symbol_table[statement["name"]] = "defined"

            elif statement_type == "Block":
                self.check_statements(
                    statement["statements"], symbols
                )

            elif statement_type == "IfStatement":
                self.check_expression(
                    statement["condition"], symbols
                )

                # Analyze each branch separately.
                original_symbols = set(symbols)
                then_symbols = set(original_symbols)

                self.check_statements(
                    statement["then_block"]["statements"],
                    then_symbols
                )

                if statement["else_block"] is not None:
                    else_symbols = set(original_symbols)

                    self.check_statements(
                        statement["else_block"]["statements"],
                        else_symbols
                    )

                    # A variable is guaranteed to exist after
                    # the if-else only if both branches define it.
                    symbols.update(then_symbols & else_symbols)
                # Without an else, the if body might not execute.

    def analyze(self, ast):
        """Run semantic checks on the AST."""
        self.errors = []
        symbols = set(self.symbol_table.keys())

        self.check_statements(ast["statements"], symbols)

        if self.errors:
            return {
                "success": False,
                "errors": self.errors,
                "symbols": sorted(symbols)
            }

        return {
            "success": True,
            "errors": [],
            "symbols": sorted(symbols)
        }
