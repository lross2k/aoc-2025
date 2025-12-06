def process_forklift_area(lines: list[str]):
    # check if we don't have top or bottom lines
    top_line = lines[0] != ""
    bottom_line = lines[2] != ""
    line = lines[1]

    new_level_line = ""
    accessible = 0

    for x in range(len(line)):
        if line[x] != '@':
            new_level_line += line[x]
            continue
        surrounding = []
        # top line
        if top_line:
            if (x > 0):
                surrounding.append(lines[0][x-1])
            else:
                surrounding.append("#")
            surrounding.append(lines[0][x])
            if (x < len(line) - 1):
                surrounding.append(lines[0][x+1])
            else:
                surrounding.append("#")
        else:
            surrounding += ["#","#","#"]
        # level line
        if (x > 0):
            surrounding.append(line[x-1])
        else:
            surrounding.append("#")
        if (x < len(line) - 1):
            surrounding.append(line[x+1])
        else:
            surrounding.append("#")
        # bottom line
        if bottom_line:
            if (x > 0):
                surrounding.append(lines[2][x-1])
            else:
                surrounding.append("#")
            surrounding.append(lines[2][x])
            if (x < len(line) - 1):
                surrounding.append(lines[2][x+1])
            else:
                surrounding.append("#")
        else:
            surrounding += ["#","#","#"]
        if ''.join(surrounding).count('@') < 4:
            new_level_line += 'x'
            accessible += 1
        else:
            new_level_line += line[x]

    print(new_level_line)
    return accessible

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

    accessible = 0
    for line_index in range(len(file_contents)):
        lines = []
        if line_index > 0:
            lines.append(file_contents[line_index - 1])
        else:
            lines.append("")
        lines.append(file_contents[line_index])
        if line_index < (len(file_contents) - 1):
            lines.append(file_contents[line_index + 1])
        else:
            lines.append("")

        accessible_in_line = process_forklift_area(lines)
        accessible += accessible_in_line
    print(accessible)

def main():
    #process_file("test01.txt")
    #process_file("test02.txt")
    process_file("input.txt")

if __name__ == "__main__":
    main()
