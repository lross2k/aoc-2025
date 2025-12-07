def simulate_tachyons(lines, tachyons):
    next_tachyons = {}
    next_line = lines[0]

    # Defines the positions of splitters
    splitters = []
    for char_index in range(len(next_line)):
        char = next_line[char_index]
        if char == '^':
            splitters.append(char_index)
        elif char == '.':
            # check if there is a free falling tachyon coming
            if char_index in tachyons:
                next_tachyons[char_index] = tachyons[char_index]

    # Process new tachs for each splitter
    for splitter in splitters:
        if splitter in tachyons.keys():
            tachs = tachyons[splitter]
            if splitter-1 in next_tachyons.keys():
                next_tachyons[splitter-1] += tachs
            else:
                next_tachyons[splitter-1] = tachs
            if splitter+1 in next_tachyons.keys():
                next_tachyons[splitter+1] += tachs
            else:
                next_tachyons[splitter+1] = tachs

    # create the updated line and print it, then recursive call
    line = ''
    for i in range(len(lines[0])):
        char = lines[0][i]
        if i in next_tachyons:
            line += '|'
        else:
            line += char
    print(line)#, next_tachyons)
    if len(lines) > 1:
        return simulate_tachyons(lines[1:],next_tachyons)
    else:
        res = 0
        for key in next_tachyons:
            res += next_tachyons[key]
        return res

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

    start_tachyon = file_contents[0].index('S')
    tachyons = {start_tachyon: 1}

    print(file_contents[0])
    print('total', simulate_tachyons(file_contents[1:], tachyons))

def main():
    #process_file("test01.txt")
    #process_file("test02.txt")
    process_file("input.txt")

if __name__ == "__main__":
    main()
