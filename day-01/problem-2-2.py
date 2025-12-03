def rotate_dial(dial_state: int, clockwise: bool, amount: int) -> list[int]:
    # start at 50 and go many loops right into 30
    # start at 30 and go many loops left into 30
    # start at 30 and go right to 0
    # start at 0 and go left to 30
    # start at 30 and go left to 0
    # start at 0 and go right to 0
    # start at 0 and go left to 0
    return [new_dial_state, extra_zeroes]

def get_line_orientation(line_code: str) -> bool:
    return line_code[0] == 'R'

def get_line_amount(line_code: str) -> int:
    return int(line_code[1:])

def process_line_new_state(current_state: int, line_code: str) -> list[int]:
    orientation = get_line_orientation(line_code)
    amount = get_line_amount(line_code)
    return rotate_dial(current_state, orientation, amount)

def process_file_lines(file_contents):
    times_at_zero: int = 0
    dial_state: int = 50
    for line in file_contents:
        results = process_line_new_state(dial_state, line)
        new_state = results[0]
        extra_zeroes = results[1]
        print(dial_state, line, new_state, extra_zeroes)
        times_at_zero += (extra_zeroes)
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
    #process_file("test-2.txt")
    #process_file("test-3.txt")
    #process_file("test-4.txt")
    #process_file("puzzle-1.txt")
    process_file("test-1.txt")

if __name__ == "__main__":
    main()
