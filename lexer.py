
import re

# Keywords in our conditional statement language
KEYWORDS = {
    "if": "IF",
    "else": "ELSE",
    "true": "BOOLEAN",
    "false": "BOOLEAN",
}

# Token patterns: longer operators must come before shorter ones
TOKEN_SPECIFICATION = [
    ("WHITESPACE", r"\s+"),
    ("NUMBER", r"\d+(?:\.\d+)?"),
    ("IDENTIFIER", r"[A-Za-z_][A-Za-z0-9_]*"),
    ("OPERATOR", r"==|!=|<=|>=|&&|\|\||[+\-*/%<>=!]"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("LBRACE", r"\{"),
    ("RBRACE", r"\}"),
    ("SEMICOLON", r";"),
]

TOKEN_REGEX = re.compile(
    "|".join(
        f"(?P<{name}>{pattern})"
        for name, pattern in TOKEN_SPECIFICATION
    )
)


def tokenize(source_code):
    """Convert source code into a list of tokens."""
    tokens = []
    position = 0

    while position < len(source_code):
        match = TOKEN_REGEX.match(source_code, position)

        if not match:
            line = source_code.count("\n", 0, position) + 1
            raise SyntaxError(
                f"Unexpected character {source_code[position]!r} "
                f"at line {line}, column {position - source_code.rfind(chr(10), 0, position)}"
            )

        token_type = match.lastgroup
        token_value = match.group()

        if token_type != "WHITESPACE":
            if token_type == "IDENTIFIER":
                token_type = KEYWORDS.get(token_value, "IDENTIFIER")

            tokens.append({
                "type": token_type,
                "value": token_value,
                "position": position,
            })

        position = match.end()

    tokens.append({
        "type": "EOF",
        "value": "",
        "position": len(source_code),
    })

    return tokens
