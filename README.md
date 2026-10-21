# CodeWise — Conditional Statement Compiler

A beginner-friendly web application that analyzes conditional statements and demonstrates the main stages of compiler design.

🌐 **Live Website:** https://conditional-statement-compiler.onrender.com

💻 **GitHub Repository:** https://github.com/JinsaMariamThomas/Conditional-Statement-Compiler

## About the Project

CodeWise is an educational compiler project designed to help students understand how a compiler analyzes source code. It focuses on conditional statements and explains compiler concepts using simple language alongside technical terminology.

The application analyzes code and reports syntax and semantic errors. It does not execute the submitted program.

## Features

- **Lexical Analysis:** Identifies keywords, operators, identifiers, and other tokens.
- **Syntax Analysis:** Checks whether the code follows the language grammar.
- **Abstract Syntax Tree (AST):** Represents the structure of the program.
- **Semantic Analysis:** Checks the meaning and correctness of the code.
- **Symbol Table:** Displays information about variables.
- **Error Reporting:** Helps identify problems in the submitted code.
- **Interactive Web Interface:** Allows users to enter code and view analysis results.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Git and GitHub
- Render (deployment)

## How to Use

1. Open the [CodeWise website](https://conditional-statement-compiler.onrender.com).
2. Enter a conditional statement program or load the example.
3. Click **Analyze My Code**.
4. Review the tokens, syntax analysis, AST, semantic analysis, symbol table, and errors.
5. Correct any errors and analyze the program again.

## Running Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/JinsaMariamThomas/Conditional-Statement-Compiler.git
   ```

2. Open the project folder:

   ```bash
   cd Conditional-Statement-Compiler
   ```

3. Create and activate a Python virtual environment:

   ```bash
   python -m venv venv
   ```

   Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the Flask application:

   ```bash
   python app.py
   ```

6. Open http://127.0.0.1:5000 in your browser.

## Project Documentation

The `docs` folder contains additional project documentation, including:

- `grammar.md` — grammar rules for the language.
- `control_flow_graph.md` — documentation about the control flow graph.

## Project Purpose

This project demonstrates the fundamental stages of compiler design in an interactive and beginner-friendly environment. It is intended for educational use and learning compiler concepts.

## Author

**Jinsa Mariam Thomas**

