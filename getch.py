import sys
import getch

def execute(filename):
    f = open(filename, "r")
    evaluate(f.read())
    f.close()


def evaluate(code):
    code = cleanup(list(code))
    bracemap = buildbracemap(code)

    cells, codeptr, cellptr = [0], 0, 0

    while codeptr < len(code):
        command = code[codeptr]

        if command == "ㄱ": #>
            cellptr += 1
            if cellptr == len(cells):
                cells.append(0)

        if command == "ㄴ": #<
            cellptr = 0 if cellptr <= 0 else cellptr - 1

        if command == "ㄷ": #+
            cells[cellptr] = (cells[cellptr] + 1) % 256

        if command == "ㄹ": #-
            cells[cellptr] = (cells[cellptr] - 1) % 256

        if command == "ㅁ" and cells[cellptr] == 0: #[
            codeptr = bracemap[codeptr]

        if command == "ㅂ" and cells[cellptr] != 0: #]
            codeptr = bracemap[codeptr]

        if command == "ㅅ": # .
            sys.stdout.write(chr(cells[cellptr]))

        if command == "ㅇ": # ,
            cells[cellptr] = ord(getch.getch())

        codeptr += 1


def cleanup(code):
    return ''.join(filter(lambda x: x in ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ'], code))


def buildbracemap(code):
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        if command == "ㅁ":
            temp_bracestack.append(position)
        if command == "ㅂ":
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap


def main():
    if len(sys.argv) == 2:
        execute(sys.argv[1])
    else:
        print("Usage:", sys.argv[0], "filename")


if __name__ == "__main__":
    main()
