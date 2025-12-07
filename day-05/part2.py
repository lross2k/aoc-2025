def calculate_total_fresh_ingredients(freshes):
    total = 0
    for r in freshes:
        total += r[1] - r[0] + 1
    print(total)

def rebuild_ranges(starting, ending):
    ranges = []
    for i in range(len(starting)):
        current = [starting[i], ending[i]]
        ranges.append(current[:])
    return ranges

def check_overlaps(starting, ending):
    for index in range(len(starting) - 1):
        # ensure that next starting is greater than current
        if starting[index + 1] > starting[index]:
            # problem detected! the next range is mixed with current range
            # check if the ending is also lower, in this case, simply delete the next range
            if ending[index + 1] < ending[index]:
                # simply delete the next range
                print("REPEATED RANGE", starting[index+1],'-',ending[index+1], "REMOVED")
                starting.pop(index + 1)
                ending.pop(index + 1)
                return check_overlaps(starting, ending) # HAS to end to prevent out of bound index
            # check wether the next starting is lower than the current ending
            elif (starting[index + 1] < ending[index]) or (starting[index + 1] == ending[index]):
                # in this case, both ranges can be merged into one using the first starting and second ending
                print("MERGED RANGE", starting[index+1],'-',ending[index+1])
                starting.pop(index + 1)
                ending.pop(index)
                return check_overlaps(starting, ending) # HAS to end to prevent out of bound index
        else:
            # it means it must be equal, which can be a whole issue to tacke
            print("EQUAL STARTINGS MERGED TO ONE RANGE")
            # easy, just ensure to leave the highest value ending, thus merging the ranges
            print(starting)
            print(ending)
            if ending[index] > ending[index + 1]:
                starting.pop(index + 1)
                ending.pop(index + 1)
            else:
                starting.pop(index)
                ending.pop(index)
            return check_overlaps(starting, ending) # HAS to end to prevent out of bound index

    print(starting)
    print(ending)
    return rebuild_ranges(starting, ending)

def find_fresh_ingredients(ranges):
    # determine range overlaps and merge those ranges
    range_starting = []
    range_ending = []
    for x in ranges:
        range_starting.append(x[0])
        range_ending.append(x[1])
    print(range_starting)
    print(range_ending)

    # create a copy of starting and sort real starting
    copy_starting = range_starting[:]
    fixed_ending = []
    range_starting.sort()

    # find the old index and use it to fix the order of endings
    for index in range(len(range_starting)):
        # change to use enumerate here
        indices = [i for i, x in enumerate(copy_starting) if x == range_starting[index]]
        if len(indices) < 2:
            copy_starting.index(range_starting[index])
            old_index = copy_starting.index(range_starting[index])
            print('item', range_starting[index], 'old position', old_index, 'new position', index)
            fixed_ending.append(range_ending[old_index])
        else:
            values = []
            for j in indices:
                values.append(range_ending[j])
                print(range_ending[j])
            print('item', range_starting[j], 'used biggest repeated value')
            fixed_ending.append(max(values))

    print(range_starting)
    print(fixed_ending)
    return check_overlaps(range_starting, fixed_ending)

def prepare_environment(ranges):
    improved_ranges = []
    for range_x in ranges:
        values = range_x.split('-')
        improved_ranges.append([int(values[0]), int(values[1])])
    return find_fresh_ingredients(improved_ranges)

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

    ranges = []
    for content in file_contents:
        if content == "":
            break
        ranges.append(content)

    fresh_ranges = prepare_environment(ranges)
    print('freshy', fresh_ranges)
    calculate_total_fresh_ingredients(fresh_ranges)

def main():
    #process_file("test01.txt")
    #process_file("test02.txt")
    #process_file("test03.txt")
    process_file("input.txt")

if __name__ == "__main__":
    main()
