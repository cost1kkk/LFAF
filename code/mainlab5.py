import os

print(os.getcwd())

from Parser import Parser

def main():
    file_path = r"C:\Users\User\Desktop\lab5 lfaf/test.txt"  # Replace with the path to your code file
    parser = Parser(file_path)
    parser.parse()
    parser.show_ast()

if __name__ == "__main__":
    main()
