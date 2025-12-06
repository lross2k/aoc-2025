def process_battery_line(line: str):
    last_index = len(line)-1

    left_number = [int(line[last_index-1]), last_index-1]
    right_number = [int(line[last_index]), last_index]
    for index in range(last_index-2, -1, -1):
        number = int(line[index])
        if number > left_number[0]:
            old_left = left_number[:]
            left_number = [number, index]
            if old_left[0] > right_number[0]:
                right_number = old_left[:]
        elif number == left_number[0] and number > right_number[0]:
            old_left = left_number[:]
            left_number = [number, index]
            right_number = old_left[:]
    return left_number[0] * 10 + right_number[0]

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
    total_jolts = 0
    for line in file_contents:
        line_jolts = process_battery_line(line)
        total_jolts += line_jolts
        print(line, line_jolts)
    print(total_jolts)

def main():
    #process_file("test01.txt")
    #process_file("test02.txt")
    process_file("input.txt")

if __name__ == "__main__":
    main()
