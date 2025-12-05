def process_battery_line_OLD(line: str):
    # First of search the biggest number(s) in the battery line
    biggest_number_found = 0
    biggest_numbers_found = []
    for char in line:
        if (int(char)) >= biggest_number_found:
            biggest_number_found = int(char)
            biggest_numbers_found.append(biggest_number_found)
    # Then, out of the biggest number(s) found, determine the left and right numbers
    if len(biggest_numbers_found) == 1:
        # Special case of all batteries being the same highest value
        return biggest_number_found * 10 + biggest_number_found

def process_battery_line_ALMOST(line: str):
    left_number = [0, -1]
    right_number = [0, -1]
    for index in range(len(line)-1, -1, -1):
        current_value = int(line[index])
        # if the value in the left number is lower than current value, assign the new one
        if (current_value > left_number[0]):
            # check if the old value is useful for the right_number
            if (left_number[0] > right_number[0]):
                right_number = left_number[:]
            left_number[0] = current_value
            left_number[1] = index
        # if the value in the right number is lower than current value, assign the new one
        if (current_value > right_number[0]) and left_number[1] != index:
            right_number[0] = current_value
            right_number[1] = index
    # if the indexes are inverted, JUST INVERT THEM AGAIN
    if (left_number[1] > right_number[1]):
        temp = left_number[:]
        left_number = right_number[:]
        right_number = temp[:]
    #print(line, left_number, right_number)
    return left_number[0] * 10 + right_number[0]

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
