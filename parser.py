
from lexer import tokenize


class Parser:
    def __init__(self, source_code):
        self.tokens = tokenize(source_code)
        self.position = 0

    def current(self):
        return self.tokens[self.position]

    def advance(self):
        token = self.current()
        if token["type"] != "EOF":
            self.position += 1
        return token

    def expect(self, token_type):
        token = self.current()

        if token["type"] != token_type:
            raise SyntaxError(
                f"Expected {token_type}, "
                f"but found {token['value']!r} "
                f"({token['type']})"
            )

        return self.advance()

    def parse(self):
        statements = []

        while self.current()["type"] != "EOF":
            statements.append(self.parse_statement())

        return {
            "type": "Program",
            "statements": statements
        }

    def parse_statement(self):
        token_type = self.current()["type"]

        if token_type == "IF":
            return self.parse_if()

        if token_type == "LBRACE":
            return self.parse_block()

        if token_type == "IDENTIFIER":
            return self.parse_assignment()

        raise SyntaxError(
            f"Unexpected token: {self.current()['value']!r}"
        )

    def parse_if(self):
        self.expect("IF")
        self.expect("LPAREN")
        condition = self.parse_expression()
        self.expect("RPAREN")

        then_block = self.parse_block()
        else_block = None

        if self.current()["type"] == "ELSE":
            self.advance()
            else_block = self.parse_block()

        return {
            "type": "IfStatement",
            "condition": condition,
            "then_block": then_block,
            "else_block": else_block
        }

    def parse_block(self):
        self.expect("LBRACE")
        statements = []

        while self.current()["type"] not in ("RBRACE", "EOF"):
            statements.append(self.parse_statement())

        self.expect("RBRACE")

        return {
            "type": "Block",
            "statements": statements
        }


    def parse_assignment(self):
        name = self.expect("IDENTIFIER")["value"]

        operator = self.expect("OPERATOR")["value"]
        if operator != "=":
            raise SyntaxError(
                f"Expected '=' for assignment, found {operator!r}"
            )

        value = self.parse_expression()
        self.expect("SEMICOLON")

        return {
            "type": "Assignment",
            "name": name,
            "value": value
        }


    def parse_expression(self):
        return self.parse_or()

    def parse_or(self):
        node = self.parse_and()

        while self.current()["value"] == "||":
            operator = self.advance()["value"]
            right = self.parse_and()
            node = {
                "type": "BinaryExpression",
                "operator": operator,
                "left": node,
                "right": right
            }

        return node

    def parse_and(self):
        node = self.parse_equality()

        while self.current()["value"] == "&&":
            operator = self.advance()["value"]
            right = self.parse_equality()
            node = {
                "type": "BinaryExpression",
                "operator": operator,
                "left": node,
                "right": right
            }

        return node

    def parse_equality(self):
        node = self.parse_comparison()

        while self.current()["value"] in ("==", "!="):
            operator = self.advance()["value"]
            right = self.parse_comparison()
            node = {
                "type": "BinaryExpression",
                "operator": operator,
                "left": node,
                "right": right
            }

        return node

    def parse_comparison(self):
        node = self.parse_additive()

        while self.current()["value"] in (">", "<", ">=", "<="):
            operator = self.advance()["value"]
            right = self.parse_additive()
            node = {
                "type": "BinaryExpression",
                "operator": operator,
                "left": node,
                "right": right
            }

        return node

    def parse_additive(self):
        node = self.parse_multiplicative()

        while self.current()["value"] in ("+", "-"):
            operator = self.advance()["value"]
            right = self.parse_multiplicative()
            node = {
                "type": "BinaryExpression",
                "operator": operator,
                "left": node,
                "right": right
            }

        return node

    def parse_multiplicative(self):
        node = self.parse_unary()

        while self.current()["value"] in ("*", "/", "%"):
            operator = self.advance()["value"]
            right = self.parse_unary()
            node = {
                "type": "BinaryExpression",
                "operator": operator,
                "left": node,
                "right": right
            }

        return node

    def parse_unary(self):
        if self.current()["value"] in ("!", "-", "+"):
            operator = self.advance()["value"]
            operand = self.parse_unary()
            return {
                "type": "UnaryExpression",
                "operator": operator,
                "operand": operand
            }

        return self.parse_primary()

    def parse_primary(self):
        token = self.current()

        if token["type"] == "NUMBER":
            self.advance()
            return {
                "type": "Number",
                "value": token["value"]
            }

        if token["type"] == "BOOLEAN":
            self.advance()
            return {
                "type": "Boolean",
                "value": token["value"]
            }

        if token["type"] == "IDENTIFIER":
            self.advance()
            return {
                "type": "Identifier",
                "name": token["value"]
            }

        if token["type"] == "LPAREN":
            self.advance()
            expression = self.parse_expression()
            self.expect("RPAREN")
            return expression

        raise SyntaxError(
            f"Expected an expression, "
            f"but found {token['value']!r}"
        )


def parse_source(source_code):
    return Parser(source_code).parse()
