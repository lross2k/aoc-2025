import re

def detect_repeating(number: str):
    num_len = len(number)
    if num_len % 2 == 0:
        half_len = int(num_len / 2)
        first_half = number[0:half_len]
        last_half = number[half_len:]
        if first_half == last_half:
            return first_half
        else:
            for n in range(1, half_len):
                semi_number = number[0:n]
                regex = re.findall(semi_number, number)
                if len(regex) == num_len/n:
                    return semi_number
    else:
        half_len = int(num_len / 2)
        for n in range(1, half_len+1):
            semi_number = number[0:n]
            regex = re.findall(semi_number, number)
            if len(regex) == num_len/n:
                return semi_number
    return None

def is_valid_id(id_0: int) -> bool:
    id_0 = str(id_0)
    if id_0[0] == '0':
        return False
    detected = detect_repeating(str(id_0))
    if detected != None:
        #print(id_0, detected)
        return False
    return True

def process_ranges(ranges):
    total_sum = 0
    for id_range in ranges:
        id_1 = int(id_range[0])
        id_2 = int(id_range[1])
        for value in range(id_1, id_2+1):
            if not is_valid_id(value):
                #print("1.0", value)
                total_sum += int(value)
    return total_sum

def split_contents(contents: str):
    matches = re.findall(r"(\d{1,})-(\d{1,}),{0,1}", contents)
    return matches

def process_file(file_name: str):
    file_contents = open(file_name, 'r').read()
    file_contents = split_contents(file_contents)
    print("2.0", process_ranges(file_contents))

def main():
    #process_file("test01.txt")
    process_file("input.txt")

if __name__ == "__main__":
    main()
