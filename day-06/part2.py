import re

def process_symbol_line(line: str) -> list[str]:
    return re.findall(r' {0,}([*+]) {0,}', line)

def process_number_line(line: str) -> list[str]:
    return re.findall(r' {0,1}([\d ]{1,4}) {0,1}', line)

def do_cephalopod_calculations(numbers, operations):
    columns = len(operations)
    column_results = []
    #print(columns, numbers)
    for i in range(columns):
        opcode = operations[i]
        result = numbers[i][0]
        for j in range(1, len(numbers[i])):
            if opcode == '*':
                result *= int(numbers[i][j])
            else:
                result += int(numbers[i][j])
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

def read_cephalopod_numbers(lines):
    groups = []
    longest = 0
    for line in lines:
        length = len(line)
        if length > longest:
            longest = length

    subgroup = []
    for c in range(longest):
        number = ''
        for r in range(len(lines)):
            if c > len(lines[r]) - 1:
                number += ' '
            else:
                number += lines[r][c]
        if number.count(' ') == len(number):
            # it means it's an empty column
            groups.append(subgroup[:])
            subgroup = []
        else:
            subgroup.append(int(number))
            #print('c'+str(c), number)
    groups.append(subgroup[:])
    return groups

def process_file(file_name: str):
    file_contents = open(file_name, 'r').read()
    file_contents = split_contents(file_contents)

    numbers = read_cephalopod_numbers(file_contents[:-1])

    operations = process_symbol_line(file_contents[-1])
    values = do_cephalopod_calculations(numbers, operations)
    print(sum(values))

def main():
    #process_file("test01.txt")
    process_file("input.txt")

if __name__ == "__main__":
    main()
