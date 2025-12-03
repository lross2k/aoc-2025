import re

def is_valid_id(id_0: int) -> bool:
    id_0 = str(id_0)
    if id_0[0] == '0':
        return False
    id_len = len(id_0)
    if (id_len % 2 != 0):
        print("0.0 Can't be twice because it's not even number, right?")
        return True
    else:
        half_len = int(id_len / 2)
        #print("0.1", half_len)
        first_half = id_0[0:half_len]
        last_half = id_0[half_len:]
        #print("0.2", id_0, first_half, last_half)
        return first_half != last_half

def process_ranges(ranges):
    total_sum = 0
    for id_range in ranges:
        id_1 = int(id_range[0])
        id_2 = int(id_range[1])
        for value in range(id_1, id_2+1):
            if not is_valid_id(value):
                print("1.0", value)
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
