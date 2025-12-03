def rotate_dial(dial_state: int, clockwise: bool, amount: int) -> int:
    if amount > 99:
        full_loops = amount // 99
        amount = amount - 100 * full_loops
    new_dial_state = dial_state - amount * (not clockwise) + amount * clockwise
    if new_dial_state > 99:
        new_dial_state -= 100
    elif new_dial_state < 0:
        new_dial_state += 100
    return new_dial_state

def get_line_orientation(line_code: str) -> bool:
    return line_code[0] == 'R'

def get_line_amount(line_code: str) -> int:
    return int(line_code[1:])

def process_line_new_state(current_state: int, line_code: str) -> int:
    orientation = get_line_orientation(line_code)
    amount = get_line_amount(line_code)
    return rotate_dial(current_state, orientation, amount)

def process_file_lines(file_contents):
    times_at_zero: int = 0
    dial_state: int = 50
    for line in file_contents:
        new_state = process_line_new_state(dial_state, line)
        times_at_zero += 1 * new_state == 0
        dial_state = new_state
    return times_at_zero

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
    print(process_file_lines(file_contents))

def main():
    process_file("test-1.txt")
    process_file("test-2.txt")
    process_file("puzzle-1.txt")

if __name__ == "__main__":
    main()
