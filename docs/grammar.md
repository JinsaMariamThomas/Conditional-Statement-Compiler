
# Context-Free Grammar (CFG)
## Conditional Statement Compiler

### 1. Purpose

This document describes the grammar of the source language accepted by the Conditional Statement Compiler. The parser supports conditional statements, blocks, assignments, and expressions.

### 2. Grammar Notation

- `|` means OR (alternative production).
- `ε` means an empty production.
- Quoted words and symbols are terminals.
- Capitalized names such as `Statement` and `Expression` are non-terminals.
- In the EBNF rules, `*` means zero or more repetitions.

### 3. EBNF Grammar

```text
Program              ::= StatementList

StatementList        ::= Statement*

Statement            ::= IfStatement
                       | Block
                       | Assignment

IfStatement          ::= "if" "(" Expression ")" Block ElsePart

ElsePart             ::= "else" Block
                       | ε

Block                ::= "{" StatementList "}"

Assignment           ::= Identifier "=" Expression ";"

Expression           ::= OrExpression

OrExpression         ::= AndExpression ("||" AndExpression)*

AndExpression        ::= EqualityExpression
                         ("&&" EqualityExpression)*

EqualityExpression   ::= ComparisonExpression
                         (("==" | "!=") ComparisonExpression)*

ComparisonExpression ::= AdditiveExpression
                         ((">" | "<" | ">=" | "<=")
                         AdditiveExpression)*

AdditiveExpression   ::= MultiplicativeExpression
                         (("+" | "-") MultiplicativeExpression)*

MultiplicativeExpression
                     ::= UnaryExpression
                         (("*" | "/" | "%") UnaryExpression)*

UnaryExpression      ::= ("!" | "-" | "+") UnaryExpression
                       | Primary

Primary              ::= Number
                       | Boolean
                       | Identifier
                       | "(" Expression ")"
```

### 4. Terminals

The parser recognizes these important terminal symbols:

- Keywords: `if`, `else`
- Delimiters: `(`, `)`, `{`, `}`, `;`
- Assignment operator: `=`
- Logical operators: `||`, `&&`, `!`
- Equality operators: `==`, `!=`
- Relational operators: `>`, `<`, `>=`, `<=`
- Arithmetic operators: `+`, `-`, `*`, `/`, `%`
- Values: identifiers, numbers, Boolean literals

The lexer determines the exact spellings and token classifications of numbers, identifiers, and Boolean literals.

### 5. Operator Precedence

From highest to lowest precedence:

1. Primary expressions: identifiers, numbers, Boolean values, parentheses
2. Unary operators: `!`, `-`, `+`
3. Multiplication, division, modulo: `*`, `/`, `%`
4. Addition and subtraction: `+`, `-`
5. Relational operators: `>`, `<`, `>=`, `<=`
6. Equality operators: `==`, `!=`
7. Logical AND: `&&`
8. Logical OR: `||`

The parser implements these precedence levels using separate parsing functions.

### 6. Grammar Transformations

**Left recursion removal**

The expression rules are implemented using loops in the recursive-descent parser. For example, `parse_additive()` first parses a multiplicative expression and then repeatedly processes `+` or `-`.

Therefore, the parser does not directly use a left-recursive production such as:

`Expression ::= Expression "+" Term | Term`

No left-recursion removal is required for the parser implementation as written.

**Left factoring**

The grammar presented here does not require an additional left-factoring transformation for the parser's current parsing strategy. The parser selects statements based on their starting token and handles expression operators at separate precedence levels.

### 7. Conclusion

The grammar describes the main statement structures and expression precedence supported by the Conditional Statement Compiler. The parser uses recursive-descent methods to validate syntax and construct an Abstract Syntax Tree (AST).

Note: This is an EBNF specification. It should be compared with the lexer and parser implementation before being presented as a formally verified grammar.
```
