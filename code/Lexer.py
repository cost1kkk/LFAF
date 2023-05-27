import re
import Tokens as Tokens


class Lexer:
    file = None
    content = ""
    tokens = "|".join(f"(?P<{name}>{regex})" for name, regex in Tokens.tokens.items())

    def __init__(self, file_name):
        self.file = open(file_name)
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