def add_tachyon(tachyons, tachyon):
    if tachyon not in tachyons:
        tachyons.append(tachyon)

def simulate_tachyons(lines, tachyons):
    next_tachyions = []
    splits = 0
    for tachyon in tachyons:
        # tachyon is the index, just check the landing char
        landing_char = lines[0][tachyon]
        if landing_char == '^':
            # SPLIT!
            splits += 1
            add_tachyon(next_tachyions, tachyon - 1)
            add_tachyon(next_tachyions, tachyon + 1)
        else:
            add_tachyon(next_tachyions, tachyon)
    # create the updated line and print it, then recursive call
    line = ''
    for i in range(len(lines[0])):
        char = lines[0][i]
        if i in next_tachyions:
            line += '|'
        else:
            line += char
    print(line)
    if len(lines) > 1:
        #print('spl', splits, len(lines))
        return splits + int(simulate_tachyons(lines[1:],next_tachyions))
    else:
        #print('spl', splits)
        return splits

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
    tachyons = [start_tachyon]

    print(file_contents[0])
    print('total', simulate_tachyons(file_contents[1:], tachyons))

def main():
    #process_file("test01.txt")
    #process_file("test02.txt")
    process_file("input.txt")

if __name__ == "__main__":
    main()
