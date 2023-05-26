
# Lexer & Scanner
### Course: Formal Languages & Finite Automata
### Author: Baxanean Constantin FAF213
### Variant: 4
## Theory
Def: 
Lexical Analysis and Scanners: for the purposes of this laboratory, lexical analysis means the transformation of a sequence of characters into a series of lexical tokens. The program/algorithm that does this is called the lexer (or scanner), and it is the main character of this here laboratory.

## Implementation description
First o all I create a file named token.py code there looks like 
```
tokens = {
    
    "INT" : r"[0-9]+",
    "PLUS" : r"\+",
    "MINUS" : r"\-",
    "DIVIDE" : r"\/",
    "MULTIPLY" : r"\*",
    "LPAREN" : r"\(",
    "RPAREN" : r"\)",
    "NEWLINE": r"\n | \r | \r \n",
    "WHITESPACE": r"[ ]+",
    "INVALID": r".+"

}
```

After I create lexer.py fil where I cretaed class Lexer

```
import re
import token


class Lexer:
    file = None
    content = ""
    tokens = "|".join(f"(?P<{name}>{regex})" for name, regex in token.tokens.items())

    def __init__(self, file_name):
        self.file = open(file_name, "r")
        self.content = self.file.read()

    def tokenize(self):
        matches = re.finditer(self.tokens, self.content)

        tokens = []
        for match in matches:
            token_name = match.lastgroup
            token_value = match.group(token_name)

            if token_name in ["WHITESPACE", "NEWLINE"]:
                continue

            if token_name == "INVALID":
                raise Exception(f"Invalid token '{token_value}'")

            tokens.append((token_name, token_value))

        return tokens
```
And the last step was creating a file named main.py that run the project:
```
from lexer import Lexer

def main():
    program = Lexer("test.txt")
    toks = program.tokenize()
    for t in toks: 
        print(t)

if __name__ == '__main__':
    main()
```

And the output for the test.txt file was:
12 + (34 - 5)

```
('INT', '12')
('PLUS', '+')
('LPAREN', '(')
('INT', '34')
('MINUS', '-')
('INT', '5')
('RPAREN', ')')

```
## Conclusion
In conclusion, lexical analysis and scanners are important components of the compiler or interpreter process in programming languages. Lexical analysis involves breaking down the source code into individual tokens, such as keywords, identifiers, literals, and operators. Scanners, also known as lexical analyzers, are responsible for performing this task efficiently.
Lexical analysis plays a vital role in the compilation process as it serves as the first step in translating human-readable source code into machine-readable form. By identifying and categorizing tokens, scanners provide a structured representation of the source code, which is easier for subsequent phases of the compiler to process.
Scanners typically use regular expressions or finite automata to recognize patterns in the input stream and generate tokens accordingly. They handle various tasks, including skipping whitespace and comments, handling escape sequences, and identifying lexical errors.
Overall, lexical analysis and scanners are fundamental elements of programming language processing. Their accurate and efficient operation ensures the proper interpretation and translation of source code, leading to the successful execution of programs.
