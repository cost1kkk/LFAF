from lexer import Lexer

def main():
    program = Lexer("test.txt")
    toks = program.tokenize()
    for t in toks: 
        print(t)

if __name__ == '__main__':
    main()