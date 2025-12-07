import re

def process_symbol_line(line: str) -> list[str]:
    return re.findall(r' {0,}([*+]) {0,}', line)

def process_number_line(line: str) -> list[str]:
    return re.findall(r' {0,}(\d+) {0,}', line)

def do_actual_calculations(numbers, operations):
    columns = len(operations)
    column_results = []
    for i in range(columns):
        opcode = operations[i]
        result = int(numbers[0][i])
        for j in range(1, len(numbers)):
            if opcode == '*':
                result *= int(numbers[j][i])
            else:
                result += int(numbers[j][i])
        column_results.append(result)
    return column_results

def split_contents(contents):
    content_list = []
    current = ""
    for character in contents:
        if character == "\n":
            content_list.append(current)
            current = ""
            continue
        current += character
    return content_list

def process_file(file_name: str):
    file_contents = open(file_name, 'r').read()
    file_contents = split_contents(file_contents)
    number_lines = []
    for line in file_contents[:-1]:
        number_lines.append(process_number_line(line))
    operations = process_symbol_line(file_contents[-1])
    values = do_actual_calculations(number_lines, operations)
    print(sum(values))

def main():
    #process_file("test01.txt")
    #process_file("test02.txt")
    process_file("input.txt")

if __name__ == "__main__":
    main()
